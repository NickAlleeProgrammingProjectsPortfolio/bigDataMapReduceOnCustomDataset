
input = open("accidents.txt", "r")
output = open("mapped.txt","w")

for line in input:
    listOfData = line.strip().split("\t")
    try:
        if len(listOfData) == 5:
            user_id, city, state, temperature, weather_condition = listOfData
            if not (city):
                city = "na"
            if not (state):
                state = "na"
            if not (temperature):
                #arbirtary average guess of temp here
                temperature = 66
            output.write("\n"+ city + "\t" + state + "\t" + temperature )
    except:
        print("skipped")
input.close()
output.close()