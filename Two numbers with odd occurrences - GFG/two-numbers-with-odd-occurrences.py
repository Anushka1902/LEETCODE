#User function Template for python3
class Solution:
    def twoOddNum(self, Arr, N):
        # code here
        xor2=Arr[0]
        set_bit=0
        n=N-2
        x,y=0,0
        for i in range(1,N):
            xor2=xor2^Arr[i]
        set_bit=xor2&~(xor2-1)
        for i in range(N):
            if (Arr[i]&set_bit):
                x=x^Arr[i]
            else:
                y=y^Arr[i]
        if y>x:
            t=x
            x=y
            y=t
        return x,y

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        N = int(input())
        Arr = input().split()
        for itr in range(N):
            Arr[itr] = int(Arr[itr])
        ob = Solution();
        ans = ob.twoOddNum(Arr,N)
        for i in range(len(ans)):
        	print(ans[i], end = " ")
        print()
# } Driver Code Ends