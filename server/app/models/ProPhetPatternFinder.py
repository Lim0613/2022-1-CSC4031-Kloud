import numpy as np
import pandas as pd
import json
from fbprophet import Prophet
import matplotlib.pyplot as plt
class ProPhetPatternFinder:
    def __init__(self,data):
        self.data = data
        self.cost = []
        for d in data["ResultsByTime"]:
            c = 0
            for d2 in d["Groups"]:
                c += float(d2['Metrics']['UnblendedCost']["Amount"])
            self.cost.append([d["TimePeriod"]["Start"],c])
        self.df = pd.DataFrame(self.cost)
        self.data_df = self.df.rename(columns = {0:"ds",1:"y"})
    
    def show_plot(self):
        self.data_df.plot(x="ds", y="y",figsize=(16,8))
        
    # defalut로 이후 10일 예측
    def model_fit(self,periods=10):
        try:
            self.model = Prophet()
            self.model.fit(self.data_df)
            # 앞으로 365일 뒤를 예측하겠다. 
            future = self.model.make_future_dataframe(periods=periods)
            # 예측 데이터가 df형태로 들어옴
            self.forecast = self.model.predict(future)
            return self.forecast
        except:
            return print("Fitting 실패")
    
    def show_expect_plot(self):
#         fig1 = model.plot(self.forecast.iloc[150:])
        fig2 = self.model.plot(self.forecast)
    
    def expose_data(self):
        return self.forecast

    # 예측에 영향을 준 요소를 출력
    # 어떤 근거를 가지고 예측을 했는지 
    # 트랜드를 분석해보니 ~~경향을 가지더라
    # yearly하게 연간 가격 변동 그래프를 보면 이런 패턴이 있더라~~
    def component_plot(self):
        fig3 = fig3 = self.model.plot_components(self.forecast)


with open('data.json', 'r') as f:
    data = json.load(f)
f.close()
p = ProPhetPatternFinder(data)
p.show_plot()
p.model_fit(periods=10)
p.show_expect_plot()
p.component_plot()


