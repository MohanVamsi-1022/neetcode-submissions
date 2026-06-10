class TimeMap:

    def __init__(self):
        self.mp = {}

    def binary_serach(self,arr,target):
        l, r = 0, len(arr)-1
        res = -1
        while l <= r:
            mid = l + (r - l) // 2
            if arr[mid][0] <= target:
                res = mid
                l = mid + 1
            else:
                r = mid - 1
        return res 
    
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.mp:
            self.mp[key] = []
        self.mp[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.mp:
            return ""
        val = self.mp[key]
        ans = self.binary_serach(val,timestamp)
        if ans != -1:
            return val[ans][1]
        else:
            return ""


        
