import random


def ist():
 guessestaken=0
 print('hi~你叫什麼名字呢？')
 name=input()
 print(name +'你好喔~')


 

 number=random.randint(1,20) 
 print(name+'猜一個數字，這個數字是從1~20，你有六次機會可以猜。')


 while guessestaken<6:


      guessnumber=input()
      guessnumber=int(guessnumber)
      
      if guessnumber<number:
       print ('太小了喔。')

      if guessnumber>number:
       print ('太大了喔。')

      if guessnumber==number:
       print ('對了')
       break
      guessestaken=guessestaken+1
      
    

 if guessestaken<6:
    print('做的不錯')

 if guessestaken==6:
    print('下次再來吧')

    yesorno=input()

playagine='yes'

while playagine!='n':

    ist()
    print('要再玩一次嗎，要的話按任意鍵繼續，不完的話按\'n\'結束')
    playagine=input()

print('byebye~')


