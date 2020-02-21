unsorted = open("mapped.txt", "r")
sorted = open("sorted.txt", "w")

dataList = unsorted.readlines()
dataList.sort()

for line in dataList:
    sorted.write(line)

unsorted.close()
sorted.close()