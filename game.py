import random
print('Wie heisst du?')
name = input()
print ('Sali Hoi ' + name)
print('Ich denke an eine Zahl zwischen 1 und 20')
print ('Du hast fünf Versuche sie zu erraten')

secret = random.randint(1,20)

print('An welche Zahl denke ich?')
for i in range(6):
  if i == 5:
    print('Leider sind deine Versuche vorbei. Fail!')
  else:
    print('Rate!')
    zahl = int(input())
    if zahl == secret:
      print('Yes! Bist du Hellseher?')
      break
    elif zahl > secret:
      print('zu hoch')
    elif zahl < secret:
      print('zu niedrig')

print('Ade Messi!')
