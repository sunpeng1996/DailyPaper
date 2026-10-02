---
title: 'Learning What to Recall: Adaptive Multi-Cue Episodic Memory for World Models'
title_zh: 面向世界模型的自适应多线索情景记忆召回框架FAR
authors:
- Beomsu Kim
- Chieh-Hsin Lai
- Bac Nguyen
- Amir Bar
- Jong Chul Ye
- Yuki Mitsufuji
affiliations:
- KAIST
- Sony Group Corporation
- Imperial College London
arxiv_id: '2609.34677'
url: https://arxiv.org/abs/2609.34677
pdf_url: https://arxiv.org/pdf/2609.34677
published: '2026-09-27'
collected: '2026-10-02'
category: Agent
direction: Agent 情景记忆自适应多线索召回
tags:
- Episodic Memory
- World Model
- Multi-Cue Retrieval
- Embodied Agent
- Retrieval Optimization
one_liner: 提出未来感知召回框架FAR，用预测效用监督自适应多线索记忆选择，性能超越手工设计规则
practical_value: '- 推荐/搜索/RAG系统的召回模块可借鉴FAR的训练范式：训练阶段用下游真实业务指标（如推荐CTR、RAG回答正确率）作为监督信号，训练推理阶段无未来信息的检索器，替代泛化性差的人工相似度规则

  - 多特征召回场景（如电商搜索同时用用户行为、query语义、商品属性多维度特征）可借鉴自适应cue融合思路，为每个查询动态分配不同特征的权重，无需固定融合系数

  - 候选池冗余场景可借鉴分块召回技巧：将候选集按时间/类别分块，每块选最高得分样本后再统一召回TopK，避免召回结果高度重复'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有世界模型的情景记忆召回普遍依赖时间近邻、姿态重叠、视觉相似等手工固定规则，不同场景下各检索线索的可靠性波动极大，固定规则无法适配动态环境，也无法保证召回的记忆对未来预测最有价值，长时序预测误差高。
### 方法关键点
- 训练阶段利用观测到的真实未来计算每个候选记忆的预测效用（用Diffusion负预测损失近似），构造融合当前检索得分和预测效用的后验分布，作为监督信号训练推理阶段无未来信息的检索器
- 支持多类检索线索（时间、姿态、视觉、音频等），每个线索单独训练打分器，得分标准化后采用查询依赖的动态权重融合，自动适配不同场景下的线索可信度
- 采用分块召回策略，将记忆按时间分块后每块选取最高分样本，再取整体TopK，避免召回结果冗余
### 关键结果
在LoopNav、SoundSpaces、AI2-THOR三个具身环境测试，对比WorldMem、LongLive-RAG等基线：LoopNav场景下多线索FAR的DreamSim指标比WorldMem低19%，比LongLive-RAG低17%；AI2-THOR动态场景下状态预测准确率比WorldMem提升超30个百分点，双Agent动态预测场景下多线索FAR准确率达94.5%，远高于基线的32.5%~41.8%。
### 核心结论
检索的核心目标是选出对下游任务最有用的结果，而非与查询相似度最高的结果，用下游任务反馈监督检索是比手工规则更通用的优化路径
