---
title: Parameter-Efficient Quantum-Inspired Fast Weight Programmers for Traffic-Matrix
  Forecasting
title_zh: 参数高效量子启发快速权重编程器用于流量矩阵预测
authors:
- Kuo-Chung Peng
- Jiun-Cheng Jiang
- Chun-Hua Lin
- Tai-Yue Li
- Nan-Yow Chen
- Samuel Yen-Chi Chen
affiliations:
- National Taiwan University
- National Center for High-Performance Computing, National Institutes of Applied Research
- Wells Fargo
arxiv_id: '2606.27821'
url: https://arxiv.org/abs/2606.27821
pdf_url: https://arxiv.org/pdf/2606.27821
published: '2026-06-25'
collected: '2026-07-05'
category: Other
direction: 序列建模 · 低资源时序预测
tags:
- Time Series Forecasting
- KAN
- Fast Weight Programming
- Parameter Efficient
- Sequence Modeling
one_liner: 提出量子启发KAN快速权重编程器，仅用大LSTM 22.4%参数量实现更优多步流量矩阵预测
practical_value: '- 电商/广告时序预测场景（如站点流量预判、广告库存预测、大促峰值预估）可尝试将KAN与快速权重编程框架结合，在低参数量约束下提升预测精度

  - 资源受限的在线预测场景可参考「经典慢编程器+量子启发快编程器」的异构架构设计，平衡推理效率、内存占用与预测效果

  - 训练预算有限的时序建模场景可优先测试量子启发的轻量化循环模型，无需盲目堆叠Transformer、扩散模块即可获得效果收益'
score: 4
source: huggingface-daily
depth: abstract
---

### 动机
网络流量矩阵（TM）预测是流量工程核心能力，在线网络控制场景下的预测需严格满足内存、更新速度、训练预算约束，现有基于图、Transformer、扩散模块的模型无法适配低资源要求。
### 方法关键点
适配门控量子启发Kolmogorov-Arnold网络快速权重编程器（QKAN-FWP）实现端到端多步TM预测，输入2小时历史数据即可输出未来20个5分钟粒度的144维OD矩阵预测结果；在固定训练预算下，对3种QKAN放置变体、同参数量LSTM、大参数量LSTM、经典门控快速权重编程器（G-FWP）基线做基准测试。
### 关键结果
G-QKANFWP取得最优 pooled RMSE，参数量仅为大LSTM的22.4%，效果优于同规模LSTM和经典G-FWP基线；量子启发变体的验证集损失学习曲线AULC低于同规模循环基线，在更多OD通道的预测任务上效果占优。
