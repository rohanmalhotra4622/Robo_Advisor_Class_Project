# Robo_Advisor_Class_Project
print(response.text)  is a string, so we have to use the JSON module to process it into a dictionary. 

The geometric average is a good measure for calculating per-period-return.  However, the arithmetic average can be an ok indicator for the next period's forecast.  Therefore, I am using the arithmetic average to determine the buy or sell rating for the stock. This is ofcourse a very simple method of determing the recommendation. Since this is a coding class, this method will suffice for our purpose.

The user will have a choice of entering the stock symbol and the number of days for which they would like to claculate the arithmetic average. If I am not mistaken the data we are pulling is for the last 100 days.  Therefore that should be the upper bound.  If the user chooses a higher number than 100, the system will prompt the user to re-enter.  

The stock symbol can be entered in both upper or lower case.  The results will display the the stock symbol in upper case.  

If the arithmetic average for the days specified is higher than the latest price the system will dispaly a 'BUY' rating and specify the amount by which the stock is undervalued and vice versa.  Although unlikely, if the the average price and latest price are equal, a 'HOLD' reccomendation will be given.