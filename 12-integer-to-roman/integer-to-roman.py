class Solution:
    def intToRoman(self, n):
        v=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
        s=["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        r=""
        for i in range(13):
            while n>=v[i]:
                r+=s[i]
                n-=v[i]
        return r