class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        
        i = 0
        l = len(intervals)
        merge = False
        while i < l:
            start = newInterval[0]
            end = newInterval[1]
            if intervals[i][0] > end:
                intervals.insert(i, newInterval)
                merge = True
                break
            else:
                if start > intervals[i][1]:
                    i = i + 1
                else:
                    mi = min(start, intervals[i][0])
                    ma = max(end, intervals[i][1])
                    newInterval[0] = mi
                    newInterval[1] = ma
                    del intervals[i]
                    l = len(intervals)
                    merge = True
                    if i == l:
                        intervals.append(newInterval)
        if not merge:
            intervals.append(newInterval)
        
        return intervals