class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()
        #print(people)
        
        i = 0
        l = len(people) - 1
        curr = 0
        count = 0
        ans = 0
        while i<l:
            if people[i] + people[l] <= limit:
                count = count + 1
                i = i + 1
                l = l - 1
            else:
                count = count + 1
                l = l - 1
        if i==l:
            count = count + 1
        return count 
        