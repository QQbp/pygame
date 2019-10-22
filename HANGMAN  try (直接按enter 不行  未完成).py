
import random

HANGMANPIC='''
---------
    I   I
        I
        I
        I
        I
        I
        I
--------------''','''

---------
    I   I
    O   I
        I
        I
        I
        I
        I
--------------''','''
---------
    I   I
    O   I
   /    I
        I
        I
        I
        I
--------------''','''

---------
    I   I
    O   I
   /l   I
        I
        I
        I
--------------''','''


---------
    I   I
    O   I
   /l\  I
        I
        I
        I
--------------''','''


---------
    I   I
    O   I
   /l\  I
    A   I
        I
        I
--------------'''







#==============================
a={'first':'secretword dog fish cat happy '.split(),'second':'one  kkbox three  two four'.split()}

#=============================
def pick(a):
    

    wordkey=random.choice(list(a.keys()))
    
    b=random.randint(0,len(a[wordkey])-1)
    
    return a[wordkey][b]
#================================
def p(v,HANGMANPIC):
  
  n=0
  blanks='_'*len(v)    
  QQ=' '*6
  
  while n<len(HANGMANPIC) :
     
     print('正確的單字:',end='')
     for i in blanks:
       print(i+' ',end='')
     print()
     print('猜過的字：'+QQ,end='')
     print()
     print(HANGMANPIC[n])
     print('猜一個字阿~')
     c=input()
     c=c.lower()

     if c in blanks:
         print('這個字你猜過了喔，再猜一次吧~')
         

     elif c in QQ:
         print('這個字你猜過了喔，再猜一次吧~')
         

     elif len(c)!=1:
         print('只能打一個字喔')
        

     elif c not in 'qwertyuiopasdfghjklzxcvbnm':
         print('要打英文字母喔')


     else:
       for i in  range(len(v)):
           if v[i] in c:
             blanks=blanks[:i]+v[i]+blanks[i+1:]

            
     

       if c not in v :
        
             QQ=QQ[:n]+c[0]+QQ[n+1:]
                  
             n=n+1

       if n==len(HANGMANPIC):
              print('正確的單字:',end='')
              for i in blanks: 
                print(i+' ',end='')
              print()
              print('猜過的字：'+QQ,end='')
              print()
              print('好可惜喔，沒能猜到。')
    
     if blanks==v :
         print('正確的單字:',end='')
         for i in blanks:
            print(i+' ',end='')
         print()
         print('猜過的字：'+QQ,end='')
         print()
         print('對阿就是 '+v+'  好強喔，答對了~')
         break

     
#===========下面正文開始============

play='y'

while play!='n' :
    print('HANGMAN')
    
    v=pick(a)
    p(v,HANGMANPIC)  
    print()
    print('press n to qiut')
    play=input().lower()
    









