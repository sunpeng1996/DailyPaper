---
title: Predicting Partial Answer Quality and Utility in Agentic Retrieval-Augmented
  Generation
title_zh: 智能体检索增强生成（Agentic RAG）的中间回答质量与效用预测
authors:
- Fangzheng Tian
- Debasis Ganguly
- Craig Macdonald
affiliations:
- University of Glasgow
arxiv_id: '2609.16453'
url: https://arxiv.org/abs/2609.16453
pdf_url: https://arxiv.org/pdf/2609.16453
published: '2026-09-15'
collected: '2026-09-16'
category: RAG
direction: Agentic RAG 效率优化 · 早停控制
tags:
- Agentic RAG
- Early Stopping
- Utility Prediction
- RAG Efficiency
- Trajectory Probing
one_liner: 提出轨迹内探测框架预测Agentic RAG中间回答状态，早停可降11%迭代量且保留98%回答质量
practical_value: '- 电商导购/客服Agentic RAG pipeline可复用双阈值早停策略，基于中间回答质量+边际效用判断停止时机，在不损失用户体验的前提下降低推理时延与算力成本

  - 可复用三类轨迹信号（迭代内特征/迭代间变化/原始query对齐特征）训练轻量监督预测器，无需额外大模型调用即可实现低开销的中间状态判断

  - 多轮搜索推荐/多跳召回场景可借鉴轨迹探测思路，量化每轮召回的边际效用，识别无效环节优化全链路效率'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
Agentic RAG通过多轮检索推理解决多跳复杂问题效果突出，但现有评估仅关注端到端结果，无法感知中间回答状态变化，大量冗余迭代既增加算力成本，又推高推理时延，高并发场景（如电商客服、导购Agent）下的效率瓶颈尤为明显。
### 方法关键点
- 设计轨迹内探测机制：每轮检索推理后强制生成中间回答，定义两个核心指标：部分回答质量（当前中间回答与ground truth的F1值）、部分效用（相邻轮次回答质量的差值）
- 构建三类可解释预测信号：迭代内信号（当前轮检索质量、推理一致性等）、迭代间信号（相邻轮query/检索结果/推理内容的相似度变化）、query-迭代对齐信号（当前轮内容与原始用户query的匹配度）
- 基于轻量交叉编码器+MLP时序预测头实现质量/效用预测，通过双阈值划分4种回答状态触发早停，支持回滚到历史最优回答点
### 关键实验结果
在Search-R1、R1-Searcher两个主流Agentic RAG pipeline上测试，覆盖HotpotQA、2Wiki、MuSiQue三个多跳QA数据集：部分回答质量预测的Pearson r最高达0.438，预测准确性显著高于部分效用；早停策略可降低11%的平均迭代次数，同时保留98%的自然停止下的最终回答质量，效果远优于固定轮次截断的Cap@k baseline。
### 核心结论
Agentic RAG的有效迭代稀疏且多集中在前几轮，大部分后续迭代对回答质量几乎无贡献，轻量预测驱动的动态早停是平衡效果与效率的高性价比方案。
