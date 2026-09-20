---
title: Recursive Quantum Long Short-Term Memory for Stable Short-Horizon Temperature
  Forecasting
title_zh: 递归量子长短期记忆网络用于稳定短周期温度预测
authors:
- Mu-En Lee
- Yen-Ku Liu
- Samuel Yen-Chi Chen
- Yun-Cheng Tsai
affiliations:
- University of Toronto
- National Yang Ming Chiao Tung University
- Brookhaven National Laboratory
- PecuLab LLC
arxiv_id: '2609.20594'
url: https://arxiv.org/abs/2609.20594
pdf_url: https://arxiv.org/pdf/2609.20594
published: '2026-09-17'
collected: '2026-09-20'
category: Other
direction: 量子机器学习 · 时序预测
tags:
- QLSTM
- TimeSeriesForecasting
- QuantumML
- VariationalQuantumCircuits
- RecursiveStructure
one_liner: 提出递归QLSTM架构，提升短周期时序预测的收敛速度、精度与泛化稳定性
practical_value: '- 电商场景的销量、流量等时序预测任务，可借鉴递归特征变换思路，降低不同初始化下的结果波动

  - 对需要快速收敛的线上时序预估模型，可参考递归结构设计减少训练迭代轮次

  - 量子LSTM当前距推荐广告场景工业落地尚远，暂不建议投入大量资源复现'
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
标准QLSTM结合变分量子电路实现时序建模，但受随机初始化、时序上下文影响大，优化稳定性差，短周期预测效果波动高。
### 方法关键点
1. 设计递归QLSTM架构，将递归量子特征变换嵌入传统QLSTM结构，适配NISQ硬件的轻量化混合量子-经典时序建模需求
2. 控制训练参数完全一致，在多伦多日气温数据集上，对比8/16/32天三种输入窗口、20组随机种子下的模型表现
### 关键结果
递归QLSTM更早收敛到接近最优的测试损失，MAE、RMSE均低于标准QLSTM，泛化gap更小，不同种子下的预测稳定性大幅提升
