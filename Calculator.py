import random
from fractions import Fraction

def create1(q, ans):   # 两个整数的四则运算
    symbol = random.choice(['+', '-', '*', '/']) # 生成随机符号
    if symbol == '+':
        n1 = random.randint(0, 100)  # 随机生成0到100的整数
        n2 = random.randint(0, 100)
        q.append(str(n1) + ' + ' + str(n2)+' = ')
        ans.append(n1 + n2)
    elif symbol == '-':
        n1 = random.randint(0, 100)  # 随机生成0到100的整数
        n2 = random.randint(0, n1)
        q.append(str(n1) + ' - ' + str(n2)+' = ')
        ans.append(n1 - n2)
    elif symbol == '*':
        n1 = random.randint(0, 50)  # 随机生成0到100的整数
        n2 = random.randint(0, 50)
        q.append(str(n1) + ' × ' + str(n2)+' = ')
        ans.append(n1 * n2)
    else:
        n1 = random.randint(0, 50)  # 随机生成0到100的整数
        if n1 == 0:
            n2 = random.randint(1, 50)
        else:
            n2 = random.randint(1, n1)
            while n1 % n2 != 0:
                n1 = random.randint(1, 50)
                n2 = random.randint(1, n1)
        q.append(str(n1) + ' ÷ ' + str(n2)+' = ')
        ans.append(Fraction(n1, n2))

def createf():
    # 生成2个分数
    fz = random.randint(0, 20)
    if fz == 0:
        fm = random.randint(1, 20)
    else:
        fm = random.randint(fz,20)
    f1 = Fraction(fz, fm) # 第一个分数
    fz = random.randint(1, 20)
    fm = random.randint(fz, 20)
    f2 = Fraction(fz, fm) # 第二个分数
    return f1, f2

def create2(q, ans):   # 两个分数的四则运算
    symbol = random.choice(['+', '-', '*', '/'])  # 生成随机符号
    f1, f2 = createf()
    if symbol == '+':
        while f1 + f2 > 1:
            f1, f2 = createf()
        q.append(str(f1) + ' + ' + str(f2)+' = ')
        ans.append(f1 + f2)
    elif symbol == '-':
        f1, f2 = max(f1, f2), min(f1, f2)
        q.append(str(f1) + ' - ' + str(f2)+' = ')
        ans.append(f1 - f2)
    elif symbol == '*':
        while f1 * f2 > 1:
            f1, f2 = createf()
        q.append(str(f1) + ' × ' + str(f2)+' = ')
        ans.append(f1 * f2)
    else:
        while Fraction(f1, f2) > 1:
            f1, f2 = createf()
        q.append(str(f1) + ' ÷ ' + str(f2)+' = ')
        ans.append(Fraction(f1, f2))

while 1:
    print("请输入类型：1、测试 2 、练习 3、退出")
    t = int(input())
    if t == 3:
        break
    elif t == 1:           # 测试
        print("请输入你想要的四则运算：1、整数 2、分数 3、混合 4 、退出")
        n = int(input())
        while n > 4:
            print("选择类型有误！请重新选择")
            n = int(input())
        if n == 4:
            break
        print("请输入你想要的题目数量（5的倍数）：", end='   ')
        qu = int(input())
        while qu % 5 != 0:
            print("输入数目有误，请重新输入！")
            qu = int(input())
        pscore = 100 / qu
        sscore = 0
        ques = []
        ans = []
        if n == 1:         # 整数测试题目

            for i in range(qu):
                create1(ques, ans)
        elif n == 2:        #分数测试题目
            for i in range(qu):
                create2(ques, ans)
        elif n == 3:            # 混合测试题目
            for i in range(qu):
                n = random.randint(0, 3)
                if n == 0:
                    create2(ques, ans)
                else:
                    create1(ques, ans)
        for i in range(qu):
            print("第{}题：{}".format(i + 1, ques[i]),end='  ')
            a = input()
            if a == str(ans[i]):
                sscore = sscore + pscore
        print("你所得分数为：{}".format(sscore))
        print("是否查看正确答案? y/n", end='  ')
        pan = input()
        if pan == 'y':
            for i in range(qu):
                print(ques[i] + str(ans[i]))
    elif t == 2:
        print("请输入你想要的四则运算：1、整数 2、分数 3、混合 4、退出")
        n = int(input())
        while n > 4:
            print("选择类型有误！请重新选择")
            n = int(input())
        if n == 4:
            break
        print("请输入你想要的题目数量：")
        qu = int(input())
        ques = []
        ans = []
        if n == 1:                # 整数练习题目
            for i in range(qu):
                create1(ques, ans)
        elif n == 2:               # 分数练习题目
            for i in range(qu):
                create2(ques, ans)
        elif n == 3:                     # 混合练习题目
            for i in range(qu):
                n = random.randint(0,3)
                if n == 0:
                    create2(ques, ans)
                else:
                    create1(ques, ans)
        else:
            print("选择类型有误！请重新选择")
        for i in range(qu):
            print("第{}题：{}".format(i + 1, ques[i]),end='  ')
            a = input()
            if a == str(ans[i]):
                print("回答正确！")
            else:
                print("回答错误！正确答案为：{}".format(ans[i]))
    else:
        print("选择类型有误！请重新选择")