---
title: 'Kalman Delta Networks: Uncertainty-aware Associative Memory'
title_zh: 卡尔曼增量网络：感知不确定性的关联记忆模型
authors:
- Ngoc Bui
- Tinglin Huang
- Rex Ying
affiliations:
- Yale University
arxiv_id: '2609.07816'
url: https://arxiv.org/abs/2609.07816
pdf_url: https://arxiv.org/pdf/2609.07816
published: '2026-09-06'
collected: '2026-09-09'
category: LLM
direction: LLM 线性注意力架构优化
tags:
- Linear Attention
- Kalman Filter
- Associative Memory
- Long Context
- State Space Model
one_liner: 将Delta规则关联记忆与卡尔曼滤波结合，提出两种低开销感知不确定性的线性注意力结构，性能超SOTA
practical_value: '- 长上下文Agent的记忆模块可复用KDN的不确定性加权更新逻辑：对已验证的高置信度记忆降低覆写权重，对新的低置信度信息灵活更新，有效减少事实幻觉

  - 推荐系统的用户长短期兴趣建模可借鉴Isotropic KDN的轻量方案：用O(1)额外状态跟踪兴趣置信度，替代固定权重的兴趣衰减策略，提升长周期兴趣召回准确率

  - 电商搜索的长序列Query理解建模可替换原线性注意力层为KDN：在保持线性推理速度的同时提升长上下文检索准确率，1.3B规模下RULER多键检索准确率比KDA高8%以上'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有线性注意力的Delta系列循环记忆模型依赖当前token预测的固定写入权重，无法跟踪历史记忆的置信度，易出现保留陈旧信息或误删有效记忆的问题，长上下文性能受限；而精确卡尔曼滤波的Riccati递归不兼容GPU并行扫描，无法支撑大模型规模化训练。

### 方法关键点
- 将循环关联记忆建模为线性高斯状态空间模型，推导证明DeltaNet、Gated DeltaNet、KDA等模型本质是卡尔曼滤波的固定增益特例，缺失不确定性跟踪环节
- 提出两种GPU扫描兼容的近似方案：Diagonal KDN用对角高斯假设+在线变分推理跟踪每个key通道的不确定性，单头额外开销O(dk)；Isotropic KDN用各向同性假设跟踪单标量不确定性，单头额外开销仅O(1)
- 引入信息缩放因子μ修正反向KL变分推理导致的模型过度自信问题，避免可靠记忆被意外覆写

### 关键结果
在750M参数/50B token、1.3B参数/100B token两个尺度预训练，对比KDA、Mamba-3、GDN-2等SOTA线性注意力模型：1.3B尺度下Diagonal KDN的LAMBADA困惑度低至9.75，6项零样本任务平均准确率达60.45%，优于KDA的60.28%；RULER多键长上下文检索准确率比KDA高8.6%，同时保持线性推理速度。

### 核心结论
在循环线性注意力中引入显式不确定性跟踪，仅需极少量额外开销就能同时提升长上下文建模能力和推理效率。
