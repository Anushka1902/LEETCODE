#User function Template for python3

class Solution:
    def decodedString(self, s):
        # code here
        st =[]
        ans =""
        for i in s:
            if i!=']':
                st.append(i)
            else:
                tmp=""
                while(st and st[-1]!='['):
                    tmp+=st.pop(-1)
                st.pop(-1)
                tmp=tmp[::-1]
                x=""
                while(st and  '0'<=st[-1]<='9'):
                    k =st.pop(-1)
                    x=k+x
                x=int(x)
                tmp=tmp*x 
                for i in tmp:
                    st.append(i)
                    
        return ''.join(st)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        
        ob = Solution()
        print(ob.decodedString(s))
# } Driver Code Ends