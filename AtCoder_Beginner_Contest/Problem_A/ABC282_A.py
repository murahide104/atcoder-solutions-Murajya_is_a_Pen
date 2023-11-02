Al = ["a","b","c","d","e","f","g","h","i","j","k","l","m",
      "n","o","p","q","r","s","t","u","v","w","x","y","z"]
Al = [i.upper() for i in Al]
n = int(input())

print(*Al[0:n], sep="") 