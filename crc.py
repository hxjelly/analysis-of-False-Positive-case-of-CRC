#!/usr/bin/env python
# coding: utf-8

# In[60]:


import math
R.<x>=GF(2)[]
E = []  #存放结果

#input:1010 output:x^3 + x
def bin_2_poly(P_bin): 
    before = bin(int(str(P_bin),2))[2:]
    P = 0
    for i in range(len(before)):
        if (before[i] == (bin(1)[2:])):
            P += x^(len(before) - 1-i)
    return P

#input:10 output:x^3 + x
def int_2_poly(P_int): 
    before = bin(int(str(P_int),10))[2:]
    P = 0
    for i in range(len(before)):
        if (before[i] == (bin(1)[2:])):
            P += x^(len(before) - 1-i)
    return P

#poly_2_bin(x^3+1)  output:1001
def poly_2_bin(poly_nstr):  
    poly = str(poly_nstr)
    poly_final = poly.replace(' ','')
    terms = poly_final.split('+')
    terms_final = [element.replace('x^','') for element in terms]
    #print(terms_final)
    sum = 0
    for element in terms_final:
        if (element == '1'):
            sum += 1
        elif (element == '0'):
            pass
        elif(element == 'x'):
            sum += 2
        else:
            deg = int(element,10)
            sum += 2^deg
    return bin(sum)[2:]

#tot个比特中取num个为1，剩余为0,返回列表
def recur(tot,num): 
    res = []
    if(tot < num): #出错
        res.append('null')
        return res
    if(tot == num): #相等
        p = ''
        for i in range(tot):
            p+='1'
        res.append(p)
        return res
    if(tot==1): #1,1 1,0
        if (num == 1):
            res.append('1')
            return res
        if (num == 0):
            res.append('0')
            return res
        res.append('null')
        return res
    if (num == 0): #x,0
        p = ''
        for i in range(tot):
            p+='0'
        res.append(p)
        return res
    if (num == 1): #x,1
        for j in range(tot):
            p = ''
            for i in range(j): #0...0
                p += '0'
            p+='1' #0..01
            for x in range(j+1,tot): #0..010..0
                p+='0'
            res.append(p)
        return res
    #非边界情况
    a = recur(tot-1,num-1)
    if (('null' in a) == False):
        for i in a:
            res.append('1'+i)
    b = recur(tot-1,num)
    if (('null' in b) == False):
        for j in b:
            res.append('0'+j)
    return res
#根据得到的结果，进行形式化输出
def convert_result_output(result1):
    new_result = []
    for element in result1:
        if(len(element) < n):
            padding = ''
            for i in range(n - len(element)):
                padding += '0'
            new_element = padding + element
            new_result.append(new_element)
        else:
            new_result.append(element)
    location_all = []
    for element in new_result:
        location = []
        for i in range(len(element)):
            if(element[i] == '1'):
                location.append(i+1)
        location_all.append(location)
    for j in range(len(result1)):
        print('case'+str(j+1)+': bit flipping ',end='')
        cnt = 0
        for t in location_all[j]:
            if(cnt == len(location_all[j]) - 1):
                print('and '+str(t)+'th bits(i.e. E(x) = '+str(new_result[j])+')')
            else:
                print(str(t)+' ',end='')
            cnt+=1
    print('Remark: counting from left to right,beginning from 1')

#plan1
def plan1():
    print('testing...')
    for i in range(1,2^k): #1 ~  2^k-1
        temp_poly = P_poly * int_2_poly(i)
        real_num = len(temp_poly.coefficients()) #翻转了多少位，就有多少项
        if (real_num == expect_num):
            E.append(temp_poly)
    print('testing done.')
    if(E == []):
        print('No possible case that can pass the CRC!')
    else:
        print(str(len(E))+' cases that can pass the CRC:')
        result = [poly_2_bin(i) for i in E]
        convert_result_output(result)
        
def plan2():
    choice_bin = recur(n,expect_num)
    choice_poly = [bin_2_poly(i) for i in choice_bin]
    print('testing...')
    for loop in choice_poly:
        if(loop % P_poly == 0):
            E.append(loop)
    print('testing done.')
    if(E == []):
        print('No possible case that can pass the CRC!')
    else:
        print(str(len(E))+' cases that can pass the CRC:')
        result = [poly_2_bin(i) for i in E]
        convert_result_output(result)

# --- main ---
        
#各个参数
print('input whole length of message (demo: 10)  n = ')
n = int(input())
print('input the P polynomial, need to match with 1(0|1)* demo:11001.  P =')
P = input()
r = len(str(P)) - 1
k = n - r
P_poly = bin_2_poly(P)
print('Expecting how many bits to be inverted,i.e 0to1,1to0? input a number(demo:3):')
while(1):
    expect_num = int(input())
    if(expect_num >= 0 and expect_num <= n):
        break
    else:
        print('invalid input. Please check and input again!')
        continue
#计算迭代循环的复杂度（具体次数）
deg_plan1 = 2^k-1
deg_plan2 =(math.factorial(n)//(math.factorial(expect_num)*math.factorial(n-expect_num)))
if(deg_plan1 > deg_plan2):#先筛比特翻转数再遍历，更快
    print('---using plan2---')
    plan2()
else:#先遍历再筛比特翻转数，更快
    print('---using plan1---')
    plan1()


# In[55]:





# In[ ]:




