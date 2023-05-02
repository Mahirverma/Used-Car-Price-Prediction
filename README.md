# Used-Car-Price-Prediction
<br><br><h1>Introduction</h1>
<p>This project is based on the deployment of a machine learning model in API to predict the price of the used car.</p>
<p>It will  work on the basis of 12 features: Brand, Name, Location, Fuel Type, Transmission, Owner Type(First,Second,etc), Year(in which it was bought), Kilometers 
   Driven, Mileage, Engine, Power and Seats.</p>
<br><br>
<h1>How to use</h1>
<p>To use this api, just enter the data in respected blanks and click on the 'Predict' button to see the price</p>
<br><br>
<h1>Model Used</h1>
<p>Random Forest Regressor model is used in the above API. This model is used to predict the data as it works well with number type data.</p>
<br><br>
<h1>How categorial data was dealt?</h1>
<p>Binary Encoder function was used to deal with the categorial data. It conversts our aplhabetical data into a binary code series and trained accordingly to convert 
   any other categorial data.</p>
<br><br>
<h1>How was data normalize?</h1>
<p>Data was normalize by using another function known as Power Transoformer which will normalize the data equally to enhance the performance of the prediction model.</p>
<br><br>
<h1>Technology Used</h1>
<p>Technologies and libraries used in the above Project are:
   <ol>
      <li>Python Flask - for the API</li>
      <li>Python(libraries: Numpy, Pandas, Sklearn, Seaborn) - for the prediction Model</li>
      <li>Python(library: Pickle) - for deploying model into API</li>
   </ol>
     
  
