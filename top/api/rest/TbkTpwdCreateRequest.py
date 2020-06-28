'''
Created by auto_sdk on 2019.11.01
'''
from top.api.base import RestApi

"""
TbkTpwdCreateRequest.py
淘宝客-公用-淘口令生成
"""

class TbkTpwdCreateRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.ext = None  # 扩展字段JSON格式
		self.logo = None  # 口令弹框logoURL
		self.text = None  #  口令弹框内容
		self.url = None  # 口令跳转目标页
		self.user_id = None  # 生成口令的淘宝用户ID

	def getapiname(self):
		return 'taobao.tbk.tpwd.create'
