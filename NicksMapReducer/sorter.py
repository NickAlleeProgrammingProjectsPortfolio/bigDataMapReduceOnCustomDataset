unsorted = open("mapped.txt", "r")
sorted = open("sorted.txt", "w")

dataList = unsorted.readlines()
dataList.sort()

for line in dataList:
    print (line)
    sorted.write(line)

unsorted.close()
sorted.close()