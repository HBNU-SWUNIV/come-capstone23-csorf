#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
import talib as ta
import pyupbit as up
import matplotlib.pyplot as plt
import tensorflow as tf
from sklearn.preprocessing import MinMaxScaler, PolynomialFeatures, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from tensorflow.keras.models import load_model


# In[ ]:

# Predict Tomorrow's Close
def predict(df, input_var, model, n):
    X = df[input_var].values
    
    scaler = MinMaxScaler()
    
    X = X = scaler.fit_transform(X)
    
    Y = model.predict(X)
    
    extended_Y = np.tile(Y, (1, n))
    
    price = scaler.inverse_transform(extended_Y)
    
    price_array = []
    for i in range(0, len(price)):
        price_array.append(price[i][0])
    
    print(price_array[-1])
    
    return price_array

# Visualization Real Close & Predict (days means (int)duration, dot meas choose display dot on graph (Y or N))
def visualization(close, pred, days, dot=''):
    plt.figure(figsize=(12, 6))
    
    if dot == 'Y':
        plt.plot(close[-days:], label='Actual', linestyle = '--', marker = 'o', markersize = 7)
        plt.plot(pred[-(days+1):-1], label='Predicted', linestyle = '--', marker = 'o', markersize = 7)
        
    else:
        plt.plot(close[-days:], label='Actual')
        plt.plot(pred[-(days+1):-1], label='Predicted')
        
    plt.title('Prediction')
    plt.legend()
    plt.show()
    
# Predict Tomorrow's Trends    
def pred_UpDown(pred):
    y_pred = pred[-2]
    t_pred = pred[-1]
    
    print("Yesterday Predict : " + str(y_pred) + "    Today's Predict : " + str(t_pred))
    
    if y_pred > t_pred :
        diff = y_pred - t_pred
        avg = (y_pred + t_pred) / 2
        per = diff / avg * 100
        print("=== " + str(round(per, 3)) + " %  Down ===")
    else :
        diff = t_pred - y_pred
        avg = (y_pred + t_pred) / 2
        per = diff / avg * 100
        print("=== " + str(round(per, 3)) + " %  Up ===")
        
# Masking Up or Down (if masking real close, t = 'C')
def mask_UpDown(arr, t = ''):
    mask = []
    
    if t == 'C':
        for i in range(1, (len(arr)-1)):
            if arr[i] > arr[i+1]:
                mask.append('D')
            else:
                mask.append('U')
            
    else:
        for i in range(0, (len(arr)-2)):
            if arr[i] > arr[i+1]:
                mask.append('D')
            else:
                mask.append('U')
            
    return mask

# Checking predict mask with real close
def mask_check(close_mask, pred_mask, days):
    c_mask = close_mask[-days:]
    p_mask = pred_mask[-days:]
    cor = 0
    
    for ci, pi in zip(c_mask, p_mask):
        if ci == pi:
            cor += 1
    per = cor / days * 100
    
    print(str(round(per, 3)) + " %  Correct")
    
# Calculation Earning Rate (Invest strategy is Buy&Hold&Sell)    
def earning_rate(pred_mask, close, days):
    real_price = close[-(days+1):]
    coin = real_price[0]
    prin = coin
    own = 0
    p_mask = pred_mask[-days:]
    
    for i in range(0, len(p_mask)):
        if coin != 0.0:
            if p_mask[i] == 'D':
                own += coin
                coin = 0.0
                
            else:
                coin = real_price[i+1]
                
        elif coin == 0.0:
            if p_mask[i] == 'U':
                coin = real_price[i+1]
                own -= real_price[i]
                
        e_r = (coin + own - real_price[0]) / prin * 100
                
    return print(str(round(e_r, 3)) + " %")
    
    
# Bring bitcoin data from upbit api and preprocessing data before use    
def df_proc():
    df = up.get_ohlcv(ticker="KRW-BTC", interval="day", count=500)
    df.to_csv('bitcoin_data_predict.csv')
    
    df = pd.read_csv('bitcoin_data_predict.csv')
    df.drop([499], axis=0, inplace=True)
    
    df_data = pd.DataFrame()
    df_data['Close'] = df['close']

    # 이동평균
    df_data['MA5'] = ta.SMA(df['close'], timeperiod=5)
    df_data['MA20'] = ta.SMA(df['close'], timeperiod=20)

    # RSI
    df_data['RSI'] = ta.RSI(df['close'], timeperiod=14)

    # MACD
    df_data['MACD'], df_data['Signal'], df_data['Hist'] = ta.MACD(df['close'], fastperiod=12, 
                                                              slowperiod=26, signalperiod=9)

    # 볼린저 밴드
    df_data['Upper'], df_data['Middle'], df_data['Lower'] = ta.BBANDS(df['close'], timeperiod=20, 
                                                                   nbdevup=2, nbdevdn=2)

    # 스토캐스틱 #
    df_data['SlowK'], df_data['SlowD'] = ta.STOCH(df['high'], df['low'], df['close'], 
                                                  fastk_period=5, slowk_period=3, slowd_period=3)

    # OBV
    df_data['OBV'] = ta.OBV(df['close'], df['volume'])

    # ADX
    df_data['ADX'] = ta.ADX(df['high'], df['low'], df['close'])

    # ATR
    df_data['ATR'] = ta.ATR(df['high'], df['low'], df['close'])

    # MFI
    df_data['MFI'] = ta.MFI(df['high'], df['low'], df['close'], df['volume'], timeperiod=14)

    # ROC
    df_data['ROC'] = ta.ROC(df['close'], timeperiod=10)

    # CCI
    df_data['CCI'] = ta.CCI(df['high'], df['low'], df['close'], timeperiod=20)

    # DMI
    df_data['DMI+'] = ta.PLUS_DI(df['high'], df['low'], df['close'], timeperiod=14)
    df_data['DMI-'] = ta.MINUS_DI(df['high'], df['low'], df['close'], timeperiod=14)

    df_data.dropna(inplace=True)

    df_data.reset_index(drop=True, inplace=True)
    
    return df_data
       