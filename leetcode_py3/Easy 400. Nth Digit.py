# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/3/18
File:   Easy 400. Nth Digit.py
"""
'''
Find the nth digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...

Note:
n is positive and will fit within the range of a 32-bit signed integer (n < 2^31).

Example 1:
Input:
3
Output:
3

Example 2:
Input:
11
Output:
0

Explanation:
The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, 
which is part of the number 10.
'''


class Solution:
    def findNthDigit(self, n: int) -> int:
        num_length = 1
        count = 9
        start = 1
        while n > num_length * count:
            n -= num_length * count
            start *= 10
            count *= 10
            num_length += 1
        start += (n - 1) // num_length
        return int(str(start)[(n - 1) % num_length])


if __name__ == '__main__':
    s = Solution()
    print(s.findNthDigit(10))





