#encoding=utf-8    
#������������ȡÿһ�е�����  
import linecache    
import random  

#oversampling
for i in range(0,6000,1):#forѭ������  
    a = random.randrange(1, 1128) #1-9�����������  
    #print a  
    #���ļ�poem.txt�жԶ�ȡ��a�е�����  
    theline = linecache.getline(r'trainF', a)  
    print theline

'''
#undersampling
for i in range(0,10000,1):#forѭ������ 
	a = random.randrange(1, 17550) #1-9�����������     
	theline = linecache.getline(r'trainN', a)  
	print theline
'''