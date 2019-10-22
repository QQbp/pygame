import random

def drawBoard(board):

    print('  |   |')
    print(' '+board[7]+'|  '+board[8]+'|'+board[9])
    print('  |   |')
    print('-----------')
    print('  |   |')
    print(' '+board[4]+'|  '+board[5]+'|'+board[6])
    print('  |   |')
    print('-----------')
    print('  |   |')
    print(' '+board[1]+'|  '+board[2]+'|'+board[3])
    print('  |   |')

def getCopy(board):
    copy=[]
    for i in board:
        copy.append(i)
    return copy

def whoGo1st():
    a=random.randint(0,1)
    if a==0:
      print('you go 1st')
      return 0 
    else :
      print('computer will go 1st')
      return 1

def playerLetter():
    humanLetter=''
    while humanLetter!='O' and humanLetter!='X':
      print('Do you want \'X\' or \'O\'?')
      humanLetter=input().upper()
    
    if humanLetter=='O':
        computerLetter='X'
        playerLetter=['O','X']
    else:
        playerLetter=['X','O']
    return playerLetter

def isSpaceFree(nb):
    return nb[move]==' '


def isWin(b,L):
    return (b[1]==L and b[2]==L and b[3]==L)or(b[4]==L and b[5]==L and b[6]==L)or(b[7]==L and b[8]==L and b[9]==L)or(b[1]==L and b[4]==L and b[7]==L)or(b[2]==L and b[5]==L and b[8]==L)or(b[3]==L and b[6]==L and b[9]==L)or(b[1]==L and b[5]==L and b[9]==L)or(b[3]==L and b[5]==L and b[7]==L)
     

def isTie(board):
    cc=getCopy(board)
    dd=[]
    for i in range(10):
        if cc[i]!=' ':
           dd.append(i)
          
               
    if len(dd)==9:
       print('It is tie!!!')
       print(dd)
       print('================')
       return True
    else:
       return False

def playAgain():
    print('Do you wana play again? (y or n)')
    playAgain=input().lower().startswith('y')
    return playAgain

def lastcheck(nb):
    if nb[1]==' 'or nb[3]==' ' or nb[7]==' ' or nb[9]==' ':
                           
                            nnnb=[]
                            for i in [1,3,7,9]:
                               print(i)##
                               if nb[i]==' ':
                                  nnnb.append(i)
                                  
                                  ##print(nnb)
                            k=random.choice(nnnb)
                            print('==========')
                            print(k)####
                            nb[k]=computerLetter
                            print('============')
                            turn=0

    elif nb[5]==' ':
                            nb[5]=computerLetter
                            print('5')##
                            turn=0

    else:
                            for i in [2,4,6,8]:
                                if nb[i]==' ':
                                    nnb.append(i)
                            y=random.choice(nnb)
                            print('2')##
                            y=int(y)
                            nb[y]=computerLetter
                            turn=0
    



#===========game start=========================================

print('welcome to Tic Tac Toe!!!')
b=True

while b:

  nb=[' ']*10
  nnb=['0','1','2','3','4','5','6','7','8','9']
  drawBoard(getCopy(nnb))
  humanLetter,computerLetter=playerLetter()
  turn=whoGo1st()
  a=True
  

  while a:
        if turn==0:
            b='kk'
            while b=='kk':
              print('plz input a number to choose the place')
              move1=input()

              if move1 in ['1','2','3','4','5','6','7','8','9']:
                 move1=int(move1)
             
                 if nb[move1]==' ':
                    nb[move1]=humanLetter
                    b='gg'
         


            drawBoard(nb)
            if isWin(nb,humanLetter):
                print(' You win the game')
                break
            elif isTie(nb):
                print('the game is tie')
                break
            else:
                turn=1

        else:
          nn='mm'
         
          for i in [0,1,2,3,4,5,6,7,8,9]:
              if nn!='gg':
                 copy=getCopy(nb)
                 if copy[i]==' ':
                    copy[i]=computerLetter
                    
                    if isWin(copy,computerLetter):
                       int(i) 
                       nb[i]=computerLetter
                       drawBoard(nb)
                       print('The AI is win~')
                       print('============')
                       print(i)
                       print('=============')
                       nn='gg'
                       a=False
                       break #<<<這個break只是結束掉for這個迴圈
                       
                          
                      

                    else :
                          if isTie(copy):
                             drawBoard(nb)
                             nn='gg'
                             a=False
                             break #<<<這個break只是結束掉for這個迴圈

          for i in [0,1,2,3,4,5,6,7,8,9]:

               copy=getCopy(nb)
               if copy[i]==' ':                    
                  copy[i]=humanLetter

                  if  nn!='gg':
                        if isWin(copy,humanLetter):
                           nb[i]=computerLetter
                           nn='gg'
                           drawBoard(nb)
                           turn=0
                           
                           break #<<<這個break只是結束掉for這個迴圈 
                    
                          

                   
          if nn!='gg':
               if nb[1]==' 'or nb[3]==' ' or nb[7]==' ' or nb[9]==' ':
                            
                            nnnb=[]
                            for i in [1,3,7,9]:
                               
                               if nb[i]==' ':
                                  nnnb.append(i)
                                  
                            k=random.choice(nnnb)
                            print('==========')
                            print(k)##
                            nb[k]=computerLetter
                            print('============')
                            drawBoard(nb)
                            turn=0

               elif nb[5]==' ':
                            nb[5]=computerLetter
                            drawBoard(nb)
                            turn=0

               else:
                            nnnb=[]                 
                            for i in [2,4,6,8]:
                                if nb[i]==' ':
                                   nnnb.append(i)
                            y=random.choice(nnnb)
                            y=int(y)
                            nb[y]=computerLetter
                            drawBoard(nb)
                            turn=0
    

                   

                   
          
            
            

  if not playAgain():
           break
             
            
            
         
    


    
        



