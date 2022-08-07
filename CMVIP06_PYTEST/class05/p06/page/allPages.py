#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
淘宝首页登陆
https://login.taobao.com/
page_indexLogin
"""
# 用户名
page_indexLogin_user = ['id', 'fm-login-id']
# 密码
page_indexLogin_pwd = ['id', 'fm-login-password']
# 登陆按钮
page_indexLogin_loginBtn = ['xpath', "//div[@class='fm-btn']"]

"""
购物车详情页
https://cart.taobao.com/cart.htm
page_cartDetail
"""
# 全选按钮
page_cartDetail_selectAll = ["id","J_SelectAll1"]
# 结算按钮
page_cartDetail_payBtn = ["xpath","//div[@class='btn-area']"]
# 提交订单按钮
page_cartDetail_submitBtn = ["link text","提交订单"]
# 删除按钮
page_cartDetail_delBtn = ["link text","删除"]
# 关闭按钮
page_cartDetail_closeBtn = ["partial link text","闭"]
# 确定按钮
page_cartDetail_confirmBtn = ["partial link text","确"]
# 颜色分类栏
page_cartDetail_colorClum = "//p[@class='sku-line']"
# SKU修改按钮
page_cartDetail_modifyBtn = ["xpath","//span[text()='修改']"]
# 颜色分类
page_cartDetail_colors = ["xpath","//div[@class='sku-edit-content']/div/dl/dd/ul/li[2]"]
# 颜色分类确认按钮
page_cartDetail_colorsConfirmBtn = ["xpath","//div[@class='sku-edit-content']/div/p/a"]
# 移入收藏夹
page_cartDetail_favorites = ["link text","移入收藏夹"]
# 单一商品信息栏
page_cartDetail_singleGoodsClum = "//div[@class='order-content']"
# 相似宝贝超链接
page_cartDetail_similarGoodsLink = ["link text","相似宝贝"]
# 翻页按钮
# page_cartDetail_simlarGoddsNext = ["xpath","//a[@class='fss-navigator fss-next J_fs_next ']"]
page_cartDetail_simlarGoddsNext = ["xpath","//a[contains(@class,'J_fs_next')]"]
# 相似宝贝
page_cartDetail_simlarGoods = ["xpath","//div[@class='find-similar-body']/div/div/div[2]"]