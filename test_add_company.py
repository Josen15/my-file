#!/usr/bin/env python
# -*- coding: utf-8 -*-
#新建公司
from splinter import Browser
class newcompany(object):
	def __init__(self,browser_type):
		self.browser_type=browser_type
		self.site='http://www.kuaixiuagency.com'#登录网址
		self.url=''#新增公司网址
	def config(self,name='',type=''):
		self.name=name
		self.type=type
	def verify(self,case):
		self._fill_form()
		if case==1:#正确输入公司的有关内容可以新增成功
			pass
			if True:#验证输入内容是否一致
				self.browser.quit()
				return u'通过'
			else:
				self.browser.quit()
				return u'失败'
		elif case==2:#输入公司名称不选择公司类型不能新增成功
			pass#验证不能提交
			self.browser.quit()
		elif case==3:#输入已有的公司名称不能新增成功
			pass #验证不能提交
			self.browser.quit()
		elif case==4:#在公司名输入框输入字符不能新增成功
			pass#验证不能提交
			self.browser.quit()
	def _login(self):#登录
		self.browser=Browser(self.browser_type)
		self.browser.visit(self.site)
	def _fill_form(self):#填写新增公司内容
		self._login()
	
a=newcompany('chrome')
a.config()
print a.verify(1)