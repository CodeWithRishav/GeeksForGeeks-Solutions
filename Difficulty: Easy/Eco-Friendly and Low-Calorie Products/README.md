<h2><a href="https://www.geeksforgeeks.org/problems/eco-friendly-and-sugar-free-products/1">Eco-Friendly and Low-Calorie Products</a></h2><h3>Difficulty Level : Difficulty: Easy</h3><hr><div class="problems_problem_content__Xm_eO"><h3><span style="font-size: 14pt;">Problem Description:</span></h3>
<p><span style="font-size: 14pt;">Write a solution to find the <strong>product_id</strong>, <strong>product_name</strong>, and <strong>calories</strong> of all products that are <strong>eco-friendly</strong> and have <strong>low calories</strong>.</span></p>
<ul>
<li>
<p><span style="font-size: 14pt;">A product is considered <strong>eco-friendly</strong> if the <strong>eco_friendly</strong> field has a value of 'Y'.</span></p>
</li>
<li>
<p><span style="font-size: 14pt;">A product is considered to have <strong>low calories</strong> if the <strong>calories</strong> are less than or equal to 200.</span></p>
</li>
</ul>
<p><span style="font-size: 14pt;">Return the result table in any order.</span></p>
<h3><span style="font-size: 14pt;">Pandas Schema:</span></h3>
<p><span style="font-size: 14pt;"><img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/895027/Web/Other/blobid0_1747028596.png" width="418" height="231"></span></p>
<ul>
<li>
<p style="font-weight: 400;"><span style="color: #000000; font-size: 14pt;"><strong>product_id:</strong> Unique ID for each product (Primary key).</span></p>
</li>
<li>
<p><span style="font-size: 14pt;"><strong>product_name</strong>: Name of the product.</span></p>
</li>
<li><span style="font-size: 14pt;"><strong>eco_friendly</strong>: An enum indicating whether the product is eco-friendly ('Y' for Yes, 'N' for No).</span></li>
<li>
<p><span style="font-size: 14pt;"><strong>calories</strong>: The number of calories in the product (integer value).</span></p>
</li>
</ul>
<h3><span style="font-size: 14pt;">Task:</span></h3>
<p><span style="font-size: 14pt;">Write a solution to find the <strong>product_id</strong>, <strong>product_name</strong>, and <strong>calories</strong> of all products that are <strong>eco-friendly</strong> and have <strong>low calories</strong>.</span></p>
<h3><span style="font-size: 14pt;">Example :</span></h3>
<p><span style="font-size: 14pt;"><strong>Input table:</strong></span></p>
<p><span style="font-size: 14pt;"><strong><img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/895027/Web/Other/blobid1_1747028608.png" width="695" height="265"></strong></span></p>
<p><span style="font-size: 14pt;"><strong>Output table:</strong></span></p>
<p><span style="font-size: 14pt;"><strong><img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/895027/Web/Other/blobid2_1747028620.png" width="565" height="226"></strong></span></p>
<p><span style="font-size: 14pt;"><strong>Explanation</strong>:</span></p>
<ul>
<li>
<p><span style="font-size: 14pt;"><strong>Product 1 (Green Juice)</strong>: It is eco-friendly and has 150 calories (which is low).</span></p>
</li>
<li>
<p><span style="font-size: 14pt;"><strong>Product 3 (Organic Snack)</strong>: It is eco-friendly and has 120 calories (which is low).</span></p>
</li>
<li>
<p><span style="font-size: 14pt;"><strong>Product 5 (Eco Water)</strong>: It is eco-friendly and has 50 calories (which is low).</span></p>
</li>
<li>
<p><span style="font-size: 14pt;"><strong>Products 2 and 4</strong>: Either not eco-friendly or have more than 200 calories.</span></p>
</li>
</ul></div>