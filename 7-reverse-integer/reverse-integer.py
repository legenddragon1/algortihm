class Solution(object):
    def reverse(self, x):
        X= abs(x)
        
        X=str(X)
        Y=''
        for i in X:
            Y=  i+ Y 
        Y= int(Y)
        if Y<= 2**31 - 1:
            return Y if x>=0 else -Y
        else:
            return 0