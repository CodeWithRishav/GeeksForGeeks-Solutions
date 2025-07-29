<h2><a href="https://www.geeksforgeeks.org/problems/invalid-comments/1">Invalid Comments</a></h2><h3>Difficulty Level : Difficulty: Easy</h3><hr><div class="problems_problem_content__Xm_eO"><h3 class="" data-start="35" data-end="59">Problem Description:</h3>
<p class="" data-start="61" data-end="233">Write a solution to find the IDs of the invalid comments. The comment is invalid if the number of characters used in the content of the comment is strictly greater than 20.</p>
<p class="" data-start="274" data-end="292"><strong data-start="274" data-end="292">Pandas Schema:</strong></p>
<p class="" data-start="274" data-end="292"><img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/894934/Web/Other/blobid3_1746698149.png" width="321" height="203"></p>
<ul data-start="477" data-end="662">
<li class="" data-start="477" data-end="538">
<p class="" data-start="479" data-end="538"><strong data-start="479" data-end="493">comment_id</strong>: The unique ID of the comment (Primary key).</p>
</li>
<li class="" data-start="539" data-end="662">
<p class="" data-start="541" data-end="662"><strong data-start="541" data-end="552">content</strong>: The content of the comment (contains alphanumeric characters, '!', and ' ' and no other special characters).</p>
</li>
</ul>
<h3 class="" data-start="664" data-end="673">Task:</h3>
<p class="" data-start="675" data-end="830">Write a solution to find the <strong data-start="704" data-end="718">comment_id</strong> of all invalid comments. A comment is invalid if the <strong data-start="772" data-end="783">content</strong> length is strictly greater than 20 characters.</p>
<h3 class="" data-start="837" data-end="851">Example :</h3>
<p class="" data-start="853" data-end="869"><strong data-start="853" data-end="869">Input table:</strong></p>
<p class="" data-start="853" data-end="869"><strong data-start="853" data-end="869"><img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/problem_desc/Web/Other/blobid1_1746697916.png" width="575" height="170"></strong></p>
<p class="" data-start="1198" data-end="1215"><strong data-start="1198" data-end="1215">Output table:</strong></p>
<p class="" data-start="1198" data-end="1215"><strong data-start="1198" data-end="1215"><img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/problem_desc/Web/Other/blobid0_1746697897.png" width="196" height="158"></strong></p>
<p class="" data-start="1301" data-end="1317"><strong data-start="1301" data-end="1316">Explanation</strong>:</p>
<ul data-start="1318" data-end="1460">
<li class="" data-start="1318" data-end="1387">
<p class="" data-start="1320" data-end="1387"><strong data-start="1320" data-end="1333">Comment 1</strong> has a length of 17 characters. It is a valid comment.</p>
</li>
<li class="" data-start="1388" data-end="1460">
<p class="" data-start="1390" data-end="1460"><strong data-start="1390" data-end="1403">Comment 2</strong> has a length of 38 characters. It is an invalid comment.</p>
</li>
</ul></div>