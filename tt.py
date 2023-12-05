import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt







# st.image('gam.jpg', width=300)
col1, col2 = st.columns(2)
with col1:
    st.image('gam.jpg', width=300)
with col2:
    st.write('놓치면 후회할 인재(김인..직, 시급 3만원🔥)')
    '전화번호📞 : 010-xxxx-xxxx'
    'email✉️ : xxxxxx@xxxxx.com'
    '주소🏠 : 충남 논산시 대학로 121'
''
''
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.link_button("YouTube(🌐)", "https://www.youtube.com/@gamst6217")
with col2:
    st.link_button("AfreecaTV(🌏)", "https://bj.afreecatv.com/devil0108")
with col3:
    st.link_button("Instagram(📷)", "https://www.instagram.com/gamst17172/")
with col4:
    st.link_button("Cafe(☕)", "https://cafe.naver.com/gamstfan")

''
''
'## :red[자기소개]'
'#### 맹박사님을 아세요?'


# fig, ax = plt.subplots()

# c = 20 #원하는 수 정의
# x = []
# y = []
# for i in range(-c,c,5):
#     x.append(i)
#     y.append(3*i**3 - 5*i**2 + 3*i - 7)

# col1, col2, col3 = st.columns(3)
# with col1:
#     color = st.radio('선의 색을 선택하시오.', ['red', 'green', 'blue', 'orange'])
# with col2:
#     marker = st.radio('마커의 형태를 선택하시오', ['o', '^', 's', 'p','h'])
# with col3:
#     linestyle = st.radio('선의 스타일을 선택하시오.', ['-', '-.', ':'])


# plt.plot(x, y, color = color, marker = marker, linestyle = linestyle)
# st.pyplot(fig)






# a = 2
# b = -5
# c = 3
# d = -7

# x = []
# y = []
# for i in range(-100, 101, 50):
#     x.append(i)
#     y.append(2*i**3 + 5*i**2 + 3*i - 7)
#     # y.append(a*i**3 + b*i**2 + c*i + d)

# col1, col2, col3 = st.columns(3)
# with col1:
#     color = st.radio('색을 선택하시오.', ('red', 'green', 'blue'))
# with col2:
#     linestyle = st.radio('선의 스타일을 선택하시오.', ('-', '-.', ':'))
# with col3:
#     marker = st.radio('마커의 스타일을 선택하시오', ('s', '^', 'o'))

# if 'red' in color:
#     t = '-.r^'
# if 'green' in color:
#     t = '-.g^'
# if 'blue' in color:
#     t = '-.b^'


# plt.plot(x, y, color = color, marker = marker, linestyle = linestyle)
# st.pyplot(fig)






# a = pd.Series([1, 2, 3, 4])
# st.write(a)
# b = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
# st.write(b)

# list1 = list([['한빛', '남자', '20', '180'], ['한결', '남자', '21', '177'], ['한라', '여자', '20', '160'], ['김한결', '남자', '27', '170'], ['허준호', '남자', '30', '183'], ['이가원', '여자', '24', '162'], ['배규민', '님자', '23', '179'], ['고고림', '남자', '21', '182'], ['이새봄', '여자', '28', '160'], ['이보람', '여자', '26', '163'], ['이루리', '여자', '24', '157'], ['오다현', '여자', '24', '172']])
# col_names = ['이름', '성별', '나이', '키']
# df = pd.DataFrame(list1, columns=col_names, index=['1행', '2행', '3행', '4행', '5행', '6행', '7행', '8행', '9행', '10행', '11행', '12행'])
# df
# number = st.number_input('Insert a number', value=20, step=1)
# df.iloc[3, 2] = number

# import streamlit as st

# genre = st.radio("선택하시오", ["오름차순", "내림차순", "기타", "요약"], horizontal=True, index=2)

# if '오름' in genre:
#     st.dataframe(df.sort_values(by=['키']))
# if '내림' in genre:
#     st.dataframe(df.sort_values(by=['키'], ascending=False))
# if '기타' in genre:
#     st.dataframe(df)
# if '요약' in genre:
#     st.dataframe(df.describe())


# li = [1, 2, 3, 4]
# li

# for i in range(4):
#     li[i] = li[i] + 3
#     li
# li = np.array([7, 2, 5, 4])
# li
# li_sort = np.sort(li)[::-1]
# li_sort
#오름차순 : ascending, 내림차순 : descending





# import random


# t = turtle.Turtle()
# t.shape('turtle')

# t.width(3)
# t.speed(0)
# # t.color('olive')
# t.penup()
# t.goto(-200, 0)
# t.pendown()

# #기말고사 문제!!
# def shape(n):
#     if n == 'circle':
#         t.circle(1 + 5*i)
#     else:
#         for _ in range(n):
#             t.forward(1 + 5*i)
#             t.left(360/n)

# while True:
#     for i in range(30):
#         shape('circle')
#         t.color((random.random(), random.random(), random.random()))
#         t.goto(i*20, 0)
#     t.clear()

# Turtle.done()

# while True:
#     for _ in range(4):
#         t.forward(100)
#         t.left(90)
#         t.forward(100)
#         t.left(90)
#         t.forward(100)
#         t.left(90)
#         t.forward(100)
#         t.color((random.random(), random.random(), random.random()))
#         t.goto(i*20, 0)
#     t.clear()


# import random

# t1 = turtle.Turtle()
# t1.shape('turtle')

# t1.width(5)
# t1.color('red')
# t1.penup()
# t1.goto(-100, 100)
# t1.pendown()
# t1.forward(100)

# t2 = turtle.Turtle()
# t2.shape('turtle')


# t2.width(5)
# t2.color('blue')
# t2.penup()
# t2.goto(-100, -100)
# t2.pendown()
# t2.forward(100)

# for i in range(30):
#     d1 = random.randint(1, 60)
#     t1.forward(d1)
#     d2 = random.randint(1, 60)
#     t2.forward(d2)

# turtle.done()


# #1차원 배열 생성하기
# a = np.arange(8)
# st.write('a\n', a)

# #다차원 배열로 변경하기
# a.shape = (2,4)
# st.write('shape\a', a)

# #1차원 배열로 변경하기
# st.write('flatten\n', a.flatten())

# #resize 함수로 모양 변경하기
# a.resize((4,2))
# st.write('resize\n', a)

# def find_number(n):
#     result = []
#     for number in range(1, n + 1):
#         if number % 7 == 3:
        

# n = 100
# for i in range(1,n):
#     if i % 7 == 3:
#         i

# def generate_diagonal_matrix(n):
#     matrix = [['나머지' if i != j else '대각선' for i in range(n)] for j in range(n)]
#     return matrix

# n = 5
# result = generate_diagonal_matrix(n)

# for row in result:
#     st.write(row)

# n1 = np.zeros((4, 5))
# n1
# for i in range(4):
#     n1[i, j] = 10
# n1

# n2 = []
# n2.append(10)
# n2
# n2 = np.append(n2, 15)
# n2

# arr = np.array([1, 2, 3])
# s = arr.sum()
# s
# s1 = np.sum(arr)
# s1


# n = 10  #원하는 n 값을 지정
# arr = np.full((n, n), ' ')
# st.write(arr)

# for i in range(n):
#     for j in range(n):
#         arr[i, j] = '나머지'
#         if i == j:
#             arr[i, j] = '대각선'
#         if i + j == n-1:
#             arr[i, j] = '대각선'

# st.write(arr)

# def create_diagonal_matrix(n):
#     matrix = []
#     for i in range(n):
#         row = []
#         for j in range(n):
#             if i == j:
#                 row.append('대각선')
#             else:
#                 row.append('나머지')
#         matrix.append(row)
#     return matrix

# n = 5  # 원하는 n 값을 지정하세요
# result_matrix = create_diagonal_matrix(n)

# # 배열 출력
# for row in result_matrix:
#     print(row)

# list1 = [[10, 10, 10, 10],
#          [10, 10, 10, 10],
#          [10, 10, 10, 10],
#          [10, 10, 10, 10],
#          [10, 10, 10, 10]]
# a = np.array(list1)
# st.write(a)






# list1 = [[1, 2, 3, 4], [3, 5, 7, 9]]
# a = np.array(list1)
# a

# arr = np.array([[0, 1, 2], [3, 4 ,5]])

# st.write('type(arr): ', type(arr))
# st.write('arr.ndim: ', arr.ndim)
# st.write('arr.dtype: ', arr.dtype)
# st.write('arr.itemsize: ', arr.itemsize)
# st.write('arr.size: ', arr.size)
# st.write('arr.nbytes: ', arr.nbytes)
# st.write('arr.T:\n', arr.T)
# st.write('arr.shape: ', arr.shape)



# n = np.full((10,5), 7)

# n = np.eye(5)
# n


# n = 80
# def user_eye(n):
#     arr = np.zeros((n, n))
#     for i in range(n):
#         for j in range(n):
#             if i == j:
#                 arr[i, j] = 1
#     return arr

# arr = user_eye(10)
# arr





# s = a.sum(axis=0)
# s
# mn = a.min(axis=1)
# mn

# a = np.zeros(2)
# st.write('a\n', a)
# b = np.zeros((2,2))
# st.write('b\n', b)
# c = np.ones((2,3))
# st.write('c\n', c)
# d = np.full((2,3), 5)
# st.write('d\n', d)
# e = np.eye(3)
# st.write('e\n', e)




# #리스트를 생성하고 배열로 변환하기
# list1 = [1, 2, 3, 4]
# a = np.array(list1)
# st.write('a.shape: ', a.shape)
# st.write('a[0]: ', a[0])

# #2차원 배열 생성하기
# b = np.array([[1, 2, 3], [4, 5, 6]])
# st.write('b.shape: ', b.shape)
# st.write('b[0,0]: ', b[0,0])

# t = turtle.Turtle()
# t.shape('turtle')
# t.speed(1)
# t.width(5)
# t.color('blue')

# t.hideturtle()

# t.write("조윤찬",  move=False, align="center", font=("arial",50,"bold"))

# t.penup()
# t.sety(-100)
# t.pendown()

# t.write("Hello Python", move=False, align="center", font=("Freestyle Script",50,"normal"))


# t.forward(100)
# # t.backward(100)
# t.left(120)
# t.forward(100)
# t.left(120)
# t.fd(100)
# t.left(180)
# t.fd(100)

# t.circle(100)

# t.forward(200)


# turtle.done()

# print("파이선의 세계에 오신 것을 환영합니다.")

# st.write("파이선의 세계에 오신 것을 환영합니다.")

# name = '철수'
# print(name)

# name = '영희'
# print(name)

# 2_name = '철수, 영희'
# print(name)

# Addr = '서울특별시 중구'
# print(Addr)

# Area = 3.14*10*10
# st.write(Area)
# print(Area)

# a = 11
# b = 4

# st.write('15', a + b)
# st.write('7', a - b)
# st.write('44', a * b)
# st.write('2.75', a / b)
# st.write('2', a // b)
# st.write('3', a % b)
# st.write('14641', a ** b)

# st.write(a > b)
# st.write(a >= b)
# st.write(a < b)
# st.write(a <= b)


# a = 10
# b = 5

# st.write(a == b)
# st.write(a != b)


# a = True
# b = False

# st.write(a and b)
# st.write(a or b)


# a = True
# b = False

# st.write(not a)
# st.write(not b)


# a = 3
# B = [1, 3, 5, 7, 9]

# st.write(a in B)
# st.write(a not in B)


# A = "엄마"
# B = ["아빠", "엄마", "딸"]

# st.write(A in B)
# st.write(A not in B)

# PI = 3.14
# 5.5 * 5.5 * PI

# A = 10 * 4 * (1/2)
# B = 9 * 5 * (1/2)
# st.write(A == B)

# 92 * 4 - 95 - 88 - 90

# a = 5

# if a == 5:
#     st.write('Right!')
#     st.write('a is 5')
# if a == 3:
#     st.write('Right!')
#     st.write('a is 3')
# if a != 3:
#     st.write('Right!')
#     st.write('a is not 3')


# a = 5

# if a == 5:
#     st.write('Right!')
#     st.write('a is 5')
# else :
#     st.write('a is not 5')

# a = 3

# if a == 5:
#     st.write('Right')
#     st.write('a is 5')
# else :
#     st.write('a is not 5')


# a = 5

# if a < 5:
#     st.write('a is smaller than 5')
# elif a > 5:
#     st.write('a is larger than 5')
# else:
#     st.write('a is 5')


# a = 19
# b = 12
# c = a * b * 3

# if c % 2 == 0:
#     st.write('짝수')
# else:
#     st.write('홀수')


# a = 5
# i = 1

# while i <=9:
#     st.write(str(a) + 'X' + str(i) + '=' + str(a*i))
#     i += 1
# st.write('파이썬으로 구구단 5단을 계산할 수 있다.')

# a = 5

# for i in range(1,10):
#     st.write(str(a) + 'X' + str(i) + '=' + str(a*i))
# st.write('while 조건문을 for 조건문으로 바꾸어 사용할 수 있다!')

# grade = 60

# if grade >= 60:
#     st.write('Right!')
#     st.write('grade larger than 60')

# a = 5

# if  a == 5:
#     st.write('Right!')
#     st.write('a is 5')
# if a == 3:
#     st.write('Right!')
#     st.write('a is 3')
# if a != 3:
#     st.write('Right!')
#     st.write('a is not 3')


# sum = 0
# for in range(0:11):
#     if i % 2 == 0:
#         sum += i
# st.write(sum)

# while True:

#     print('음료목록 1.오렌지주스(100원), 2.커피(200원), 3.콜라(300원)')
#     coin = int(input('동전을 넣으세요.'))
#     drink = int(input('음료를 고르세요.\n'))
#     if drink == 1:
#     #오렌지주스 100원
#         if coin >= 100:
#             remain = coin - 100
#             print('오렌지주스가 곧 제공됩니다.')
#             print('거스름돈은 {}원입니다.'.format(remain))
#         else:
#             st.write('잔액이 부족합니다.')   
#     elif drink == 2:
#         #커피 200원
#         if coin >= 200:
#             remain = coin - 200
#             print('커피가 곧 제공됩니다.')
#             print('거스름돈은 {}원입니다.'.format(remain))
#         else:
#             print('잔액이 부족합니다.')
#     elif drink == 3:
#         #콜라 300원
#         if coin >= 300:
#             remain = coin - 300
#             print('콜라가 곧 제공됩니다.')
#             print('거스름돈으 {}원입니다.'.format(remain))
#         else:
#             print('잔액이 부족합니다.')
#     else:
#         #없는 번호
#         print('없는 메뉴입니다. 다시 입력해 주세요.')
#     coin = 0
#     break

# sum = 0 
# for i in range(0,11):
#     if i % 2 == 0:
#         sum += i
# print(sum)

# a = 12

# for i in range(1,10):
#     st.write(str(a) + 'X' + str(i) + '=' + str(i*a))

# for a in range(1,10):
#     ''
#     a, '단 입니다.'
#     for i in range(0,10):
#         st.write(str(a) + 'X' + str(i) + '=' + str(i*a))

# integer_1 = 3214
# integer_2 = -128109
# float_1 = -1.986214
# float_2 = 123.e2

# st.write(integer_1, type(integer_1))
# st.write(integer_2, type(integer_2))
# st.write(float_1, type(float_1))
# st.write(float_2, type(float_2))

# st.write(integer_1 / integer_2, type(integer_1 / integer_2))

# string_1 = 'This is String!'
# string_2 = "This is String!"
# string_3 = '''This is String!'''
# string_4 = """This is String!"""

# st.write(string_1)
# st.write(string_2)
# st.write(string_3)
# st.write(string_4)

# string_5 = "This is String! \"따옴표 \" 기호 : !@#$%^"

# st.write(string_5)

# number_1 = 0
# number_2 = 0.0
# string_1 = "Python!" * 3
# st.write(type(number_1))
# st.write(type(number_2))
# st.write(string_1)

# tuple_1 = 1, 2, 3, 4, 5
# tuple_2 = ('가', '나', '다', '라', '마')
# tuple_3 = '파이썬', 10000, False
# tuple_4 = '파이썬', (10000, '만큼', '어려워'), False

# st.write(tuple_1, type(tuple_1))
# st.write(tuple_2, type(tuple_2))
# st.write(tuple_3, type(tuple_3))
# st.write(tuple_4, type(tuple_4))

# tuple_1 = 1, 2, 3, 4, 5
# tuple_1[2] = 100
# st.write(tuple_1)

# tuple_1 = 1, 2, 3, 4, 5
# st.write(len(tuple_1))

# set_1 = {1, 2, 3, '가', '나', '다'}

# set_1.add('추가')
# st.write(set_1)
# set_1.remove('가')
# st.write(set_1)
# set_copy_1 = set_1.copy()
# st.write(set_copy_1)
# set_copy_1.clear()
# st.write(set_copy_1)

# #리스트 생성하기
# list_1 = [1, 2, 3, 4, 5, 1, 3]
# list_2 = []
# st.write(list_1)
# st.write(list_2)
# st.write(len(list_1))

# #리스트 변경하기
# list_1[3] = 9999
# st.write(list_1)
# list_1.append(100)
# st.write(list_1)
# list_1.remove(9999)
# st.write(list_1)
# list_1.insert(0,777)
# st.write(list_1)

# #리스트 복제하기
# list_2 = list_1.copy()
# st.write(list_2)

# #딕셔너리 생성하기
# dict_1 = {'name': '홍길동', 'birth': 1990, 'addr': 'KR'}
# st.write(dict_1)
# st.write(dict_1['birth'])

# #키와 값 추가하기
# dict_1['weight'] = 60.5
# dict_1['family'] = ['아빠', '엄마', '여동생']
# st.write(dict_1)

# #여러 키와 값을 동시에 추가하기
# dict_1.update({'weight':67.8, 'hobby': ['게임', '독서']})

# #딕셔너리 값 변경하기
# dict_1['hobby'] = ['축구', '등산']
# st.write(dict_1)

# #데이터 삭제하기
# del dict_1['weight']
# del dict_1['birth']
# del dict_1['addr']
# st.write(dict_1)

# menu = 0
# food = []

# while menu != 5:
#     print('-'*10)
#     print('''1.보관 식재료 출력
#           2,식재료 추가
#           3.식재료 삭제
#           4.식재료 변경
#           5.종료''')
#     print('-'*10)
# menu = int(input('관리 메뉴를 선택하시오: '))
# if menu == 1:
#     print(food)
# elif menu == 2:
#     name = input('추가할 식재료를 입력하시오')
#     food.append(name)
#     print(food)
# elif menu == 3:
#     eli_name = input('삭제할 식재료를 입력하시오: ')
#     if eli_name in food:
#         food.remove(eli_name)
#     else:
#         print('식재료 재고 없음')
# elif menu == 4:
#     exch_name = input('교환할 식재료를 입력하시오: ')
#     idx = food.index(exch_name)
#     new_name = input('새로운 식재료를 입력하시오: ')
#     food[idx] = new_name
# else:
#     print('식재료 재고 없음')
# elif menu == 5:
# break

# list_1 = [1, 2, 3, 4, 5, 1, 3, 13, 41, 51]
# length = len(list_1)
# st.write(length)

# def sum_list(a):
#     j = 0
#     for i in a:
#         j = j + i
#     st.write(j)

# list_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# sum_list(list_a)

# def sum_list_r(a):
#     j = 0
#     for i in a:
#         j = j + i
#     return j


# list_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# sum = sum_list_r(list_a)
# st.write(sum)
# sum10 = sum * 10
# st.write(sum10)


#소수 판별기

# def check_prime_num(x):
#     for i in range(2, x):
#         if x % i == 0:
#             #x가 i로 나누어 떨어지면 실행하기
#             return False
#     return True
# number = int(input('판별할 자연수를 입력하세요'))
# print(check_prime_num(number))


# 예금 이자 계산기

# def interest_year(p, r, n):
#     return p * (1+r)**n
# p = 3000000
# r = 0.051
# n = 3

# result = interest_year(p, r, n)

# print('원금: {0}, 이자: {1}'.format(p, result-p))

# a = 3
# b = 8
# st.write(a != b)


# word = 'school'
# if word:
#     st.write('high school')
# else :
#     st.write('university')

# data = ['kim', 'lee', 'park']
# for i in data:
#     st.write(i)

# a = 6
# for i in range(1,10):
#     st.write(a*i)

# s = 0
# for i in range(2,10+1):
#     s = s + i
# st.write(s)


# st.write(list_1)


# def sta(arr):
#     sum = 0 #초기값
#     mx = -1e-10
#     mn = 1e10
#     for i in arr:
#         sum = sum + i
#         if mx < i:
#             mx = i
#         if mn > i:
#             mn = i
#     arr
#     'sum = ', sum, 'min = ', mn, 'max = ', mx
#     return sum, mx, min

# list_1 = ([5, 13, 7, 4, 11])
# sta(list_1)
# [sum1, mx1, mn1] = sta(list_1)
# sum1, mx1, mn1

# list_1 = [1, 2, 7, 4, 50]
# s = sum(list_1)
# mx = max(list_1)
# mn = min(list_1)

# st.write(sta(list_1))


# st.write(sum)

# data = ['kim', 'lee', 'park']
# data.remove('lee')
# st.write(data)

#numpy
import numpy as np


# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# st.write(arr[1:4])

# #리스트를 생성하고 배열로 변환하기
# list1 = [1, 2, 3, 4]
# a = np.array(list1)
# st.write('a.shape: ', a.shape)
# st.write('a[0]: ', a[0])

# #2차원 배열 생성하기
# b = np.array([[1, 2, 3], [4, 5, 6]])
# st.write('b.shape', b.shape)
# st.write('b[0,0]: ', b[0,0])
# st.write('b[0]: ', b[0])

# #배열 생성 함수
# a = np.zeros(2)
# st.write('a\n', a)
# b = np.zeros((2,2))
# st.write('b\n', b)
# c = np.ones((2,3))
# st.write('c\n', c)
# d = np.full((2,3), 5)
# st.write('d\n', d)
# e = np.eye(3)
# st.write('e\n', e)

# #넘파이 자료형 변환

# #실수형 배열 생성하기
# a = np.array([1, 2], dtype=np.float64)
# st.write(a.dtype)

# #정수형 배열 생성하기
# a_i8 = a.astype(np.int8)
# st.write(a_i8.dtype)

# list1 = [1, 2, 3, 4]

# a = np.array(list1)
# a + 10

