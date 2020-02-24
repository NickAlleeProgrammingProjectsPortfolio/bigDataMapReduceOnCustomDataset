unreduced = open("sorted.txt","r")
reduced = open("reduced.txt", "w")

thisKey = ""
count = 0

for line in unreduced:
  data = line.strip().split('\t')
  weather_condition, state = data

  if weather_condition != thisKey:
    if thisKey:
      # output the last key value pair result
      reduced.write(thisKey + '\t' + str(count)+'\n')

    # start over when changing keys
    thisKey = weather_condition
  
  # apply the aggregation function
  # thisValue += int(severity)
  count += 1

# output the final entry when done
reduced.write(thisKey + '\t' + str(count)+'\n')

unreduced.close()
reduced.close()
