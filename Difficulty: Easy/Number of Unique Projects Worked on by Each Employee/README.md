<h2><a href="https://www.geeksforgeeks.org/problems/number-of-unique-projects-worked-on-by-each-employee/1">Number of Unique Projects Worked on by Each Employee</a></h2><h3>Difficulty Level : Difficulty: Easy</h3><hr><div class="problems_problem_content__Xm_eO"><h3 class="" data-start="71" data-end="95">Problem Description:</h3>
<p class="" data-start="97" data-end="200">Write a solution to calculate the number of unique projects each employee has worked on in the company.</p>
<p class="" data-start="202" data-end="368">Each employee works on several projects, and each project may belong to different departments. You need to find how many unique projects each employee is involved in.</p>
<p class="" data-start="370" data-end="388"><strong data-start="370" data-end="388">Pandas Schema:</strong></p>
<p class="" data-start="370" data-end="388"><strong data-start="370" data-end="388"><img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/problem_desc/Web/Other/blobid0_1746690952.png" width="325" height="211"></strong></p>
<ul data-start="581" data-end="742">
<li class="" data-start="581" data-end="632">
<p class="" data-start="583" data-end="632"><strong data-start="583" data-end="598">employee_id</strong>: The unique ID for each employee.</p>
</li>
<li class="" data-start="633" data-end="682">
<p class="" data-start="635" data-end="682"><strong data-start="635" data-end="649">project_id</strong>: The unique ID for each project.</p>
</li>
<li class="" data-start="683" data-end="742">
<p class="" data-start="685" data-end="742"><strong data-start="685" data-end="696">dept_id</strong>: The department ID where the project belongs.</p>
</li>
</ul>
<p class="" data-start="744" data-end="866">The combination of <strong data-start="763" data-end="777">project_id</strong> and <strong data-start="782" data-end="793">dept_id</strong> serves as a unique identifier for each project in a specific department.</p>
<h3 class="" data-start="868" data-end="877">Task:</h3>
<p class="" data-start="879" data-end="977">Write a solution to calculate the number of unique projects each employee works on in the company.</p>
<p class="" data-start="979" data-end="1081">Return the result table with <strong data-start="1008" data-end="1023">employee_id</strong> and the count of unique <strong data-start="1048" data-end="1062">project_id</strong> for each employee.</p>
<h3 class="" data-start="1088" data-end="1102">Example :</h3>
<p class="" data-start="1104" data-end="1120"><strong data-start="1104" data-end="1120">Input table:</strong></p>
<p class="" data-start="1104" data-end="1120"><strong data-start="1104" data-end="1120"><img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/problem_desc/Web/Other/blobid1_1746690968.png" width="452" height="321"></strong></p>
<p class="" data-start="1560" data-end="1577"><strong data-start="1560" data-end="1577">Output table:</strong></p>
<p class="" data-start="1560" data-end="1577"><strong data-start="1560" data-end="1577"><img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/problem_desc/Web/Other/blobid2_1746690992.png" width="302" height="200"></strong></p>
<p class="" data-start="1720" data-end="1736"><strong data-start="1720" data-end="1735">Explanation</strong>:</p>
<ul data-start="1737" data-end="1889">
<li class="" data-start="1737" data-end="1810">
<p class="" data-start="1739" data-end="1810"><strong data-start="1739" data-end="1753">Employee 1</strong>: Works on project 101, 102, and 103 (3 unique projects).</p>
</li>
<li class="" data-start="1811" data-end="1889">
<p class="" data-start="1813" data-end="1889"><strong data-start="1813" data-end="1827">Employee 2</strong>: Works on project 101, 102, 103, and 104 (4 unique projects).</p>
</li>
</ul></div>