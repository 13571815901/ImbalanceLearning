# -*- encoding:utf-8 -*-  
#xgboost��װ�̳� �ο� http://blog.csdn.net/lht_okk/article/details/54311333  
#xgboostԭ��ο� http://www.cnblogs.com/mfryf/p/6238185.html  
#http://blog.csdn.net/bryan__/article/details/52056112  
#xgboost ���ξ��� http://blog.csdn.net/u010414589/article/details/51153310  
  
import xgboost as xgb  
import numpy as np  
  
#1,xgBoost�Ļ���ʹ��  
#2,�Զ�����ʧ�������ݶȺͶ��׵�  
#3,binary:logistic/logitraw  
  
# ����f��theta*x  
  
#xgboost��װ�̳� �ο� http://blog.csdn.net/lht_okk/article/details/54311333  
  
def log_reg(y_hat, y):  
    p = 1.0 / (1.0 + np.exp(-y_hat))  
    g = p - y.get_label()  
    h = p * (1.0-p)  
    return g, h  
  
  
def error_rate(y_hat, y):  
    return 'error', float(sum(y.get_label() != (y_hat > 0.5))) / len(y_hat)  
  
if __name__=="__main__":  
    #��ȡ����  
    data_train=xgb.DMatrix('train');  
    data_test=xgb.DMatrix('test_class.txt')  
  
    #print 'data_train'  
    #print data_train  
    #print 'type(data_train)'  
    #print type(data_train)  
  
    #���ò���  
    #max_depth:����������,ȱʡֵΪ6ͨ��ȡֵ3-10  
  
    #eta:Ϊ�˷�ֹ�����,���¹������õ�����������,��ÿ����������֮��,�㷨��ֱ�ӻ����������Ȩ��  
    #etaͨ������������Ȩ��ʹ������������̸��ӱ���,Ĭ��ֵ0.3  ȡֵ��Χ[0,1] ͨ������Ϊ[0.01-0.2]  
  
    #silent:ȡ0ʱ��ʾ��ӡ������ʱ��Ϣ��ȡ1ʱ��ʾ�Լ�Ĭ��ʽ���У�����ӡ����ʱ��Ϣ��ȱʡֵΪ0  
    #����ȡ0�������е�����������������ģ���Լ����Ρ�����ʵ������������Ϊ1Ҳͨ���޷���Ĭ����  
  
    #objective:ȱʡֵ reg:linear ����ѧϰ������Ӧ��ѧϰĿ�꣬��ѡĿ�꺯�����£�  
    # ��reg:linear�� �C���Իع顣  
    #��reg:logistic�� �C�߼��ع顣  
    #��binary:logistic�� �C��������߼��ع����⣬���Ϊ���ʡ�  
    #��binary:logitraw�� �C��������߼��ع����⣬����Ľ��ΪwTx��  
    #��count:poisson�� �C���������poisson�ع飬������Ϊpoisson�ֲ�,��poisson�ع��У�max_delta_step��ȱʡֵΪ0  
    #��multi:softmax�� �C��XGBoost����softmaxĿ�꺯�������������⣬ͬ?????ò??num_class����������  
    #��multi:softprob�� �C��softmaxһ���������������ndata * nclass�����������Խ�������reshape��ndata��nclass�еľ���û�����ݱ�ʾ����������ÿ�����ĸ��ʡ�  
    #��rank:pairwise�� �Cset XGBoost to do ranking task by minimizing the pairwise loss  

    for i in range(2,3,1):
    	for ii in range(3,4,1):
    		ii=float(ii)/100
    		for iii in range(10,11,1):
    			iii=float(iii)/10
    			for iiii in range(1,2,1):
    				for iiiii in range(70,80,10):
    					param={'silent':0,'max_depth':i,'eta':0.03,'scale_pos_weight':1,'min_child_weight':0.5,'subsample':1,'booster':'gbtree','colsample_bytree':1,'objective':'binary:logistic'}  
					#param={'max_depth':2,'subsample':1,'booster':'gbtree','colsample_bytree':1,'objective':'binary:logistic'}  


	#param={'max_depth':6,'eta':0.01,'gamma':0.1,'min_child_weight': 0.01,'silent':1,'objective':'binary:logistic'}  
    					watchlist=[(data_test,'eval'),(data_train,'train')]  
    					n_round=100
    #xgboost ����������Ĭ�ϲ���  
    #����ԭ��:xgboost.train(params,dtrain,num_boost_round=10,evals=(),obj=None,feval=None,maximize=False,early_stopping_rounds=None,evals_result=None,verbose_eval=True,learning_rates=None,xgb_model=None)  
    # params  
    # ����һ���ֵ䣬���������ѵ���еĲ����ؼ��ֺͶ�Ӧ��ֵ����ʽ��params = {��booster��:��gbtree��, ��eta��:0.1}  
    # dtrain  
    # ѵ��������  
    # num_boost_round  
    # ����ָ���������ĸ���  
    # evals  
    # ����һ���б����ڶ�ѵ�������н��������б��е�Ԫ�ء���ʽ��evals = [(dtrain,��train��), (dval,��val��)]������evals = [  
    #     (dtrain,��train��)], ���ڵ�һ���������ʹ�����ǿ�����ѵ�������й۲���֤����Ч����  
    # obj, �Զ���Ŀ�ĺ���  
    # feval, �Զ�����������  
    # maximize, �Ƿ�����������������  
    # early_stopping_rounds, ����ֹͣ���� ������Ϊ100����֤������������һ���̶���100���ڲ����ټ������ͣ���ֹͣ��������Ҫ��evals  
    # ��������  
    # һ��Ԫ�أ�����ж���������һ��ȥִ�С����ص������ĵ���������������õģ������early_stopping_rounds  
    # ���ڣ�??ģ?ͻ??��?����ԣ�bst.best_score, bst.best_iteration, ��bst.best_ntree_limit  
    # evals_result  
    # �ֵ䣬�洢��watchlist  
    # �е�Ԫ�ص����������  
    # verbose_eval(�������벼���ͻ���ֵ��)��ҲҪ��evals  
    # ��������  
    # һ��Ԫ�ء����ΪTrue, ���evals��Ԫ�ص��������������ڽ���У�����������֣�����Ϊ5����ÿ��5���������һ�Ρ�  
    # learning_rates  
    # ?�һ�??����ѧϰ�ʵ��б�? 
    # xgb_model, ��ѵ��֮ǰ���ڼ��ص�xgb  
    # model��  
    					bst=xgb.train(param,data_train,num_boost_round=n_round,evals=watchlist,obj=log_reg,feval=error_rate)  
  					print param
  					print n_round
    #���������  
					y_hat=bst.predict(data_test)
					y=data_test.get_label()  
    #print 'y_hat'   
    #print 'y'  
    #print y  

					for t in range(0,11,1):
						m=float(t)/10
						print m
						sum1=0
						sum0=0
						error=sum(y!=(y_hat>m))   
						error_rate=float(error)/len(y_hat) 


						print 'sample_sum  =\t',len(y_hat)  
						print 'error_num1  =\t%4d'%error
						print 'error_rate  =\t%.5f%%'%(100*error_rate)

#������Ԥ��Ϊ����������û��ʶ��ĸ��ʡ�
						for i in range(0,y_hat.size):
							if y[i]==1:
								if y_hat[i]<m:
									sum1=sum1+1
						print 'sum1_error:'+str(sum1)
						print 'sum1:'+str(sum(y==1))
						error_sum1=1-(float(sum1)/sum(y==1))
						print 'zhengque:'+str(error_sum1)

#������Ԥ��Ϊ���ϣ������ʶ����ϵĸ��ʡ�
						for i in range(0,y_hat.size):
							if y[i]==0:
								if y_hat[i]>=m:
									sum0=sum0+1
						print 'sum0_error:'+str(sum0)
						print 'sum0:'+str(sum(y==0))
						error_sum0=1-(float(sum0)/sum(y==0))	
						print 'zhengque:'+str(error_sum0)
						print '-----------------------------------'








'''
					list_time=[]
					list_p=[]
					list_starttime=[]
					list_endtime=[]
					list_faulttime=[]
					list_truetime=[]

    					for t in range(2,9,1):
						m=float(t)/10
						#m=0.5	
						print m					
						print 'all fault timestamp:'	
    						for i in range(0,y_hat.size):
							if y_hat[i]>m:
								xuhao=i*20+1
								list_time.append(xuhao)
								list_p.append(y_hat[i])	
			#print y_hat[i]
	#print list_time
	#print '--------------------------------'
						w=0
						list_starttime.append(list_time[0])
						while w<len(list_time)-1:
							chazhi=list_time[w+1]-list_time[w]
							if chazhi>106:
								list_endtime.append(list_time[w])
								list_starttime.append(list_time[w+1])
							w=w+1
						list_endtime.append(list_time[len(list_time)-1])

						for nn in range(0,len(list_starttime)):
							list_endtime[nn]=list_endtime[nn]+106
						for x in range(0,len(list_starttime)):
							print list_starttime[x]+89999,
							print list_endtime[x]+89999,
							print list_endtime[x]-list_starttime[x]
						print '----------------------'

'''

						





'''

k=10
while k<100:
	m=float(k)/100
	k=k+10
	print m
	sum1=0
	sum0=0
	error=sum(y!=(y_hat>m))   
	error_rate=float(error)/len(y_hat) 


	print 'sample_sum  =\t',len(y_hat)  
	print 'error_num1  =\t%4d'%error
	print 'error_rate  =\t%.5f%%'%(100*error_rate)

	#������Ԥ��Ϊ����������û��ʶ��ĸ��ʡ�
	for i in range(0,y_hat.size):
		if y[i]==1:
			if y_hat[i]<m:
				sum1=sum1+1
	print 'sum1_error:'+str(sum1)
	print 'sum1:'+str(sum(y==1))
	error_sum1=float(sum1)/sum(y==1)
	print 'error:'+str(error_sum1)

	#������Ԥ��Ϊ���ϣ������ʶ����ϵĸ��ʡ�
	for i in range(0,y_hat.size):
		if y[i]==0:
			if y_hat[i]>=m:
				sum0=sum0+1
	print 'sum0_error:'+str(sum0)
	print 'sum0:'+str(sum(y==0))
	error_sum0=float(sum0)/sum(y==0)
	print 'error:'+str(error_sum0)


	sum2=sum(y==2)
	#print sum2

	S=(1-0.5*error_sum0-0.5*error_sum1)*100
	print S
	print '---------------------------------------------------'

'''
















'''
m=0.5
sum1=0
sum0=0
error=sum(y!=(y_hat>m))   
error_rate=float(error)/len(y_hat) 


print 'sample_sum  =\t',len(y_hat)  
print 'error_num1  =\t%4d'%error
print 'error_rate  =\t%.5f%%'%(100*error_rate)

#������Ԥ��Ϊ����������û��ʶ��ĸ��ʡ�
for i in range(0,y_hat.size):
	if y[i]==1:
		if y_hat[i]<m:
			sum1=sum1+1
print 'sum1_error:'+str(sum1)
print 'sum1:'+str(sum(y==1))
error_sum1=1-(float(sum1)/sum(y==1))
print 'zhengque:'+str(error_sum1)

#������Ԥ��Ϊ���ϣ������ʶ����ϵĸ��ʡ�
for i in range(0,y_hat.size):
	if y[i]==0:
		if y_hat[i]>=m:
			sum0=sum0+1
print 'sum0_error:'+str(sum0)
print 'sum0:'+str(sum(y==0))
error_sum0=1-(float(sum0)/sum(y==0))
print 'zhengque:'+str(error_sum0)


#sum2=sum(y==2)
#print sum2

#S=(1-0.5*error_sum0-0.5*error_sum1)*100
#print S
'''


for i in range(0,y_hat.size):
	print y_hat[i]



'''
for i in range(0,y_hat.size):
	if y_hat[i]>0.4:
		print '1'
	if y_hat[i]<=0.4:
		print '0'

print 'haha'
for i in range(0,y.size):
	print y[i]
'''