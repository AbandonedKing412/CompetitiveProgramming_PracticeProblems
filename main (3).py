x = list(map(int, input().split()))
print("Even: " + str(len([(i) for i in x if i % 2 == 0 and  i!=0])) + "\nOdd: " + str(len(x)-len([(i) for i in x if i % 2 == 0])))