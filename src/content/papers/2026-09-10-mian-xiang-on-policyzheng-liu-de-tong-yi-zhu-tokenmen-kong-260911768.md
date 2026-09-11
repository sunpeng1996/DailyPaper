---
title: 'A Unified Per-Token Gating Family for On-Policy Distillation: FKL/RKL Mixing
  with Multi-Channel and Bias Coefficients'
title_zh: 面向On-Policy蒸馏的统一逐Token门控家族：多通道与偏置的FKL/RKL混合
authors:
- Suwan Wu
- Yumeng Lin
- Pengcheng Yuan
- Xiaolong Jiang
affiliations:
- Xiaohongshu Inc.
- Tianjin University
arxiv_id: '2609.11768'
url: https://arxiv.org/abs/2609.11768
pdf_url: https://arxiv.org/pdf/2609.11768
published: '2026-09-10'
collected: '2026-09-11'
category: Training
direction: 大模型知识蒸馏 · 逐Token动态门控
tags:
- Knowledge Distillation
- On-Policy Distillation
- Per-Token Gating
- FKL-RKL
- LLM Training
one_liner: 提出四参数逐Token门控框架，统一两类现有On-Policy蒸馏方法，可作为门控设计的统一分析坐标系
practical_value: '- 做电商/广告场景小模型蒸馏（如文案生成、query改写、短文本分类）时，可直接用该四系数门控框架替代固定λ或单信号门控，无需纠结EOPD/ToDi选型，做多通道网格搜索可获得0.5~1.7pp的精度提升

  - 蒸馏调参时可先做动态门控与静态KL比例的隔离实验：计算动态门控的平均λ训练对应静态基线，确认收益来自动态结构而非KL比例偏移，避免无效调参

  - 门控信号组合注意粒度匹配：sample级门控基底不要叠加token级gap信号会降分，短文本分类优先用sample级u(x)通道，长序列生成优先用token级h_t和gap信号

  - 蒸馏实验必须做多种子重复，单种子的效果估计会比真实值高1.5~3倍，上线前需验证多种子鲁棒性，避免被虚高结果误导'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有On-Policy蒸馏（OPD）的逐Token FKL/RKL门控方法（EOPD、ToDi）各固定单一信号和方向，无法直接横向对比，也未验证动态门控的真实收益是否来自平均KL比例的偏移，缺少统一的分析框架支撑门控设计选型。

### 方法关键点
- 提出四系数参数化门控公式 $\lambda_t = \sigma(a·h_t + b·u(x) + c + d·gap_t)$，其中 $h_t$ 为token级教师熵，$u(x)$ 为sample级prompt熵，$gap_t$ 为师生预测差异，$\lambda_t$ 为RKL损失权重，FKL权重为 $1-\lambda_t$
- 现有EOPD、ToDi可作为该框架的单通道1D约束特例，框架新增多通道组合、显式偏置两个自由度，严格覆盖两类现有方法的设计空间
- 设计隔离实验：对每个动态门控配置计算训练期间平均$\lambda_t$，训练对应静态比例基线，分离动态门控结构和平均KL比例的贡献

### 关键实验
- 数据集：TweetEval的emotion、hate、offensive三个短文本分类任务
- 配置：教师模型Qwen3-32B，学生模型Qwen3-4B，对比单通道约束基线、同平均KL比例静态基线
- 结果：36组可比实验中多通道配置赢过单通道约束33次，胜率91.7%；26组隔离实验中动态门控赢过同平均KL比例静态基线19次；三种子重复下平均收益0.5~1.7pp，方向一致但单组无统计显著性。

### 核心结论
逐Token动态门控的收益核心来自多信号的任务适配组合，而非单一信号的选择，且单种子实验的效果估计普遍偏乐观。
