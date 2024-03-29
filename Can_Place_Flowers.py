"""
    
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.
Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new 
flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.


Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false

"""

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        planted = 0
        i = 0
        while i < len(flowerbed):
            # Check if the current plot is empty.
            if flowerbed[i] == 0:
                # Check the left plot or if it's the first plot.
                left_empty = (i == 0) or (flowerbed[i - 1] == 0)
                # Check the right plot or if it's the last plot.
                right_empty = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)
                
                if left_empty and right_empty:
                    flowerbed[i] = 1  # Plant the flower here.
                    planted += 1  # Increment the number of planted flowers.
                    i += 2  # Move two plots over.
                    continue  # Skip to the next iteration of the loop.

            i += 1  # Move to the next plot.

        return planted >= n