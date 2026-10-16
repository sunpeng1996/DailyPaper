---
title: Aligning LLMs with Sparse Retrieval via Adaptive Sparse Supervision
title_zh: 基于自适应稀疏监督的大语言模型稀疏检索对齐方法
authors:
- Tongna Chen
- Minghan Li
- Guodong Zhou
affiliations:
- Soochow University
arxiv_id: '2610.21877'
url: https://arxiv.org/abs/2610.21877
pdf_url: https://arxiv.org/pdf/2610.21877
published: '2026-10-15'
collected: '2026-10-16'
category: RecSys
direction: 稀疏检索 · LLM语义对齐
tags:
- Sparse Retrieval
- LLM Alignment
- LoRA
- Knowledge Distillation
- Contrastive Learning
one_liner: 提出动态α截断对齐LLM与稀疏检索空间，较同类方案降6.4倍存储提11倍查询速度
practical_value: '- 动态α截断trick可直接复用，将LLM语义表示映射到现有SPLADE稀疏检索空间，无需重建倒排索引，兼容业务现有检索架构

  - 两阶段LoRA微调方案训练成本低，先对齐稀疏空间再做对比+蒸馏优化，适合业务场景快速迭代，无需全量微调LLM

  - 查询、文档分开设置稀疏正则的策略可直接迁移到业务稀疏召回模型，平衡检索效果与存储/延迟成本，适配电商搜索、广告等低延迟要求场景'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有神经稀疏检索（如SPLADE）依赖小编码器，语义表达能力有限；直接用LLM构建稀疏检索模型会产生过密激活，存储、延迟成本过高，无法落地到对响应速度要求严格的搜索推荐生产环境，亟需在保留LLM语义优势的同时兼容稀疏检索的高效性。
### 方法关键点
- 第一阶段稀疏对齐：将LLM隐状态投影到SPLADE词表空间，采用动态α截断策略，根据SPLADE参考向量的累计激活占比动态选择核心保留词，对齐损失同时约束核心词拟合与非核心词抑制，全程用LoRA微调降低训练成本
- 第二阶段检索微调：融合对比学习、跨编码器知识蒸馏、FLOPS式稀疏正则（查询、文档分别设置正则权重），优化检索效果的同时严格控制稀疏度
- 推理阶段无额外截断操作，输出稀疏向量直接兼容现有倒排索引架构
### 关键结果
在MS MARCO、6个BEIR数据集上验证，对比基线包括SPLADE++、Lion-sp等：MS MARCO MRR@10达0.408，接近Lion-sp的0.410，优于SPLADE++的0.383；平均非零激活数仅182，较Lion-sp降低6.4倍存储，端到端查询延迟从1046ms降至89.87ms，提速超11倍；BEIR零样本平均NDCG@10达50.3，优于SPLADE++的48.2，接近Lion-sp的51.3。
### 核心结论
LLM增强稀疏检索的核心是平衡语义表达与稀疏度，自适应监督信号比固定截断预算更易实现效果与效率的帕累托最优
