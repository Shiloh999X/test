# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

weight=input("请输入您的体重(kg)：")
height=input("请输入您的身高(m)：")
BMI=float(weight)/float(height)**2
print("您的BMI指数是：",BMI)
if BMI<18.5:
    print("您的体重过轻！")
elif BMI<25:
    print("您是正常体重")
elif BMI<30:
    print("您的体重略胖！")
else:
    print("您过度肥胖！")