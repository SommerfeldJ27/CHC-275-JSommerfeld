file = open("day1_20.txt","r")
buffer=file.readlines()
file.close()
print(buffer[0])
print(buffer[1])
print(buffer[2])
MSFT1 = buffer[0].strip().split(",")
MSFT1.pop(0)
print(MSFT1)
AMZN1 = buffer[1].strip().split(",")
AMZN1.pop(0)
print(AMZN1)
NVDA1 = buffer[2].strip().split(",")
NVDA1.pop(0)
print(NVDA1)
for i in range(len(MSFT1)):
    MSFT1[i] = int(MSFT1[i])
    AMZN1[i] = int(AMZN1[i])
    NVDA1[i] = int(NVDA1[i])

mean1 = sum(MSFT1)/len(MSFT1)
print(mean1)
mean2 = sum(AMZN1)/len(AMZN1)
print(mean2)
mean3 = sum(NVDA1)/len(NVDA1)
print(mean3)

file = open("day21_40.txt","r")
buffer=file.readlines()
file.close()
print(buffer[0])
print(buffer[1])
print(buffer[2])
MSFT2 = buffer[0].strip().split(",")
MSFT2.pop(0)
print(MSFT2)
AMZN2 = buffer[1].strip().split(",")
AMZN2.pop(0)
print(AMZN2)
NVDA2 = buffer[2].strip().split(",")
NVDA2.pop(0)
print(NVDA2)
for i in range(len(MSFT2)):
    MSFT2[i] = int(MSFT2[i])
    AMZN2[i] = int(AMZN2[i])
    NVDA2[i] = int(NVDA2[i])

mean4 = sum(MSFT2)/len(MSFT2)
print(mean4)
mean5 = sum(AMZN2)/len(AMZN2)
print(mean5)
mean6 = sum(NVDA2)/len(NVDA2)
print(mean6)

buys = []
if mean4 > mean1:
    buys.append("MSFT")
if mean5 > mean2:
    buys.append("AMZN")
if mean6 > mean3:
    buys.append("NVDA")
print(buys)
    
avg_filename = "report_1.txt"
file = open(avg_filename,"w")
line0 = f"MSFT: {mean1} , {mean4}\n"
line1 = f"AMZN: {mean2} , {mean5}\n"
line2 = f"NVDA: {mean3} , {mean6}\n"
line3 = f"The best investments would be {buys}"
buffer = [line0, line1, line2, line3]
file.writelines(buffer)
file.close()