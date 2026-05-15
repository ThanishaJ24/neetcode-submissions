class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        r={}
        for i in strs:
            key=''.join(sorted(i))
            if key not in r:
                r[key]=[]
            r[key].append(i)

        return list(r.values())    
