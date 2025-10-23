i=0
while True:
    print(i)
    if i==1000:
        break
    i+=1

i=0
while(i<=10):
    i+=1
    if i==5:
        continue
    print(i)
    i+=1

for i in range(1,101):
    if i%57 == 0:
        print(f'{i} is divisible by 57')
        break
    print(i)
    
while True:
    string1=input('enter a value (enter "quit" or "exit" to exit the loop:')
    if string1.lower()=='quit'or string1.lower()=='exit':
        print('have a nice day') 
        break
    print(string1)


for i in range(1,51):
    if i%2==0:
        continue
    print(i)

str1 = input('enter a string:')
vowels = 'aeiou'
for i in str1:
    if i.lower() in vowels:
        continue
    print(i, end='')


while True:
    string1=input("enter the value(enter 'quit or 'exit' to exit the loop:")
    if string1.lower()=='quit' or string1.lower()=='exit':
        print('have anice day')
        break
    print(string1)