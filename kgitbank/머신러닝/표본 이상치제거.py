# 전체 데이터중에 표본을 추출한다. 

# 1000 -> 10 표본을 뽑아서 평균 연봉을 구하자 

import numpy as np 

year_pay = np.array([400, 3000, 5000, 6000, 4000, 300000, 7000, 8000, 6000, 2800])

print( np.mean(year_pay) )
print( np.median(year_pay) )
print( np.std(year_pay) )
print( np.max(year_pay) )
print( np.min(year_pay) )

import matplotlib.pyplot as plt 
plt.boxplot(year_pay) #이상치를 시각적으로 확인하기 위한 차트이다. 
plt.show()

#통계학자들이 생각하는 정당한 범위의 값 
# 1/4(25) 2/4(50) 3/4(75)  4/4(100)
#IQR이란  3/4분위수에서 - 1/4분위수를 빼자 
#하한범위는 1/4 분위수에서 - IQR*1.5
#상한범위는 1/4 분위수에서 + IQR*1.5

np.percentile(year_pay, 25)
np.percentile(year_pay, 50) #median 과 동일한다 
np.percentile(year_pay, 75)


def outfliers_iqr(data):
    q1, q3 = np.percentile(data, [25, 75])
    iqr = q3-q1 
    lower_bound = q1 - (iqr*1.5)
    upper_bound = q3 + (iqr*1.5)

    return lower_bound, upper_bound  #tuple형태로 두개를 반환한다 

lower, upper = outfliers_iqr(year_pay)
print( lower )
print( upper )


year_pay[ year_pay > upper] = upper # 상한이 여기다 

plt.boxplot(year_pay) #이상치를 시각적으로 확인하기 위한 차트이다. 
plt.show()
print( np.mean(year_pay) )
print( np.median(year_pay) )
print( np.std(year_pay) )
print( np.max(year_pay) )
print( np.min(year_pay) )
