import
# looping through a string
word = "word"
for letter in word:
  #print(letter)
  pass

# looping through a list
words = ["words0", "words1", "words2", "words3"]
for w in words:
  for lett in w:
    #print(lett)
    pass

items = [1, 4, 8, 2, 7, 3, 9]
for num in items:
  if num == 4:
    continue
    # break
    #print(num)

list = ["2", 2, "2", 2]
a = 0
for thing in list:
  a += int(thing)
#print(a)

count = 0
for x in range(10):
  #print(x)
  count += 1
#print("count ", count)

# looping through a list
words2 = ["words0", "words1", "words2", "words3"]
for i in range(len(words2)):
  print(i, words2[i])

print(random.randint(2,3))