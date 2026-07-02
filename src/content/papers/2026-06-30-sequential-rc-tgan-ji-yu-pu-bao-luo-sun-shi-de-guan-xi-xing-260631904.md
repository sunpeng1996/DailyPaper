---
title: 'Sequential RC-TGAN: Generating Relational Time Series with Spectral Envelope
  Loss'
title_zh: Sequential RC-TGAN：基于谱包络损失的关系型时间序列生成方法
authors:
- Mohamed Gueye
- Yazid Attabi
- Manuel Morales
- Maxime Dumas
affiliations:
- Croesus Lab, Croesus, Laval, Québec, Canada
- Dept. of Mathematics and Statistics, University of Montreal, Montréal, Canada
arxiv_id: '2606.31904'
url: https://arxiv.org/abs/2606.31904
pdf_url: https://arxiv.org/pdf/2606.31904
published: '2026-06-30'
collected: '2026-07-02'
category: Other
direction: 关系型时序合成数据生成
tags:
- Time Series Generation
- GAN
- Spectral Envelope
- Synthetic Data
- Categorical Sequence
one_liner: 提出带谱包络可微损失的时序关系型GAN，优化时序周期性与季节性特征生成保真度
practical_value: '- 建模电商用户行为序列、交易时序等离散分类数据时，可引入谱包络损失作为正则项，提升时序周期性、季节性特征的建模效果

  - 处理GMV、用户活跃度等连续时序特征时，可先采用VGM离散化策略，再引入频域正则约束，优化长期趋势拟合效果

  - 评估时序生成类任务（如用户行为模拟、销量预测生成）效果时，可复用两个频域 divergence 指标衡量频域保真度'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
关系型时序合成数据生成（如交易日志、事件序列）场景中，独热编码等常规方法无法捕捉分类时序内在的季节性、周期性等频域特征，且缺乏频域维度的统一评估标准。
### 方法关键点
1. 提出时序扩展版RC-TGAN，新增基于谱包络理论的可微损失，支持通过反向传播直接优化生成数据的潜在周期结构保留效果
2. 采用VGM离散化策略，将频域正则能力扩展到连续时序场景
3. 提出Spectral Density Divergence、Spectral Envelope Divergence两个频域保真度评估指标，配套构造带理论真值的模拟基准数据集
### 关键结果
在真实数据集与模拟基准上，相比SOTA方法，在分类、连续特征的周期模式、长期季节性复现效果上实现显著提升。
