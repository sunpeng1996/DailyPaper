---
title: Decoupled Temporal Encoding for Generative Recommendation
title_zh: 面向生成式推荐的解耦时序编码框架
authors:
- Pengfei Jia
- Jingjian Wang
- Jingmao Li
- Ge Zhang
- Feng Shi
affiliations:
- Rajax Network Technology (Alibaba Taobao Shangou)
- Yale School of Public Health
arxiv_id: '2608.16274'
url: https://arxiv.org/abs/2608.16274
pdf_url: https://arxiv.org/pdf/2608.16274
published: '2026-08-17'
collected: '2026-08-18'
category: GenRec
direction: 生成式推荐 · 时序位置编码优化
tags:
- Generative Recommendation
- Temporal Encoding
- Sequential Recommendation
- CTR Prediction
- Transformer
one_liner: 提出解耦宏观时序与微观序列的轻量编码框架，在淘宝即时零售广告获+1.8%CTR +3%RPM
practical_value: '- 可直接复用DTE双模块设计替换现有Transformer推荐的位置编码，新增参数仅238个，latency overhead<1%，适配严格的线上性能要求

  - 宏观时序模块的4种时序原语可按需裁剪：近因衰减、日内/周内周期性为通用组件，流量波动项仅在大促频繁的场景启用即可

  - 微观模块的时间门控机制可复用在密集交互序列建模场景，仅当交互时间差小于阈值时引入相对顺序偏差，避免无效计算'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
生成式推荐常用的位置编码多继承自NLP，仅建模离散序列顺序，而电商/即时零售场景用户行为存在多层级时序规律（近因效应、饭点高峰、周内周末偏好差异、大促流量突增），现有方法多将异构时序信号塞到单一表示中，无法区分全局时序动态和局部顺序线索，还容易带来参数、latency过高的问题，难以适配工业级部署要求。

### 方法关键点
- 宏观时序模块：将近因衰减、日内周期性、周内周期性、流量波动4种时序原语通过用户自适应MLP权重融合为标量信号，映射后加到item embedding中，无需大体积的时间间隔嵌入表，参数极轻
- 微观序列模块：在self-attention层加入时间门控的相对顺序偏差，仅当两个交互的时间差小于可学习阈值时激活顺序偏差，解决密集交互下时间戳区分度不足的问题

### 关键实验
数据集覆盖淘宝闪购4亿用户25亿样本的工业数据集、公开KuaiRand1K数据集；对比baseline包括RoPE、ALiBi、BST、TiSASRec、生产基线BST+ALiBi；离线工业数据集GAUC达0.7098，较生产基线提升1.16个千分点，Logloss下降0.0011；线上A/B测试获得+1.8% CTR、+3.0% RPM，平均serving latency仅上涨0.3%，目前已全量上线淘宝闪购广告流量。

最值得记住的一句话：时序建模要区分全局上下文和局部顺序的不同作用，轻量解耦设计比统一表示更适配工业推荐的性能与效果平衡要求。
