<h2><a href="https://www.geeksforgeeks.org/problems/count-city-population-categories/1">Count City Population Categories</a></h2><h3>Difficulty Level : Difficulty: Easy</h3><hr><div class="problems_problem_content__Xm_eO"><h3 class="" data-start="231" data-end="255">Problem Description:</h3>
<p class="" data-start="257" data-end="367">Write a solution to calculate the number of cities in each population category. The population categories are:</p>
<ul data-start="369" data-end="619">
<li class="" data-start="369" data-end="444">
<p class="" data-start="371" data-end="444"><strong data-start="371" data-end="387">"Small City"</strong>: Cities with population strictly less than <strong data-start="431" data-end="443">1,00,000</strong>.</p>
</li>
<li class="" data-start="445" data-end="539">
<p class="" data-start="447" data-end="539"><strong data-start="447" data-end="464">"Medium City"</strong>: Cities with population in the inclusive range <strong data-start="512" data-end="538">[1,00,000, 10,00,000]</strong>.</p>
</li>
<li class="" data-start="540" data-end="619">
<p class="" data-start="542" data-end="619"><strong data-start="542" data-end="558">"Large City"</strong>: Cities with population strictly greater than <strong data-start="605" data-end="618">10,00,000</strong>.</p>
</li>
</ul>
<p class="" data-start="621" data-end="720">The result table must contain all three categories. If there are no cities in a category, return 0.</p>
<h3 class="" data-start="766" data-end="784">Pandas Schema:</h3>
<p><img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/894782/Web/Other/blobid1_1746687221.png" width="354" height="211"></p>
<ul data-start="939" data-end="1034">
<li class="" data-start="939" data-end="992">
<p class="" data-start="941" data-end="992"><strong data-start="941" data-end="952">city_id</strong>: Unique ID for each city (Primary key).</p>
</li>
<li class="" data-start="993" data-end="1034">
<p class="" data-start="995" data-end="1034"><strong data-start="995" data-end="1009">population</strong>: Population of the city.</p>
</li>
</ul>
<h3 class="" data-start="1041" data-end="1055">Example :</h3>
<p class="" data-start="1057" data-end="1073"><strong data-start="1057" data-end="1073">Input table:</strong></p>
<p class="" data-start="1057" data-end="1073"><strong data-start="1057" data-end="1073"><img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/894782/Web/Other/blobid2_1746687237.png" width="300" height="291"></strong></p>
<p class="" data-start="1334" data-end="1351"><strong data-start="1334" data-end="1351">Output table:</strong></p>
<p class="" data-start="1334" data-end="1351"><strong data-start="1334" data-end="1351"><img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/894782/Web/Other/blobid3_1746687251.png" width="434" height="218"></strong></p>
<h3 class="" data-start="1619" data-end="1635">Explanation:</h3>
<ul data-start="1637" data-end="1742">
<li class="" data-start="1637" data-end="1671">
<p class="" data-start="1639" data-end="1671"><strong data-start="1639" data-end="1653">Small City</strong>: city_id 1 and 5.</p>
</li>
<li class="" data-start="1672" data-end="1707">
<p class="" data-start="1674" data-end="1707"><strong data-start="1674" data-end="1689">Medium City</strong>: city_id 2 and 4.</p>
</li>
<li class="" data-start="1708" data-end="1742">
<p class="" data-start="1710" data-end="1742"><strong data-start="1710" data-end="1724">Large City</strong>: city_id 3 and 6.</p>
</li>
</ul></div>