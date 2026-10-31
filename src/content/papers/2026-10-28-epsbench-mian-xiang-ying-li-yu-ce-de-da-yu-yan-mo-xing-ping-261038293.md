---
title: 'EPSBench: Benchmarking LLM Agents for Earnings Forecasting'
title_zh: EPSBench：面向盈利预测的大语言模型Agent测评基准
authors:
- Yanbin Yin
- Chuyu Xu
- Liqin Ye
- Jing Peng
- Chao Zhang
affiliations:
- Georgia Institute of Technology
arxiv_id: '2610.38293'
url: https://arxiv.org/abs/2610.38293
pdf_url: https://arxiv.org/pdf/2610.38293
published: '2026-10-28'
collected: '2026-10-31'
category: Agent
direction: Agent 预测任务基准测评
tags:
- LLM Agent
- Benchmark
- Forecasting
- Evaluation
- Financial NLP
one_liner: 推出含149个企业季度样本的EPSBench基准，可统一测评LLM Agent的季度盈利预测能力
practical_value: '- 做数值预测类Agent时，可借鉴「先拆解预测维度、再用统一计算器转换为最终结果」的架构，避免黑箱预测误差不可追溯

  - Agent多模型测评时，可复用「点预测误差对比行业共识、预测区间覆盖率校验置信度」的双维度评估范式

  - 预测类任务的误差归因可借鉴逐层回溯拆解思路，定位核心误差来源模块，快速优化迭代'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
季度盈利预测需要Agent整合多源异构证据、关联财报指标完成数值推算，现有Agent测评基准缺乏针对结构化数值预测、可解释性溯源的专用数据集。
### 方法关键点
1. 构建EPSBench基准，覆盖86家美国企业的149个企业季度样本，配套财报、电话会议纪要、新闻三类固定证据集；
2. 测评流程要求Agent先估算各财报驱动因子并标注证据来源，再通过统一会计计算器转换为GAAP摊薄每股收益（EPS），消除计算逻辑差异的干扰；
3. 从点预测误差、80%预测区间覆盖率两个维度对比6款模型与分析师共识的表现。
### 关键结果
3款模型点预测误差与分析师共识无统计差异，另3款误差更高；所有模型标称80%预测区间实际覆盖率仅37%-70%，误差主要来自营业收入估算偏差。
