# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Project 1: Exploring climate data of Singapore

## Overview
Singapore's ageing population is due to increasing life expectancy and declining fertility rates, which may be influenced by exposure to high temperatures. This project aims to investigate the relationship between temperature and fertility in Singapore, with the goal of addressing declining fertility rates and promoting healthy reproductive outcomes.


## Contents:
- [Problem Statement](#Problem-Statement)
- [Data dictionary](#Data-dictionary)
- [Analysis](#Analysis)
- [Conclusions and Recommendations](#Conclusions-and-Recommendations)

## Problem Statement
As is common in most parts of the world, Singapore is facing an ageing population. According to a recent [straits time report](https://www.straitstimes.com/singapore/singapores-population-ageing-rapidly-184-of-citizens-are-65-years-and-older), the proportion of citizens aged 65 and above is 18.4 per cent in 2022, an increase from 11.1 per cent in 2012. It was 17.6 per cent in 2021. In this project, we analyse how surface temperature affects sexual activity. This analysis can help policy makers plan policies surrounding the issue of an ageing population.

## Data dictionary
|Feature|Type|Dataset|Description|
|---|---|---|---|
|quarter|datetime|quarterly-live-births|Year in quarters denoted as yyyy-mm-dd, where mm is the first month of the quarter and dd is 01|
|mean_temp|float|surface-air-temperature-monthly-mean|Quarterly mean of temperature|
|total_rainfall|float|rainfall-monthly-total|Quarterly mean of total_rainfall. Total rainfall in mm|
|mean_rh|float|relative-humidity-monthly-mean|Quarterly mean of relative humidity|
|mean_sunshine|float|sunshine-duration-monthly-mean-daily-duration|Quarterly mean of daily sunshine duration|
|rain_days|int|rainfall-monthly-number-of-rain-days|Total number of days it rained in quarter|
|births|int|quarterly-live-births|Total births in quarter|

## Analysis
It was found that number of birth increases as temperature decreases, as seen in the change in number of births 9 months after a given quarter.

## Conclusions and Recommendations
The evidence gathered suggests an inverse relationship between temperature and the number of births. However, the available data does not clarify the extent to which the changes in birth rate are solely due to temperature. The decline in the number of births may also be attributed to a rising proportion of singles, later marriages, and married couples having fewer children. Studies on mammals show that heat stress can negatively affect follicular development in female cows, the extent to which this applies to the Singapore population requires further research. Policies allowing an increased chance of exposure to reproduction activities during the colder quarters of the year could help improve the ageing population situation in the long run.


## Future Work
Rainfall, relative humidity and sunlight hours affect temperature, and since birth rate is related to temperature, we should expect some correlation between birth, relative humidity, sunlight and rainfall as well. However, it seems that rainfall has no linear correlation to birth rate, which suggests that temperature could just be a trojan horse for one or some of the other factors. Future research needs to be done.