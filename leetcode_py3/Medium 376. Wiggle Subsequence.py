# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/3/15
File:   Medium 376. Wiggle Subsequence.py
"""
from typing import List

'''
A sequence of numbers is called a wiggle sequence if the differences between successive numbers 
strictly alternate between positive and negative. The first difference (if one exists) may be 
either positive or negative. A sequence with fewer than two elements is trivially a wiggle sequence.

For example, [1,7,4,9,2,5] is a wiggle sequence because the differences (6,-3,5,-7,3) 
are alternately positive and negative. In contrast, [1,4,7,2,5] and [1,7,4,5,5] are not 
wiggle sequences, the first because its first two differences are positive and the second 
because its last difference is zero.

Given a sequence of integers, return the length of the longest subsequence that is 
a wiggle sequence. A subsequence is obtained by deleting some number of elements 
(eventually, also zero) from the original sequence, leaving the remaining elements 
in their original order.

Example 1:
Input: [1,7,4,9,2,5]
Output: 6
Explanation: The entire sequence is a wiggle sequence.

Example 2:
Input: [1,17,5,10,13,15,10,5,16,8]
Output: 7
Explanation: There are several sub-sequences that achieve this length. One is [1,17,10,13,10,16,8].

Example 3:
Input: [1,2,3,4,5,6,7,8,9]
Output: 2

Follow up:
Can you do it in O(n) time?
'''


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        up = [0 for _ in range(len(nums))]
        down = [0 for _ in range(len(nums))]
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    up[i] = max(up[i], down[j] + 1)
                elif nums[i] < nums[j]:
                    down[i] = max(down[i], up[j] + 1)
        return 1 + max(up[-1], down[-1])

    def wiggleMaxLength2(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        up = [0 for _ in range(len(nums))]
        down = [0 for _ in range(len(nums))]
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                up[i] = up[i - 1]
                down[i] = up[i - 1] + 1
            elif nums[i] < nums[i - 1]:
                up[i] = down[i - 1] + 1
                down[i] = down[i - 1]
            else:
                up[i] = up[i - 1]
                down[i] = down[i - 1]
        return max(up[-1], down[-1]) + 1


if __name__ == '__main__':
    s = Solution()
    print(s.wiggleMaxLength2([1]))
