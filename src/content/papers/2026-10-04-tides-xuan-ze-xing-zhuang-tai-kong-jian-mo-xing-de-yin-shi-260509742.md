---
title: 'TIDES: Implicit Time-Awareness in Selective State Space Models'
title_zh: TIDES：选择性状态空间模型的隐式时间感知优化方法
authors:
- Taylan Soydan
- Miguel A. Bessa
- Dirk Mohr
- Rui Barreira
affiliations:
- AIMM, ETH Zürich
- Brown University
- Inspire AG
arxiv_id: '2605.09742'
url: https://arxiv.org/abs/2605.09742
pdf_url: https://arxiv.org/pdf/2605.09742
published: '2026-10-04'
collected: '2026-10-08'
category: Training
direction: SSM结构优化 · 不规则时间序列处理
tags:
- SSM
- Mamba
- Irregular Time Series
- Model Architecture
- Sequence Modeling
one_liner: 提出兼顾不规则时间序列处理与逐token表达能力的选择性SSM变体TIDES，性能优于现有SOTA架构
practical_value: '- 电商用户行为序列多为不规则采样，可将TIDES替换现有序列建模的Mamba/Transformer模块，提升用户行为表征精度

  - 可复用「将输入依赖从步长转移到对角状态矩阵」的trick，适配需要保留真实物理时间间隔信息的序列建模场景

  - 可复用Fading Flash基准的设计思路，构建业务专属的序列模型诊断工具，测试模型对时间间隔OOD数据的泛化能力'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有选择性SSM（如Mamba）将时间离散化步长设为输入相关可学习参数，无法匹配真实物理时间间隔，不适配不规则时间序列；连续时间SSM（如S5）保留真实步长但动态为线性时不变，逐token表达能力不足。
### 方法关键点
提出TIDES选择性SSM变体，将输入依赖从步长转移到对角状态矩阵，既保证步长等于真实物理时间间隔，又保留选择性SSM的逐token表达能力；同时构造Fading Flash诊断基准，可同时测试序列模型的输入依赖性和对分布外时间间隔的外推能力。
### 关键结果
UEA时间序列分类、Physiome ODE回归基准上取得最优平均排名；在天文、农业、神经传感等领域8个原生不规则数据集上，6个超过或持平基准SOTA。
