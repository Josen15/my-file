#!/usr/bin/env python
# -*- coding: utf-8 -*-
#新建订单
from splinter import Browser
class neworder(object):
	def __init__(self,browser_type):
		self.browser_type=browser_type
		self._site='http://www.kuaixiuagency.com'#登陆页面
		self._url=''#新增订单页面
	def cofig(self,photo='',username='',usermobile='',useraddress='',repaircontent='',):
		self.username=username
		self.usermobile=usermobile
		self.useraddress=useraddress
		self.repaircontent=repaircontent
		self.photo=photo
	def verify(self,case):
		self._fill_form()
		if case==1:#正确输入订单有关内容可以新建成功
			pass
			if True:#验证订单的内容是否和输入的一致
				self.browser.quit()
				return u'测试通过'
			else:
				self.browser.quit()
				return u'测试未通过'
		elif case==2:#上传照片不能超过5张
			pass#上传六张照片，第六张上传不了
			self.browser.quit()
				
		elif case==3:#上传非照片格式不能上传成功
			pass#不能提交
			self.browser.quit()
				
		elif case==4:#输入报修联系人，报修联系人电话，报修地址，报修内容，不上传照片可以新建成功
			pass#验证订单的内容是否和输入的一致
			self.browser.quit()
				
		elif case==5:#删除上传错的现场照片提交，不显示已删除的照片
			pass##验证订单的内容是否和输入的一致
			self.browser.quit()
				
		elif case==6:#联系人电话输入不是有效的不能新增成功
			pass#验证不能提交
			self.browser.quit()
				
		elif case==7:#输入报修联系人，电话，地址，不输入报修内容不能新建成功
			pass#验证不能提交
			self.browser.quit()
				
		elif case==8:#输入报修联系人，电话，报修内容，不输入地址不能新建成功
			pass#验证不能提交
			self.browser.quit()
				 
		elif case==9:#输入报修联系人，报修内容，地址，不输入电话不能新建成功
			pass#验证不能提交
			self.browser.quit()
				
		elif case==10:#输入报修人电话，地址，报修内容，不输入报修联系人不能新建成功
			pass#验证不能提交
			self.browser.quit()
	def _login(self):#以业务员身份登陆
		self.browser=Browser(self.browser_type)
		self.browser.visit(self._site)
	def _fill_form(self):#填写订单内容
		self._login()

		
m=neworder('chrome')
m.cofig()
print m.verify(1)
			
		