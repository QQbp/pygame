import random
import time

def discription():
 print('你到了一座森林，必須越過一座山才能到到村落，太陽快下山了，現在你面前有兩個洞可以通往前眠的村落，你要選哪個洞呢？')
 time.sleep(0.5)
 print('1 or 2')

def choosecave():
   
    cave=''
    while cave!='1' and cave!='2':
       print('選一個洞吧')
       cave=input()

    return cave


def result(choosecave):



 goodcave=random.randint(1,2)


 if choosecave==str(goodcave):
   print('你進到了洞裡，這個洞穴有很多的蝙蝠，你驚擾到的它們，但是你安全的到達的村落了。')

 else:
   print('洞裡有很多的龍，你好自為之吧....QQ')
  
    


playAgaine='y'

while playAgaine!='n':

    discription()
    abc=choosecave()
    result(abc)
   
    print('Do you want to paly agine?press yes or anykey to quite.')

    playAgaine=input()
