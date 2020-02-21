unreduced = open("sorted.txt","r")
reduced = open("reduced.txt", "w")

thisKey = ""
thisValue = 0
count = 0

for line in unreduced:
  data = line.strip().split('\t')
  state, severity = data

  if state != thisKey:
    if thisKey:
      # output the last key value pair result
      reduced.write(thisKey + '\t' + str(thisValue/count)+'\n')

    # start over when changing keys
    thisKey = state
    thisValue = 0
    count = 0
  
  # apply the aggregation function
  thisValue += int(severity)
  count += 1

# output the final entry when done
reduced.write(thisKey + '\t' + str(thisValue/count)+'\n')

unreduced.close()
reduced.close()
