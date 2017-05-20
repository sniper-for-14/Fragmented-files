# 文件名：实验一：作业调度的模拟.py
# 時間:2017-05-19
# 運行環境:OS X , Python3.6
# 年級:15級
# 班級:4班
# 作者:曹國鴻
# 學號:2015015305

from operator import itemgetter


# 先來先服務調度模塊
def fifo(list):
    list=sorted(list,key=itemgetter(1))
    print("""
先來先服務調度算法
*****************************************************************************************
*\t作業編號\t*\t進入時間\t*\t服務時間\t*\t開始時間\t*\t完成時間\t*\t週轉時間\t*\t帶權周轉時間\t*
*****************************************************************************************""")
    end_list=[];zhou_list=[];dq_zhou_list=[];now=0
    for i in range(len(list)):
        if i==0:
            end_list.append(list[0][1]+list[0][2]);zhou_list.append(end_list[0]-list[0][1]);dq_zhou_list.append(zhou_list[0]/list[0][2])
            now=now+list[0][1]+list[0][2]
        else:
            if list[i][1]<=now:
                end_list.append(now+list[i][2]);zhou_list.append(end_list[i]-list[i][1]);dq_zhou_list.append(zhou_list[i]/list[i][2])
                now=now+list[i][2]
            else:
                end_list.append(list[i][1]+list[i][2]);zhou_list.append(end_list[i]-list[i][1]);dq_zhou_list.append(zhou_list[i]/list[i][2])
                now=end_list[i]
    avg=0
    for i in range(len(list)):
        print("""*\t  %d  \t*\t  %d  \t*\t  %d  \t*\t  %d  \t*\t  %d  \t*\t  %d  \t*\t  %.2f  \t*
*****************************************************************************************"""
        % (list[i][0], list[i][1], list[i][2],end_list[i]-list[i][2],end_list[i],zhou_list[i],dq_zhou_list[i]))
        avg+=dq_zhou_list[i]
    print("\n平均帶權周轉時間："+str(avg/len(list))+"\n")



# 短任務優先調度模塊
def si(list):
    list=sorted(list,key=itemgetter(2))

    now=0;i=0;run=False
    print("""
短任務優先調度
*****************************************************************************************
*\t作業編號\t*\t進入時間\t*\t服務時間\t*\t開始時間\t*\t完成時間\t*\t週轉時間\t*\t帶權周轉時間\t*
*****************************************************************************************""")
    while i < len(list):
        # if i==0:
        #     list[i].append(list[i][1]);list[i].append(list[i][3]+list[i][2]);list[i].append(list[i][4]-list[i][1]);list[i].append(list[i][5]/list[i][2])
        #     now+=list[0][4];i+=1
        # else:
        if list[i][1]<=now:
            list[i].append(list[i-1][4]);list[i].append(list[i][2]+list[i][3]);list[i].append(list[i][4]-list[i][1]);list[i].append(list[i][5]/list[i][2])
            i += 1
        else:
            mi=list[i];t=0;m=0
            for a in list:
                if a[1]<mi[1]:
                    m=t
                    mi=a
                # list.insert(i,list[m])
                # del list[t+1]
                t+=1
            list.insert(i,list[m])
            del list[m+1]
            list[i].append(list[i][1]);list[i].append(list[i][3] + list[i][2]);list[i].append(list[i][4] - list[i][1]);list[i].append(list[i][5] / list[i][2]);now += list[0][4];i += 1


    avg=0
    for i in list:
        print("""*\t  %d  \t*\t  %d  \t*\t  %d  \t*\t  %d  \t*\t  %d  \t*\t  %d  \t*\t  %.2f  \t*
*****************************************************************************************"""
              %(i[0],i[1],i[2],i[3],i[4],i[5],i[6]))
        avg+=i[6]
    print("\n平均帶權周轉時間："+str(avg/len(list))+"\n")



# 展示作業狀態
def show(list):
    print("""
*************************************
*\t作業編號\t*\t進入時間\t*\t服務時間\t*
*************************************""")
    for i in list:
        print("""*\t  %d  \t*\t  %d  \t*\t  %d  \t*
*************************************""" %(i[0],i[1],i[2]))



if __name__=="__main__":
    work=[];bo=False
    try:
        i = int(input('請輸入作業數量(默認為4)：'))
    except:
        i=4
    while bo==False:
        try:
            for num in range(i):
                temp = input("請輸入作業%s進入時間和服務時間(用空格隔離)：" % str(num + 1)).split()
                start = temp[0]
                ti = temp[1]
                work.append([num + 1, int(start), int(ti)])
                del temp, start, ti
                bo=True
        except:
            print("輸入異常,請重新輸入所有數據")
            bo=False
    show(work)
    try:
        typ = input("""

1. 先來先服務調度算法
2. 短作業優先調度算法
3. 兩者比較
請輸入作業編號(默認執行3)：""")
    except:
        typ=3
    if typ=="1":
        fifo(work)
    elif typ=="2":
        si(work)
    else:
        fifo(work)
        si(work)
