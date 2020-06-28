'''
Created by auto_sdk on 2020.06.19
'''
from top.api.base import RestApi

"""
TbkCouponGetRequest.py
淘宝客-公用-阿里妈妈推广券详情查询
"""

class TbkCouponGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.activity_id = None  # 券ID
		self.item_id = None  # 	商品ID
		self.me = None  # 带券ID与商品ID的加密串

	def getapiname(self):
		return 'taobao.tbk.coupon.get'
