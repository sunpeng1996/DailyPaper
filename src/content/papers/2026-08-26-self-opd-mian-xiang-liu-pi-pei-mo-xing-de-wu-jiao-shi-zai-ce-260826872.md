---
title: 'Self-OPD: On-Policy Distillation for Flow Matching Models without Teacher'
title_zh: Self-OPD：面向流匹配模型的无教师在策略蒸馏框架
authors:
- Shiyi Zhang
- Mushui Liu
- Yunze Tong
- Wanggui He
- Siyu Zou
- Jinlong Liu
- Yunlong Yu
- Jian Song
- Hao Jiang
- Pipei Huang
affiliations:
- Tsinghua University
- Zhejiang University
- Alibaba Group
arxiv_id: '2608.26872'
url: https://arxiv.org/abs/2608.26872
pdf_url: https://arxiv.org/pdf/2608.26872
published: '2026-08-26'
collected: '2026-08-28'
category: Training
direction: 生成模型训练 · 无教师在策略蒸馏
tags:
- Flow Matching
- On-Policy Distillation
- Self-Alignment
- Multi-Objective Optimization
- LoRA
one_liner: 提出无教师流匹配在策略蒸馏框架，通过自探索分支奖励生成逐步监督信号，性能优于现有RL与有教师OPD方法
practical_value: '- 多目标优化场景可复用奖励层融合方案：先对各目标分数做z-score归一化再加权，仅用于候选排序不回传梯度，彻底避免CTR、CVR、用户满意度等多目标的梯度冲突问题

  - 生成式内容（商品图、营销文案）对齐调优可直接复用无教师蒸馏范式：无需额外训练高成本教师模型，通过K分支自探索+自参考基线生成逐步监督，训练效率较有教师方案提升2倍

  - RL排序/生成模型优化可复用方向感知衰减的正负样本利用策略：负样本仅在和最优方向相反时生效，大幅降低训练方差，避免梯度震荡

  - 垂类生成模型迭代可搭配LoRA使用该蒸馏方案，仅需微调小部分参数即可快速适配垂类需求，适合电商服饰、美妆等细分场景的商品生成模型快速迭代'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有流匹配模型下游对齐有两类方案：RL类仅用终端奖励做信用分配，梯度方差大、多目标优化不稳定；有教师OPD类需要为每个任务单独训练专属教师，计算成本高，且师生分布偏差会带来生成轨迹的误差累积，多目标融合时还存在梯度冲突问题，亟需低成本、稳定的无教师OPD方案。
### 方法关键点
- 自探索分支设计：每个时间步仅做1次Transformer前向得到确定性预测，叠加K个轻量SDE噪声生成候选分支，探索半径由噪声系数控制
- 自参考基线评估：每个分支通过ODE滚到最终生成结果，和当前模型确定性ODE生成的基线结果对比，计算归一化优势值
- 全分支推拉蒸馏：高优势分支拉速度场向优轨迹靠近，低优势分支经方向感知衰减后推速度场远离差轨迹，配合SDE方差归一化稳定训练
- 多目标奖励层融合：多个奖励先做z-score归一化再加权得到复合奖励，仅用于分支排序，不参与梯度回传，从根源避免梯度冲突
### 关键实验
以SD3.5-Medium为基座，用LoRA训练，对比Flow-GRPO等无教师RL方法、Flow-OPD等有教师OPD方法：单奖励场景OCR准确率达97.5%、GenEval strict分数0.95，较最优RL基线分别提升5pct、4pct；混合奖励场景无需教师，GenEval strict分数0.95、OCR准确率96.0%，较有教师的DiffusionOPD分别提升4pct、2pct，训练总时长较DiffusionOPD缩短50%。
### 核心结论
多目标对齐的核心矛盾不在参数空间的梯度妥协，而在轨迹空间的联合高优区域采样，奖励层融合能从根源避免梯度冲突。
