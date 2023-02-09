course = 'Python for testing'

print(course)
print(course.upper())
print(course.lower())
print(course.replace('x', '4'))
print('Python' in course)

print(3 ** 10)

x = 10
x = x + 4
x += 3
print(x)

y = 17

print(y)

if x == 16 and not y == 16:
  print('both true')
elif x == 16 : #hello
  print('only x')
else:
  print('neither')

while x < 20:
  print(x * '*')
  x += 1

names = ['Hello', 'Hi', "What's up", 8]
print(names[-2])
names.append('Another')
print(names)
names.insert(0, 0)
print(names)
print(len(names))

for name in names:
  print(name)

print('')
i = 0
while i < len(names):
  print(names[i])
  i+= 1

print('')
#range func
numbers = range(5)
print(numbers)
for number in numbers:
  print(number)

numbers = range(0, 5)
print(numbers)
for number in numbers:
  print(names[number])

print('')
numbers2 = (7, 8, 9)
print(numbers2)