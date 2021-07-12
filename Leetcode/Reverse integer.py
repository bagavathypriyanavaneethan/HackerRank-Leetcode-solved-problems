class Solution:
    def reverse(self, x: int) -> int:
        no = str(x)
        x = str(abs(x))
        a=''
        for i in range(len(x)-1,-1,-1):
            a = a+x[i]
        if no[0]=='-':
            a=no[0]+a
            if int(a) in range(-2**31,2**31,1):
                return int(a)
            elif int(a) not in range(-2**31,2**31,1):
                return 0
        else:
            if int(a) in range(-2**31,2**31,1):
                return int(a) 
            elif int(a) not in range(-2**31,2**31,1):
                return 0
            
        
