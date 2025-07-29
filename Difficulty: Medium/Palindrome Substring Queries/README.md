<h2><a href="https://www.geeksforgeeks.org/problems/palindrome-substring-queries/1">Palindrome Substring Queries</a></h2><h3>Difficulty Level : Difficulty: Medium</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size: 18.6667px;">Given a string <strong>s</strong> and a 2D list <strong>queries[][]</strong>, where each <strong>queries[i]</strong> consists of two integers <strong>[left, right]</strong>. Each query refers to the substring <strong>s[left : right]</strong>, where both left and right are inclusive (0-based indexing).</span></p>
<p><span style="font-size: 18.6667px;">For each query, find whether the substring <strong>s[left : right]</strong> forms a <strong>palindrome</strong>.</span></p>
<p><span style="font-size: 14pt;"><strong>Examples :</strong></span></p>
<pre><span style="font-size: 14pt;"><strong>Input: </strong>s = "abaaabaaaba", queries[][] = [[0, 10], [5, 8], [2, 5], [5, 9]]
<strong>Output:</strong> [1, 0, 0, 1]
<strong>Explanation</strong>: Lets process all the queries one by one:<br>[0, 10]: The substring is "abaaabaaaba" which is a palindrome.
[5, 8]: The substring is "baaa" which is not a palindrome.
[2, 5]: The substring is "aaab" which is not a palindrome. 
[5, 9]: The substring is "baaab" which is a palindrome.
</span></pre>
<pre><span style="font-size: 14pt;"><strong style="font-size: 14pt;">Input</strong><span style="font-size: 14pt;">: s = "abdcaaa", queries[][] = [[0, 1], [2, 2], [4, 6]]
</span><strong style="font-size: 14pt;">Output:</strong><span style="font-size: 14pt;"> [0, 1, 1]
</span><strong style="font-size: 14pt;">Explanation</strong><span style="font-size: 14pt;">: </span><span style="font-size: 18.6667px;">Lets process all the queries one by one:</span><span style="font-size: 14pt;"><br></span><span style="font-size: 18.6667px;">[0, 1]: The substring is "ab" which is not a palindrome.
[2, 2]: The substring is "d" which is a palindrome.
[4, 6]: The substring is "aaa" which is a palindrome.</span></span></pre>
<p><span style="font-size: 14pt;"><strong>Constraints:</strong><br>1 ≤ s.size() ≤ 10<sup>5<br></sup></span><span style="font-size: 14pt;"><span style="font-size: 14pt;">1 ≤ queries.size() ≤ 10</span><sup style="font-size: 14pt;">5</sup><br><span style="font-size: 14pt;">0 ≤ queries[i][0] ≤ queries[i][1] &lt; s.size()</span><br><span style="font-size: 18.6667px;">s consists of lowercase english alphabets</span></span></p></div><br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Strings</code>&nbsp;<code>Hash</code>&nbsp;<code>Algorithms</code>&nbsp;