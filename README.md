<div style="text-align: center;">
  <h1>Mars2042</h1>
</div>


<h1>Application of Function Fitting in Game Design</h1>
<p>$\textbf{Problem Description:}$ To create a mathematical function in a video game to model some behaviour is not easy from our experience, there might be some method that the industry has been using that we might not know. However, from our experience, it is hard to find the perfect function that describe exactly the dynamic of the game functions that we want.</p>

<p>$\textbf{Solution:}$ Manually generate datapoints over the interval in which we want the function to be defined. Then, uning the following method to approximate those datapoints, to create a function.</p>
    <ul>
      <li>Linear Regression</li>
      <li>Bernstein Polynomial</li>
      <li>Neural Network</li>
    </ul>
<p>The results of the above function approximation will be studied, and we will investigate their mean squared error</p>
We generally have 4 types of problems:
<ul>
  <li>High Dimensional Problem with High Linearity: Neural Network/Linear Regression</li> 
  <li>Low Dimensional Problem with Low Linearity: Neural Network/Bernstein Polynomial</li>
  <li>High Dimensionail Problem with Low Linearity: Neural Network/Bernstein Polynomial</li>
  <li>Low Dimensional Problem with High Linearity: Neural Network/Linear Regression</li>
</ul>
