---
title: 'SimpleSearch-VL: A Simple Recipe for Multimodal Agentic Deep Search'
title_zh: SimpleSearch-VL：高效轻量的多模态智能深度搜索框架
authors:
- Ming Dai
- Zhihong Lu
- Jinjie Gu
- Jiedong Zhuang
- Yefeng Liu
- Wankou Yang
- Jian Wang
- Chunhua Shen
affiliations:
- Southeast University
- Ant Group
arxiv_id: '2606.31504'
url: https://arxiv.org/abs/2606.31504
pdf_url: https://arxiv.org/pdf/2606.31504
published: '2026-06-30'
collected: '2026-07-01'
category: Agent
direction: 多模态搜索Agent 高效训练与推理优化
tags:
- Multimodal Agent
- Deep Search
- Reinforcement Learning
- Rollout Optimization
- Evidence Verification
one_liner: 仅用7K训练数据，通过三个轻量化设计实现性能追平闭源Gemini-3-Pro的多模态搜索Agent
practical_value: '- 训练侧可复用Factorized Adaptive Rollout（FAR）机制：优先给全错的难样本分配更多rollout额度，一旦出现正确样本就停止冗余采样，能降低RL训练的长尾等待耗时，提升小样本训练效率，尤其适合电商多模态搜推Agent的低成本迭代

  - 推理侧可复用缩略图证据校验逻辑：反向图搜返回结果时携带缩略图，让Agent先校验视觉匹配度再使用关联文本/URL信息，能减少电商场景下同款/相似款误判，提升多模态检索准确率

  - 工程上可落地网页自摘要方案：不用依赖外部独立的摘要模型，让搜索Agent自身根据查询目标生成网页摘要，减少服务依赖，同时适配Agent自身的信息需求，电商商品详情页信息抽取场景可直接复用

  - 小样本训练范式可参考：仅用5K SFT+2K RL数据就能实现基线15+分的提升，不需要大规模标注数据，适合中小团队快速迭代多模态搜索Agent能力'
score: 9
source: arxiv-cs.CV
depth: full_pdf
---

### 动机
现有多模态智能搜索Agent普遍面临三大落地瓶颈：RL训练阶段多轮工具调用导致rollout生成存在严重长尾耗时，训练效率极低；多模态检索结果（尤其是反向图搜）易出现视觉相似但内容不匹配的问题，输出可靠性不足；大多依赖外部网页摘要、工具编排等辅助组件，部署复杂度高、依赖多，难以轻量化落地。

### 方法关键点
- 提出**Factorized Adaptive Rollout（FAR）** 采样策略：将rollout预算拆分为prompt扩容和组内分配两个维度，仅对全错的难样本分配额外采样额度，一旦出现正确样本就停止冗余采样，同时设置99%采样完成阈值避免等待慢轨迹，大幅降低RL训练等待耗时
- 设计证据校验推理流程：反向图搜返回结果时同时携带缩略图、标题、URL，让Agent先校验视觉内容与查询的匹配度再使用关联信息，同时对工具调用结果做区域级缓存，减少重复调用成本
- 实现网页自摘要能力：无需调用外部独立摘要模型，由Agent自身根据查询目标提取网页相关信息生成摘要，减少服务依赖的同时提升摘要与Agent信息需求的适配性

### 关键实验结果
在MMSearch、LiveVQA、FVQA等6个多模态搜索基准上测试：对比原生Qwen3-VL Agent基线，8B/30B版本分别平均提升15.8/16.0分；8B版本性能超过多数开源30B规模多模态搜索Agent，30B-A3B版本性能追平闭源agentic Gemini-3-Pro；仅需5K监督轨迹+2K RL数据，8卡H200训练1天即可完成，训练数据量仅为同类方案的1/7。

### 核心结论
对于多模态搜索Agent，优化自身的搜索验证流程与训练采样效率，比单纯堆数据、堆模型规模、增加辅助组件的性价比高得多
