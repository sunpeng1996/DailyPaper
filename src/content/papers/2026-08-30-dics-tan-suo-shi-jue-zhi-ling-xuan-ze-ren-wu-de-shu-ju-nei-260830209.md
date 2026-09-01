---
title: 'DICS: Exploring Data Intrinsic Consistency for Visual Instruction Selection'
title_zh: DICS：探索视觉指令选择任务的数据内在一致性
authors:
- Yuyang Hong
- Jinhui Guo
- Jiaqi Gu
- Lubin Fan
- Ruixiang Wang
- Kun Ding
- Yue Wu
- Shiming Xiang
- Jieping Ye
affiliations:
- School of Artificial Intelligence, University of Chinese Academy of Sciences
- MAIS, Institute of Automation, Chinese Academy of Sciences
- Alibaba Token Hub, Alibaba Group
arxiv_id: '2608.30209'
url: https://arxiv.org/abs/2608.30209
pdf_url: https://arxiv.org/pdf/2608.30209
published: '2026-08-30'
collected: '2026-09-01'
category: Multimodal
direction: 多模态大模型 · 指令微调数据筛选
tags:
- VLM
- Instruction Tuning
- Data Selection
- Multimodal Alignment
- Training Efficiency
one_liner: 提出基于样本内在一致性的VLM指令数据筛选方法，仅用25%数据即超过全量微调效果
practical_value: '- 电商多模态商品素材生成、图文理解的指令微调场景，可复用VIC+RIC双维度指标筛选低质量训练样本，降低75%训练成本的同时保证效果

  - 电商多模态Agent、搜推多模态召回的VLM微调阶段，可直接复用DICS框架在固定数据预算下平衡样本质量与分布多样性

  - 涉及多模态指令微调的业务场景，可直接复用开源DICS代码快速实现高效数据筛选，也可基于6M规模DICS-6M语料优化自有模型'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
VLM视觉指令微调是提升多模态对齐、指令跟随能力的核心，但现有数据筛选方法仅关注分布多样性或启发式过滤，忽略单样本内部组件一致性，导致训练效率低、海量数据下效果提升有限，固定比例下选最优数据子集是核心瓶颈。

### 方法关键点
提出样本级自评分指标DIC量化样本内多组件一致性：1. VIC模块评估视觉内容与指令的对齐程度；2. RIC模块评估回复与指令的一致性。基于DIC构建自适应选择方法DICS，可在不同数据预算下最优平衡高内样本一致性与全局分布多样性。

### 关键结果
仅用25%的LLaVA-1.5-665K数据微调，效果超过全量数据微调；仅用不到25%的InternVL3-8B-Instruct训练数据，即可达到官方94.52%的效果；开源6M规模多模态指令语料库DICS-6M，为当前最大规模视觉指令选择研究数据集。
