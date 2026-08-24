---
title: 'Partition the Support, Reconstruct the Residual: Training-Free Sparse Attention
  for Video Generation and World Models'
title_zh: 分区支持域重构残差：面向视频生成与世界模型的免训练稀疏注意力
authors:
- Pardis Taghavi
- Reza Langari
- Gaurav Pandey
affiliations:
- Texas A&M University
arxiv_id: '2608.18484'
url: https://arxiv.org/abs/2608.18484
pdf_url: https://arxiv.org/pdf/2608.18484
published: '2026-08-18'
collected: '2026-08-24'
category: LLM
direction: LLM推理优化 · 免训练稀疏注意力
tags:
- Sparse-Attention
- Training-Free
- Inference-Optimization
- Transformer
- Video-Generation
one_liner: 提出免训练稀疏注意力方案SparsePR，保留生成质量的同时实现1.48x-2.61x端到端加速
practical_value: '- 免训练稀疏注意力思路可直接迁移到生成式推荐/Agent场景，无需微调即可降低长序列推理延迟，不损失生成效果

  - Response-Coupled Partitioning路由策略可复用在推荐长用户行为序列注意力计算优化，降低长序列召回/排序开销

  - Probe-Fitted残差校正方法可借鉴到RAG/多轮导购Agent场景的注意力近似误差修正，用小样本探针保证输出质量'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
视频生成/世界模型的长时空token序列导致self-attention二次复杂度成为推理瓶颈，现有免训练块稀疏注意力存在同路由query支持域重叠差、跳过交互的后softmax误差不可控问题。
### 方法关键点
提出SparsePR，核心包含两个模块：1）响应耦合分区：基于采样query的key响应构建K/V分组，用组质心生成query-响应坐标实现共享路由；2）探针适配残差重构：用少量精确计算的query行校准稀疏输出的仿射校正，抵消残差误差。
### 关键结果
在4种异构视频生成/世界模型上测试：保持生成质量不变，仅执行22.0%-26.0%的注意力pair，实现1.48x-2.61x端到端加速；探针拟合贡献主要误差降低，响应耦合分区可降低硬丢弃误差、提升有限探针预算下的重构效果
