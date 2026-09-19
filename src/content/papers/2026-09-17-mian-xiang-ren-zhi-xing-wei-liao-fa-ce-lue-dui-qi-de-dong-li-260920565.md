---
title: 'Steering the Compass: Aligning Dynamic Psychological Counseling Conversations
  with Cognitive Behavioral Therapy Strategies'
title_zh: 面向认知行为疗法策略对齐的动态心理咨询对话数据集StratCBT
authors:
- Zimu Wang
- Yiwen Jiang
- Xiangyu Zhao
- Yaling Shen
- Jiahe Liu
- Stephanie Fong
- Maxmartwell H Cheng
- Guilherme C Oliveira
- Anh Nguyen
- Robert Desimone
affiliations:
- Monash University
- University of Liverpool
- Massachusetts Institute of Technology
- The University of Melbourne
- Orygen
arxiv_id: '2609.20565'
url: https://arxiv.org/abs/2609.20565
pdf_url: https://arxiv.org/pdf/2609.20565
published: '2026-09-17'
collected: '2026-09-19'
category: LLM
direction: LLM 垂直领域对话数据集构建
tags:
- LLM
- Dataset
- Conversational Agent
- CBT
- Dialogue Generation
one_liner: 构建含9688个会话25.6万条utterance的CBT策略对齐心理咨询数据集并验证策略对齐生成有效性
practical_value: '- 多轮对话策略对齐的标注框架可迁移到客服、导购类对话Agent构建，按业务目标（转化、满意度等）定义话术策略池做标注对齐

  - 用真实会话做引导、LLM self-chat生成高质量标注数据集的方法可复用，大幅降低垂直领域对话数据的标注成本

  - 用LLM模拟不同特征用户评估对话系统效果的范式可借鉴，降低线上AB测的风险与成本'
score: 5
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有基于LLM的认知行为疗法（CBT）心理咨询系统忽略了根据用户实时心理状态动态决策的核心要求，灵活性与治疗效果受限，且缺乏高质量的策略对齐标注数据集支撑相关研发。
### 方法关键点
1. 构建StratCBT数据集，基于用户负面想法建模用户特征，以真实咨询会话为引导通过LLM自聊生成高质量对话，每个咨询师回复都对齐8类CBT策略之一；
2. 采用LLM模拟真实客户的评估范式，验证策略对齐对话生成的有效性。
### 关键结果
数据集包含9688个完整会话、约25.6万条utterance，在通用咨询能力、CBT专项技能两个维度上均显著优于现有同类数据集，验证了策略对齐的对话生成专业度与效果更优。
