# -*-coding:utf-8-*-


def bubble_sort_1(mylist):
    print()
    for i in range(len(mylist)):
        print(mylist[i])
        for j in range(0, len(mylist)):
            if mylist[i] > mylist[j]:
                print(mylist)
                temp = mylist[i]
                mylist[i] = mylist[j]
                mylist[j] = temp
                # (mylist[i], mylist[j]) = (mylist[j], mylist[i])
                print(mylist)
        print()
    return (mylist)


def bubble_sort_2(mylist):
    for i in range(len(mylist)):
        for j in range(len(mylist)):
            if mylist[i] < mylist[j]:
                temp = mylist[i]
                mylist[i] = mylist[j]
                mylist[j] = temp

    return mylist


def bubble_sort_3(mylist):
    for i in range(len(mylist)):
        for j in range(len(mylist) - 1 - i):
            if mylist[j] > mylist[j+1]:
                (mylist[j], mylist[j+1]) = (mylist[j+1], mylist[j])
    return mylist



def bubble_sort_4(mylist):
    for i in range(len(mylist)):
        for j in range(len(mylist) - 1 - i):
            if mylist[j] < mylist[j+1]:
                (mylist[j], mylist[j+1]) = (mylist[j+1], mylist[j])

    return mylist


if __name__ == '__main__':
    print("冒泡排序的实现")
    mylist = [1, 4, 6, 5, 2, 8, 7, 7, 9, 3]
    print(bubble_sort_4(mylist))

    # print(mylist)
    #
    # print(sorted(mylist))
    # print(mylist)

    # mylist.sort()
    # print(mylist)
