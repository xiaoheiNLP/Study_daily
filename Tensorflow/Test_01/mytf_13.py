# -*-coding:utf-8-*-
# @Time    : 2019/10/15 0015 16:22
# @Author  :zhu
# @File    : mytf_13.py
# @task description : 一个约束rate的实例
import math
import numpy as np
from six.moves import xrange
import tensorflow as tf

import tensorflow_constrained_optimization as tfco



# Create a simulated 10-dimensional training dataset consisting of 1000 labeled
# examples, of which 800 are labeled correctly and 200 are mislabeled.
num_examples = 1000
num_mislabeled_examples = 200
dimension = 10
# We will constrain the recall to be at least 90%.
recall_lower_bound = 0.9

# Create random "ground truth" parameters for a linear model.
ground_truth_weights = np.random.normal(size=dimension) / math.sqrt(dimension)
ground_truth_threshold = 0

# Generate a random set of features for each example.
features = np.random.normal(size=(num_examples, dimension)).astype(np.float32) / math.sqrt(dimension)
# Compute the labels from these features given the ground truth linear model.
labels = (np.matmul(features, ground_truth_weights) > ground_truth_threshold).astype(np.float32)
# Add noise by randomly flipping num_mislabeled_examples labels.
mislabeled_indices = np.random.choice(
    num_examples, num_mislabeled_examples, replace=False)
labels[mislabeled_indices] = 1 - labels[mislabeled_indices]


# Create variables containing the model parameters.
weights = tf.Variable(tf.zeros(dimension), dtype=tf.float32, name="weights")
threshold = tf.Variable(0.0, dtype=tf.float32, name="threshold")

# Create the optimization problem.
constant_labels = tf.constant(labels, dtype=tf.float32)
constant_features = tf.constant(features, dtype=tf.float32)


predictions = tf.tensordot(constant_features, weights, axes=(1, 0)) - threshold

context = tfco.rate_context(predictions, labels=constant_labels)
problem = tfco.RateMinimizationProblem(
    tfco.error_rate(context), [tfco.recall(context) >= recall_lower_bound])


def average_hinge_loss(labels, predictions):
  # Recall that the labels are binary (0 or 1).
  signed_labels = (labels * 2) - 1
  return np.mean(np.maximum(0.0, 1.0 - signed_labels * predictions))


def recall(labels, predictions):
  # Recall that the labels are binary (0 or 1).
  positive_count = np.sum(labels)
  true_positives = labels * (predictions > 0)
  true_positive_count = np.sum(true_positives)
  return true_positive_count / positive_count

optimizer = tfco.ProxyLagrangianOptimizer(optimizer=tf.train.AdagradOptimizer(learning_rate=1.0))
train_op = optimizer.minimize(problem)

with tf.Session() as session:
  session.run(tf.global_variables_initializer())
  for ii in xrange(1000):
    session.run(train_op)

  trained_weights, trained_threshold = session.run((weights, threshold))

trained_predictions = np.matmul(features, trained_weights) - trained_threshold
print("Constrained average hinge loss = %f" % average_hinge_loss(labels, trained_predictions))
print("Constrained recall = %f" % recall(labels, trained_predictions))


