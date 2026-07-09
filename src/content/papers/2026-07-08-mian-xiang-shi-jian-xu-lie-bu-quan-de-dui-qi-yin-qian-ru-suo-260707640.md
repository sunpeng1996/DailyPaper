---
title: 'ALER-TI: Aligned Latent Embedding Retrieval for Time Series Imputation'
title_zh: 面向时间序列补全的对齐隐嵌入检索框架ALER-TI
authors:
- Xuan-Thong Truong
- Trung-Kien Le
- Tung Kieu
- Thi-Thu Nguyen
- Nhat-Hai Nguyen
affiliations:
- Hanoi University of Science and Technology
- Aalborg University
arxiv_id: '2607.07640'
url: https://arxiv.org/abs/2607.07640
pdf_url: https://arxiv.org/pdf/2607.07640
published: '2026-07-08'
collected: '2026-07-09'
category: Other
direction: 检索增强 · 时间序列缺失值补全
tags:
- Time Series Imputation
- Retrieval Augmented
- Latent Embedding Alignment
- Model Agnostic
- Representation Matching
one_liner: 提出带隐嵌入对齐的检索增强时序补全框架，兼容任意骨干，提升不同缺失率下的补全表现
practical_value: '- 处理电商用户行为/交易时序数据缺失时，可借鉴隐空间后掩码对齐方案，解决带缺失的查询序列与历史完整候选的表征mismatch问题

  - 检索增强模块可设计为模型无关的轻量化适配组件，无需重训原有骨干模型，大幅降低业务侧落地成本

  - 历史候选embedding可预计算缓存，在线检索时延可控，适合高并发的实时时序特征补全场景'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有深度学习时序补全方法仅依赖损坏输入的局部上下文，在非平稳、弱时序相关性、罕见模式的业务场景下，仅靠近邻观测难以重建缺失值，会大幅降低下游预测、推荐等任务的效果。

### 方法关键点
1. 提出检索增强框架ALER-TI，引入历史模式补充受损局部上下文，提升缺失值重建可靠性；
2. 核心为Latent Embedding Alignment (LEA)模块，在隐空间施加后掩码，对齐损坏查询与完整历史候选的表征，同时历史嵌入可预计算缓存，检索效率高；
3. 框架模型无关，通过轻量化适配模块可接入任意补全骨干。

### 关键结果
在6个真实数据集、多组缺失率配置下，ALER-TI可稳定提升各类强基线的补全精度，跨场景鲁棒性显著优于基线方案。
