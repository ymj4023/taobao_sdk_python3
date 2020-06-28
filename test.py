# -*- coding: utf-8 -*-
'''
Created on 2012-7-3

@author: lihao
'''
import top.api
import json
top.setDefaultAppInfo("xxxx", "xxxx")




class TaobaoWordCommand(object):
    


    def get_word_command(self,user_id="xxxx",text="粉丝优惠券",url="https://uland.taobao.com/",logo="https://uland.taobao.com/"):

        req = top.api.TbkTpwdCreateRequest()
        req.user_id= user_id
        req.text= text
        req.url=url
        req.logo= logo
        req.ext="{}"
        try:
            resp= req.getResponse()
            print(resp)
            return resp
        except Exception as e:
            return e
    
if __name__ =="__main__":
    word_command = TaobaoWordCommand()
    word_command.get_word_command()