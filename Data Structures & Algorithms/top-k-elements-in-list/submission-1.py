class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d=defaultdict(int)
        for i in nums:
            d[i]+=1
        print(d)
        sorted_d=dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
        r=[]
        
        for key,v in sorted_d.items():
            if k>0:
                r.append(key)
                k-=1

            
        return r
            
        