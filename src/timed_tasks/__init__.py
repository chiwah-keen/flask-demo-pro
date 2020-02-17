#! /usr/bin/env python
# -*- coding:utf-8 -*-
"""
@attention: 定时任务模块

@note: 
- 启动脚本用start_xx开头,方便部署的兄弟很快找到
- 可以直接调用app中的control功能,但是不能在control中调用定时模块的功能,防止交叉引用
- 如果有外部任务管理工具,不建议使用celery来做定时控制,小项目随意
"""