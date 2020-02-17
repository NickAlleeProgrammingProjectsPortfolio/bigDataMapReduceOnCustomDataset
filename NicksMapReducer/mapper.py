
input = open("Us_Accidents_Dec19.txt", "r")
output = open("mapped.txt","w")

for line in input:
    listOfData = line.strip().split("\t")
    print(listOfData)
    # 16 vars
    junk1, junk2, user_id, tmc, severity, start_time, end_time, city, state, timezone, visibility, temperature, humidity, wind_speed, precipitation, weather_condition = listOfData
    #print(severity,state,weather_condition)
    output.write(severity + "\t" + state + "\t" + temperature + "\t" + weather_condition + "\n")
    #['185873', '185873', 'A-185875', '201', '2', '11/21/2016 8:59', '11/21/2016 9:35', 'Detroit', 'MI', 'US/Eastern', '10', '30.7', '55', '13.8', '', 'Scattered Clouds']
input.close()
output.close()