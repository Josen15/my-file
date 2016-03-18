#!/usr/bin/env python
# -*- coding: utf-8 -*-
#关闭公司
from splinter import Browser
class closecompany(object):
	def __init__(self,browser_type):
		self.browser_type=browser_type
		self.site='http://www.kuaixiuagency.com'#登录页面
	def config(self,username='',password=''):
		self.username=username
		self.password=password	
	def verify(self,case):
		self._fill_form()
		if case==1:#在公司列表可以关闭公司
			pass
			if True:#验证公司处于关闭状态
#			        相关业务员不能登录
#			        管理员不能登录
				self.browser.quit()
				return u'通过'
			else:
				self.browser.quit()
				return u'失败'
		elif case==2:#已关闭的公司不能重复关闭
			pass#关闭后没有关闭按钮
			self.browser.quit()
		elif case==3:#已关闭的公司可以开启
			pass#关闭后可以点击开启按钮开启
#                开启后业务员可以登录
#                开启后管理员可以登录
			self.browsre.quit()
	def _login(self):#登录
		self.browser=Browser(self.browser_type)
		self.browser.visit(self.site)
	def _fill_form(self):#填写用户名密码
		self._login()

a=closecompany('chrome')
a.config()				
print a.verify(1)
