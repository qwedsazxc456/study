import os
filename=input("파일명:")

if not os.path.exists(filename):
    print(f'(filename)이 존재하지 않습니다.')
    exit() #프로그램 종료
    
f=open(filename,'r',encoding='utf-8')
lines=f.readlines()
i=1
for line in lines:
    line=line.replace("\n",'')
    print("{:04d} {}".format(i,line))
    i +=1
f.close()