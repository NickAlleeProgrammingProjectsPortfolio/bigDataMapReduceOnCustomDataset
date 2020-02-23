unsorted = open("mapped.txt", "r")
sorted = open("sorted.txt", "w")

dataList = unsorted.readlines()
dataList.sort()

numOfLines = 0

for line in dataList:
    sorted.write(line)
    numOfLines += 1

unsorted.close()
sorted.close()

print("Sorter complete. sorted.txt created with", numOfLines, "lines")