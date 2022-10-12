#User function Template for python3

class Solution:
    def cutRod(self, price, n):
        #code here
        INT_min=-3267
        val=[0 for _ in range(n+1)]
        val[0]=0
        for i in range(1,n+1):
            max_val=INT_min
            for j in range(i):
                max_val=max(max_val,price[j]+val[i-j-1])
            val[i]=max_val
        return val[n]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.cutRod(a, n))

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends