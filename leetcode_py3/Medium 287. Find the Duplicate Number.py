# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/2/14
File:   Medium 287. Find the Duplicate Number.py
"""
'''
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), 
prove that at least one duplicate number must exist. Assume that there is only one duplicate number, 
find the duplicate one.

Example 1:
Input: [1,3,4,2,2]
Output: 2

Example 2:
Input: [3,1,3,4,2]
Output: 3

Note:
You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n^2).
There is only one duplicate number in the array, but it could be repeated more than once.
'''


class Solution:
    def findDuplicate(self, nums: 'List[int]') -> 'int':
        length = len(nums)
        for i in range(length):
            dup = 0
            for num in nums:
                if i == num:
                    dup += 1
            if dup >= 2:
                return i


if __name__ == '__main__':
    s = Solution()
    print(s.findDuplicate([3, 1, 3, 4, 2]))
