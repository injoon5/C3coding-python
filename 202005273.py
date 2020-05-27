sum_val = 0
count = 0

while True:
  scores = int(input("type scores (type -1 to quit):"))
  if scores > -1:
    sum_val += scores
    count += 1
  else:
      break

print("the num of javascripts:", count)
print("Sum = ", sum_val, "avg = ", sum_val / count)
