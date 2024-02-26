//{ Driver Code Starts
//Initial Template for Java

import java.util.*;
import java.lang.*;
import java.io.*;
class GFG
{
    public static void main(String[] args) throws IOException
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine().trim());
        while(T-->0)
        {
            String s = br.readLine().trim();
            Solution ob = new Solution();
            List<String> ans = ob.AllPossibleStrings(s);
            for(String i: ans)
                System.out.print(i + " ");
            System.out.println();
            
        }
    }
}

// } Driver Code Ends


//User function Template for Java



//User function Template for Java

class Solution
{
    public List<String> AllPossibleStrings(String s)
    {
        // Code here
        List<String> list = new ArrayList<>();
        solve(s,"", list);
        Collections.sort(list);
        list.remove("");
        return list;
    }
    public void solve(String s , String ans,List<String> list){
        if(s.length()==0){
            list.add(ans);
            return;
        }
           char ch = s.charAt(0);
          String ros = s.substring(1);
          solve(ros,ans+"",list);
          solve(ros,ans+ch,list);
      return;
        
    
    }
}