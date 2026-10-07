---
title: Learning to Retrieve via Reinforcement Learning in Embedding Space
title_zh: 基于嵌入空间强化学习的检索训练框架RELER
authors:
- Qi Liu
- Fengming Liang
- Yiqun Chen
- Erhan Zhang
- Jiaxin Mao
affiliations:
- Renmin University of China
arxiv_id: '2610.07731'
url: https://arxiv.org/abs/2610.07731
pdf_url: https://arxiv.org/pdf/2610.07731
published: '2026-10-06'
collected: '2026-10-07'
category: RecSys
direction: 稠密检索 · 强化学习对齐优化
tags:
- DenseRetrieval
- ReinforcementLearning
- RAG
- Embedding
- PolicyGradient
one_liner: 提出嵌入空间强化学习检索训练框架RELER，直接对齐检索与下游指标，推理无额外开销
practical_value: '- 检索/召回模型后调可复用RELER的vMF嵌入采样+RLOO方案，直接对齐GMV、点击率、转化率等不可微的业务目标，推理保留原有确定性向量检索逻辑，无额外性能开销

  - 面对电商/内容平台百万级以上的大规模向量索引，可采用仅微调query编码器的方案，配合嵌入锚定损失限制漂移，无需重建全量文档索引，大幅降低落地成本

  - 高维连续动作RL训练时可直接复用CMP梯度投影trick，将采样向量投影到任务相关的低维子空间，在不改变梯度期望的前提下大幅降低噪声，提升训练稳定性

  - RAG/搜索全链路优化可采用混合奖励策略，同时对齐检索指标和下游业务效果指标，比单独优化检索指标的端到端收益更高'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有稠密检索模型普遍基于对比学习训练，损失函数仅要求相关query-doc对相似度高于负例，与nDCG、下游RAG答案准确率等核心业务指标没有直接对齐，优化对比损失不一定能带来实际检索效果的提升，存在和LLM预训练到人类偏好对齐类似的目标gap。

### 方法关键点
- 训练时在编码器输出的归一化嵌入上套von Mises-Fisher（vMF）分布做连续动作采样，将检索指标、下游业务指标作为奖励，用REINFORCE with leave-one-out baseline（RLOO）计算策略梯度更新编码器，推理阶段仍然输出确定性单一向量，无额外开销
- 提出条件均值投影（CMP）：计算梯度时将采样嵌入投影到由当前编码器输出和候选嵌入张成的低维子空间，过滤高维采样带来的无关噪声，同时保证梯度期望无偏，大幅提升训练稳定性
- 支持固定文档索引场景下仅微调query编码器，加入锚定损失限制query嵌入漂移，无需重建全量文档向量索引，适配大规模线上部署场景

### 关键结果
- 在推理密集型检索基准BRIGHT上，仅用不到5k条query后调，RELER在BGE-M3、Qwen3-Embedding-0.6B/4B骨干上的平均nDCG@10，较InfoNCE baseline最高提升3.22个点
- 在7个QA数据集的固定索引RAG任务上，仅微调query编码器、冻结文档索引和生成器，混合nDCG与答案F1奖励的方案，较预训练编码器的平均答案EM、F1分别提升0.66、0.34个点

### 核心结论
检索模型可通过嵌入空间RL直接对齐业务目标，无需改变推理链路，落地成本低且收益明确
