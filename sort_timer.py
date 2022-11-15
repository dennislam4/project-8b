# Author: Dennis Lam
# GitHub username: dennislam4
# Date: 11-14-2022
# Description: Decorator function that uses the time, random, and fucntools modules as well as the matplotlib package
# from the pyplot library. The function records the time in seconds for it to take the decorated function to run.

import time
import random
from matplotlib import pyplot
import functools


def sort_timer(func):
    """
    Decorator function that times how many seconds it takes for function to run.
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        """
        wrapper
        """
        beggining = time.perf_counter()
        func(*args, **kwargs)
        end = time.perf_counter()
        time_elapsed = end - beggining
        return time_elapsed

    return wrapper


@sort_timer
def bubble_sort(a_list):
    """
    Sorts a_list in ascending order using bubble sort.
    """
    for pass_num in range(len(a_list) - 1):
        for index in range(len(a_list) - 1 - pass_num):
            if a_list[index] > a_list[index + 1]:
                temp = a_list[index]
                a_list[index] = a_list[index + 1]
                a_list[index + 1] = temp


@sort_timer
def insertion_sort(a_list):
    """
    Decorated insertion sort function that sorts a_list in ascending order.
    """
    for index in range(1, len(a_list)):
        value = a_list[index]
        pos = index - 1
        while pos >= 0 and a_list[pos] > value:
            a_list[pos + 1] = a_list[pos]
            pos -= 1
            a_list[pos + 1] = value


def compare_sorts(bubble_func, insertion_func):
    """
    Function that compares the times it takes for bubble and insertion sort functions to finish in seconds. Red line
    represents the bubble_sort function and the green line represents the insertion_sort.
    """
    bubble_y = []
    insertion_y = []
    x_axis = []
    for element in range(1000, 10001, 1000):
        list_1 = []
        pass
        for index in range(element):
            numbers = random.randint(1, 10000)
            list_1.append(numbers)
        list_2 = list(list_1)
        x_axis.append(element)
        bubble_y.append(bubble_func(list_1))
        insertion_y.append(insertion_func(list_2))
    pyplot.plot(x_axis, bubble_y, 'ro--', linewidth=2, label='series 1')
    pyplot.plot(x_axis, insertion_y, 'go--', linewidth=2, label='series 2')
    pyplot.xlabel("Number of Elements Being Sorted")
    pyplot.ylabel("Time(seconds)")
    pyplot.legend(loc='upper left')
    pyplot.show()


def display_plot():
    """
    Method to display plot generated from compare_sorts.
    """
    compare_sorts(bubble_sort, insertion_sort)
    return


display_plot()
