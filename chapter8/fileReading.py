# with keyword

# file = open("report.txt", "r")
# data = file.read()
# file.close()

# read entire line
# with open("report.txt", "r") as f:
#     data = f.read()
#     print("File Data", data) 

# Read line by line
# with open("NewTextFile.txt", "r") as f:
#     data1 = f.readline()
#     data2 = f.readline()

#     print(data1)
#     print(data2)


# read lines function
with open("NewTextFile.txt", "r") as f:
    readLines = f.readlines()
    print(readLines)