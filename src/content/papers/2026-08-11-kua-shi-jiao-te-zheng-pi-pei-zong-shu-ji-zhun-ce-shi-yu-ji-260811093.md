---
title: 'Cross-View Feature Matching: Survey, Benchmarking, and Foundation-Model Perspectives'
title_zh: 跨视角特征匹配：综述、基准测试与基础模型视角
authors:
- Songlin Du
- Xiaoyong Lu
- Zeyu Wu
- Xiaobo Lu
- Guobao Xiao
- Bin Fan
- Jiayi Ma
- Takeshi Ikenaga
arxiv_id: '2608.11093'
url: https://arxiv.org/abs/2608.11093
pdf_url: https://arxiv.org/pdf/2608.11093
published: '2026-08-11'
collected: '2026-08-12'
category: Other
direction: 跨视角特征匹配 · 视觉基础模型综述
tags:
- Cross-View Matching
- Vision Foundation Model
- Feature Matching
- Survey
- Benchmark
one_liner: 系统梳理跨视角特征匹配领域进展，构建统一分类体系与评测基准，指明VFM时代发展方向
practical_value: '- 跨域特征匹配的分类框架可迁移至多模态推荐的跨场景商品特征对齐任务，优化跨域召回准确率

  - 统一基准评测的设计逻辑可复用在推荐算法迭代的基线对比环节，规避不同实验设置带来的结果偏差

  - 通用匹配模型的设计思路可参考用于构建跨业务线的统一推荐匹配范式，降低多场景适配成本'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
跨视角特征匹配旨在建立大视角差异图像间的可靠对应关系，近年视觉基础模型（VFM）推动领域快速向通用匹配模型演进，但现有研究在问题定义、模型架构、训练范式、评测协议上差异极大，缺乏统一认知框架。

### 方法关键点
1. 构建结构化分类体系，覆盖特征提取、单/多类型特征匹配器、VFM基方法、训练策略、鲁棒估计五大模块，形成统一分析对比框架；
2. 梳理近年进展提炼核心设计原则，总结领域向统一通用匹配模型演进的核心趋势；
3. 采用一致评测协议对代表性SOTA方法开展统一基准测试，实现公平全面的性能对比；
4. 明确效率、极端条件鲁棒性、跨域泛化三大开放挑战与未来方向。

### 关键结果
无特定任务量化指标，输出了覆盖全领域的统一评测基准与系统化参考体系，可为VFM时代跨视图匹配研究提供完整参照。
