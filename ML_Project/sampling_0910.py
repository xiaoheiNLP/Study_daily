# -*-coding:utf-8-*-
import tensorflow as tf


with tf.variable_scope(tf.get_variable_scope()):
    for i in xrange(FLAGS.num_gpus):
        with tf.device('/gpu:%d' % i):
            with tf.name_scope('%s_%d' % (cifar10.TOWER_NAME, i)) as scope:
                # Dequeues one batch for the GPU
                image_batch, label_batch = batch_queue.dequeue()
                # Calculate the loss for one tower of the CIFAR model. This function
                # constructs the entire CIFAR model but shares the variables across
                # all towers.
                loss = tower_loss(scope, image_batch, label_batch)
                # Reuse variables for the next tower.
                tf.get_variable_scope().reuse_variables()

                # Retain the summaries from the final tower.
                summaries = tf.get_collection(tf.GraphKeys.SUMMARIES, scope)

                # Calculate the gradients for the batch of data on this CIFAR tower.
                grads = opt.compute_gradients(loss)

                # Keep track of the gradients across all towers.
                tower_grads.append(grads)

    # We must calculate the mean of each gradient. Note that this is the
    # synchronization point across all towers.

grads = average_gradients(tower_grads)
# Add a summary to track the learning rate.
summaries.append(tf.summary.scalar('learning_rate', lr))