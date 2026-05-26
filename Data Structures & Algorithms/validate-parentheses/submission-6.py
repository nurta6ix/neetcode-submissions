class Solution:
    def isValid(self, s: str) -> bool:
        d = { "(" : ")", '[' : ']', '{' : '}'}
        isit = True

        if len(s) % 2 == 1 or len(s) == 0: return False

        for i in range(0, len(s) - 1, 2):
            try:
                if d[s[i]] != s[i+1]: 
                    isit = False
                    break
            except:
                isit = False
                break
        if isit: return isit

        isit = True

        for i in range(0, len(s)//2):
            try:
                if d[s[i]] != s[len(s)- i - 1]:
                    isit = False
                    break
            except:
                isit = False
                break

        return isit
        
        

