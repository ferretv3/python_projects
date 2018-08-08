min_weight = 1000
max_weight = 0
min_height = 5.00
max_height = 0.00
min_BMI = 50.00
max_BMI = 0
sum_height = 0
sum_weight = 0
sum_BMI = 0
hwc = 0 #Height & weight, count



data = open("data.txt","r")

outfile = open("output.txt","w")

print("{:<12s}{:<12s}{:<12s}{:<12s}".format("Name","Height(m)","Weight(kg)","BMI"),file = outfile)

for line in data:
    line = line.split()
    if line[1].isalpha() or "(" in line[1] or line[2].isalpha() or "(" in line[2]:
        pass
    else:
        
        BMI = float(line[2]) / (float(line[1]) ** 2)
        
        sum_height += float(line[1])
        sum_weight += float(line[2])
        sum_BMI += BMI
        hwc += 1
        
        if float(line[1]) > max_height:
            max_height = float(line[1])
        elif float(line[1]) < min_height:
            min_height = float(line[1])
            
        if float(line[2]) > max_weight:
            max_weight = float(line[2])
        elif float(line[2]) < min_weight:
            min_weight = float(line[2])
            
        if BMI > max_BMI:
            max_BMI = BMI
        elif BMI < min_BMI:
            min_BMI = BMI
            
        
        
        print("{:<12s}{:<12.2f}{:<12.2f}{:<12.2f}".format(line[0],float(line[1]),float(line[2]),BMI),file = outfile)

avg_weight = sum_weight / hwc
avg_height = sum_height / hwc
avg_BMI = sum_BMI / hwc
print(" ",file = outfile)
print("{:<12s}{:<12.2f}{:<12.2f}{:<12.2f}".format("Average",avg_height,avg_weight,avg_BMI), file = outfile)
print("{:<12s}{:<12.2f}{:<12.2f}{:<12.2f}".format("Max",max_height,max_weight,max_BMI), file = outfile)
print("{:<12s}{:<12.2f}{:<12.2f}{:<12.2f}".format("Min",min_height,min_weight,min_BMI), file = outfile)

outfile.close()