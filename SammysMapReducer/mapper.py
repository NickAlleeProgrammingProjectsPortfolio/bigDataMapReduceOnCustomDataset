input = open("accidents.txt", "r")
output = open("mapped.txt","w")

numOfLines = 0

for line in input:
    listOfData = line.strip().split("\t")
    try:
        severity, city, state, temperature, weather_condition = listOfData
        output.write(state + "\t" + severity + "\n")
        numOfLines += 1
    except:
        continue
        
input.close()
output.close()

print("Mapper complete. mapped.txt created with", numOfLines, "lines")