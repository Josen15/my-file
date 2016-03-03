# -*- coding: utf-8 -*-
from splinter import Browser

class test_add_agent(object):
  def __init__(self,browser_type,url):
    self.browser_type=browser_type
    self.url=url
  def config(self,username='',password='',mobile='',name='',group=''):
    self.username=username
    self.password=password
    self.name=name
    self.group=group
  def verify(self,case):
    self.__fill_form()
    if case==1:# 判断正常填写表单是否能新增业务员
      print self.username
      pass
    elif case==2:# 判断组是否是必填项
      pass 
    elif case==3:# 判断用户名是否是必填项
      pass 
    elif case==4:# 判断手机号是否是必填项
      pass 
    elif case==5:# 判断姓名是否是必填项
      pass 
    elif case==6:# 判断密码是否是必填项
      pass 
    elif case==7:# 判断重复密码不一致是否有报错
      pass 
    elif case==8:# 判断不填写重复密码是否有报错
      pass 
    elif case==9:# 判断创建已存在的业务员是否报错
      pass 
      
  def __fill_form(self): #填写表单
    pass
a=test_add_agent('chrome','http://www.baidu.com')
a.config(u'周子予')
a.verify(1)