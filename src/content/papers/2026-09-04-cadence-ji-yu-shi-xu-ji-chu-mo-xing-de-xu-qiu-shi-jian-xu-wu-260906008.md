---
title: 'Cadence: Error-Bounded Lossy Compression of Demand Time Series with a Time-Series
  Foundation Model'
title_zh: Cadence：基于时序基础模型的需求时间序列误差有界有损压缩
authors:
- Roberto Tacconelli
affiliations:
- Independent Researcher
arxiv_id: '2609.06008'
url: https://arxiv.org/abs/2609.06008
pdf_url: https://arxiv.org/pdf/2609.06008
published: '2026-09-04'
collected: '2026-09-09'
category: Other
direction: 时序基础模型 · 误差有界压缩
tags:
- Time-Series Compression
- Foundation Model
- Lossy Compression
- TimesFM
- Error-Bounded Coding
one_liner: 提出结合TimesFM-3的误差有界有损时序压缩器Cadence，在需求类时序上压缩率远优于传统方案
practical_value: '- 电商销量/流量/用户行为时序存储可复用该误差有界压缩逻辑，可控误差下降低存储成本，误差边界比常规降采样严格28~56倍

  - 结论可直接复用：大模型预测精度提升对时序无损压缩增益极低，无需投入资源研发基于大模型的时序无损压缩方案

  - 预训练时序大模型落地业务时，需注意跨batch size预测结果不一致问题，固定分组大小可保证结果可复现'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
时序数据存储成本高，传统压缩方案要么无损压缩收益极低，要么有损压缩误差不可控，需明确预训练时序大模型在压缩场景的价值边界。
### 方法关键点
1. 配对330M参数的Google TimesFM-3时序基础模型与自适应算术编码器，保证每个样本压缩恢复误差≤预设阈值τ；
2. 针对PyTorch下跨batch size预测结果无法完全对齐的问题，将分组大小与执行设备写入容器格式保证解压一致性；
3. 实现上下文建模的二值化自适应范围编码器，编码效率比通用xz/zstd高9.7%。
### 关键结果
在2026年电网需求、MTA客流两类训练集外的需求时序上，压缩率比最优传统预测器分别高13.3%、28.3%，297组序列-误差阈值对全部获胜；同等体积下最坏误差比时序数据库常用降采样方案小28~56倍；长时序端到端压缩收益渐近达15.1%，非需求类时序上无明显增益；大模型做无损压缩仅能带来0.03%的中位收益。
