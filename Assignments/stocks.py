"""Lab 3 - Stock Market Evaluation
In the stock market, it is common to take a 20-day average and see which stocks are out performing their 20-day average, and which stocks are under performing their 20 day average. For example, when a stock market has a 20 day-moving average that is trending upwards, that indicates a favorable trend for buyers, therefore they should buy the stock and sell when the moving average starts to reverse. 
Your job is, given two 20-day snapshots, determine which stocks to buy and generate a report for each.
You will be supplied two files
Day1_20.txt, which has
	- three stock tickers, NVDA, AMZN, and MSFT
	- 20 data points associated with each ticker
Day21_40.txt which has
	- three stock tickers, NVDA, AMZN, and MSFT
	- 20 data points associated with each ticker.

Days 21-40 occur AFTER days 1-20. Your goal is to create a file called report.txt where
-	Each Ticker and their two 20-day averages
-	Which tickers had a higher 21-40 day average compared to their 1-20 day average.

You will need to use try-except-else blocks and file I/O to complete this task, along with any skills we previously worked with before (such as lists, data types, for-loops, etc.) 

You do not need to write a menu routine for this program. All your program needs to do is generate the report."""



#I can write to a file that did not previously exist while also using write mode. 

file = open("day1_20.txt","r")
buffer=file.readlines()
file.close()
print(buffer)
print(buffer[0])
print(buffer[1])
print(buffer[2])
MSFT1 = buffer[0]
AMZN1 = buffer[1]
NVDA1 = buffer[2]
mean = sum("day1_20.txt","r")/len("day1_20.txt","r") #this takes the mean
print(mean)

file = open("day21_40.txt","r")
buffer=file.readlines()
file.close()
print(buffer)
print(buffer[0])
print(buffer[1])
print(buffer[2])
MSFT2 = buffer[0]
AMZN2 = buffer[1]
NVDA2 = buffer[2]

avg_filename = "report_0.txt"
file = open(avg_filename,"w")
line = f"MSFT: avg1: avg2:"
line = f"AMZN: avg1: avg2:"
line = f"NVDA: avg1: avg2:"
line = f"The best investments are []"
file.write(line)
file.close()