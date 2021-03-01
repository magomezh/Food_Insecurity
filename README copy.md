# On the U.S. County Level, is Distance to Food Banks a Predictor for Food Insecurity?


![InstacartShopper](Images/Instacart_Shopper.png)

## Background
___

Food banks have been a staple of citizenship and generosity in America for decades. As we all know, the COVID-19 pandemic has caused a public health and economic crisis, and the effects of these are extensive.

The repercussions will include an increase in hardship for those populations who were already vulnerable, including the number of people experiencing food insecurity. Food insecurity is defined as “the state of being without reliable access to a sufficient quantity of affordable, nutritious food.” According to the United Nations, COVID-19 could ​double the global food insecurity rate!

As the pandemic continues, unemployment has ascended, and demand has spiked at food banks and food pantries across the United States. This will likely result in worse health outcomes for the general population who rely on food banks, and more so in times of crisis.

COVID-19 has highlighted the necessity for food banks in many communities in America. 

## Purpose
___

The project sought to understand how well distributed the network of food banks is in the US. 
​
The aim of the project was to answer the question: On the U.S. County Level, is Distance to Food Banks a Predictor for Food Insecurity?

## Tools Used
---

Machine Learning - Python (Mlxtend Library to import Apriori and Association Rules).

Visualizations - Tableau, Matlplotlib, Seaborn, Networkx

Data Manipulation - D3.js, JSON

Web - HTML, CSS, Flask, JavaScript, Heroku

## Data Source
---
We used Kaggle.com -- Instacart’s 2017 Online Grocery Shopping Dataset for our analysis: [Instacart Market Basket Analysis](https://www.kaggle.com/c/instacart-market-basket-analysis/data)


| Data          | Year          | Source        | Date Retrieved | 
| ------------- | ------------- | ------------- | -------------  | 
| [Food Insecurity Rate](https://www.feedingamerica.org/research/coronavirus-hunger-research)  | 2018-2020  | Feeding America – ​The Impact of Coronavirus on Food Insecurity​, Map the Meal Gap (October, 2020). |December 8, 2020  | 
| [FIPS Codes Dataset](https://www2.census.gov/geo/docs/reference/codes/files/national_county.txt)  | 2010  | Data.world retrieved from the U.S. Government Census (2010). | January 20, 2021 | 
| [Food Bank Locations](https://www.feedingamerica.org/find-your-local-foodbank) | Current  | Feeding America Organization | January 19, 2021 | 
| [County Demographics](https://www.ers.usda.gov/data-products/county-level-data-sets/download-data/)  | 2019  | U.S. Department of Agriculture – Economic Research Service (USDA)  | December 12, 2020 | 
| [County Distance Dataset (100 miles)](https://www.nber.org/research/data/county-distance-database) | 2010  | National Bureau of Economic Research (NBER)  | January 18, 2020 | 

## Findings
___

> ### Instacart Shoppers love Bananas and Organic Food!

<table>
  <tr>
    <td>Product Frequency</td>
     <td>Relative Frequency</td>
  </tr>
  <tr>
    <td valign="top"><img src="Images/products.png"></td>
    <td valign="top"><img src="Images/Product_relative_freq.png"></td>
  </tr>
 </table>

> ### Graph of 10 Product Rules (group of items frequently bought together) 

Once we fed our model with a relative frequency rate, and provided it with the basket transaction data. It created for us rules (or the combination of item sets) that had a higher value of support than the minimum threshold we provided. 

![Product Association Rules](Images/product_rules.png)

> ### Heatmaps of top 10 Product Rules

We further filtered the rules by choosing those with higher confidence levels, and ordering the rules by their higher (descending) lift values. 

The following heatmaps help us evaluate the results of our model. It tells us the level of confidence and lift values present in each combination set or rule.

<table>
  <tr>
    <td>Product Support</td>
    <td>Product Lift</td>
    <td>Product Confidence</td>
  </tr>
  <tr>
    <td valign="top"><img src="Images/product_support.png"></td>
    <td valign="top"><img src="Images/product_lift.png"></td>
    <td valign="top"><img src="Images/product_confidence.png"></td>
  </tr>
 </table>

## Predictions
---
Page to display combination of item sets. The image below shows that customers who buy cilantro are likely to buy limes as well. 

<table>
  <tr>
    <td>Are you forgetting something?</td>
    <td>Select your Item</td>
  </tr>
  <tr>
    <td valign="top"><img src="Images/Information_Hub.png"></td>
    <td valign="top"><img src="Images/select_your_item.png"></td>
  </tr>
 </table>

> ### Are you forgetting something?
![Information Hub](Images/Information_Hub.png)

> ### Select your Item
![Select Your Item](Images/select_your_item.png)