# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input())
book = [ input().split() for _ in range(T) ]
phoneBook = {k:v for k, v in book}
while True:
  try:
    name = input()
    if name in phoneBook:
      print('%s=%s' % (name, phoneBook[name]))
    else:
      print("Not found")
  except:
    break
