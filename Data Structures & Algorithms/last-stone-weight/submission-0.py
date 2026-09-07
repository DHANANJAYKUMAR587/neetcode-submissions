class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq
        while len(stones)>1:
            heap=[]
            for i in stones:
                heapq.heappush(heap,i)
            a,b=heapq.nlargest(2,heap)
            stones.remove(a)
            stones.remove(b)
            if a!=b:
                stones.append(a-b)
        return sum(stones)