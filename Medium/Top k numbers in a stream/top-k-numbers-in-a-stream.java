//{ Driver Code Starts
import java.io.*;
import java.util.*;


class IntArray
{
    public static int[] input(BufferedReader br, int n) throws IOException
    {
        String[] s = br.readLine().trim().split(" ");
        int[] a = new int[n];
        for(int i = 0; i < n; i++)
            a[i] = Integer.parseInt(s[i]);

        return a;
    }

    public static void print(int[] a)
    {
        for(int e : a)
            System.out.print(e + " ");
        System.out.println();
    }

    public static void print(ArrayList<Integer> a)
    {
        for(int e : a)
            System.out.print(e + " ");
        System.out.println();
    }
}


class IntMatrix
{
    public static int[][] input(BufferedReader br, int n, int m) throws IOException
    {
        int[][] mat = new int[n][];

        for(int i = 0; i < n; i++)
        {
            String[] s = br.readLine().trim().split(" ");
            mat[i] = new int[s.length];
            for(int j = 0; j < s.length; j++)
                mat[i][j] = Integer.parseInt(s[j]);
        }

        return mat;
    }

    public static void print(int[][] m)
    {
        for(var a : m)
        {
            for(int e : a)
                System.out.print(e + " ");
            System.out.println();
        }
    }

    public static void print(ArrayList<ArrayList<Integer>> m)
    {
        for(var a : m)
        {
            for(int e : a)
                System.out.print(e + " ");
            System.out.println();
        }
    }
}

class GFG {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t;
        t = Integer.parseInt(br.readLine());
        while(t-- > 0){
            
            String St[] = br.readLine().split(" ");
            int N = Integer.parseInt(St[0]);
            int K = Integer.parseInt(St[1]);
           
            int[] arr = IntArray.input(br, N);
            
            Solution obj = new Solution();
            ArrayList<ArrayList<Integer>> res = obj.kTop(arr, N, K);
            
            IntMatrix.print(res);
            
        }
    }
}

// } Driver Code Ends



class Solution {
    public static ArrayList<ArrayList<Integer>> kTop(int[] arr, int n, int k) {
        // code here
        ArrayList<ArrayList<Integer>> res = new ArrayList<>();
        Map<Integer,Integer> map = new HashMap<>();
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>((a,b)->{
            if(map.get(a)!=map.get(b))
                return map.get(b) - map.get(a);
            else
                return a - b;
        });
        
        ArrayList<Integer> temp = new ArrayList<>();
        for(int ele:arr){
            map.put(ele,map.getOrDefault(ele,0)+1);
            maxHeap = new PriorityQueue<>((a,b)->{
                if(map.get(a)!=map.get(b))
                    return map.get(b) - map.get(a);
                else
                    return a - b;
            });
            for(int key:map.keySet()){
                maxHeap.add(key);
            }
            int tempK = k;
            temp.clear();
            while(tempK>0 && !maxHeap.isEmpty()){
                int a = maxHeap.poll();
                temp.add(a);
                tempK--;
            }
            res.add(new ArrayList<>(temp));
        }
        return res;
    }
}
        
