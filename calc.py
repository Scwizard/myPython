# -*- coding: UTF-8 -*-

#@Auther: Scwizard, EmginNetwork
#@Time: 2023.5.18
#@Python 3.10
import statistics
import random
import os

def choose():
    print("欢迎使用计算器程序.\n1.最大值计算.\n2.最小值计算.\n3.平均数计算.\n4.中位数计算.\n5.极差计算.\n6.求和计算.\n7.猜数游戏.\n8.范围内随机取值.\n0.退出\n")
    try:
        choice=int(input("请选择数字：\n"))
    except:
        print("能不能输点正常的东西？\n")
        choose()
        return false
    if choice==1:
        queryMax()
    elif choice==2:
        queryMin()
    elif choice==3:
        queryAverage()
    elif choice==4:
        queryMedian()
    elif choice==5:
        queryRange()
    elif choice==6:
        queryAnd()
    elif choice==7:
        randomCheck()
    elif choice==8:
        queryRandom()
    elif choice==0:
        exit()
    else:
        print("不在可选范围内")
        choose()

def queryMax():
    maxCheck()
    Array=list(range(0,numberLengthMax))
    numberCurrent=0
    for numberCurrent in Array:
        global numberDisplay
        numberDisplay = str(numberCurrent+1)
        inputCheck()
        Array[numberCurrent]=numberInput
    maxNumberDisplay=str(max(Array))
    input("最大值为："+maxNumberDisplay)
def queryMin():
    numberLengthMin=int(input("你选择了计算最小值，请输入一共要计算多少个数字："))
    Array=list(range(0,numberLengthMin))
    numberCurrent=0
    for numberCurrent in Array:
        global numberDisplay
        numberDisplay=str(numberCurrent+1)
        inputCheck()
        Array[numberCurrent]=numberInput
    minNumberDisplay=str(min(Array))
    input("最小值为："+minNumberDisplay)
def inputCheck():
    global numberInput
    try:
        numberInput=int(input("请输入第 "+numberDisplay+" 个数字：\n"))
    except:
        print("输入有误，请输入一个数字！")
        inputCheck()
def queryAverage():
    try:
        numberLength=int(input("你选择了计算平均数，请输入一共要计算多少个数字："))
    except:
        print("输入有误，请输入一个数字！")
        queryAverage()
    Array=list(range(0,numberLength))
    numberCurrent=0
    for numberCurrent in Array:
        global numberDisplay
        numberDisplay=str(numberCurrent+1)
        inputCheck()
        Array[numberCurrent]=numberInput
    averageNumberDisplay=str(sum(Array)/len(Array))
    input("平均数为："+averageNumberDisplay)
def queryMedian():
    try:
        numberLengthMedian=int(input("你选择了计算中位数，请输入一共要计算多少个数字："))
    except:
        print("输入有误，请输入一个数字！")
        queryMedian()
    Array=list(range(0,numberLengthMedian))
    numberCurrent=0
    for numberCurrent in Array:
        global numberDisplay
        numberDisplay=str(numberCurrent+1)
        inputCheck()
        Array[numberCurrent]=numberInput
    medianNumberDisplay=str(statistics.median(Array))
    input("中位数为："+medianNumberDisplay)
def queryRange():
    try:
        numberLengthRange=int(input("你选择了计算极差，请输入一共要计算多少个数字："))
    except:
        print("输入有误，请输入一个数字！")
        queryRange()
    Array=list(range(0,numberLengthRange))
    numberCurrent=0
    for numberCurrent in Array:
        global numberDisplay
        numberDisplay=str(numberCurrent+1)
        inputCheck()
        Array[numberCurrent]=numberInput
    RangeNumberDisplay=str(max(Array)-min(Array))
    input("极差为："+RangeNumberDisplay)
def queryAnd():
    try:
        numberLengthAnd=int(input("你选择了数组求和，请输入一共要计算多少个数字："))
    except:
        print("输入有误，请输入一个数字！")
        queryAnd()
    Array=list(range(0,numberLengthAnd))
    numberCurrent=0
    for numberCurrent in Array:
        global numberDisplay
        numberDisplay=str(numberCurrent+1)
        inputCheck()
        Array[numberCurrent]=numberInput
    AndNumberDisplay=str(sum(Array))
    input("数组和为："+AndNumberDisplay)
#这里是该死的一堆输入验证
def maxCheck():
    global numberLengthMax
    try:
        numberLengthMax=int(input("你选择了计算最大值，请输入一共要计算多少个数字：\n"))
    except:
        print("输入有误，请输入一个数字！")
        maxCheck()
def randomCheck():
    global guessTimes
    guessTimes = 0
    global numberStart
    global numberEnd
    try:
        numberStart=int(input("你选择了猜数游戏.\n请输入开始数字：\n"))
    except:
        print("输入有误，请输入一个数字！\n")
        randomCheck()
    try:
        numberEnd=int(input("请输入结束数字：\n"))
    except:
        print("输入有误，请输入一个数字！\n")
        randomCheck()
    if numberStart>=numberEnd:
        print("输入错误，结束量不能小于开始量！\n")
        randomCheck()
        return false
    global numberGenerated
    # guessTimes = int(guessTimes)
    numberGenerated=random.randint(numberStart,numberEnd)
    getGuessInput()
def getGuessInput():
    try:
        guessNumberInput = int(input("猜猜看：\n"))
    except:
        print("输入有误，请输入一个数字！")
        getGuessInput()
        return false
    if guessNumberInput == numberGenerated:
        global guessTimes
        guessTimes = guessTimes + 1
        input("猜对啦，你猜了 "+str(guessTimes)+" 次！\n")
    else:
        guessTimes = guessTimes + 1
        if guessNumberInput >= numberGenerated:
            print("恭喜你，猜错了，这个数太大了！\n")
        else:
            print("恭喜你，猜错了，这个数太小了！\n")
        getGuessInput()
def queryRandom():
    global numberStart
    global numberEnd
    try:
        numberStart=int(input("你选择了随机取值.\n请输入开始数字：\n"))
    except:
        print("输入有误，请输入一个数字！\n")
        queryRandom()
    try:
        numberEnd=int(input("请输入结束数字：\n"))
    except:
        print("输入有误，请输入一个数字！\n")
        queryRandom()
    if numberStart>=numberEnd:
        print("输入错误，结束量不能小于开始量！\n")
        rqueryRandom()
        return false
    global numberGenerated
    # guessTimes = int(guessTimes)
    numberGenerated=random.randint(numberStart,numberEnd)
    input("随机数为：" + str(numberGenerated))
choose()