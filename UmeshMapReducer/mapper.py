input = open("accidents.txt", "r")
output = open("mapped.txt","w")

for line in input:
    listOfData = line.strip().split("\t")
    try:
        severity, city, state, temperature, weather_condition = listOfData
        output.write(weather_condition + "\t" + state + "\n")
    except:
        print("skipped")
        
input.close()
output.close()