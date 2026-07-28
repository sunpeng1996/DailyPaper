---
title: Rethinking Classifier-Free Guidance in On-Policy Diffusion Distillation
title_zh: 重探On-Policy扩散蒸馏中的无分类器引导机制
authors:
- Bingnan Li
- Haozhe Wang
- Haozhong Xiong
- Fangtai Wu
- Jinpeng Yu
- Yang Shi
- Jiaming Liu
- Ruihua Huang
affiliations:
- Qwen Business Unit of Alibaba
arxiv_id: '2607.24731'
url: https://arxiv.org/abs/2607.24731
pdf_url: https://arxiv.org/pdf/2607.24731
published: '2026-07-26'
collected: '2026-07-28'
category: Training
direction: 扩散模型蒸馏 · CFG优化
tags:
- Diffusion Model
- Classifier-Free Guidance
- On-Policy Distillation
- Knowledge Distillation
- Training Objective
one_liner: 提出分支感知的正方向匹配PDM目标，解决扩散CFG On-Policy蒸馏的负分支不对称失效问题
practical_value: '- 电商AIGC/生成式推荐场景下做扩散模型轻量化蒸馏时，若依赖CFG生成可控内容，可直接复用PDM目标，避免负分支信息不对称导致的蒸馏效果劣化

  - 大扩散教师模型蒸馏到端侧/小模型上线时，采用PDM可提升蒸馏后模型对CFG缩放系数的鲁棒性，无需针对小模型重新调优CFG参数

  - 若蒸馏时教师负条件分支包含学生无法获取的特权信息，优先采用分支独立约束的蒸馏目标，不要直接匹配CFG融合后的输出'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
On-Policy扩散蒸馏（OPD）是扩散模型轻量化落地的核心技术，但现有方法直接匹配CFG融合后的师生输出，存在正负分支误差相互抵消的欠定问题；当教师负分支包含学生无法获取的特权信息时，会触发负分支不对称（NBA）失效，正分支误差降低的同时负分支误差抬升，最终蒸馏效果劣化。
### 方法关键点
提出分支感知的正方向匹配（PDM）OPD目标，拆分为两个独立约束：1）单独对齐师生的正条件分支预测；2）对齐师生的CFG条件方向（正负分支预测的差值），从根源消除误差抵消的可能性。
### 关键结果
在稠密到稀疏视频控制任务上，原生OPD对CFG缩放系数高度敏感，PDM蒸馏后的模型在全CFG系数区间保持稳定效果，知识迁移鲁棒性与精度均显著优于基线。
