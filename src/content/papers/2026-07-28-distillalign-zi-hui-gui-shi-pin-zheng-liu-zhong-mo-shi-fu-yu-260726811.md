---
title: 'DistillAlign: Coordinating Mode Covering and Mode Seeking in Autoregressive
  Video Distillation'
title_zh: DistillAlign：自回归视频蒸馏中模式覆盖与模式搜索的协调方法
authors:
- Jiaxing Li
- Kai Zou
- Cindy Zhou
- Kaichen Huang
- Junyao Gao
- Zile Wang
- Yang Liu
- Bin Liu
- Bo An
- Yangguang Li
affiliations:
- Riemann Dynamics
- Nanyang Technological University
- Wellington College, UK
arxiv_id: '2607.26811'
url: https://arxiv.org/abs/2607.26811
pdf_url: https://arxiv.org/pdf/2607.26811
published: '2026-07-28'
collected: '2026-07-31'
category: Training
direction: 自回归模型蒸馏 · 分布对齐优化
tags:
- Knowledge Distillation
- Autoregressive Model
- Distribution Alignment
- Consistency Distillation
- Reverse KL
one_liner: 提出融合模式搜索与覆盖约束的自回归蒸馏框架，提升小模型生成质量、覆盖度与多样性
practical_value: '- 做生成式推荐/LLM小模型蒸馏时，不能只关注生成质量/准确率指标，需额外对齐教师模型的分布覆盖度，避免小模型仅拟合高频样本、长尾泛化能力差

  - 可将「反向KL模式搜索损失+一致性蒸馏覆盖约束」的组合思路迁移到生成式推荐的LoRA蒸馏/离线蒸馏流程，平衡推荐的准确率和多样性

  - 评估生成模型/生成式推荐效果时，补充隐空间的分布精度、覆盖度指标，规避常规业务指标掩盖的分布偏移问题'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有基于DMD的自回归蒸馏多阶段流程存在两个核心问题：一是初始化与DMD阶段目标分布解耦，仅用视觉类指标评估中间模型，忽略分布匹配度；二是DMD的反向KL损失自带模式搜索特性，训练后期会驱使学生模型向教师高概率区域收敛，损失覆盖度与多样性。
### 方法关键点
1. 设计共享隐空间的分布评估协议，量化师生分布的精度和覆盖度，暴露常规质量指标隐藏的分布差异；
2. 设计DistillAlign联合蒸馏框架，融合DMD的模式搜索目标与一致性蒸馏的模式覆盖约束，同时对齐初始化与DMD阶段的目标分布。
### 关键结果
仅用1.3B参数的Wan模型作为DMD教师蒸馏得到的学生模型，效果超过基于14B参数Wan优化的基线，同时显著提升生成质量、分布覆盖度与多样性。
