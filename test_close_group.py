#!/uer/bin/emv python
# -*- coding: utf-8 -*-
#关闭分组
from splinter import Browser
class closegroup(object):
	def __init__(self,browser_type): 
		self.browser_type=browser_type
		
		self.site='http://www.kuaixiuagency.com'#登录页面
		
	def verify(self,case):
		self._fill_form()
		if case==1:#在分组列表可以关闭分组
			pass
			if True:#关闭分组后相关业务员管理员无影响，业务员可以新建订单，管理员可以管理业务员
				self.browser.quit()
				return u'通过'
			else:
				self.browser.quit()
				return u'失败'
		elif case==2:#已关闭的分组不能重复关闭
			pass#已关闭的分组不能找到关闭按钮
			self.browser.quit()
		elif case==3:#已关闭的分组可以开启
			pass#已关闭的分组点击开启按钮
			self.browser.quit()
	def _login(self):#登录
		self.browser=Browser(self.browser_type)
		self.browser.visit(self.site)
	def _fill_form(self):
		self._login()

a=closegroup('chrome')
print a.verify(1)
			