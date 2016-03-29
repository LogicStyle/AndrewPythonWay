__author__ = 'aming.tao'
from WindPy import w
from datetime import *
w.start()
data=w.wsd("600000.SH","close,amt","2013-04-30", datetime.today()-timedelta(1))#取浦发银行收盘价等信
data=w.wsd("600000.SH","close,amt", datetime.today()-timedelta(100))#

data=w.wsi("600000.SH","close,amt","2015-10-01 9:00:00")#取浦发银行分钟收盘价等信息

data=w.wst("600000.SH","open", datetime.today()-timedelta(0,2*3600), datetime.now())#取浦发银行tick数据信息

data=w.wss("600000.SH,000001.SZ","eps_ttm,orps,surpluscapitalps","rptDate=20121231")#取浦发银行等财务数据信息


data=w.wset("SectorConstituent",u"date=20130608;sector=全部A股")#取全部A 股股票代码、名称信息
w.wset("IndexConstituent","date=20130608;windcode=000300.SH;field=wind_code,i_weight")#取沪深300 指数中股票代码和权重
w.wset("TradeSuspend","startdate=20130508;enddate=20130608;field=wind_code,sec_name,suspend_type,suspend_reason")#取停牌信息
w.wset("SectorConstituent",u"date=20130608;sector=风险警示股票;field=wind_code,sec_name")#取ST 股票等风险警示股票信息

w.tdays("2013-05-01","2013-06-08")#返回5 月1 日到6 月8 日之间的交易日序列
w.tdays("2013-05-01")#返回5 月1 日到当前时间的交易日序列
w.tdaysoffset(-5,"2013-05-01")#返回5 月1 日前推五个交易日的日期，返回2013-4-19
w.tdaysoffset(-5)#返回当前时间前推五个交易日的日期
w.tdayscount("2013-05-01","2013-06-08")#返回5 月1 日到6 月8 日之间的交易日序列长度，为27

w.stop()