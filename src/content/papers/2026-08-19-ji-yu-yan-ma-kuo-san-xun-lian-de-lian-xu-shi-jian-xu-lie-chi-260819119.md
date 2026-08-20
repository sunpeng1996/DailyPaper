---
title: Discretizing Continuous Time Series for Imputation with Masked Diffusion Training
title_zh: 基于掩码扩散训练的连续时间序列离散化补全方法
authors:
- Dongbin Kim
- Seungyun Lee
- Geonwoo Shin
- Jaewook Lee
affiliations:
- Seoul National University
arxiv_id: '2608.19119'
url: https://arxiv.org/abs/2608.19119
pdf_url: https://arxiv.org/pdf/2608.19119
published: '2026-08-19'
collected: '2026-08-20'
category: Other
direction: 时序数据补全 · 掩码扩散建模
tags:
- Time Series Imputation
- Masked Diffusion
- Stochastic Discretization
- Representation Learning
- Generative Model
one_liner: 融合随机离散化的掩码扩散时序补全模型，解决缺失值表示混淆与扩散训练目标错配问题
practical_value: '- 电商用户行为序列、广告点击时序的缺失值补全场景可复用正交MASK表示设计，避免缺失值占位符引入伪相关性

  - 连续时序特征转序数感知Token的随机离散化方法，可迁移到生成式推荐的用户行为序列建模任务

  - 扩散模型直接预测原始信号而非噪声的训练范式，可优化时序类生成任务的收敛速度与效果'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有时间序列补全方法存在两个核心缺陷：一是缺失值与观测值共享同一表示空间，无明确结构区分，缺失位置的占位符易引入虚假相关性；二是连续扩散类方法的训练目标为预测额外添加的噪声而非原始信号，与补全任务目标不匹配。
### 方法关键点
1. 掩码扩散时序补全模型MDTIM采用与合法观测值结构正交的[MASK] token编码缺失位置，直接预测原始值，天然对齐补全任务的表示设计与学习目标；
2. 新增随机离散化模块，将连续时序值映射为保留序数信息的Token，同时保留原始连续动态特性，解决离散掩码扩散与连续时序属性的适配gap。
### 关键结果
在多类公开时序基准的各类缺失场景下，MDTIM鲁棒性与可扩展性均全面优于现有SOTA确定性、生成式补全基线。
