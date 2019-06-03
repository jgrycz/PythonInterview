# -*- coding: utf-8 -*-
"""
:author: Jaroslaw Grycz
:contact: jaroslaw.grycz@gmail.com
"""
# 1. Zaimplementuj sortowanie bąbelkowe

nums = [5, 4, 3, 2, 1]


def bubble_sort(nums):
    length = len(nums) - 1
    index = 0
    sorted = False  # no sorting happened yet
    while not sorted:
        sorted = True  # assume that list should be sorted by now
        for index in range(0, length):
            if nums[index] > nums[index + 1]:
                sorted = False  # we found 2 elements that were not sorted
                temp = nums[index]
                nums[index] = nums[index + 1]
                nums[index + 1] = temp
    print(nums)


if __name__ == "__main__":
    bubble_sort([1, 2, 3, 4, 5, 6, 1])
