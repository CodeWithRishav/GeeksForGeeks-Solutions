<h2><a href="https://www.geeksforgeeks.org/problems/rank-scores/1">Rank Scores</a></h2><h3>Difficulty Level : Difficulty: Easy</h3><hr><div class="problems_problem_content__Xm_eO"><h3 class="" data-start="35" data-end="59">Problem Description:</h3>
<p class="" data-start="61" data-end="200">Write a solution to find the rank of the scores from the <code data-start="118" data-end="126">Scores</code> table. The ranking should be calculated according to the following rules:</p>
<ul data-start="202" data-end="546">
<li class="" data-start="202" data-end="263">
<p class="" data-start="204" data-end="263">The scores should be ranked from the highest to the lowest.</p>
</li>
<li class="" data-start="264" data-end="338">
<p class="" data-start="266" data-end="338">If there is a tie between two scores, both should have the same ranking.</p>
</li>
<li class="" data-start="339" data-end="479">
<p class="" data-start="341" data-end="479">After a tie, the next ranking number should be the next consecutive integer value. In other words, there should be no holes between ranks.</p>
</li>
<li class="" data-start="480" data-end="546">
<p class="" data-start="482" data-end="546">The result table should be ordered by score in descending order.</p>
</li>
</ul>
<p class="" data-start="548" data-end="566"><strong data-start="548" data-end="566">Pandas Schema:</strong></p>
<p class="" data-start="548" data-end="566"><strong data-start="548" data-end="566"><img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/problem_desc/Web/Other/blobid0_1746686281.png" width="359" height="192"></strong></p>
<ul data-start="738" data-end="870">
<li class="" data-start="738" data-end="787">
<p class="" data-start="740" data-end="787"><strong data-start="740" data-end="746">id</strong>: Unique ID for each score (Primary key).</p>
</li>
<li class="" data-start="788" data-end="870">
<p class="" data-start="790" data-end="870"><strong data-start="790" data-end="799">score</strong>: The score of the game (floating point value with two decimal places).</p>
</li>
</ul>
<h3 class="" data-start="872" data-end="881">Task:</h3>
<p class="" data-start="883" data-end="963">Write a solution to rank the <strong data-start="912" data-end="922">scores</strong> according to the ranking rules provided.</p>
<h3 class="" data-start="1037" data-end="1051">Example 1:</h3>
<p class="" data-start="1053" data-end="1069"><strong data-start="1053" data-end="1069">Input table:</strong></p>
<p class="" data-start="1053" data-end="1069"><strong data-start="1053" data-end="1069"><img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/problem_desc/Web/Other/blobid1_1746686296.png" width="255" height="345"></strong></p>
<p class="" data-start="1230" data-end="1247"><strong data-start="1230" data-end="1247">Output table:</strong></p>
<p class="" data-start="1230" data-end="1247"><strong data-start="1230" data-end="1247"><img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/problem_desc/Web/Other/blobid2_1746686332.png" width="250" height="329"></strong></p>
<div class="contain-inline-size rounded-md border-[0.5px] border-token-border-medium relative bg-token-sidebar-surface-primary">
<div class="sticky top-9">
<div class="absolute end-0 bottom-0 flex h-9 items-center pe-2">&nbsp;</div>
</div>
</div>
<h3 data-start="1503" data-end="1519">Explanation:</h3>
<p class="" data-start="1709" data-end="1753">&nbsp;</p>
<ul data-start="1520" data-end="1808">
<li class="" data-start="1520" data-end="1567">
<p class="" data-start="1522" data-end="1567">The highest score is 9.50, so it gets rank 1.</p>
</li>
<li class="" data-start="1568" data-end="1622">
<p class="" data-start="1570" data-end="1622">The second highest score is 9.25, so it gets rank 2.</p>
</li>
<li class="" data-start="1623" data-end="1675">
<p class="" data-start="1625" data-end="1675">The next highest score is 9.00, so it gets rank 3.</p>
</li>
<li class="" data-start="1676" data-end="1761">
<p class="" data-start="1678" data-end="1761">The next distinct score is 8.75, which gets rank 4 (with two entries due to a tie).</p>
</li>
<li class="" data-start="1762" data-end="1808">
<p class="" data-start="1764" data-end="1808">The lowest score is 7.85, which gets rank 5.</p>
</li>
</ul></div>