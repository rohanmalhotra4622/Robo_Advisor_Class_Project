# Robo_Advisor_Class_Project
print(response.text)  is a string, so we have to use the JSON module to process it into a dictionary. 

The geometric average is a good measure for calculating per-period-return.  However, the arithmetic average can be an ok indicator for the next period's forecast.  Therefore, I am using the arithmetic average to determine the buy or sell rating for the stock. This is ofcourse a very simple method of determing the recommendation. Since this is a coding class, this method will suffice for our purpose.

The user will have a choice of entering the stock symbol and the number of days for which they would like to claculate the arithmetic average. If I am not mistaken the data we are pulling is for the last 100 days.  Therefore 100 as the number of days should be the upper bound.  If the user chooses a number higher than 100 or enters a number less than 1, the system will prompt the user to re-enter till a correct entry is made.  

The stock symbol can be entered in both upper or lower case.  The results will display the  stock symbol in upper case. If an integer is entered as the symbol, the system will exit.  If a string is entered the user will be given a prompt that the input seems valid.  It is still possible that data may not be returned as a bogus symbol eg.('msfta') can be entered by mistake.  In this case an error will be returned and the system will exit. 

There is an additonal section that displays the prices and cumulative prices for the number of days requested.  I found this useful as one can easily see the if the calculations have been performed correctly.  The user has the option of commenting this print statement out in line 120.  

If the arithmetic average for the days specified is higher than the latest price, the system will dispaly a 'BUY' rating and specify the percent by which the stock is undervalued and vice versa.  Although unlikely, if the the average price and latest price are equal, a 'HOLD' reccomendation will be given. The 'HOLD' condition can be tested by entering the number of days as 1 as the average will be equal to the latest price for a one day period.