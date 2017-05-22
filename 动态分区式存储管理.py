# 文件名:任务4：动态分区式存储管理
# 時間:2017-05-18
# 運行環境:OS X , Python3.6
# 年級:15級
# 班級:4班
# 作者:曹國鴻
# 學號:2015015305

# 部分主变量

from operator import itemgetter
import sys
import os

# 初始化模拟内存空间
def init(size):
    if int(size[0])>=int(size[1]):
        RAM = [[1],[int(size[1])+1]]
        RAM[0].append(int(size[1]));RAM[0].append("Busy");RAM[0].append("OS")
        RAM[1].append(int(size[0]) - int(size[1]));RAM[1].append("Free");RAM[1].append(" ")
        print("初始化内存(" + str(size[0]) + "KB)成功")
        return RAM
    else:
        return False



# 分配内存 best：最佳适应算法  first：首次适应算法
def allocation(RAM,type="first"):
    name = input("请输入需要分配的内存作业编号: ")
    size = int(input("请输入需要分配的内存作业占用空间大小(KB): "))
    bo=False
    if type=="best":
        RAM,bo=best(RAM,name,size)
    else:
        RAM,bo=first(RAM,name,size)
    if bo:
        print("内存分配成功")
    else:
        print("内存分配失败")
    show(RAM)
    return RAM


def best(RAM,name,size):
    try:
        l=0;bo=False;mi=None;ad=0
        for li in RAM:
            if li[2]=="Free" and li[1]>=size:
                if mi==None:
                    mi=li[1];ad=l
                else:
                    if mi>li[1]:
                        mi=li[1];ad=l
                bo=True
            l+=1
        if bo:
            RAM.append([RAM[ad][0], size, "Busy", name])
            RAM[ad][0] += size;RAM[ad][1] -= size
            # RAM=sorted(RAM,key=itemgetter(1))
            RAM.sort()
        return RAM, bo
    except:
        return RAM,False



def first(RAM,name,size):
    try:
        l=0;bo=False
        for li in RAM:
            if li[2]=="Free" and li[1]>=size:
                RAM.append([li[0],size,"Busy",name])
                RAM[l][0]=li[0]+size;RAM[l][1]-=size
                bo=True
                break
            l+=1
        # RAM=sorted(RAM,key=itemgetter(1))
        RAM.sort()
        return RAM,bo
    except:
        return RAM,False




# 回收内存
def recover(RAM,name):
    l=0;bo=False
    for li in RAM:
        if li[3]==name:
            RAM[l][2]="Free";RAM[l][3]=" "
            bo=True
        l+=1
    l=0
    for li in RAM:
        if li[2]=="Free":
            try:
                if RAM[l+1][2]=="Free":
                    RAM[l][1]+=RAM[l+1][1];del RAM[l+1]
            except:
                pass
        l+=1
    if bo:
        print("作业 %s 回收成功！"%(name))
    else:
        print("内存回收失败")
    show(RAM)
    return RAM



# 展示内存状况  a=[num,num,str,str]
def show(RAM):
    print("""
**************************************************
*              \t当前的内存分配情况\t                 *
**************************************************
*\t起始地址\t*\t空间大小\t*\t工作状态\t*\t作业号\t *
**************************************************""")
    for a in RAM:
        print("""*\t %d  \t*\t %d  \t*\t %s  \t*\t %s  \t *
**************************************************"""%(a[0],a[1],a[2],a[3]))




# 主函数
if __name__=="__main__":
    # try:
        size=input('请输入初始化内存大小和OS占用大小(中间用空格隔开)：').split()
        RAM = init(size)
        show(RAM)
        type=input("""
1、最佳適應算法
2、首次適應算法
3、退出程式
請選擇算法類型: """)
        exi=True;bo=False;t="1"
        while exi:
            t=input("""
1、分配内存
2、回收内存
3、退出程式
請選擇任務: """)
            # RAM = sorted(RAM, key=itemgetter(1))
            RAM.sort()
            if type=="1" and t=="1":
                RAM=allocation(RAM,type="best")
            elif type=="2" and t=="1":
                RAM=allocation(RAM,type="first")
            elif t=="2":
                na=input("請輸入回收等任務名稱: ")
                RAM=recover(RAM,na)
            elif t=="3" or type=="3":
                sys.exit("程式已結束")
            else:
                print("請確認輸入算法类型")

    # except:
    #     print("⚠：内存初始化失败")
