<h2><a href="https://www.geeksforgeeks.org/problems/find-the-maximum-element-along-each-axses-in-a-3d-array/1">Find the Maximum Element along Each Axses in a 3D Array</a></h2><h3>Difficulty Level : Difficulty: Easy</h3><hr><div class="problems_problem_content__Xm_eO"><h3 class="" data-start="5280" data-end="5304"><span style="font-size: 14pt;">Problem Description:</span></h3>
<p class="" data-start="5305" data-end="5390"><span style="font-size: 14pt;">Given a 3D Numpy array, write a function to find the maximum element along each axis.</span></p>
<h3 class="" data-start="5392" data-end="5409"><span style="font-size: 14pt;">Numpy Schema:</span></h3>
<p class="" data-start="5410" data-end="5452"><span style="font-size: 14pt;">You are given a 3-dimensional Numpy array.</span></p>
<h3 class="" data-start="5454" data-end="5466"><span style="font-size: 14pt;">Example:</span></h3>
<p class="" data-start="5468" data-end="5478"><span style="font-size: 14pt;"><strong data-start="5468" data-end="5478">Input:</strong></span></p>
<blockquote>
<pre data-start="5468" data-end="5478"><span style="font-size: 14pt;"><strong>array = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])</strong></span></pre>
</blockquote>
<p class="" data-start="5549" data-end="5560"><span style="font-size: 14pt;"><strong data-start="5549" data-end="5560">Output:</strong></span></p>
<blockquote>
<pre data-start="5549" data-end="5560"><strong><span style="font-size: 18.6667px;">Maximum along axis 0:
[[ 7  8  9]
 [10 11 12]]
Maximum along axis 1:
[[ 4  5  6]
 [10 11 12]]
Maximum along axis 2:
[[ 3  6]
 [ 9 12]]</span></strong></pre>
</blockquote>
<p class="" data-start="5600" data-end="5679"><span style="font-size: 14pt;"><strong data-start="5600" data-end="5616">Explanation:</strong> </span></p>
<ul>
<li data-start="5600" data-end="5679"><span style="font-size: 14pt;">The maximum along axis 0&nbsp; is <strong>[ 7,&nbsp; 8,&nbsp; 9] ,</strong><strong>[ 10, 11, 12].</strong></span></li>
<li data-start="5600" data-end="5679"><span style="font-size: 14pt;">The maximum along axis 1&nbsp; is <strong>[ 4,&nbsp; 5,&nbsp; 6] ,</strong><strong>[ 10, 11, 12].</strong></span></li>
<li data-start="5600" data-end="5679"><span style="font-size: 14pt;"><strong><span style="font-weight: 400;">The maximum along axis 2&nbsp; is <strong>[ 3, 6] ,[ 9, 12]</strong> .</span></strong></span></li>
</ul></div>