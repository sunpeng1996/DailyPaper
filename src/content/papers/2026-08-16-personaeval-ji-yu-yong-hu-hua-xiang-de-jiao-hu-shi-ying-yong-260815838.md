---
title: 'PersonaEval: Persona-Based User Simulation for Evaluating Interactive Applications'
title_zh: PersonaEval：基于用户画像的交互式应用用户模拟评估框架
authors:
- Yifan Simon Liu
- Qianfeng Wen
- Yilan Fan
- Shirley Huang
- Ruoqi Gao
- Jianheng Hou
- Muhammad Ahmed Mohsin
- Zonglin Di
- Brihi Joshi
- Xincheng Tan
affiliations:
- MatrAIx Team
arxiv_id: '2608.15838'
url: https://arxiv.org/abs/2608.15838
pdf_url: https://arxiv.org/pdf/2608.15838
published: '2026-08-16'
collected: '2026-08-18'
category: Eval
direction: 用户模拟 · 交互式系统自动评估
tags:
- PersonaSimulation
- EvaluationFramework
- UserBehaviorSimulation
- LLM4Eval
- InteractiveSystem
one_liner: 提出基于persona的用户模拟框架，低成本替代真人测试实现交互式系统可扩展评估
practical_value: '- 可复用该框架的persona+LLM用户模拟逻辑，替代推荐系统/对话Agent上线前的小批量真人众包测试，降低前期评估的人力与时间成本

  - 参考其plug-and-play适配架构，将模拟用户模块接入推荐策略AB测试的前置校验流程，快速对比多版策略的不同用户分层反馈差异

  - 可基于该框架生成冷启动用户群的交互轨迹数据，补充新业务场景下的用户行为训练样本，优化冷启动阶段的召回排序效果'
score: 7
source: arxiv-cs.HC
depth: abstract
---

## 动机
真人用户研究是评估交互式系统表现的黄金标准，但存在成本高、周期长、用户招募难度大、规模化落地困难的问题，无法支撑产品快速迭代的高频评估需求。

## 方法关键点
- 搭建PersonaEval用户模拟评估框架，直接复用现有persona数据集生成对应特征的模拟用户，对接不同任务的目标应用接口，自动采集全链路交互轨迹与结果数据
- 设计低侵入式plug-and-play评估工作流，仅需少量接口适配即可更换待评估应用，无需重构整体评估链路

## 关键结果
在问卷调研、Chatbot、Web应用三类场景完成验证，可实现可复现、可并行、可扩展的全自动化评估，输出的用户导向反馈与任务特定行为符合真实用户特征，大幅降低交互式系统前期评估的时间与人力成本。
