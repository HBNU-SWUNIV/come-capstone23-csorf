# 한밭대학교 컴퓨터공학과 재벌집코인아들(Coin Son Of Rich Family)팀

**팀 구성**
- 20181590 김희섭 
- 20181581 강현욱

## <u>Teamate</u> Project Background
- ### 배경
  - 비트코인(Bitcoin)은 블록체인 기술 기반으로 만들어진 온라인 암호화폐이다. 2008년 10월 '사토시 나카모토'라는 가명을 쓰는 프로그래머가 개발하여 2009년 1월 소스를 배포했다. 중앙은행이 없이 세계적 범위에서 P2P 방식으로 개인 간 자유롭게 송급 등 거래가 가능하다. 또한 중앙은행을 거치지 않기에 수수료 부담이 적다. 안전하고 모든 거래 내역이 투명하며 총 2100만 개로 한정되어 있는 희소성 있는 화폐로 결제 및 투자 자산등으로 사용되고 있다.
- ### 문제점
  - 비트코인의 장점만큼이나 여러 단점들이 있지만, 그 중 가장 크게 꼽히는 문제는 바로 가격 변동성이다. 이는 비슷한 투자 수단인 주식과 비교하였을 때 일 최대 등락 30% 로 제한되는 주식과는 다르게 비트코인은 상 하한가의 제한이 없기에 리스크가 더 높다. 또한 장이 평일에 정해진 시간 동안 열려있는 주식과는 다르게 1년 24시 계속 열려있는 비트코인은 새벽에도 긴장을 풀 수 없다. 이 외에도 다른 여러 외부 요인에 의해서 쉽게 가격이 변동된다.
  - 이렇게 불안정한 투자를 그나마 안정적으로 하기 위해 여러 보조지표들을 참고하지만, 각 지표들간 연관성을 찾기 어려우며 여러 지표들을 한 눈에 보기 어려워 실질적인 투자에서 십분 활용하기에 어려움이 있다. 또한, 과연 높은 변동성을 띄는 지표들이 실질적으로 투자 시 도움이 되는지도 확실치 않다.
- ### 필요성
  - 여러 지표들을 기반으로 가격의 추세를 예측하여 여러 지표들을 한 번에 참고하여 매수, 매도에 어려움을 겪는 투자자들의 스트레스를 조금이나마 줄일 수 있을 것이다.
- ### 목표
  - 종가를 사용한 예측 모델의 경우 손실값을 낮추려는 컴퓨터의 동작으로 인해 예측값이 전날 종가를 따라가려는 문제가 있으며, 앞서서 보조지표들이 실 투자에 있어 실질적으로 도움이 되는지를 알아보기 위해 학습 및 예측 시 입력 데이터는 종가를 제외한 지표들로만 구성할 것이다.
  - 예측 목표는 다음날의 추세를 예측하는 것으로 예측이 어렵고 그 값의 정확도가 떨어질 수 있는 종가를 최종적으로 예측하는 것이 아닌 상승, 하락을 예측하는 방향으로 진행할 것이다.    
  
## System Design
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white"><img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=NumPy&logoColor=white"><img src="https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white"><img src="https://img.shields.io/badge/scikitlearn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white"><img src="https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=TensorFlow&logoColor=white"><img src="https://img.shields.io/badge/Bitcoin-F7931A?style=for-the-badge&logo=Bitcoin&logoColor=white">

![image](https://github.com/HBNU-SWUNIV/come-capstone23-csorf/assets/147990515/7fc3e8c9-04d3-47da-959e-3ebe2231c620)
  - ### System Requirements
    - 정확도(일별 상승/하락 추세)
    - 수익률(최소 손실)
    
## Progress
  - ### 1. 데이터 전처리
    - 학습에 필요한 비트코인 가격 데이터를 Upbit API로부터 불러와 저장
      
      ![image](https://github.com/HBNU-SWUNIV/come-capstone23-csorf/assets/147990515/56002c8d-725e-4b0c-a879-9fe9ac919564)
    - 지표데이터를 사용하기 위해 ta.lib과 불러온 가격 데이터를 통해 지표값 산출
      
      ![image](https://github.com/HBNU-SWUNIV/come-capstone23-csorf/assets/147990515/2c1604eb-20d1-4d15-a81c-610a6bfa66a3)
    - 특정 지표(MA, MACD 등) 같은 경우 일정 기간값이 필요하므로 NaN값으로 산출된 부분 처리, 시계열 데이터이므로 순서대로 다시 인덱싱
      
      ![image](https://github.com/HBNU-SWUNIV/come-capstone23-csorf/assets/147990515/18d116d4-d87e-40ce-b1bb-38d06c4e6f14)
   
  - ### 2. 데이터 분석
    #### 1)  지표 선정 및 특징 분석
    - 비트코인 투자에 많이이 사용되는 지표 별 특징을 파악, 각 지표가 의미하는 바를 정리
      - 추세 : 이동평균(MA5, MA20), RSI, MACD(MACD, Signal, Hist), ADX, ROC, CCI, DMI(+/-)
      - 탄력성 : 볼린저 밴드(Upper, Middle, Lower), 스토캐스틱(SlowK, SlowD), ATR
      - 거래량 : OBV
      - 시장 : MFI
    #### 2)  시각화
    - 종가 및 지표를 시각화하여 종가의 흐름에 따라 각 지표별로 어떻게 흘러가는지 파악
      
      ![image](https://github.com/HBNU-SWUNIV/come-capstone23-csorf/assets/147990515/ca5062b4-fb5e-4359-8df7-b0116e82ad85)
      ![image](https://github.com/HBNU-SWUNIV/come-capstone23-csorf/assets/147990515/d7a44e32-9da0-44c7-96aa-e2369a89b161)
      ![image](https://github.com/HBNU-SWUNIV/come-capstone23-csorf/assets/147990515/479a387a-ec16-400d-9b2d-c9a2bf730e4e)
    #### 3)  상관분석(회귀직선)
    - 종가와 각 지표의 상관분석을 통해 관계성을 파악, 산출된 값으로 회귀직선을 시각화하여 관계성을 파악
      
      ![image](https://github.com/HBNU-SWUNIV/come-capstone23-csorf/assets/147990515/457a3a0c-4f63-4606-8c81-45529adef2a0)
      ![image](https://github.com/HBNU-SWUNIV/come-capstone23-csorf/assets/147990515/9e43e5e2-f4f7-465a-b849-0633f4ffef31)
      ![image](https://github.com/HBNU-SWUNIV/come-capstone23-csorf/assets/147990515/a4338487-866a-4652-9725-e5ce4d956ded)
      ![image](https://github.com/HBNU-SWUNIV/come-capstone23-csorf/assets/147990515/1a2baec0-dcdc-408b-8a66-51037d40fb70)
    #### 4)  회귀분석
    - 종가와 지표의 관계성을 수학적으로 추정, 각 지표들이 종가에 대해 어떤 경향성을 띄는지 파악
      
      ![image](https://github.com/HBNU-SWUNIV/come-capstone23-csorf/assets/147990515/8e7a98bb-c5b1-42ea-9ab4-b206e8065689)
      ![image](https://github.com/HBNU-SWUNIV/come-capstone23-csorf/assets/147990515/f76dec1e-58bd-406a-80bf-326e5858d582)
      ![image](https://github.com/HBNU-SWUNIV/come-capstone23-csorf/assets/147990515/0211ba34-ee99-42c3-b307-b9371791a906)
    #### 5)  다중선형회귀모델
    - 직접 다중선형 모델로 예측을 하여 지표들이 종가를 예측할 수 있는지 가능성을 파악 (Linear, Lasso, Ridge)
      
      ![image](https://github.com/HBNU-SWUNIV/come-capstone23-csorf/assets/147990515/594eb53a-288e-48b7-a138-c2bac7737400)

  - ### 3. 모델링
    - 시계열 데이터 예측에 많이 사용되는 LSTM/GRU로 진행, 두 모델의 성능을 비교
    - 비교적 적은 데이터에도 좋은 성능을 보이는 GRU로 선정
    - 주어진 데이터량과 목표에 맞는 모델을 위해 모델링(target은 종가, 예측된 종가로 일별 상승/하락을 산출, 데이터량이 적고 예측하려는 값의 변동성이 크므로 과적합을 피하기 위해 dropout layer를 각 layer마다 추가)
    - 모델링이 완료되면 앞선 데이터 분석의 결과에 따라 여러 지표들의 조합으로 학습, 가장 높은 성능의 모델을 추려 모델 저장, 성능은 MSE 및 RSE, 그리고 y_test 와 y_predict 시각화 결과에 따른 상위 9개 모델 저장
      
      ![image](https://github.com/HBNU-SWUNIV/come-capstone23-csorf/assets/147990515/aab3cfeb-c552-43d3-8a6a-88c8362c251c)
      ![image](https://github.com/HBNU-SWUNIV/come-capstone23-csorf/assets/147990515/3150bc34-0ab0-4108-b593-8ad9d63313c0)
      ![image](https://github.com/HBNU-SWUNIV/come-capstone23-csorf/assets/147990515/bffb8e2a-aebd-4ef9-9641-2d177102b6e8)
   
  - ### 4. 모델 검증
    #### 1)  추세
    - 검증하려는 것은 예측값으로 나온 y(다음 날의 예측 종가값)에 대해 다음날의 종가의 상승/하락을 예측
    - 이 경우 비교하려는 값이 예측값인 y와 실제 전날 종가값일 경우 모델 자체의 예측값이 실제 종가값의 큰 변동폭을 못 따라 갈 경우 실제 종가값보다 y가 지속적으로 낮게 비교되어 전날 예측값보단 상승했지만 매일 하락이라고 예측하는 문제가 있음.
    - 전날의 예측값보다 상승/하락 과 그에 따른 % 를 예측함.
      
      ![image](https://github.com/HBNU-SWUNIV/come-capstone23-csorf/assets/147990515/92bd84e5-3dc5-461b-abf1-f30be969a3f0)
    #### 2)  시각화
    - 모델의 결과로 나온 예측값 y와 실제 종가값 간의 값의 차이 및 추세를 따라갔는지에 대해 파악하기 위해 특정 일 수(ex) 100일) 기준으로 시각화를 진행. 여기서 살펴볼 것은 예측값이 전날의 종가값을 따라가려는 성질이 있는지, 두 값간의 차이, 추세성의 정확도이다.
      
      ![image](https://github.com/HBNU-SWUNIV/come-capstone23-csorf/assets/147990515/2242596c-da63-4f2a-b234-0a99951acccf)
    #### 3)  정확도
    - 종가 및 예측값의 일별 추세(상승/하락)을 masking하여 두 masking 결과를 비교해 정확도를 검증함.
      
      ![image](https://github.com/HBNU-SWUNIV/come-capstone23-csorf/assets/147990515/1ac1ca2d-b6db-4c28-9d82-e6c3f4693331)
    #### 4)  수익률
    - 실 투자에 있어 예측 모델의 가능성을 파악.
    - 투자 전략에 따라 값이 달라질 수 있지만 결과를 좀 더 rough하게 얻어내기 위해 단순한 Buy & Hold & Sell 방식 선택.
    - 시작은 코인을 소지한채로 시작. 예측이 상승일 경우 코인을 소지하고 있다면 Hold, 가지고 있지 않다면 다시 Buy. 예측이 하락일 경우 코인을 소지하고 있다면 Sell, 가지고 있지 않다면 Hold를 하는 방식으로 진행.
      
      ![image](https://github.com/HBNU-SWUNIV/come-capstone23-csorf/assets/147990515/882a5bc5-30af-4112-9af7-aae0d6d48c3e)
      ![image](https://github.com/HBNU-SWUNIV/come-capstone23-csorf/assets/147990515/1e385465-0b8b-4293-a51e-7883fd63d3dd)
    - 수익률 검증은 급상승/급하락이 있었던 최근 100일(8월 ~ 10월) 기준 및 급하락만 있었던 20일(8/8 ~ 8/28) 기준으로 진행.
   
      ![image](https://github.com/HBNU-SWUNIV/come-capstone23-csorf/assets/147990515/15ce882c-b9f3-4c3c-8509-5573de7cba20)
      ![image](https://github.com/HBNU-SWUNIV/come-capstone23-csorf/assets/147990515/0e2ad82f-d4a0-4969-b2e0-7ba19a31d62f)
    - 각 케이스 별 급변하는 시장에서의 수익성과 하락만 있던 시기에서 어느 정도의 손실을 방어할 수 있는지를 검증하는 것이 목표.
  
  
## Conclusion
  - ### 1.  추세
    
    ![image](https://github.com/HBNU-SWUNIV/come-capstone23-csorf/assets/147990515/b1aeeba2-062a-4b43-9238-2855949a36ed)
  - ### 2.  시각화
    
    ![image](https://github.com/HBNU-SWUNIV/come-capstone23-csorf/assets/147990515/753912d2-bd7e-4d10-9004-676685c963a2)
  - ### 3.  정확도
    - 최대 약 55 % (모든 지표들(ALL)), 최소 약 45 %(추세 및 시장이며 양의 상관관계를 가지는 지표들(T&M+))
    
    ![image](https://github.com/HBNU-SWUNIV/come-capstone23-csorf/assets/147990515/d0537b9f-aac2-427b-bc15-7d611c8b2906)
  - ### 4.  수익률
    - 8월 부터 10월 까지 100일 기준으로는 최대 약 22.68 %(산출 시 종가만을 사용하는 지표들(OC)), 최소 4.418 %(추세 및 시장이며 양의 상관관계를 가지는 지표들(T&M+)) 이윤
    - 해당 기간 종가의 상승 폭은 약 15 %
   
    ![image](https://github.com/HBNU-SWUNIV/come-capstone23-csorf/assets/147990515/9819ea90-5017-47fe-8593-a7053fba3024)
    - 급 하락기간 20일(8/8 ~ 8/28) 기준으로는 최소 - 0.018 %(추세 및 시장 지표들(T&M)), 최대 - 7.201 % 손실(탄력성 지표들(E))
    - 해당 기간 종가의 하락 폭은 약 11 %
    
    ![image](https://github.com/HBNU-SWUNIV/come-capstone23-csorf/assets/147990515/bf65f720-fdc5-48f7-a4d9-71960e61b113)
  - ### 5.  최종결론
    - 학습 데이터 준비에 있어 upbit에서 API를 받아올 경우 2019년 9월 25일부터 받아올 수 있어 비교적 데이터량이 적다. 따라서 다음에 같은 비트코인 관련해 학습을 준비할 때는 2013년부터 데이터를 받아올 수 있는 빗썸, 또는 해외 거래소에서 가져오는 것을 고려해볼 수 있다.
      
    - 각 지표별 해석방식을 학습시킬 수 있어 보인다. 예를 들어 RSI와 같은 지표는 모든 값이 의미있는 것이 아닌 특정 값 이상/이하(30, 70)에서 의미가 있는 지표이다. 지표값을 그대로 산출해 쓰는 것이 아닌 산출 후 어느 정도 해석적 수치로 조정하여 학습데이터에 사용하는 것을 고려해 볼 수 있다.
      
    - 시계열 데이터의 회귀 문제이기에 GRU를 사용하였는데, 추세를 예측한다고 하면 target 값을 상승(1), 하락(0)으로 간단하게 둘 수 있고 이에 따라 회귀가 아닌 분류 방식으로 모델을 구성하는 방식도 고려해 볼 수 있다고 보여진다.
      
    - 비트코인의 가격은 단순 추세, 탄력성, 거래량, 시장 등의 수치적인 요소 외에 인터넷에서 떠도는 여러 기사들, 가십 등과 투자자 참여자들의 심리적 요인까지 작용하여 변동이 이루어지고 그 변동의 폭이 크다. 예를 들어 지난 10월 16일 '블랙록의 비트코인 현물 ETF 승인'이라는 기사가 뜨고 30분만에 약 7 % 급증, 그러나 가짜뉴스라고 밝혀지자 원래가격으로 서서히 복귀했다. 이처럼 기사 중에서도 진위여부에 상관없이 가격의 변동이 크게 일어난다. 따라서 지표들뿐 아니라 웹크롤링을 통해 비트코인에 영향을 줄 수 있는 키워드들과 그래프에 따라 투자자들의 심리적 선택(매수/매도)을 데이터화하여 학습시킨다면 모델의 성능을 높일 수 있을 것 같다.
   
    - 수익률 산출에 있어 앞선 해석방식을 학습시키고 투자 방식도 이에 따라 구체화 한다면 좀 더 좋은 수익률을 올릴 수 있을 것 같다.
  
## Project Outcome
- ### 20XX 년 OO학술대회 
