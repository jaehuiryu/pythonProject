import pandas as pd
import matplotlib.pyplot as plt

# 데이터 불러오기
cbase = pd.read_csv('/Users/apple/Downloads/20220808_CBASE.csv', index_col= 1, engine='python')
upbit = pd.read_csv('/Users/apple/Downloads/20220808_UPBIT.csv', index_col= 1, engine='python')

# 인덱스를 pandas의 datetime 형태로 바꿔주기
cbase.index = pd.to_timedelta(cbase.index)
upbit.index = pd.to_timedelta(upbit.index)

# 차트 그리기
fig = plt.figure(figsize=(20, 12)) # 차트 생성 및 사이즈 설정
ax = fig.add_subplot(1,1,1) # subplot 생성

ax.plot(cbase['spot_price'], label='cbase', color='b') # coinbase 금액 불러오기
ax.plot(upbit['spot_price'].iloc[1689:], label='upbit', color='r') # upbit 금액 불러오기

ax.set_title('CBASE & UPBIT price', fontsize=20) # 타이틀 설정
ax.set_ylabel('price', fontsize=14) # x축 설정
ax.set_xlabel('Time', fontsize=14) # y축 설정

ax.legend(fontsize=12, loc='best') # 범례 설정 best로 해놓으면 가장 적절한 위치에 알아서 범례가 놓이게 됩니디

plt.show()
