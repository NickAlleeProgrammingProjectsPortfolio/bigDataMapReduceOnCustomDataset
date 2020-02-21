
input = open("Us_Accidents_Dec19.txt", "r")
output = open("mapped.txt","w")

for line in input:
    listOfData = line.strip().split("\t")
    # 14 vars
    try:
        user_id, tmc, severity, start_time, end_time, city, state, timezone, visibility, temperature, humidity, wind_speed, precipitation, weather_condition = listOfData
        output.write("\n"+ city + "\t" + state + "\t" + temperature )
    except:
        print("skipped")
    #print(severity,state,weather_condition)
    #['A-185875', '201', '2', '11/21/2016 8:59', '11/21/2016 9:35', 'Detroit', 'MI', 'US/Eastern', '10', '30.7', '55', '13.8', '', 'Scattered Clouds']
input.close()
output.close()