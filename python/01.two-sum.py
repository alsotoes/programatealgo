#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    def twoSum(self, nums, target):
        for i in nums:
            otherNumber = target -i
            try:
                if nums.index(i) != nums.index(otherNumber, nums.index(i)+1, len(nums)):
                    return [nums.index(i), nums.index(otherNumber, nums.index(i)+1, len(nums))]
            except ValueError:
                pass
        return [-1, -1]
