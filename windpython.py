__author__ = 'aming.tao'
from WindPy import w
from datetime import *
w.start()
data=w.wsd("600000.SH","close,amt","2013-04-30", datetime.today()-timedelta(1))#ȡ�ַ��������̼۵���
data=w.wsd("600000.SH","close,amt", datetime.today()-timedelta(100))#

data=w.wsi("600000.SH","close,amt","2015-10-01 9:00:00")#ȡ�ַ����з������̼۵���Ϣ

data=w.wst("600000.SH","open", datetime.today()-timedelta(0,2*3600), datetime.now())#ȡ�ַ�����tick������Ϣ

data=w.wss("600000.SH,000001.SZ","eps_ttm,orps,surpluscapitalps","rptDate=20121231")#ȡ�ַ����еȲ���������Ϣ


data=w.wset("SectorConstituent",u"date=20130608;sector=ȫ��A��")#ȡȫ��A �ɹ�Ʊ���롢������Ϣ
w.wset("IndexConstituent","date=20130608;windcode=000300.SH;field=wind_code,i_weight")#ȡ����300 ָ���й�Ʊ�����Ȩ��
w.wset("TradeSuspend","startdate=20130508;enddate=20130608;field=wind_code,sec_name,suspend_type,suspend_reason")#ȡͣ����Ϣ
w.wset("SectorConstituent",u"date=20130608;sector=���վ�ʾ��Ʊ;field=wind_code,sec_name")#ȡST ��Ʊ�ȷ��վ�ʾ��Ʊ��Ϣ

w.tdays("2013-05-01","2013-06-08")#����5 ��1 �յ�6 ��8 ��֮��Ľ���������
w.tdays("2013-05-01")#����5 ��1 �յ���ǰʱ��Ľ���������
w.tdaysoffset(-5,"2013-05-01")#����5 ��1 ��ǰ����������յ����ڣ�����2013-4-19
w.tdaysoffset(-5)#���ص�ǰʱ��ǰ����������յ�����
w.tdayscount("2013-05-01","2013-06-08")#����5 ��1 �յ�6 ��8 ��֮��Ľ��������г��ȣ�Ϊ27

w.stop()