'''
Created by auto_sdk on 2020.05.28
'''
from top.api.base import RestApi

"""

"""

class TbkItemInfoGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.ip = None  # ip地址，影响邮费获取，如果不传或者传入不准确，邮费无法精准提供
		self.num_iids = None  # 商品ID串，用,分割，最大40个
		self.platform = None  #  链接形式：1：PC，2：无线，默认：１ 

	def getapiname(self):
		return 'taobao.tbk.item.info.get'
