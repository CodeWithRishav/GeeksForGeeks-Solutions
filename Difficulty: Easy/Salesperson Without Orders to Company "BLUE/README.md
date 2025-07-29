<h2><a href="https://www.geeksforgeeks.org/problems/salesperson-without-orders-to-company-blue/1">Salesperson Without Orders to Company "BLUE</a></h2><h3>Difficulty Level : Difficulty: Easy</h3><hr><div class="problems_problem_content__Xm_eO"><h3>Problem Description:</h3>
<p>Write a solution to find the names of all the salespersons who did not have any orders related to the company with the name "BLUE".</p>
<p>Return the result table in any order.</p>
<p><strong>Pandas Schema:</strong></p>
<p><strong>Table: SalesPerson</strong></p>
<p><strong><img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/problem_desc/Web/Other/blobid0_1746783329.png" width="295" height="225"></strong></p>
<ul>
<li>
<p><strong>sales_id</strong>: Unique ID for each salesperson (Primary key).</p>
</li>
<li>
<p><strong>name</strong>: The name of the salesperson.</p>
</li>
<li>
<p><strong>salary</strong>: The salary of the salesperson.</p>
</li>
<li>
<p><strong>commission_rate</strong>: The commission rate of the salesperson.</p>
</li>
<li>
<p><strong>hire_date</strong>: The hire date of the salesperson.</p>
</li>
</ul>
<p><strong>Table: Company</strong></p>
<p><strong><img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/problem_desc/Web/Other/blobid1_1746783347.png" width="278" height="187"></strong></p>
<ul>
<li>
<p><strong>com_id</strong>: Unique ID for each company (Primary key).</p>
</li>
<li>
<p><strong>name</strong>: The name of the company.</p>
</li>
<li>
<p><strong>city</strong>: The city where the company is located.</p>
</li>
</ul>
<p><strong>Table: Orders</strong></p>
<p><strong><img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/problem_desc/Web/Other/blobid2_1746783371.png" width="223" height="204"></strong></p>
<ul>
<li>
<p><strong>order_id</strong>: Unique ID for each order (Primary key).</p>
</li>
<li>
<p><strong>com_id</strong>: Foreign key referring to the <strong>Company</strong> table.</p>
</li>
<li>
<p><strong>sales_id</strong>: Foreign key referring to the <strong>SalesPerson</strong> table.</p>
</li>
<li>
<p><strong>order_date</strong>: The date of the order.</p>
</li>
<li>
<p><strong>amount</strong>: The amount of the order.</p>
</li>
</ul>
<h3>Task:</h3>
<p>Write a solution to find the <strong>name</strong> of all salespeople who did not have any orders related to the company named <strong>"BLUE"</strong>.</p>
<p>Return the result table with the <strong>name</strong> of the salesperson.</p>
<h3>Example:</h3>
<p><strong>Input tables:</strong></p>
<p><strong>SalesPerson table:</strong></p>
<p><strong><img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/problem_desc/Web/Other/blobid3_1746783416.png" width="589" height="231"></strong></p>
<p><strong>Company table:</strong></p>
<p><strong><img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/problem_desc/Web/Other/blobid4_1746783441.png" width="303" height="203"></strong></p>
<p><strong>Orders table:</strong></p>
<p><strong><img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/problem_desc/Web/Other/blobid5_1746783488.png" width="538" height="237"></strong></p>
<p><strong>Output table:</strong></p>
<p><strong><img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/894962/Web/Other/blobid13_1746784738.png" width="122" height="226"></strong></p>
<p><strong>Explanation</strong>:</p>
<ul>
<li>
<p><strong>Sarah</strong> , <strong>Bob </strong>and <strong>Tom</strong> did not have any sales related to <strong>BLUE</strong>, so they are included in the output.</p>
</li>
</ul></div>