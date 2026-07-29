---
title: 'Causal-TS: A Python Library for Causal Discovery in High-Dimensional and Nonstationary
  Time Series'
title_zh: Causal-TS：面向高维非平稳时间序列的因果发现Python库
authors:
- Mohammad Fesanghary
affiliations:
- Bloomberg LP
arxiv_id: '2607.24673'
url: https://arxiv.org/abs/2607.24673
pdf_url: https://arxiv.org/pdf/2607.24673
published: '2026-07-27'
collected: '2026-07-29'
category: Other
direction: 时序因果发现开源工具开发
tags:
- Causal Discovery
- Time Series
- GPU Acceleration
- Python Library
- Nonstationary
one_liner: 推出集成多算法、GPU加速的高维非平稳时序因果发现开源Python库Causal-TS
practical_value: '- 可直接调用Causal-TS对用户行为时序、交易时序、流量时序做因果发现，替代自研因果推断模块降低开发成本

  - 其分regime检测结构断裂的思路可复用在推荐系统时序特征建模中，适配用户行为/大盘流量的非平稳变化

  - GPU加速的条件独立性测试实现可复用在自研因果推断工具的性能优化环节，提升高维特征下的推理速度'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有因果发现工具未同时覆盖非平稳时序适配、GPU加速条件独立性（CI）测试、端到端因果效应估计全链路，高维时序场景下易用性、性能不足。

### 方法关键点
1. 统一架构集成CDNOTS、CDNOTS+、CEDAR、GRACE共4种专用因果发现算法，同时封装GES、Granger、LASSO-VAR等常用算法，底层共享基于PyTorch的GPU加速CI测试层；
2. 内置regime发现pipeline，支持插拔式变点检测器识别结构断裂，分regime适配参数做因果发现；
3. 配套CLI、合成数据生成器、DoWhy集成能力，支持从原始时序到因果效应估计的全流程。

### 关键结果
支持Python 3.10~3.12版本，可直接pip安装，代码开源在github.com/bloomberg/causal-ts。
