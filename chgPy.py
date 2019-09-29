import sys,os


def ChangeYourPy(filePath,mode):
    headList=["import sys,os\n",
              "sys.stdin=open(r'{0}','r',encoding='utf-8')\n".format('./'+'input.txt'),
              "sys.stdout=open(r'{0}','a+',encoding='utf-8')\n".format('./'+'output.txt')
              ]
    endList=["\nsys.stdout.close()\n","sys.stdin.close()\n"]
    if mode:
        headList[2]= "sys.stdout=open(r'{0}','w',encoding='utf-8')\n".format('./'+'output.txt')
    with open(filePath,'r',encoding='utf-8') as f:
        py=f.readlines()
    upy=''
    for i in py:
        upy+=i
    s= "# -*- coding: utf-8 -*-\n"+''.join(headList)+upy+''.join(endList)
    with open(filePath, 'w', encoding='utf-8') as f:
        f.write(s)


if __name__=='__main__':
    newpy=ChangeYourPy(r'E:\refvdsvdv\evaluation\021700125\021700125.py')