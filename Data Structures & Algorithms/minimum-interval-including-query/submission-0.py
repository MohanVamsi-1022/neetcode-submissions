class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        res = {}
        min_heap = []
        intervals.sort()
        i = 0
        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= q:
                start,end = intervals[i]
                heapq.heappush(min_heap,(end-start+1,end))
                i += 1
            while min_heap and min_heap[0][1] < q:
                heapq.heappop(min_heap)
            res[q] = min_heap[0][0] if min_heap else -1
        return [res[q] for q in queries]

