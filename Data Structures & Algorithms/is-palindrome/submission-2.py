class Solution:
    def isPalindrome(self, s: str) -> bool:
        t=''.join(c.lower() for c in s if c.isalnum())
        print(t)
        st=[]
        for c in t:
            st.append(c)
        for c in t:
            if c!=st.pop():
                return False
        return True

        

        