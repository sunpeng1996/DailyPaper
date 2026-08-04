---
title: 'SmartGR: Hierarchy and Beam-Aware Knowledge Distillation for Generative Recommendation'
title_zh: SmartGR：面向生成式推荐的层级与波束感知知识蒸馏框架
authors:
- Ziheng Zhang
- Yu Cui
- Bohao Wang
- Yong He
- Chao Yu
- Chuan Yuan
- Wujie Sun
- Can Wang
- Jiawei Chen
affiliations:
- Zhejiang University
- Ant Group
arxiv_id: '2608.02048'
url: https://arxiv.org/abs/2608.02048
pdf_url: https://arxiv.org/pdf/2608.02048
published: '2026-08-03'
collected: '2026-08-04'
category: GenRec
direction: 生成式推荐 · 知识蒸馏落地加速
tags:
- Generative Recommendation
- Knowledge Distillation
- Semantic ID
- Beam Search
- Model Compression
one_liner: 针对生成式推荐蒸馏的两个特有痛点，提出层级+波束感知框架，小模型提效8.6%且推理加速2.39倍
practical_value: '- 生成式推荐蒸馏无需对所有SID层级用统一权重，可复用本文的tanh单调层级映射策略，给更深的SID层级分配更高蒸馏权重，适配粗到细的语义分布差异

  - 对齐beam search过程的前缀排序时，无需复杂listwise监督，直接选取teacher正beam的相邻低排名beam作为硬负样本做pairwise蒸馏，既能降低高得分item被提前剪枝的概率，训练成本也更低

  - 无需修改学生模型架构，仅新增两个蒸馏损失即可实现小模型效果提升，完全保留小模型的推理效率，工程落地成本极低'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
生成式推荐（GR）依托Semantic ID架构可自然融合物品语义、适配大规模物品池，且模型越大效果越好，但8B模型推理延迟比1.7B高60%~90%，完全无法满足工业级低延迟要求。传统知识蒸馏方法未适配GR的两个特有痛点：一是SID层级越深，大模型相对小模型的效果优势越明显，统一蒸馏权重无法最大化知识迁移效率；二是beam search推理时中间前缀得分低会导致高最终得分的item被提前剪枝，仅对齐单步token分布无法解决该问题。
### 方法关键点
1. **层级感知SID蒸馏**：给不同SID层级分配可学习的单调递增权重（基于tanh的归一化映射），越深的层级蒸馏权重越高；仅蒸馏teacher beam与目标SID最长公共前缀的重叠位置，避免引入无效监督。
2. **波束感知排序蒸馏**：选取teacher beam中与目标SID前缀匹配最长的作为正beam，相邻排名更低的beam作为硬负样本，对齐每一步前缀累计得分的相对排序，减少高价值item被提前剪枝的概率。
### 关键结果
在Amazon Beauty/Toys、快手Ad/Video四个跨域数据集上，对比13种传统推荐/LLM/GR蒸馏基线：相比原始1.7B学生模型，效果平均提升8.6%，最高单指标提升17.5%，推理速度平均是8B teacher模型的2.39倍，16个评测指标中15个达到SOTA。
> 最值得记住：生成式推荐蒸馏无需改动模型架构，仅适配SID层级特性和beam search逻辑的轻量损失，就能同时拿到效果提升和推理加速。
