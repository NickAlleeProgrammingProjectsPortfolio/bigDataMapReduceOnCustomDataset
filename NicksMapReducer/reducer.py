""" this will take in sorted.txt and find each cities mean temp.

to do this i will take in each line and check to see if the city is not in a dictionary. if not then i will put it in the dictionary
i will also add the temperatures up for each city. also make a count.
when the city is done it will divide the temp count up by the count. then it will write out the city and the avg temp.
then move on to the next city.

"""

input = open("sorted.txt","r")
output = open("reduced.txt","a")

currentCity = ""
count = 0
tempAdder = 0

for line in input:
    data = line.strip().split("\t")
    print(data)
    city, state, temp = data
    if city != currentCity:
        if currentCity:
            output.write("\n" + city + "\t" + state + "\t" + str(tempAdder/count))
        tempAdder = 0
        count = 0
        currentCity = city
    tempAdder += float(temp)
    count +=1
output.write("\n" + city + "\t" + state + "\t" + str(tempAdder/count))
    
"""
    
    if city == currentCity:
        count += 1
        tempAdder += temp
    else:
        output.write("\n" + city + "\t" + state + "\t" + tempAdder)
        tempAdder = 0
        currentCity = city
"""

input.close()
output.close()