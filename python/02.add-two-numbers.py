#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        extra = 0
        result = None
        solutionList = None

        while not (None == l1 and None == l2) or extra !=0:
            if None == result or None == solutionList:
                result = ListNode(0)
                solutionList = result
            else:
                result.next = ListNode(0)
                result = result.next

            l1value = l1.val if l1 != None else 0
            l2value = l2.val if l2 != None else 0
            sum = l1value + l2value + extra

            result.value = sum if sum < 10 else sum-10

            ##"""
            if sum < 10:
                result.val = sum
                extra = 0
            else:
                result.val = sum-10
                extra = 1
            ##"""
            #extra = sum//10

            l1 = None if None == l1 else l1.next
            l2 = None if None == l2 else l2.next

        return solutionList
