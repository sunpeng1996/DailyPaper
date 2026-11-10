---
title: 'SepLRM: A Foundation Model Paradigm for Recommendation'
title_zh: SepLRM：面向推荐系统的大模型范式
authors:
- Di Chen
- Xijun Xiao
- Qin Ren
- Weijiang Lai
- Zhijian Pan
- Zhentao Pan
- Pengfei Nie
- Cheng Yuan
- Zixuan Tan
- Xuyang Liu
affiliations:
- ByteDance
- Institute of Software, Chinese Academy of Sciences
arxiv_id: '2611.10356'
url: https://arxiv.org/abs/2611.10356
pdf_url: https://arxiv.org/pdf/2611.10356
published: '2026-11-07'
collected: '2026-11-10'
category: RecSys
direction: 推荐大模型 · 序列编码跨场景复用
tags:
- LRM
- KV cache
- Recommendation Foundation Model
- Sequence Modeling
- ROI Optimization
one_liner: 将端到端LRM拆为共享RFM与垂直VM，通过KV缓存复用长序列编码，大幅提升推荐规模化ROI
practical_value: '- 架构拆分参考：可将长序列编码模块从各业务端到端LRM中抽离为共享RFM，通过KV缓存跨业务、跨推荐阶段（召回/预排/精排）复用编码能力，无需每个业务单独训练长序列模型，降本提效

  - 工程落地优化：可复用两个成熟方案：一是用INT8/INT4量化、低秩投影压缩KV缓存，几乎无损降低存储成本；二是在线上将KV缓存生成与召回/预排阶段并行，把长序列编码耗时从精排关键路径移除，不影响在线延迟

  - 跨场景迁移技巧：无需对齐不同业务的训练数据流，通过用户级KV缓存索引，可直接将高资源业务训练好的RFM能力迁移到小业务，小业务仅需训练轻量VM decoder即可快速拿到长序列建模收益

  - 迭代效率提升：RFM侧重升级序列建模能力（加长序列、加大encoder容量）即可覆盖所有下游VM的收益，无需每个业务重复迭代序列模块，加速全平台效果迭代'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有LRM靠堆序列长度、模型容量提升效果，但边际收益持续递减，且不同推荐阶段、业务场景的独立LRM重复编码用户行为，平台整体规模化ROI持续走低；现有推荐基础模型方案依赖粗粒度特征接口，能力转移损失大，无法保留长序列建模的全部收益。

### 方法关键点
- 架构拆分：将多套端到端LRM重构为1个共享RFM+多套独立VM，RFM负责通用长序列编码，输出与候选无关的KV缓存，VM基于KV缓存做候选相关的交叉注意力与预测
- 接口设计：以encoder最后一层输出作为共享KV缓存，保留细粒度行为信息，原生encoder-decoder结构对齐原有query-KV交互逻辑，能力转移损失极小
- 效率优化：支持KV缓存量化、低秩投影压缩，设计用户级缓存消除跨样本冗余；配套异步训练流水线、在线KV预计算与LG-Store分布式存储系统，降低读写overhead

### 关键实验
在抖音电商、短剧、KuaiRand-27K三个数据集上，对比SIM、TWIN、HSTU、LONGER、LLaTTE等baseline，SepLRM效果与同配置端到端LRM完全持平，转移率接近100%；在线A/B测试中，广告场景ADSS/ADVV提升1.961%/2.107%，电商GMV提升0.35%-4.81%，ROI分别是同规模端到端LRM的8.62倍、2.62倍。

> 最值得记住的一句话：推荐大模型规模化的核心瓶颈已经从单模型效果提升转向全平台能力复用的ROI优化，细粒度KV缓存是实现高保真跨模型、跨场景能力迁移的最优接口。
