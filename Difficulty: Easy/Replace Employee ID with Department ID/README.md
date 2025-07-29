<h2><a href="https://www.geeksforgeeks.org/problems/replace-employee-id-with-department-id/1">Replace Employee ID with Department ID</a></h2><h3>Difficulty Level : Difficulty: Easy</h3><hr><div class="problems_problem_content__Xm_eO"><h3>Problem Description:</h3>
<p>Write a solution to show the <strong>department ID</strong> of each employee. If an employee does not have a department ID, replace it with <strong>null</strong>.</p>
<p>Return the result table in any order.</p>
<p><strong>Pandas Schema:</strong></p>
<p><strong>Table: Employees</strong></p>
<p><strong><img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/problem_desc/Web/Other/blobid4_1746790083.png" width="297" height="153"></strong></p>
<ul>
<li>
<p><strong>id</strong>: The unique ID for each employee.</p>
</li>
<li>
<p><strong>name</strong>: The name of the employee.</p>
</li>
</ul>
<p><strong>Table: EmployeeDept</strong></p>
<p><strong><img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/problem_desc/Web/Other/blobid3_1746790074.png" width="294" height="153"></strong></p>
<ul>
<li>
<p><strong>id</strong>: The unique ID of the employee (Primary key).</p>
</li>
<li>
<p><strong>department_id</strong>: The department ID corresponding to the employee.</p>
</li>
</ul>
<p><strong>Task:</strong></p>
<p>Write a solution to show the <strong>department_id</strong> of each employee. If an employee does not have a <strong>department_id</strong>, show <strong>null</strong>.</p>
<h3>Example 1:</h3>
<p><strong>Input tables:</strong></p>
<p><strong>Employees table:</strong></p>
<p><strong><img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/problem_desc/Web/Other/blobid2_1746790062.png" width="221" height="273"></strong></p>
<p><strong>EmployeeDept table:</strong></p>
<p><strong><img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/problem_desc/Web/Other/blobid1_1746790051.png" width="230" height="228"></strong></p>
<p><strong>Output table:</strong></p>
<p><strong><img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/problem_desc/Web/Other/blobid0_1746790041.png" width="251" height="213"></strong></p>
<p><strong>Explanation</strong>:</p>
<ul>
<li>
<p><strong>Anurag</strong>, <strong>Jayan</strong>, <strong>Sahil</strong>, <strong>Ansh</strong>, and <strong>Ayushi</strong> all have a <strong>department_id</strong>.</p>
</li>
<li>
<p><strong>Kareena</strong> does not have a <strong>department_id</strong>, so <strong>null</strong> is shown for <strong>Kareena</strong>.</p>
</li>
</ul></div>