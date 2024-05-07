#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""
@DATE: 2024-05-05 18:32:06
@File: Dnode\ccacnode.py
@IDE: vscode
@Description:
    用于ccac测评的基础节点类
"""
from .abnode import AbNode
from Debater import CCACDebater

class CCACNode(AbNode):
    
    
    def __init__(self,round:int,debater,language:str = "zh"):
        self.round = round
        self.debater=debater
        self.language = language
        self.get_topic()
        self.get_content()
        pass
    
    def get_round_name(self):
        """用于获取该环节名称"""
        if self.round == 1:
            self.round_name = "正方立论"
        elif self.round == 2:
            self.round_name = "反方立论"
        elif self.round == 3:
            self.round_name = "正方驳论"
        elif self.round == 4:
            self.round_name = "反方驳论"
        elif self.round == 5:
            self.round_name = "正方结辩"
        elif self.round == 6:
            self.round_name = "反方结辩"

    
    def get_topic(self):
        return super().get_topic()
    
        
    
    def get_content(self):
        if self.language == "zh":
            if self.round == 1:
                message = "正方立论"
            elif self.round == 2:
                message = "反方立论"
            elif self.round == 3:
                message = "正方驳论"
            elif self.round == 4:
                message = "反方驳论"
            elif self.round == 5:
                message = "正方结辩"
            elif self.round == 6:
                message = "反方结辩"
        elif self.language == "en":
            if self.round == 1:
                message = "正方立论"
            elif self.round == 2:
                message = "反方立论"
            elif self.round == 3:
                message = "正方驳论"
            elif self.round == 4:
                message = "反方驳论"
            elif self.round == 5:
                message = "正方结辩"
            elif self.round == 6:
                message = "反方结辩"
        answer = self.debater.invoke(message,self.round)
        self.content = answer
    
    
