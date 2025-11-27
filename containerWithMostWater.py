class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        # # max water is max area 
        # area = 0
        # max_area = 0

        # # Simple solve is brute force
        # for p1 in range(0,len(height)):
        #     for p2 in range(0,len(height)):
        #         if p1 != p2:
        #             # calculate area = height * base
        #             area = min(height[p1],height[p2]) * (p2-p1)
        #             if area>max_area:
        #                 max_area = area
        
        # return max_area

        # second solution is sliding window much quicker
        p1 = 0
        p2 = len(height)-1
        area = 0
 
        while p1<p2:
            area = max(area, min(height[p1],height[p2])*(p2-p1))
            # water height is limited by which end is smaller
            if height[p1]<height[p2]:
                p1 +=1
            else:
                p2 -= 1
        return area