# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Project 2: Development of a Machine Learning Model for Accurate Prediction of HDB Prices

## Overview
As a leading property developer in Singapore, XYZ Property Group is committed to providing accurate and reliable information to our clients to help them make informed decisions about their property investments. In line with this, we have been commissioned to develop a machine learning model that can accurately predict the selling price of HDB flats in Singapore.

Housing and Development Board (HDB) flats are a popular form of public housing in Singapore that are sold and leased by the government. The price of HDB flats depends on factors such as flat type, location, age, and remaining lease. The HDB resale price index is an indicator of overall market trends. The prices of HDB flats have generally increased over the years due to increased demand, limited supply, and government efforts to improve public housing quality.


## Contents:
- [Problem Statement](#Problem-Statement)
- [Data dictionary](#Data-dictionary)
- [Analysis](#Analysis)
- [Conclusions and Recommendations](#Conclusions-and-Recommendations)

## Problem Statement
The goal of this project is to develop a machine learning model that can predict the selling price of a new HDB flat based on relevant features such as location, size, age, and amenities. The model should be trained on a large dataset of historical HDB transaction prices and validated using appropriate performance metrics.

We will select the best-performing model based on mean squared error.

## Data dictionary
|Feature|Type|Description|
|---|---|---|
|3room_sold|int|number of 3 room flats in the block the flat was sold|
|4room_sold|int|number of 4 room flats in the block the flat was sold|
|5room_sold|int|number of 5 room flats in the block the flat was sold|
|bus_stop_nearest_distance|float|distance (in metres) to the nearest bus stop|
|exec_sold|int|number of executive flats in the block the flat was sold|
|flat_model|object|HDB model of the resale flat|
|flat_type|object|type of the resale flat unit|
|floor_area_sqm|float|floor area of the resale flat unit in square metres|
|hawker_food_stalls|int|number of hawker food stalls in the nearest hawker centre|
|hawker_market_stalls|int|number of hawker and market stalls in the nearest hawker centre|
|hawker_nearest_distance|float|distance (in metres) to the nearest hawker centre|
|hawker_within_1km|int|number of hawker centres within 1 kilometre|
|hawker_within_2km|int|number of hawker centres within 2 kilometre|
|hawker_within_500m|int|number of hawker centres within 500 metres|
|hdb_age|int|number of years from lease commence date to present year(year the sale was made)|
|mall_nearest_distance|float|distance (in metres) to the nearest mall|
|mall_within_1km|int|number of malls within 1 kilometre|
|mall_within_2km|int|number of malls within 2 kilometre|
|mall_within_500m|int|number of malls within 500 metres|
|max_floor_lvl|int|highest floor of the block of resale flat|
|mid|int|middle value of storey range of the resale flat|
|mrt_nearest_distance|float|distance (in metres) to the nearest MRT station|
|planning_area|object|Government planning area that the flat is located|
|resale_price|float|the property's sale price in Singapore dollars. This is the target variable that we are trying to predict for this project.|
|total_dwelling_units|int|total number of residential dwelling units in the resale flat|
|tranc_month|int|year of resale transaction|
|tranc_year|int|month of resale transaction|


## Analysis
The analysis of the data on HDB flats in Singapore has revealed some interesting insights into the factors that impact the resale price of flats. Floor area and maximum number of floors of the block are consistently among the features that impact the resale price of flats. These features can be used to draw conclusions about the behavioral patterns of Singaporeans when it comes to housing preferences. However, it remains unclear why the number of 3 room or 5 room flats in a block would affect the prices of a flat, as no information could be found through a quick online search. This suggests that further research may be needed to fully understand the impact of this feature on resale prices.

Another important consideration is that the limitation of using only 3 linear regression models in this project may have contributed to under-fitting, as evidenced by consistently low scores. This suggests that a more complex model with more features may be required to accurately predict HDB flat prices in the future. Furthermore, dropping certain features from the analysis, such as information about schools, longitude and latitude, and categories from within the features, limits the model's ability to provide insights into these factors.

## Conclusions and Recommendations
In conclusion, the analysis of the data on HDB flats in Singapore has provided valuable insights into the factors that impact the resale price of flats. Floor area and maximum number of floors of the block are among the most impactful features, but the reasons behind the impact of certain features, such as the number of 3 room or 5 room flats in a block, remain unclear. Additionally, the limitation of using only 3 linear regression models in this project may have contributed to under-fitting, indicating a need for a more complex model with more features in the future. Finally, dropping certain features from the analysis limits the model's ability to provide insights into these factors, suggesting that a more comprehensive approach may be needed in future analysis. Overall, this study provides valuable insights into the complex nature of the HDB flat market in Singapore, and serves as a starting point for further research into this important topic.

## Future Work
It might be interesting to investigate if there are any patterns that could possibly relate correlation coefficient and the coefficients of the linear regression model.