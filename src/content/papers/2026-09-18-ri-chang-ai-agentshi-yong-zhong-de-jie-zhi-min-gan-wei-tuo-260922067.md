---
title: 'Value-Sensitive Delegation in Everyday AI Agent Use: Evidence from OpenClaw'
title_zh: 日常AI Agent使用中的价值敏感委托：基于OpenClaw用户反馈的实证研究
authors:
- Renkai Ma
- Ruyuan Wan
- Xuan Lu
- Fan Yang
- Chen Chen
- Lingyao Li
affiliations:
- University of Cincinnati
- The Pennsylvania State University
- University of Arizona
- University of South Carolina
- Florida International University
arxiv_id: '2609.22067'
url: https://arxiv.org/abs/2609.22067
pdf_url: https://arxiv.org/pdf/2609.22067
published: '2026-09-18'
collected: '2026-09-21'
category: Agent
direction: Agent 价值对齐与用户体验优化
tags:
- AI Agent
- Value Sensitive Design
- OpenClaw
- User Experience
- Value Alignment
one_liner: 分析7万+OpenClaw用户第一人称反馈，提出价值敏感委托概念，明确Agent价值对齐需关注用户设置的运行边界
practical_value: '- 面向C端的Agent产品（如电商导购Agent、运营自动化Agent）不要只投入资源优化核心模型效果，要重点打磨运行边界配置：包括token计费规则透明度、权限可控范围、人工审核节点设置、安装接入流程，这些是用户不满的重灾区

  - 搭建Agent评估体系时要补全用户维度指标：除了常规任务完成率，还要增加资源消耗透明度、监督成本、权限风险感知、接入门槛这几类指标，和用户实际体验对齐

  - 新产品上线前可爬取公开社区的早期用户反馈，用LLM辅助标注快速挖掘用户价值诉求，提前优化用户关心的边界问题，大幅减少上线后客诉'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有AI Agent评估体系仅围绕任务完成率设计，完全忽略用户实际使用时的核心价值诉求（如使用成本、权限可控性、监督成本等），价值对齐研究多从开发者视角出发，缺乏对普通用户日常使用场景下真实诉求的实证支撑，无法明确用户价值到底绑定在Agent的哪些模块上。
### 方法关键点
- 采用价值敏感设计（VSD）分析框架，爬取2026年1-4月Reddit上的OpenClaw相关帖子，筛选出73093条第一人称使用反馈
- 用GPT-5 mini辅助标注，编码维度覆盖21类用户价值、18类Agent模块、9类用户结果，人工验证标注一致性达82%~98.8%
- 交叉分析用户价值、绑定的Agent模块、使用结果三者的关联，归纳价值敏感委托的核心特征
### 关键结果
- 70.8%的用户价值诉求集中在5类：自主性、可靠性、可负担性、资源管理、通用可用性
- 用户价值不满高发区并非模型核心，而是运行边界模块：资源计费模块满足率仅35.3%，系统接入模块47.0%，环境权限模块51.2%
- 任务完成类帖子价值满足率达67.7%，资源消耗类仅34.7%，风险暴露类仅10.7%
### 核心结论
AI Agent的价值对齐不能只关注模型输出，更要关注用户为委托任务设置的运行边界条件，包括成本、权限、监督规则
