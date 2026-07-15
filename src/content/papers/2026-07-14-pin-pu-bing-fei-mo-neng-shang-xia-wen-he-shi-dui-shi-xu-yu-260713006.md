---
title: 'The Spectrum Is Not Enough: When Context Helps Time-Series Forecasting'
title_zh: 频谱并非万能：上下文何时对时序预测生效
authors:
- Mert Onur Cakiroglu
- Mehmet Dalkilic
- Hasan Kurban
arxiv_id: '2607.13006'
url: https://arxiv.org/abs/2607.13006
pdf_url: https://arxiv.org/pdf/2607.13006
published: '2026-07-14'
collected: '2026-07-15'
category: Eval
direction: 时序预测 · 模型增益评估诊断
tags:
- Time-Series Forecasting
- Contextual Prediction
- Spectral Analysis
- Retrieval Augmentation
- Model Deployment
one_liner: 指出频谱指标无法判断时序预测引入上下文的增益，提出无标签诊断指标辅助部署决策
practical_value: '- 电商销量、流量等时序预测场景，不要仅用频谱可预测性指标判断是否需要引入RAG、长上下文窗口、预训练大模型，避免选型错误

  - 可复用文中提出的coverage deficit无标签诊断指标，快速判断当前业务时序数据加检索/长上下文/预训练模型的预期增益，降低AB测试成本

  - 低延迟要求的时序预测场景可优先选择长线性窗口方案，其效果稳定性优于检索增强方案，不受频谱相位扰动影响'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有基于功率谱的时序可预测性指标常被误用来判断引入上下文、长lookback、检索插件、预训练模型的增益，但两类问题本质不同：频谱指标对相位随机化不变，而检索、大模型带来的超二阶收益依赖相位信息，仅靠频谱无法判断这类增益。
### 方法关键点
1. 理论证明仅靠频谱指标无法判断超二阶结构的增益，提出无标签的coverage deficit诊断指标，核心项用模拟预测相对线性预测的增益衡量超频谱结构
2. 构造固定频谱和边缘分布的替代对照对做可控对比验证
### 关键结果
7个基准测试上，窗口检索的增益在替代对中从ECL中位数+33%跌到-35%（p<1e-40），而频谱指标完全不变；大模型增益拆分为留存的二阶部分和会消失的超线性边际；长线性窗口增益稳定留存。留一数据集验证下，结构项预测超频谱价值符号的效果显著优于传统频谱指标。
