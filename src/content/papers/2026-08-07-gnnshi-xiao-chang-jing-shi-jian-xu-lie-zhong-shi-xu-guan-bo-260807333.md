---
title: 'When GNNs Fail: Quantifying and Overcoming Temporal Correlation Volatility
  in Time Series'
title_zh: GNN失效场景：时间序列中时序关联波动性的量化与优化
authors:
- Chen Shao
- Yue Wang
- Zhenyi Zhu
- Zhanbo Huang
- Tobias Käfer
- Zonghan Wu
- Danai Koutra
affiliations:
- Karlsruhe Institute of Technology
- The Hong Kong University of Science and Technology
- East China Normal University
- University of Michigan
arxiv_id: '2608.07333'
url: https://arxiv.org/abs/2608.07333
pdf_url: https://arxiv.org/pdf/2608.07333
published: '2026-08-07'
collected: '2026-08-10'
category: Other
direction: 时序预测 · 动态图GNN架构优化
tags:
- GNN
- Time Series
- Dynamic Graph
- Temporal Forecasting
- Message Passing
one_liner: 提出时序关联波动性TCV度量与动态GNN层GLIDE，大幅提升多变量时序预测性能
practical_value: '- 电商用户行为、商品销量、广告转化等高波动时序场景，可先计算TCV度量判断是否适配GNN/Transformer类结构，避免无效调参

  - 动态图召回、用户兴趣建模场景，可复用GLIDE的路径消息传递+动静传播分离设计，提升动态拓扑下的模型鲁棒性

  - 流量预测、库存预估等时序任务，可直接引入开源GLIDE层替换现有GNN模块，最高有望获得45%的性能提升'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有基于静态图假设的GNN在多变量时序预测中表现优异，但当变量间时序关联随时间剧烈波动时性能退化严重，缺乏量化该波动的统一指标与适配动态拓扑的解决方案。
### 方法关键点
1. 提出模型无关的TCV（Temporal Correlation Volatility）度量，量化时序图拓扑的分布演化规律，验证TCV越高，GNN、Transformer等主流模型性能下降越明显，高TCV场景下甚至劣于无结构假设的简单基线；
2. 提出GLIDE动态GNN层，融合两个核心设计：基于路径的消息传递捕捉长程路径邻域信息，静态与动态传播分离通过局部静态近似识别最优动态模式，兼顾动态场景性能与静态场景鲁棒性。
### 关键结果数字
在合成与真实基准数据集上，GLIDE在动静态场景下平均性能提升最高达45.6%，最大单场景增益可达85.7%，代码已开源。
