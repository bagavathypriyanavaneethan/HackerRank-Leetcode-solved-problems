class Solution:
    def romanToInt(self, s: str) -> int:
        a = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        i=0
        no=0
        while(i<=len(s)-1):
            if s[i] in ('I','X','C'):
                if i<len(s)-1:
                    print("start")
                    if s[i]!=s[i+1] and ((s[i]=='I' and (s[i+1]=='V' or s[i+1]=='X')) or (s[i]=='X' and (s[i+1]=='L' or s[i+1]=='C')) or (s[i]=='C' and (s[i+1]=='D' or s[i+1]=='M'))):
                        print("A")
                        no = no + (a[s[i+1]]-a[s[i]])
                        i = i + 2 
                    elif s[i]!=s[i+1]:
                        no = no +a[s[i]]
                        i = i +1
                    elif s[i]==s[i+1]:
                        print("b")
                        no = no + a[s[i]] + a[s[i+1]]
                        i = i +2
                else:
                    print("c")
                    no = no + a[s[i]]
                    i = i+1
            else:
                print("d")
                no = no + a[s[i]]
                i = i + 1
        print(no)
        return no
            
        
