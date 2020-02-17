import pandas as pd

input = open("Us_Accidents_Dec19.txt", "r")
output = open("mapped.txt","w")
print("hello")
for line in input:
    listOfData = line.strip().split("    ")
    junk1, junk2, junk3, id, tmc, severity, start_time, end_time, city, state, timezone, visibility(mi), temperature(f), humidity(%), wind_speed(mph), precipitation(in), weather_condition = listOfData
    print(severity,state,weather_condition)
    output.write(severity + "\t" + state + "\t" + temperature(f) + "\t" + weather_condition + "\n")

input.close()
output.close()