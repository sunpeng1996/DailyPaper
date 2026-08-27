---
title: 'Retrieve, Match, Escalate: Accurate and Scalable Product Linking with VLM-Distilled
  Cross-Encoders and Agentic VLMs'
title_zh: 检索-匹配-升级：基于VLM蒸馏交叉编码器与智能体VLM的高可扩展商品链接系统
authors:
- Jian Wang
- Steven Xu
- Sanjyot Thete
- Maryam Barouti
- Tom Tang
- Elaine Wu
- Charu Sareen
- Kyle MacDonald
affiliations:
- DoorDash Inc.
arxiv_id: '2608.25037'
url: https://arxiv.org/abs/2608.25037
pdf_url: https://arxiv.org/pdf/2608.25037
published: '2026-08-25'
collected: '2026-08-27'
category: RecSys
direction: 电商商品实体匹配 · 级联推理
tags:
- Product Linking
- Cross-Encoder
- Knowledge Distillation
- VLM Agent
- Entity Resolution
one_liner: 提出算力随难度动态分配的三级级联商品链接系统，兼顾高精度与大规模落地可行性
practical_value: '- 级联推理架构可直接复用：按模型置信度分档路由，轻量模型处理80%+简单case，仅难例路由到多模态Agent，降本效果显著，适合电商大流量的实体匹配、类目打标等场景

  - 无人工标注蒸馏方案可落地：用双VLM共识作为伪标签训练轻量交叉编码器，替代人工标注，标注规模直接提升130倍，同时保证标签一致性，适合缺少高质量标注的工业场景

  - Agent优化技巧可复用：限制工具调用轮次（文中设为4轮）、增加领域专属prompt约束（比如仅认可同零售商的搜索证据），能在几乎无精度损失的前提下大幅降低Agent推理成本与延迟

  - 检索阶段优化经验：文本+BM25+条码多通道融合召回，比单独多模态嵌入召回效果更稳定，图像通道在标准品匹配场景贡献极低，可按需裁剪降低检索成本'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
电商平台需要将商户上传的海量、多噪声、跨类目的SKU映射到标准品库，下游搜索、推荐、广告的效果高度依赖这一步的准确性。传统方案要么用单一模型对所有case打分，轻量模型解决不了难例，大模型全量推理成本不可接受，同时人工标注训练数据成本高、一致性差，无法支撑十亿级SKU的规模化处理。

### 方法关键点
- 三级级联架构：Stage1用文本+图像+条码多通道ANN检索召回Top20候选标准品；Stage2用150M参数的文本Cross-Encoder打分，按置信度分三档：高置信直接接受、低置信直接拒绝、中置信路由到Stage3；Stage3用带web搜索工具的多模态VLM智能体处理难例，可主动获取商品条码、品牌等外部证据。
- 无人工标注蒸馏：用双VLM对候选对的共识判断作为伪标签，仅保留两者一致的样本（占比87%），得到5.3M训练数据，替代40k人工标注，规模提升130倍。
- 智能体成本优化：用自托管开源MoE VLM（Qwen 3.6 35B-A3B）替代闭源前沿VLM，仅需少量领域prompt适配，限制工具调用最多4轮，大幅降低推理成本。

### 关键结果
- 召回阶段多通道融合在难例集上召回率达93.06%；Stage2交叉编码器在98%精度要求下自动处理68.1%的记录，仅剩余31.9%路由到Stage3；
- 级联方案整体覆盖度从68.1%提升到77.1%，开源智能体比闭源方案成本降低7倍，仅损失4个点的召回（88% vs 92%），精度保持98%不变；智能体比人工操作员准确率高13.7pp，召回高18.5pp。

**最值得记住的一句话**：对于工业级实体匹配任务，标注生成pipeline的投入回报率远高于模型结构搜索，按难度分配算力的级联架构是兼顾精度与成本的最优落地路径。
