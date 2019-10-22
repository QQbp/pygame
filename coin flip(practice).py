import random

print('我現在丟硬幣一千次，猜猜看頭像向上的有幾次？')

guess=input()
guess=int(guess)

flip=0
head=0

while flip<1000:

      if random.randint(0,1)==1:
         head=head+1

      flip=flip+1

      if flip==100:
            print('丟了100次')
      if flip==500:
            print('丟了500次')
      if flip==900:
            print('丟了900次')

print()
print('現在一千次丟完了，頭像向上的有'+str(head)+'次')



if guess==head:
    print('答對了~ 好棒喔~')

else:
          print('猜錯了喔')
