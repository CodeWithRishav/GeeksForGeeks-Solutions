//{ Driver Code Starts
//Initial Template for Java

import java.io.*;
import java.util.*;
class GfG
{
    public static void main (String[] args)
    {
        
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        
        while(t-- > 0)
        {
            String s = sc.next ();
            int k = sc.nextInt();
    		System.out.println (new Solution().substrCount (s, k));
        }
        
    }
}
// } Driver Code Ends

class Solution
{
    long atMostK (String s, int k)
    {
        //if k is less than 0, return 0
        if (k < 0) return 0;

        //initialize variables
        int i = 0, j = 0, cnt = 0;
        long res = 0;
        int[] m = new int[26];

        //loop until the end of the string
        while (j < s.length ())
        {
            //increment frequency of current character
            m[(int)(s.charAt(j) - 'a')]++;
            
            //if frequency becomes 1, increase the count
            if (m[(int)(s.charAt(j) - 'a')] == 1) cnt++;

            //while the count is greater than k
            while (cnt > k)
            {
                //decrement frequency of character at start index
                m[(int)(s.charAt(i) - 'a')]--;
                
                //if frequency becomes 0, decrease the count
                if (m[(int)(s.charAt(i) - 'a')] == 0) cnt--;

                //move the start index to the right
                i++;
            }

            //calculate the number of substrings with at most k distinct characters
            res += (j - i + 1);
            //move the end index to the right
            j++;
        }
        //return the result
        return res;
    }

    long substrCount (String s, int k)
    {
        //return the difference between the number of substrings with at most k distinct characters
        //and the number of substrings with at most k-1 distinct characters
        return atMostK (s, k) - atMostK (s, k - 1);
    }



}