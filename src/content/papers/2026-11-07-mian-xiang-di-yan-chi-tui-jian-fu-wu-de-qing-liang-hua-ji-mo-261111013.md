---
title: Slim Foundation Models for Latency-Critical Recommendation Serving
title_zh: 面向低延迟推荐服务的轻量化基础模型框架SlimFM
authors:
- Danyal Aftab
- Anas Zafar
- Assadig Abakr
- Steven Davy
affiliations:
- Technological University Dublin
- National University of Computer and Emerging Science
arxiv_id: '2611.11013'
url: https://arxiv.org/abs/2611.11013
pdf_url: https://arxiv.org/pdf/2611.11013
published: '2026-11-07'
collected: '2026-11-10'
category: RecSys
direction: LLM增强CTR预测 · 模型轻量化
tags:
- CTR-Prediction
- Model-Pruning
- LoRA
- LLM4Rec
- Low-Latency-Serving
one_liner: 通过结构化剪枝压缩LLM+LoRA域感知微调，实现低延迟在线LLM增强CTR预测，精度保留超99%
practical_value: '- 可复用依赖感知结构化剪枝方案，将LLaMA3-8B剪至4.5B仅损失0.23% AUC，适合需要在线引入LLM语义能力的低延迟CTR场景，规避离线缓存的特征更新开销

  - 字段感知LoRA微调思路可直接迁移，仅训练注意力投影层的LoRA参数、冻结剪后LLM backbone，大幅降低域适配成本，同时保证语义嵌入质量

  - 语义引导特征融合模块可无缝接入现有CTR pipeline，用LLM字段嵌入重加权原有特征交互，无需改动现有CTR backbone架构，落地成本极低'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有LLM增强CTR方案依赖离线缓存LLM输出，无法适配电商/广告场景频繁更新的商品/特征库，且全量LLM在线推理延迟远高于实时推荐服务通常<20ms的要求，离线预计算也带来极高的存储和特征更新成本。
### 方法关键点
- 依赖感知结构化剪枝：基于Taylor展开计算注意力/FFN耦合参数组的重要性，剪去低价值单元，将LLaMA3-8B压缩44%得到4.5B backbone，保留语义表征能力
- 字段感知LoRA微调：设计字段分类prompt任务，仅更新注意力投影层的LoRA参数，让LLM输出高区分度的字段级语义嵌入，无需全量微调
- 语义引导特征融合：用LLM生成的字段嵌入相似度重加权原有CTR模型的pairwise特征交互，加入KL散度对齐两个嵌入空间分布，整体损失为BCE预测损失加对齐损失的加权和
### 关键实验
在4个公开CTR数据集（Amazon 3个品类+MovieLens-1M）、6个主流CTR backbone（FM、DeepFM、FwFM等）上测试，对比KAR、LLM-CF等SOTA LLM增强CTR方案：推理延迟降低2.7~3.4倍，单样本延迟控制在16~17.6ms，AUC保留全量LLM方案的99.77%，相对纯CTR backbone平均AUC提升0.13%~1.69%；剪枝到2B参数仍能保留99.62%的AUC。
### 核心结论
结构化剪枝不是单纯的工程优化，而是让LLM增强CTR方案从离线缓存走向在线实时服务的必要技术路径。
