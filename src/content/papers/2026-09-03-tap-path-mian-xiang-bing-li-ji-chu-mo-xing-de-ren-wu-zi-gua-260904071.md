---
title: 'TAP-Path: Task-Adaptive Structural and Token Pruning for Efficient and Trustworthy
  Pathology Foundation Models'
title_zh: TAP-Path：面向病理基础模型的任务自适应结构与Token剪枝框架
authors:
- Mehedi Hasan
- Ashfak Yeafi
- Md Khairul Islam
affiliations:
- Brac University
- Khulna University of Engineering & Technology
- Hobart and William Smith Colleges
arxiv_id: '2609.04071'
url: https://arxiv.org/abs/2609.04071
pdf_url: https://arxiv.org/pdf/2609.04071
published: '2026-09-03'
collected: '2026-09-06'
category: Training
direction: 大模型压缩 · 任务自适应剪枝
tags:
- Model Pruning
- Foundation Model
- Inference Optimization
- Model Compression
- Efficient AI
one_liner: 无需蒸馏直接对预训练大模型执行结构与Token剪枝，降本同时精度反超原模型
practical_value: '- 可借鉴「验证集驱动的Transformer block物理剪枝」思路，在LLM4Rec/Agent推理场景下，根据业务数据直接裁剪冗余层，无需额外蒸馏成本

  - 输入自适应Token剪枝+多深度特征恢复的组合方案，可复用到搜推场景的长序列用户行为/长Query输入压缩，降本同时保留核心语义信息

  - 任务自适应轻量化门控头设计，可用于多任务推荐/多Agent调用场景，降低下游任务头计算开销，同时适配不同任务分布'
score: 4
source: arxiv-cs.AI
depth: abstract
---

### 动机
大模型参数量动辄数亿，推理成本高，现有压缩方案多依赖蒸馏，额外引入训练成本，且难以适配下游特定任务的精度需求。
### 方法关键点
- 摒弃学生蒸馏范式，直接对预训练Virchow2编码器做重构
- 融合五大模块：验证集驱动Transformer块选择、冗余块物理删除、输入自适应Patch Token剪枝、多深度特征恢复、轻量化门控任务头
### 关键结果数字
最终保留24/32个Transformer块、70%的Patch Token，参数量降低24.96%、算力降低35.2%；32类病理基准测试准确率87.98%，超原全量Virchow2（86.89%）与UNI2-h（87.67%）；外部测试集准确率91.22%，同时保留优秀的故障检测能力与稀有类适配效果。
