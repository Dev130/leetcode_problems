class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        mod=10**9+7
        maxn=n
        fact=[1]*(maxn+1)
        invfact=[1]*(maxn+1)
        for i in range(1,maxn+1):
            fact[i]=fact[i-1]*i%mod
        invfact[maxn]=pow(fact[maxn],mod-2,mod)
        for i in range(maxn-1,-1,-1):
            invfact[i]=invfact[i+1]*(i+1)%mod
        def comb(a,b):
            if b<0 or b>a:
                return 0
            return fact[a]*invfact[b]%mod*invfact[a-b]%mod
        ways=comb(n-1,k)*m%mod
        ways=ways*pow(m-1,n-1-k,mod)%mod
        return ways