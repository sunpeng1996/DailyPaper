---
title: 'SAGEAgent: A Self-Evolving Agent for Cost-Aware Modality Acquisition in Multimodal
  Survival Prediction'
title_zh: SAGEAgent：面向多模态生存预测的成本感知模态获取自进化Agent
authors:
- Chongyu Qu
- Can Cui
- Zhengyi Lu
- Junchao Zhu
- Tianyuan Yao
- Junlin Guo
- Juming Xiong
- Yanfan Zhu
- Yuechen Yang
- Bennett A. Landman
affiliations:
- Vanderbilt University
- Vanderbilt University Medical Center
arxiv_id: '2607.09521'
url: https://arxiv.org/abs/2607.09521
pdf_url: https://arxiv.org/pdf/2607.09521
published: '2026-07-10'
collected: '2026-07-14'
category: Agent
direction: LLM Agent 序贯决策与自进化架构
tags:
- LLM Agent
- Sequential Decision Making
- Episodic Memory
- Semantic Memory
- Multimodal Acquisition
one_liner: 基于LLM的自进化Agent可序贯选择诊断模态，平衡多模态预测精度与采集负担
practical_value: '- 序贯决策+双记忆（episodic + semantic）架构可直接复用在成本敏感的多模态特征采集场景，比如电商用户画像补全，避免无意义的用户数据采集提升体验

  - 数值转文本的工具调用设计可借鉴到推荐系统的LLM推理流程，将离散/连续用户行为特征转化为LLM可理解的自然语言输入，降低prompt工程成本

  - 自进化的决策规则积累逻辑可用于Agent驱动的动态召回/排序策略，从历史流量中自动沉淀可复用的特征选择规则，降低运算成本'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
当前多模态预测方法普遍默认全模态可用，或仅被动处理缺失模态，未针对序贯采集流程主动判断下一模态的采集必要性，造成不必要的采集成本（如临床侵入性检查、业务端算力/用户隐私损耗）。
### 方法关键点
1. 将多模态采集过程建模为序贯决策问题，基于LLM搭建自进化Agent架构；
2. 配套三类核心组件：将数值预测转译为自然语言的工具、检索相似历史案例的episodic memory、沉淀可复用决策规则的semantic memory；
3. 决策逻辑同时权衡预测精度与模态采集负担。
### 关键结果
在包含4种诊断模态的脑胶质瘤数据集上，保持与全模态方法相当的生存预测精度的同时，平均模态采集负担降低55%。
