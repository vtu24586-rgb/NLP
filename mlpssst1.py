import re
p1=re.compile(r'defabc')
r1=p1.match('defabcdef')
if r1:
    print("Match found:",r1.group())
p2=re.compile(r'.')
r2=p2.search('Hello')
if r2:
    print("Character found:",r2.group())
p3=re.compile(r'[aEiou]')
r3=p3.search('Hello')
if r3:
    print("vowels found:",r3.group())
p4=re.compile(r'\d{3}-\d{2}-\d{4}')
r4=p4.match('123-45-67894')
if r4:
   print("Social security  number:",r4.group())

p5=re.compile(r'\.')
r5=p5.search('www.example.com')
if r5:
   print("Dot found:",r5.group())
p6=re.compile(r'(\d{2})/(\d{2})/(\d{4})')
r6=p6.match('01/09/2024')
if r6:
    print(r6.group(1))
    print(r6.group(2))
    print(r6.group(3)) 
p7=re.compile(r'mat|dog')
r7=p7.search('I have a cat and a dog')
if r7:
    print("animal found:",r7.group())
