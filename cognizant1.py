#You are given an integer array 'ARR' of size 'N' and an integer 'S'. Your task is to return the list of all pairs of elements such that each sum of elements of each pair equals 'S'.

#Note:

#Each pair should be sorted i.e the first value should be less than or equals to the second value. 

#Return the list of pairs sorted in non-decreasing order of their first value. In case if two pairs have the same first value, the pair with a smaller second value should come first.

from os import *
from sys import *
from collections import *
from math import *

def pairSum(arr, s):
    # Write your code here.
    n = int(input("Length"))
    arr = list(map(int, input("Enter the array elements separated by space: ").split()))
    s = int(input("Enter the target sum: "))

    i=0
    j=len(arr)-1
    pairs = []
    n 

    while i<j:
        if arr[i]+arr[j]==s:
            pairs.append(arr[i],arr[j])
            i = i+1
            j = j-1
        elif arr[i]+arr[j]<s:
            i = i+1
        else:
            j= j-1
    return pairs