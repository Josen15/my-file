#!/usr/bin/env python
# -*- coding: utf-8 -*-
#编辑管理员
from splinter import Browser
class editadmin(object):
	def __init__(self,browser_type):
		self.browser_type=browser_type
		self._site='http://www.kuaixiuagency.com'#登陆网页
		self._url=''#编辑管理员页面
	def config(self,username='',name='',mobile='',password=''):
		self.username=username
		self.name=name
		self.mobile=mobile
		self.password=password
	def verify(self,case):
		self._fill_form()
		if case==1:#正确更改内容后提交可以编辑成功
			pass
			if True:#验证管理员信息是否和编辑的一致，用新密码登录是否成功
				self.browser.quit()
				return u'通过'
			else:
				self.browser.quit()
				return u'失败'
		elif case==2:#用户名不能编辑
			pass#用户名不能输入
			self.browser.quit()
		elif case==3:#密码编辑应该两次一致
			pass#密码不一致不能提交
			self.browser.quit()
		elif case==4:#编辑的手机号不是有效的不能成功
			pass#验证不能提交
			self.browser.quit()
		elif case==5:#内容改为字符提交不能编辑成功
			pass#验证不能提交
			self.browser.quit()
		elif case==6:#删除必填内容不能编辑成功
			pass#验证不能提交
			self.browser.quit()
	def _login(self):#以管理员身份登陆
		self.browser=Browser(self.browser_type)
		self.browser.visit(self._site)
	def _fill_form(self):#编辑管理员信息
		self._login()

a=editadmin('chrome')
a.config()
print a.verify(1)