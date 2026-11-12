---
title: 'The Unused Input: The Initial State as a Conditioning Interface for Recurrent
  TSFMs'
title_zh: 利用循环时序基础模型初始状态作为条件输入接口
authors:
- Bernhard Voggenberger
- Christian Ganhör
- Levente Zólyomi
- Sebastian Böck
- Sepp Hochreiter
affiliations:
- NXAI GmbH, Linz, Austria
- Institute for Machine Learning, Johannes Kepler University, Linz, Austria
arxiv_id: '2611.14357'
url: https://arxiv.org/abs/2611.14357
pdf_url: https://arxiv.org/pdf/2611.14357
published: '2026-11-10'
collected: '2026-11-12'
category: Training
direction: 时序基础模型 · 零样本高效适配
tags:
- Time-Series-Foundation-Model
- xLSTM
- Zero-Shot-Forecasting
- Parameter-Efficient-Tuning
- LoRA
one_liner: 提出将循环时序基础模型的初始状态作为条件注入接口，冻结骨干即可提升零样本预测性能
practical_value: '- 电商用户行为时序、销量预测等场景用LSTM/循环类骨干时，可尝试将用户属性、商品标签等静态信息注入初始状态，无需微调骨干即可提效，参数量远低于LoRA

  - 时序类任务跨域零样本适配需求下，优先测试初始状态注入的适配方案，同参数量下效果优于LoRA，适配成本极低

  - 短上下文时序推理场景，可重点优化mLSTM模块的初始状态注入逻辑，收益更显著'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
循环架构的时序基础模型（TSFM）推理成本低、自带状态，但落地时默认仅用观测上下文窗口输入，初始状态完全未被利用，零样本跨域适配成本高。
### 方法关键点
以xLSTM架构的零样本预测器TiRex为案例，冻结骨干权重，仅训练小型头将条件向量写入初始状态，避免骨干权重适配对效果的干扰。设计两种注入方式：1）输入窗口的频谱摘要向量；2）时序关联的文本嵌入向量。
### 关键结果数字
频谱摘要注入将GiftEval数据集平均MASE降低0.175%，效果优于同参数量LoRA和可学习静态状态；静态初始状态适配在6个MoTime数据集上MASE比零样本基线低0.04-6.96%，达到全微调收益的8-70%；文本条件状态注入进一步在4个数据集上降0.15-0.41%，结合LoRA后在1个数据集上效果超过无文本输入的全微调。
