---
title: 'UniRank: Benchmarking Ranking Models for Unified Sequential Modeling and Feature
  Interaction'
title_zh: UniRank：统一序列建模与特征交互的排序模型基准
authors:
- Honghao Li
- Xianquan Wang
- Zibin Zhang
- Yi Zhang
- Kangyi Lin
- Yiwen Zhang
affiliations:
- Anhui University
- University of Science and Technology of China
- Tencent Inc.
arxiv_id: '2607.19987'
url: https://arxiv.org/abs/2607.19987
pdf_url: https://arxiv.org/pdf/2607.19987
published: '2026-07-22'
collected: '2026-07-23'
category: RecSys
direction: 推荐系统·排序模型基准测试
tags:
- Ranking
- Sequential Recommendation
- CTR Prediction
- Benchmark
- Feature Interaction
one_liner: 开源统一排序模型基准，标准化训练评估流程，提供工业级性能优化工具链
practical_value: '- 工程优化可直接复用：DDP+torch.compile+BF16+SDPA的组合在H20 GPU上实现14.24倍训练加速、单卡峰值内存降低69.2%，适配长序列排序场景

  - 调优经验可直接迁移：统一排序模型默认选GeLU/SiLU作为注意力激活，AttGate作为通用增强模块，dense参数优先尝试SOAP/Muon/LaProp优化器

  - 架构选型参考：没有跨场景通用最优统一排序模型，电商场景优先尝试EST/HeMix，短视频场景优先尝试UltraHSTU/UniMixer，广告场景优先尝试TokenFormer'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前工业界统一序列建模与特征交互的排序模型迭代快，但大量进展依赖私有数据、闭源实现和专属算力，现有开源基准不支持工业级长序列、时序数据切分、多反馈任务统一评估，导致模型复现难、对比不公平，学术与工业落地的差距持续拉大。
### 方法关键点
- 数据协议：覆盖短视频、广告、电商5个公开大规模数据集，最大数据集超7亿样本，最长行为序列超10万次交互；采用全局时序切分（8:1:1）避免未来信息泄露，使用逐点自回归监督范式，支持多反馈任务联合训练
- 工程优化：提供PyTorch原生工具链，集成DDP分布式训练、算子编译、BF16混合精度、FlashAttention/FlexAttention适配、激活重计算等能力，降低训练硬件门槛
- 评估标准：统一数据预处理、任务/指标定义、模型容量对齐、训练流程、效率优化6大复现要求，覆盖15种主流堆叠式/分层式统一排序模型
### 关键结果
- 全优化组合在H20 GPU上实现单卡训练提速5.97倍、4卡提速14.24倍，单卡峰值内存降低69.2%
- 测试显示无跨场景通用最优模型：堆叠式和分层式范式各有优劣，同一场景下不同任务的最优模型也存在差异
- 调优实验验证GeLU/SiLU作为注意力激活、AttGate注意力门控模块可跨场景稳定提升AUC

**最值得记住的结论**：统一排序模型不存在通用银弹，架构选型和调优必须结合业务场景的数据分布特性才能取得最优效果
