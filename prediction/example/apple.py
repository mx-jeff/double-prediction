import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pylab import rcParams
rcParams['figure.figsize']=20,10
from keras.models import Sequential
from keras.layers import LSTM,Dropout,Dense
from sklearn.preprocessing import MinMaxScaler


def unsanitized_data(df, close, show=False):

    df = df[['Date', close]]
    df = df.replace({'\$':''}, regex=True)

    df = df.astype({close: float})
    df['Date'] = pd.to_datetime(df.Date, format="%m/%d/%Y")
    df.index = df['Date']

    if show:
        plt.plot(df['Close/Last'],label='Close Price history')
        plt.show()

    else:
        return df


def data_prepare(df, close):
    df = df.sort_index(ascending=True,axis=0)
    data = pd.DataFrame(index=range(0,len(df)),columns=['Date',close])
   
    for i in range(0,len(data)):
        data["Date"][i] = df['Date'][i]
        data[close][i] = df[close][i]

    return data, df


def minmax_scaler(data):
    scaler=MinMaxScaler(feature_range=(0,1))
    data.index=data.Date
    data.drop("Date",axis=1,inplace=True)
    final_data = data.values
    train_data=final_data[0:200,:]
    valid_data=final_data[200:,:]
    
    scaler=MinMaxScaler(feature_range=(0,1))
    scaled_data=scaler.fit_transform(final_data)
    x_train_data,y_train_data=[],[]
    for i in range(60,len(train_data)):
        x_train_data.append(scaled_data[i-60:i,0])
        y_train_data.append(scaled_data[i,0])

    return data, x_train_data, valid_data, scaler, y_train_data


def lstm(data, x_train_data, valid_data, scaler):
    lstm_model=Sequential()
    lstm_model.add(LSTM(units=50,return_sequences=True,input_shape=(np.shape(x_train_data)[1],1)))
    lstm_model.add(LSTM(units=50))
    lstm_model.add(Dense(1))
    model_data= data[len(data)-len(valid_data)-60:].values
    model_data= model_data.reshape(-1,1)
    model_data= scaler.transform(model_data)
    return lstm_model, x_train_data, model_data


def train_test_data(lstm_model, x_train_data, y_train_data, model_data):
    lstm_model.compile(loss='mean_squared_error',optimizer='adam')
    lstm_model.fit(x_train_data,y_train_data,epochs=1,batch_size=1,verbose=2)
    X_test=[]
    for i in range(60,model_data.shape[0]):
        X_test.append(model_data[i-60:i,0])
    X_test=np.array(X_test)
    X_test=np.reshape(X_test,(X_test.shape[0],X_test.shape[1],1))

    return lstm_model, X_test


def predict(lstm_model, scaler, X_test):
    predicted_stock_price=lstm_model.predict(X_test)
    predicted_stock_price=scaler.inverse_transform(predicted_stock_price)
    return predicted_stock_price


def apple_prediction():
    # df = pd.read_excel("data/blaze_double.xlsx")
    close = 'Close/Last'
    df = pd.read_csv("data/apple.csv")

    df = unsanitized_data(df, close)
    data, df = data_prepare(df, close)
    data, x_train_data, valid_data, scaler, y_train_data = minmax_scaler(data)
    lstm_model, x_train_data, model_data = lstm(data, x_train_data, valid_data, scaler)

    lstm_model, X_test = train_test_data(lstm_model, x_train_data, y_train_data, model_data)

    predicted_stock_price = predict(lstm_model, scaler, X_test)

    train_data=data[:200]
    valid_data=data[200:]
    valid_data['Predictions']= predicted_stock_price
    plt.plot(train_data["Close"])
    plt.plot(valid_data[['Close',"Predictions"]])
    plt.show()

