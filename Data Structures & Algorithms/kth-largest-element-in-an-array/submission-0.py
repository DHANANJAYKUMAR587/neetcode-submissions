class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq
        heap=[]
        for i in nums:
            heapq.heappush(heap,i)
        return heapq.nlargest(k,heap)[-1]