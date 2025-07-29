<h2><a href="https://www.geeksforgeeks.org/problems/count-frequency-of-an-element-in-a-given-range/1">Count Frequency of an Element in a Given Range</a></h2><h3>Difficulty Level : Difficulty: Medium</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size: 14pt;">Given an array <strong>arr[] </strong>of integers and a 2D array <strong>queries[][]</strong>, where each queries[i] consists of three integers: l, r, and x. Your task is to determine, for each query, how many times the element <strong>x</strong> appears in the arr[] from index <strong>l</strong> to <strong>r</strong> (both inclusive).</span><br><span style="font-size: 14pt;">Return a list of integers where the i-th value represents the answer to the i-th query.</span></p>
<p><span style="font-size: 14pt;"><strong>Examples:&nbsp;</strong></span></p>
<pre><span style="font-size: 14pt;"><strong>Input:</strong> arr[] = [1, 2, 1, 3, 1, 2, 3], queries[][] = [[0, 4, 1], [2, 5, 2], [1, 6, 3], [0, 6, 5]]
<strong>Output:</strong> [3, 1, 2, 0]
<strong>Explanation:</strong>
query [0, 4, 1] → Subarray = [1, 2, 1, 3, 1], 1 appears 3 times
query [2, 5, 2] → Subarray = [1, 3, 1, 2], 2 appears 1 time
query [1, 6, 3] → Subarray = [2, 1, 3, 1, 2, 3] 3 appears 2 times
query [0, 6, 5] → Subarray = [1, 2, 1, 3, 1, 2, 3],  5 appears 0 times</span></pre>
<pre><span style="font-size: 14pt;"><strong>Input:</strong> arr[] = [11, 21, 51, 101, 11, 51], queries[][] = [[0, 4, 11], [2, 5, 51]]
<strong>Output:</strong> [2, 2]
<strong>Explanation:</strong>
query [0, 4, 11] → Subarray = [11, 21, 51, 101, 11], 11 appears 2 times
query [2, 5, 51] → Subarray = [51, 101, 11, 51], 51 appears 2 times<br></span></pre>
<p><strong><span style="font-size: 14pt;">Constraints:<br></span></strong><span style="font-size: 14pt;">1 ≤ arr.size(), queries.size() ≤ 10<sup>5</sup><br>1 ≤ arr[i], queries[i][2] ≤ 10<sup>8</sup><br>0 ≤&nbsp;</span><span style="font-size: 18.6667px;">queries[i][0] ≤ queries[i][1] &lt; arr.size()</span></p></div><br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Binary Search</code>&nbsp;<code>Map</code>&nbsp;<code>Data Structures</code>&nbsp;<code>Algorithms</code>&nbsp;