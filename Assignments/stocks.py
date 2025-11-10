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
print(buffer[0])
print(buffer[1])
print(buffer[2])
MSFT1 = buffer[0]
AMZN1 = buffer[1]
NVDA1 = buffer[2]


file = open("day21_40.txt","r")
buffer=file.readlines()
file.close()
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

file = open("day1_20.txt","r") #open("<filename>","<mode>") 

buffer = file.readlines() #this will take in our list of company and make each line an item inside our list 
company = [] #This would be account company
prices = [] #this would be balance
file.close() #flush the buffered memory being used for the contents of the files 
for line in buffer: #for each makes more sense here because we don't want to introduce
#index based technical overhead that is irrelevant to our program
    line = line.strip() #This removes white space
    line = line.split(",") #line is a list of two elements
                            #line[0] is the name
                            #line[1] is the grade value

try: #i'm gouing to wrap this inside of a try-except because we might get an unexpected error, we haven't 
    #closed the file yet
    for i in range(len(prices)): #for-i loop because I'm modifying the prices directly
        prices[i] = int(prices[i]) #typecast
except ValueError:
    print("grade must be a number")

print(company)
print(prices)

file = open("company.txt","w") #this is going to open our file in write mode. 

#writing into file step.

buffer = [] #creating a new buffer and making it empty
#we want our lines to look like {name},{grade}\n
#each object in the parallel lists have the same index 
#for i or for-each?

for i in range(len(company)):
        #pulling out all indices within the company list(which is also the same as the prices list)
        line =  f"{company[i]},{prices[i]}\n" #this is the format we want for our file 

file.writelines(buffer)
file.close()