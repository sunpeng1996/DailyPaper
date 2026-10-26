---
title: 'MMVistaReason: Toward Open-Data and Post-Training Recipes for Multimodal Reasoning'
title_zh: MMVistaReason：面向多模态推理的开放数据与后训练方案
authors:
- Juekai Lin
- Honglin Lin
- Yuqian Yuan
- Xiaolong Wu
- Jie Cao
- Liang Liang
- Yunqi Cao
- Yun Zhu
- Wenqiao Zhang
- Lijun Wu
affiliations:
- 浙江大学
- 蚂蚁集团AFu团队
- 上海交通大学
- 同济大学
arxiv_id: '2610.01352'
url: https://arxiv.org/abs/2610.01352
pdf_url: https://arxiv.org/pdf/2610.01352
published: '2026-10-21'
collected: '2026-10-26'
category: Multimodal
direction: 多模态推理 · 开放数据与后训练优化
tags:
- Multimodal Reasoning
- SFT
- RL
- Knowledge Distillation
- Data Curation
one_liner: 提出覆盖分析+现实场景的多模态推理数据与训练方案，4B模型性能超越8B同类基线
practical_value: '- 电商多模态内容理解（商品图/短视频理解、广告素材审核）场景可复用其分阶段数据清洗+难度分层蒸馏方案：用小模型过滤简单样本，仅将难样本路由给大模型处理，可大幅降低大模型调用成本，同时提升训练数据质量

  - 构建场景化多模态Agent（如电商导购Agent、内容理解Agent）时可参考「先训练领域专属RL专家，再通过多教师on-policy蒸馏整合能力」的架构，避免多任务混合训练的负迁移问题，同时保留统一模型的通用性

  - SFT轨迹选择环节可直接复用Answer-Likelihood Best-of-N策略，相比随机选择或选择最长正确轨迹，可稳定提升微调效果，尤其适合小模型微调场景，无需额外标注成本

  - 训练多模态模型时优先匹配数据难度与模型容量：小模型用多难度混合数据集收益更高，大模型仅用适量中等难度样本即可达到全量数据效果，可大幅降低训练数据量'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前多模态推理模型后训练存在三大核心瓶颈：能力覆盖不均衡，过度侧重数学、科学等分析类任务，忽视现实场景感知、空间理解等能力；数据效率低，蒸馏成本高，未针对SFT、RL的不同数据需求做差异化设计；跨域干扰严重，多任务混合训练易出现负迁移，难以整合多场景互补能力。

### 方法关键点
- 数据构建：覆盖分析推理（数学、科学、图表推理等）、现实推理（视觉感知、空间理解、GUI交互等）两大互补场景，经分阶段清洗、难度感知级联教师蒸馏、Answer-Likelihood Best-of-N轨迹筛选，构建MVR-SFT-528K数据集；再基于SFT模型的rollout通过率筛选63K frontier样本，拆分到两大场景作为RL训练数据。
- 训练范式：采用「专项训练-能力整合」两阶段架构：先分别训练两大场景的RL专家模型，再通过Multi-Teacher On-Policy Distillation (MOPD) 将专家能力整合到统一通用模型，支持正向/反向KL两种训练目标。

### 关键结果
在15个多模态基准上测试：MVR-4B平均得分72.8，超越Qwen3.5-9B（Instruct）和MMFineReason-8B，SFT样本量较后者少70%；MVR-9B平均得分74.4，超越Qwen3.5-35B-A3B（Instruct），接近GPT-5.1水平。

### 核心结论
多模态推理性能提升的核心不是单纯堆叠模型参数或数据规模，而是要匹配监督难度与模型容量，通过专项能力训练+低干扰整合的范式实现高效优化。
