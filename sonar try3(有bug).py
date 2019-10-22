import random
import secrets 

#==========just def==================
def spawnChests(chestsNum):
    chestsList=[]
    for i in range(int(chestsNum)):
        #print(secrets.randbelow(15))
        x=secrets.randbelow(15)
        y=secrets.randbelow(60)
        chestsList.append(i)
        chestsList[i]=x,y
    return chestsList

def boardstitle():
    
    print('   ',end='')   
    for i in range(1,6):
        print('         %s'%(i),end='')
    print()
    reboard1=''
    for i in range(6):
        title=''.join(map(str,(list(range(10)))))##<==='0123456789'
        reboard=''.join(map(str,title))
        reboard1+=reboard
        
    print('  ',end='')        
    print(reboard1,end='')
    print()

def waveBoard():
    waveBoard=[]
    for i in range(60):
        waveBoard.append(i)
        drawout=''
        wave=random.randint(0,1)
        if wave==1:
           drawout='\''
        else:
           drawout='~'
        waveBoard[i]=drawout
    return waveBoard

def boardsbody1(waveBoard):
    a=0
    for i in range(15):
        
        drawout=''
        if i<10:
           print(' %s'%(i),end='')
        else:
           print(i,end='')
        for i in range(61):
            if i !=60:            
            
               wave=random.randint(0,1)
               if wave==1:
                  drawout+='\''
               else:
                  drawout+='~'
            
            else:
               
               drawout+=str(a)
               a=a+1
            
        print(''.join(map(str,drawout)))

def drawboard(row):##
   
    for b in range(17):
        wave=''  
        z=0
        for i in range(62):
            
            row[b][i+1]=str(z)
            wave=random.randint(0,1)
            if wave==1:
               row[b][i+1]='\''
            else:
               row[b][i+1]='~'
            if z<9:# and  b!=10:(到9的原因是因為 下面就沒有再用到b去指定東西了(已經用完了，所以可以改成我們接下來要的)
               z+=1
            else:
               z=0
            for d in range(17):
                if d!=0 and d!=16:
                   row[d][0]='  '
                   row[d][61]='    '
                else:
                   for e in range(10):
                       row[d][i]+=e
            print(row)           
            print(''.join(map(str,(row[b][i]))),end='')
        print()

def inputPlayerAnswer():
    z=False
    while z==False: 
          print('plz chooce a place to put down the detector.(0~14 0~59)')
          answer=input()  
          answer=answer.split()
          #print(answer)
          if len(list(answer))!=2:
             #print(len(list(answer)))
             z=False
          else:
             #print(len(list(answer)))
             x,y=answer 
             if x.isdigit() and y.isdigit(): 
             
                if int(x) in range(15) and int(y) in range(60):
                   
                   z=True
                else:
                   
                   z=False
             else:
                z=False
    return x,y
#=======game start=======================
chestsNum=3
chance=16

while True:
      print('1')##
      chestsList=spawnChests(chestsNum)
      print(chestsList)
      gameconti=True
      while gameconti==True:
            print('2')##
            boardstitle()
            boardsbody1(waveBoard)
            if chance==0 or len(chestsList)==0:
               break
            x,y=inputPlayerAnswer()
            xylist=int(x),int(y)
            chance=chance-1
            print(chance)##
            print(xylist)##
            for i in chestsList:
                print(i)
                if i==xylist:
                   chestsList.remove(i)#remove chests
                   
                   break
            print(chestsList)
            

    
