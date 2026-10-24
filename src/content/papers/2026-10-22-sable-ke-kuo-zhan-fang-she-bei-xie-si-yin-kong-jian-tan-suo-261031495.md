---
title: 'SABLE: Scalable Affine Bayesian Latent-space Exploration'
title_zh: SABLE：可扩展仿射贝叶斯隐空间探索方法
authors:
- Erik Bodin
- Lisa Maria Kreusser
- Donney Fan
- Henry Moss
- Geoff Pleiss
- Nicolas Durrande
affiliations:
- Monumo
- University of British Columbia
- Lancaster University
- Vector Institute
arxiv_id: '2610.31495'
url: https://arxiv.org/abs/2610.31495
pdf_url: https://arxiv.org/pdf/2610.31495
published: '2026-10-22'
collected: '2026-10-24'
category: Training
direction: 高维隐空间 · 贝叶斯优化
tags:
- Bayesian Optimization
- Latent Space
- Sample Efficiency
- Low Latency
- Generative Model
one_liner: 面向高维隐空间有限预算场景提出低开销高样本效率的贝叶斯优化方法SABLE
practical_value: '- 生成式推荐/Agent的隐空间Semantic ID调优场景，可复用高低维分量拆分策略，用低维in-span部分做EI优化，大幅降低高维搜索算力开销

  - 小样本冷启动的参数寻优（如LoRA微调超参、RAG检索阈值、推荐排序权重），可复用其有限预算下样本高效优化逻辑，减少调参成本

  - 低延迟在线优化场景（如实时广告出价调整、推荐排序因子动态调优），可借鉴伪观测重压缩方案，将单次决策延迟控制在毫秒级'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
高维生成模型隐空间维度常达数千到数万，远高于评估预算，传统贝叶斯优化存在算力开销高、样本效率低的问题，无法适配有限预算下的隐空间探索需求。
### 方法关键点
1. 采用贝叶斯仿射替代模型做预测与采集，将查询拆分为维度≤N的in-span分量（用期望提升EI优化）和标量约束的off-span分量，规避维度灾难；
2. 用有限horizon调度off-span范数，解决原生仿射EI探索不足问题，无需限制在固定学习子空间搜索；
3. 引入伪观测重压缩机制，将重拟合开销控制在O(M²D+M³)。
### 关键结果
在合成基准与多类隐空间优化任务上样本效率优于基线，大预算下决策耗时降低数个数量级，单次参数推理、预测、采集决策延迟仅数十毫秒
