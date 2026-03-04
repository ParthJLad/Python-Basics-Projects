file = open("certificate.txt","r") 

data = file.read()

data = data.lower()

if "live" in data:
    print("Yes Word live is in file")
else:
    print("No word live is not in file")