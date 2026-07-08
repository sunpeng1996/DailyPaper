---
title: 'DynaKRAG: A Unified Framework for Learnable Evidence Control in Multi-Hop
  Retrieval-Augmented Generation'
title_zh: DynaKRAG：面向多跳RAG的可学习证据控制统一框架
authors:
- Yaqi Wu
- Xiaolei Guo
- Chenyu Zhou
- Jiaqi Huang
- Xianfa Zhang
- Junxu Zhang
- Zhuo Yu
- Zhubo Shi
- Jianghao Lin
- Dongdong Ge
affiliations:
- Shanghai Jiao Tong University
- Shanghai Aircraft Manufacturing Co., Ltd.
- Tongji University
arxiv_id: '2607.06507'
url: https://arxiv.org/abs/2607.06507
pdf_url: https://arxiv.org/pdf/2607.06507
published: '2026-07-07'
collected: '2026-07-08'
category: RAG
direction: 多跳RAG · 动态证据调度控制
tags:
- RAG
- Multi-Hop Reasoning
- Dynamic Control
- Evidence Acquisition
- LLM
one_liner: 将多跳RAG证据获取建模为状态条件原子操作控制，统一调度多类行为且跨LLM泛用
practical_value: '- 电商多轮搜索、客服问答类多跳RAG场景可复用原子操作+有效性过滤层的设计，替代硬编码流程，灵活适配不同用户query的证据获取需求

  - 控制器可采用轻量随机森林实现，仅需千级标注样本即可完成训练，且无需微调LLM、可跨生成模型迁移，大幅降低业务落地成本

  - 可复用sufficiency_check机制判断当前证据是否足够回答，提前终止检索，在低延迟要求的电商搜索/推荐场景下既能减少token消耗，也能避免冗余信息干扰生成效果

  - 证据收集完成后新增终端压缩步骤，提取目标相关片段再输入生成模型，适合商品文案生成、咨询问答等对生成准确率要求高的场景'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有多跳RAG多采用预定义固定流水线，无法根据当前证据状态动态选择检索、改写、终止等操作，既易产生冗余检索浪费token，也可能因操作错配导致证据不足，不同RAG策略的操作也无法在统一框架下对比优化。
### 方法关键点
- 把多跳RAG证据获取建模为状态驱动的序列决策过程，定义6种核心原子证据操作（继续检索、gap定向检索、query改写、桥接实体扩展、充分性检查、终止回答）+1种终端压缩操作，新增硬有效性层过滤当前状态下不可执行的动作
- 用轻量随机森林训练动作价值模型，基于召回文档数、检索分数、query-证据重叠度等可观测特征排序有效动作，训练标签仅需支持证据召回率变化，无需依赖答案标注
- 控制器可与底层检索、生成模块解耦，训练完成后可跨不同LLM直接迁移，无需针对目标模型重训
### 关键结果
在HotpotQA、2Wiki、MuSiQue三个多跳QA基准测试，基于Qwen2.5-7B-Instruct时F1分别达0.5998、0.5340、0.3061，相比最强基线提升2.88~7.19个点，token消耗降低13.1%~20.7%；替换为随机选择动作时F1下降3.96~5.78个点，单数据集仅需1000条训练样本即可完成控制器训练。
> 最值得记住的结论：多跳RAG的性能提升不依赖无限制增加检索次数，根据当前证据状态动态选择操作、合理终止才能兼顾效果和效率。
