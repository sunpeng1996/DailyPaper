---
title: 'KL-MOPD: Discrepancy-Aware Multi-Objective On-Policy Distillation for Generative
  Recommendation'
title_zh: KL-MOPD：面向生成式推荐的差异感知多目标同策略蒸馏
authors:
- Weiqin Yang
- Yandong Wang
- Yuan Gao
- Hao Deng
- Jinxin Hu
- Jing Cao
- Jiawei Chen
affiliations:
- Zhejiang University
- Alibaba Group
arxiv_id: '2610.36973'
url: https://arxiv.org/abs/2610.36973
pdf_url: https://arxiv.org/pdf/2610.36973
published: '2026-10-27'
collected: '2026-10-28'
category: GenRec
direction: 生成式推荐 · 多目标蒸馏优化
tags:
- Generative Recommendation
- Multi-Objective Optimization
- On-Policy Distillation
- Knowledge Distillation
- E-commerce Advertising
one_liner: 基于token级初始KL差异动态分配教师权重，解决生成式推荐多目标蒸馏的能力不平衡问题
practical_value: '- 多目标生成式推荐场景可直接复用token级权重分配trick：预计算初始学生与各单目标教师的token-wise KL，按KL比例分配蒸馏权重，无需修改模型架构，训练开销可忽略

  - 替代传统静态加权、帕累托梯度调整方案，解决多目标优化的阶段不平衡问题（如前序token偏向CTR、后序token偏向CVR），兼顾精度和训练效率

  - 电商广告多目标（CTR/CVR/GMV）生成召回/排序场景，可先训练单目标专家模型再用KL-MOPD蒸馏，实测可获得1~2%的营收和GMV提升'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
生成式推荐（GR）通过逐token自回归生成item，需每一步解码准确才能召回正样本；传统多目标推荐方法仅做item级对齐，缺少token级细粒度监督，而vanilla多目标同策略蒸馏（MOPD）存在两个核心问题：① 每个token上不同教师的蒸馏难度不平衡，学生偏向拟合分布更近的教师；② 难蒸馏的教师随token位置动态变化，导致各目标在部分解码步拟合不足，最终正样本召回效果差。

### 方法关键点
- 预计算初始学生与各单目标教师在每个token位置的期望KL divergence，作为该教师在对应token的蒸馏难度量化指标
- 每个token的教师权重按其蒸馏难度归一化分配，难度越高权重越大，针对性强化难拟合目标的监督信号
- 权重仅需预计算一次，无需修改GR模型架构，训练无额外前向传播开销，完全兼容现有生成式推荐 pipeline

### 关键结果
- 3个公开数据集上对比8个SOTA基线，单目标指标平均提升4.91%，加性联合目标平均提升4.12%
- 阿里电商广告10亿级工业数据集上，离线联合指标提升3.19%；线上10%流量A/B测试，广告营收提升1.63%，GMV提升2.20%

**最值得记住的一句话**：生成式推荐的多目标优化核心矛盾不在item级，而在逐token解码的细粒度能力平衡，基于初始分布差异的动态加权是低成本高收益的解决方案。
