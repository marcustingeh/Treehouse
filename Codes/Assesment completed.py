import pandas as pd
import requests
import json
from datetime import datetime
import time
import math 
import datetime
import re
from IPython.display import display
import matplotlib.pyplot as plt
import numpy as np


baseUrl = 'https://api.llama.fi'

alltvl = requests.get(baseUrl + '/v2/chains')

print(alltvl.json()[0].keys())

#turn into dataframe
alltvldata = pd.DataFrame.from_dict(alltvl.json())

#see types
alltvldata.dtypes

#show top 10 TVL
alltvldatasorted = alltvldata.sort_values('tvl',ascending=False)[0:10]
print(alltvldatasorted)
alltvldatasortedclean = alltvldatasorted[['gecko_id','tvl']]
print(alltvldatasortedclean)

ax = alltvldatasortedclean.plot.bar(x='gecko_id', y='tvl', rot=50)

#Question 2
#firstjan = "01/01/2023"
#lastjan = "30/01/2023"
#timestampfirstjan = time.mktime(datetime.datetime.strptime(firstjan,"%d/%m/%Y").timetuple())
#timestamplastjan = time.mktime(datetime.datetime.strptime(lastjan,"%d/%m/%Y").timetuple())

#print(timestampfirstjan)



#Eth TVL
EthereumTVL = requests.get(baseUrl + '/v2/historicalChainTvl/' + 'Ethereum')
EthereumTVLData = pd.DataFrame.from_dict(EthereumTVL.json())
EthereumTVLData['date'] = pd.to_datetime(EthereumTVLData['date'], unit='s')
EthereumTVLDataJan = EthereumTVLData.drop(EthereumTVLData.index[0:1647])
EthereumTVLDataJan2 = EthereumTVLDataJan.drop(EthereumTVLDataJan.index[31:])
EthereumTVLgraph = EthereumTVLDataJan2.plot.line(x='date',y='tvl')

#Tron TVL
TronTVL = requests.get(baseUrl + '/v2/historicalChainTvl/' + 'Tron')
TronTVLData = pd.DataFrame.from_dict(TronTVL.json())
TronTVLData['date'] = pd.to_datetime(TronTVLData['date'], unit='s')
TronTVLDataJan = TronTVLData.drop(TronTVLData.index[0:1003])
TronTVLDataJan2 = TronTVLDataJan.drop(TronTVLDataJan.index[31:])
TronTVLgraph = TronTVLDataJan2.plot.line(x='date',y='tvl')

#Binancecoin TVL
BSCTVL = requests.get(baseUrl + '/v2/historicalChainTvl/' + 'BSC')
BSCTVLData = pd.DataFrame.from_dict(BSCTVL.json())
BSCTVLData['date'] = pd.to_datetime(BSCTVLData['date'], unit='s')
BSCTVLDataJan = BSCTVLData.drop(BSCTVLData.index[0:792])
BSCTVLDataJan2 = BSCTVLDataJan.drop(BSCTVLDataJan.index[31:])
BSCTVLgraph = BSCTVLDataJan2.plot.line(x='date',y='tvl')

#Arbitrum TVL
ArbitrumTVL = requests.get(baseUrl + '/v2/historicalChainTvl/' + 'Arbitrum')
ArbitrumTVLData = pd.DataFrame.from_dict(ArbitrumTVL.json())
ArbitrumTVLData['date'] = pd.to_datetime(ArbitrumTVLData['date'], unit='s')
ArbitrumTVLDataJan = ArbitrumTVLData.drop(ArbitrumTVLData.index[0:489])
ArbitrumTVLDataJan2 = ArbitrumTVLDataJan.drop(ArbitrumTVLDataJan.index[31:])
ArbitrumTVLgraph = ArbitrumTVLDataJan2.plot.line(x='date',y='tvl')

#Polygone TVL
PolygonTVL = requests.get(baseUrl + '/v2/historicalChainTvl/' + 'Polygon')
PolygonTVLData = pd.DataFrame.from_dict(PolygonTVL.json())
PolygonTVLData['date'] = pd.to_datetime(PolygonTVLData['date'], unit='s')
PolygonTVLDataJan = PolygonTVLData.drop(PolygonTVLData.index[0:814])
PolygonTVLDataJan2 = PolygonTVLDataJan.drop(PolygonTVLDataJan.index[31:])
PolygonTVLgraph = PolygonTVLDataJan2.plot.line(x='date',y='tvl')

#Optimism TVL
OptimismTVL = requests.get(baseUrl + '/v2/historicalChainTvl/' + 'Optimism')
OptimismTVLData = pd.DataFrame.from_dict(OptimismTVL.json())
OptimismTVLData['date'] = pd.to_datetime(OptimismTVLData['date'], unit='s')
OptimismTVLDataJan = OptimismTVLData.drop(OptimismTVLData.index[0:536])
OptimismTVLDataJan2 = OptimismTVLDataJan.drop(OptimismTVLDataJan.index[31:])
OptimismTVLgraph = OptimismTVLDataJan2.plot.line(x='date',y='tvl')

#Avalanche TVL
AvalancheTVL = requests.get(baseUrl + '/v2/historicalChainTvl/' + 'Avalanche')
AvalancheTVLData = pd.DataFrame.from_dict(AvalancheTVL.json())
AvalancheTVLData['date'] = pd.to_datetime(AvalancheTVLData['date'], unit='s')
AvalancheTVLDataJan = AvalancheTVLData.drop(AvalancheTVLData.index[0:697])
AvalancheTVLDataJan2 = AvalancheTVLDataJan.drop(AvalancheTVLDataJan.index[31:])
AvalancheTVLgraph = AvalancheTVLDataJan2.plot.line(x='date',y='tvl')

#Mixin TVL
MixinTVL = requests.get(baseUrl + '/v2/historicalChainTvl/' + 'Mixin')
MixinTVLData = pd.DataFrame.from_dict(MixinTVL.json())
MixinTVLData['date'] = pd.to_datetime(MixinTVLData['date'], unit='s')
MixinTVLDataJan = MixinTVLData.drop(MixinTVLData.index[0:396])
MixinTVLDataJan2 = MixinTVLDataJan.drop(MixinTVLDataJan.index[31:])
MixinTVLgraph = MixinTVLDataJan2.plot.line(x='date',y='tvl')

#Pulse TVL
PulseTVL = requests.get(baseUrl + '/v2/historicalChainTvl/' + 'Pulse')
PulseTVLData = pd.DataFrame.from_dict(PulseTVL.json())
PulseTVLData['date'] = pd.to_datetime(PulseTVLData['date'], unit='s')
#Pulse has no data in Jan

#Cronos TVL
SolTVL = requests.get(baseUrl + '/v2/historicalChainTvl/' + 'Solana')
SolTVLData = pd.DataFrame.from_dict(SolTVL.json())
SolTVLData['date'] = pd.to_datetime(SolTVLData['date'], unit='s')
SolTVLDataJan = SolTVLData.drop(SolTVLData.index[0:654])
SolTVLDataJan2 = SolTVLDataJan.drop(SolTVLDataJan.index[31:])
SolTVLgraph = SolTVLDataJan2.plot.line(x='date',y='tvl')


#Question 3
protocol = requests.get(baseUrl + '/protocols')
#Make into dataframe
protocolData = pd.DataFrame.from_dict(protocol.json())
#only include chain, tvl, name
protocolDataclean = protocolData[['chain','tvl','name','slug']]
#remove all rows except with Arbitrum
protocolDataArbitrum = protocolDataclean[protocolData["chain"].str.contains("Arbitrum") == True]
#top 10 Arbitrum
protocolDataArbitrumsorted = protocolDataArbitrum.sort_values('tvl',ascending=False)[0:10]
print(protocolDataArbitrumsorted)

protocolDataArbitrumgraph = protocolDataArbitrumsorted.plot.bar(x='name', y='tvl', rot=50)

#Question 4
#Camelot v2
protocolFeecamelotv2 = requests.get(baseUrl + '/summary/fees/' + 'camelot-v2/' + '?datatype=dataType=dailyFees')
protocolFeecamelotv2Data = pd.DataFrame.from_dict(protocolFeecamelotv2.json()['totalDataChartBreakdown'])
#Change time series to datetime
protocolFeecamelotv2Data[0] = pd.to_datetime(protocolFeecamelotv2Data[0], unit='s')
#Latest 30D
protocolFeecamelotv2Data = protocolFeecamelotv2Data.drop(protocolFeecamelotv2Data.index[:-30])

#Clean data
protocolFeecamelotv2Data2 = protocolFeecamelotv2Data[1].astype(str).str.replace("}}", "")
protocolFeecamelotv2Data3 = protocolFeecamelotv2Data2.astype(str).str.replace("{'arbitrum': {'camelot': ", "")
#Turn into numeric
protocolFeecamelotv2Data3 = pd.to_numeric(protocolFeecamelotv2Data3)
#1 year annulised
Totalfeecamelotv2 = (protocolFeecamelotv2Data3.sum())*12
print(Totalfeecamelotv2)


#GND 
protocolFeegnd = requests.get(baseUrl + '/summary/fees/' + 'gnd-protocol/' + '?datatype=dataType=dailyFees')
protocolFeegndData = pd.DataFrame.from_dict(protocolFeegnd.json()['totalDataChartBreakdown'])
#Change time series to datetime
protocolFeegndData[0] = pd.to_datetime(protocolFeegndData[0], unit='s')
#Latest 30D
protocolFeegndData = protocolFeegndData.drop(protocolFeegndData.index[:-30])

#Clean data
protocolFeegndData2 = protocolFeegndData[1].astype(str).str.replace("}}", "")
protocolFeegndData3 = protocolFeegndData2.astype(str).str.replace("{'arbitrum': {'gnd-protocol': ", "")
#Turn into numeric
protocolFeegndData3 = pd.to_numeric(protocolFeegndData3)
#1 year annulised
Totalfeegnd = (protocolFeegndData3.sum())*12
print(Totalfeegnd)

#Chronos
protocolFeeChronos = requests.get(baseUrl + '/summary/fees/' + 'chronos/' + '?datatype=dataType=dailyFees')
protocolFeeChronosData = pd.DataFrame.from_dict(protocolFeeChronos.json()['totalDataChartBreakdown'])
#Change time series to datetime
protocolFeeChronosData[0] = pd.to_datetime(protocolFeeChronosData[0], unit='s')
#Latest 30D
protocolFeeChronosData = protocolFeeChronosData.drop(protocolFeeChronosData.index[:-30])

#Clean data
protocolFeeChronosData2 = protocolFeeChronosData[1].astype(str).str.replace("}}", "")
protocolFeeChronosData3 = protocolFeeChronosData2.astype(str).str.replace("{'arbitrum': {'chronos': ", "")
#Turn into numeric
protocolFeeChronosData3 = pd.to_numeric(protocolFeeChronosData3)
#1 year annulised
TotalfeeChronos = (protocolFeeChronosData3.sum())*12
print(TotalfeeChronos)

#vesta-finance
protocolFeeVesta = requests.get(baseUrl + '/summary/fees/' + 'vesta-finance/' + '?datatype=dataType=dailyFees')
protocolFeeVestaData = pd.DataFrame.from_dict(protocolFeeVesta.json()['totalDataChartBreakdown'])
#Change time series to datetime
protocolFeeVestaData[0] = pd.to_datetime(protocolFeeVestaData[0], unit='s')
#Latest 30D
protocolFeeVestaData = protocolFeeVestaData.drop(protocolFeeVestaData.index[:-30])

#Clean data
protocolFeeVestaData2 = protocolFeeVestaData[1].astype(str).str.replace("}}", "")
protocolFeeVestaData3 = protocolFeeVestaData2.astype(str).str.replace("{'arbitrum': {'vesta-finance': ", "")
#Turn into numeric
protocolFeeVestaData3 = pd.to_numeric(protocolFeeVestaData3)
#1 year annulised
TotalfeeVesta = (protocolFeeVestaData3.sum())*12
print(TotalfeeVesta)

#Lodestar-finance (No chart breakdown?)
protocolFeeLodestar = requests.get(baseUrl + '/summary/fees/' + 'lodestar/' + '?datatype=dataType=dailyFees')
protocolFeeLodestarData = pd.DataFrame.from_dict(protocolFeeLodestar.json()['totalDataChartBreakdown'])


#Vela-exchange
protocolFeeVela = requests.get(baseUrl + '/summary/fees/' + 'vela-exchange/' + '?datatype=dataType=dailyFees')
protocolFeeVelaData = pd.DataFrame.from_dict(protocolFeeVela.json()['totalDataChartBreakdown'])
#Change time series to datetime
protocolFeeVelaData[0] = pd.to_datetime(protocolFeeVelaData[0], unit='s')
#Latest 30D
protocolFeeVelaData = protocolFeeVelaData.drop(protocolFeeVelaData.index[:-30])

#Clean data
protocolFeeVelaData2 = protocolFeeVelaData[1].astype(str).str.replace("}}", "")
protocolFeeVelaData3 = protocolFeeVelaData2.astype(str).str.replace("{'arbitrum': {'vela': ", "")
#Turn into numeric
protocolFeeVelaData3 = pd.to_numeric(protocolFeeVelaData3)
#1 year annulised
TotalfeeVela = (protocolFeeVelaData3.sum())*12
print(TotalfeeVela)

#Shell (No chart breakdown)
protocolFeeShell = requests.get(baseUrl + '/summary/fees/' + 'shell-protocol/' + '?datatype=dataType=dailyFees')
protocolFeeShellData = pd.DataFrame.from_dict(protocolFeeShell.json()['totalDataChartBreakdown'])

#Camelot v3
protocolFeeCamelotv3 = requests.get(baseUrl + '/summary/fees/' + 'camelot-v3/' + '?datatype=dataType=dailyFees')
protocolFeeCamelotv3Data = pd.DataFrame.from_dict(protocolFeeCamelotv3.json()['totalDataChartBreakdown'])
#Change time series to datetime
protocolFeeCamelotv3Data[0] = pd.to_datetime(protocolFeeCamelotv3Data[0], unit='s')
#Latest 30D
protocolFeeCamelotv3Data = protocolFeeCamelotv3Data.drop(protocolFeeCamelotv3Data.index[:-30])

#Clean data
protocolFeeCamelotv3Data2 = protocolFeeCamelotv3Data[1].astype(str).str.replace("}}", "")
protocolFeeCamelotv3Data3 = protocolFeeCamelotv3Data2.astype(str).str.replace("{'arbitrum': {'camelot-v3': ", "")
#Turn into numeric
protocolFeeCamelotv3Data3 = pd.to_numeric(protocolFeeCamelotv3Data3)
#1 year annulised
TotalfeeCamelotv3 = (protocolFeeCamelotv3Data3.sum())*12
print(TotalfeeCamelotv3)

#PlutusDao (No total data chart breakdown)
protocolFeePlutus = requests.get(baseUrl + '/summary/fees/' + 'plutusdao/' + '?datatype=dataType=dailyFees')
protocolFeePlutusData = pd.DataFrame.from_dict(protocolFeePlutus.json()['totalDataChartBreakdown'])

#Rage Trade (No Total data chart breakdown)
protocolFeeragetrade = requests.get(baseUrl + '/summary/fees/' + 'rage-trade/' + '?datatype=dataType=dailyFees')
protocolFeeragetradeData = pd.DataFrame.from_dict(protocolFeeragetrade.json()['totalDataChartBreakdown'])

allfees = pd.DataFrame({'Protocol' : ['Camelot-V2','GND' ,'Chronos','Vesta','LodeStar','Vela','Shell','Camelotv3','PlutusDAO','Rage Trade'],'Amount' : [Totalfeecamelotv2,Totalfeegnd,TotalfeeChronos,TotalfeeVesta,0,TotalfeeVela,0,TotalfeeCamelotv3,0,0]})
allfeesgraph = allfees.plot.bar(x='Protocol', y='Amount', rot=50)
