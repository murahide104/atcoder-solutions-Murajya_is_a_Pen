d = int(input())
if d % 5 == 0:
    print("Christmas")
else:    
    print("Christmas" + " Eve"*(5-(d%5)))