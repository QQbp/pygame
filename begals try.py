##IndexError: list index out of range <<<1.可能是因為我們給的INDEX太短，而程式裡寫得太長 2.也可能是因為我們要的INDEX裡沒東西
import random
import math
import time

def gotquestion():
    question=random.randint(100,1000)
    return question
##str = raw_input("please input the number:")

##if str.isdigit():

def separatenumber(number):
    #print(number)
    a=number/100
    a=math.floor(a)
    #print(a)
  
    b=(number-(a*100))/10
    b=math.floor(b)
    #print(b)

    c=(number-(a*100)-(b*10))
    #print(c)

    list=[a,b,c]
    return list       

def answer():####
    oo=True
    while oo:
       print('plz guess 3 number and set the place which you want.')
       answer=input()
       if answer.isdigit():###
          answer=int(answer)
          if answer in range(100,1000):
             return answer
             oo=False
          else:
             if answer in range(0,100):###answer(000~099)跟(0~99)的差別
                separatenumber(answer)
                if a!=none and b!=none and c!=none:
                   return answer
                   oo=False
             else:
                 oo=True

def checkanswer(question,answer):
    qlist=separatenumber(question)
    alist=separatenumber(answer)
    
    if alist[0]==qlist[0] and alist[1]==qlist[1] and alist[2]==qlist[2]:
       print('猜對了~好強喔~')
       return False##

    else:
      
       if (alist[0] in qlist) and (alist[1] in qlist) and (alist[2] in qlist ):#(012)
          print('fermi pico pico')
          
          return True##
             
       elif  (alist[0] in qlist) and (alist[1] in qlist) and (alist[2] not in qlist):#(01_)
             if alist[0]==qlist[0] and alist[1]==qlist[1]:
                print('fermi fermi begal')
                
                return True##

             elif ((alist[0]==qlist[0]) and (alist[1]!=qlist[1]))or((alist[0]!=qlist[0]) and (alist[1]==qlist[1])):
                  print('fermi pico begal')
                  
                  return True##
             else:
                  print('pico pico begal')
                  
                  return True##
                  

       elif  (alist[0] in qlist) and (alist[1] not in qlist) and (alist[2] in qlist):#(0_2)
             if alist[0]==qlist[0] and alist[2]==qlist[2]:
                print('fermi fermi begal')
                
                return True##

             elif ((alist[0]==qlist[0]) and (alist[2]!=qlist[2]))or((alist[0]!=qlist[0]) and (alist[2]==qlist[2])):
                  print('fermi pico begal')
                  
                  return True##
             else:
                  print('pico pico begal')
                  
                  return True##

       elif  (alist[0] not in qlist) and (alist[1] in qlist) and (alist[2] in qlist):#(_12)
             if alist[2]==qlist[2] and alist[1]==qlist[1]:
                print('fermi fermi begal')
                
                return True##

             elif ((alist[2]==qlist[2]) and (alist[1]!=qlist[1]))or((alist[2]!=qlist[2]) and (alist[1]==qlist[1])):
                  print('fermi pico begal')
                  
                  return True##
             else:
                  print('pico pico begal')
                   
                  return True##

       elif  (alist[0] in qlist) and (alist[1] not in qlist) and (alist[2] not in qlist):#(0_ _ )
             if alist[0]==qlist[0]:
                print('fermi begal begal')
                
                return True##
             else:
                print('pico begal begal')
                                                                     
       elif  (alist[0] not in qlist) and (alist[1] in qlist) and (alist[2] not in qlist):#(_ 1 _)
             if alist[1]==qlist[1]:
                print('fermi begal begal')
                
                return True##
             else:
                print('pico begal begal')

       elif  (alist[0] not in qlist) and (alist[1] not in qlist) and (alist[2] in qlist):#(_ _2)
             if alist[2]==qlist[2]:
                print('fermi begal begal')
                
                return True##
             else:
                print('pico begal begal')
                
                return True
       else:
           print('begal begal begal!!!')
           
           return True###


def wantplayagain():
    print('Do you want play again?(y or n)')
    wantplayagain=input().lower().startswith('y')
    return wantplayagain

#===game is start======================
print('welcome begals!!!!')
a=True


while a:
     print('我現在寫下三個數字，請把數字跟數字的位置都猜對~')
     time.sleep(1)
     print('我說begals的話，就是沒有任何一個數字是有在裡面的喔~')
     time.sleep(1)
     print('我說fermi的話就是，某個數字跟位置都對囉~')
     time.sleep(1)
     print('我說pico的話，就是有某個數字對了，但是位置不對喔~~')
     time.sleep(1)
     print('begal----->全錯')
     print('pico------->數字對了但是位置錯了')
     print('fermi------>數字跟位置都對了')
     time.sleep(1)
     q=gotquestion()
     k=0
     while k<=10:
           print('現在有三個數字  請猜吧~')
           k=k+1
           a=answer()
           
           if checkanswer(q,a)==False:
               break
           #print(k) 
     if not wantplayagain():
       break
           
           
             

