sugar = int(input())
if(sugar==4 or sugar==7):sugar=-1
elif(sugar%10==1):sugar=(sugar-6)//5+2
elif(sugar%10==2):sugar=(sugar-12)//5+4
elif(sugar%10==3):sugar=(sugar-3)//5+1
elif(sugar%10==4):sugar=(sugar-9)//5+3
elif(sugar%10==5 or sugar%10==0):sugar=sugar//5
elif(sugar%10==6):sugar=(sugar-6)//5+2
elif(sugar%10==7):sugar=(sugar-12)//5+4
elif(sugar%10==8):sugar=(sugar-3)//5+1
elif(sugar%10==9):sugar=(sugar-9)//5+3
print(sugar)
