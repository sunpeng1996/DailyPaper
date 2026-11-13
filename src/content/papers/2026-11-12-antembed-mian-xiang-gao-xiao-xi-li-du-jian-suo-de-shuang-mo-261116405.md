---
title: 'AntEmbed: Dual-Mode Multimodal Embedding Model for Efficient and Fine-Grained
  Retrieval'
title_zh: AntEmbed：面向高效细粒度检索的双模式多模态嵌入模型
authors:
- Kehang Jia
- Teng Liu
- Juntao Li
- Hua Chen
- Jinxiong Chang
- Xiaobo Liang
- Min Zhang
affiliations:
- Soochow University
- Ant Group
arxiv_id: '2611.16405'
url: https://arxiv.org/abs/2611.16405
pdf_url: https://arxiv.org/pdf/2611.16405
published: '2026-11-12'
collected: '2026-11-13'
category: RecSys
direction: 多模态检索 · 双模式嵌入对齐
tags:
- Multimodal Embedding
- Contrastive Learning
- Knowledge Distillation
- Chain-of-Thought
- Retrieval
one_liner: 提出双模式多模态嵌入模型，统一两类嵌入空间，兼顾低延迟与细粒度检索精度
practical_value: '- 电商多模态商品检索场景可复用双模式设计：日常流量用低延迟判别式嵌入承接，复杂细粒度查询（如「带蕾丝边的白色法式连衣裙」）调用生成式嵌入提升准确率，无需维护两套向量索引。

  - 多模态召回训练可借鉴confusion-aware CoT构造方法：用base检索模型捞取相似候选作为混淆集，引导模型学习商品细粒度区分特征，解决同款/相似商品匹配不准问题。

  - 可直接复用「多正例对比学习+跨模式自蒸馏」训练范式：仅需单embedding token即可对齐生成式与判别式表示，降低推理逻辑复杂度与向量存储成本。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有多模态检索方案中，判别式嵌入编码速度快但细粒度语义捕捉能力弱，带CoT推理的生成式嵌入匹配精度高但推理延迟大，两类方法表示空间相互独立需维护两套索引，无法同时满足大规模在线检索的低延迟要求与复杂查询的细粒度匹配要求。

### 方法关键点
- 构造confusion-aware CoT增强视图：用外部MLLM生成查询意图、候选与相似样本的区分性语义证据，将原始输入、CoT增强输入作为同一实例的两个语义等价视图。
- 第一阶段多正例对比学习：用单个预定义embedding token，将原始候选与CoT增强候选同时作为对应查询的正例，对齐两类视图的表示到统一嵌入空间。
- 第二阶段跨模式自蒸馏：以CoT增强分支为教师，通过候选相似度分布蒸馏+查询表示对齐，将推理获得的细粒度语义信息迁移到判别式嵌入，无需额外推理开销即可提升其语义建模能力。

### 关键结果
在MMEB-v2基准上，AntEmbed-8B的生成式嵌入总得分81.5，超出SOTA基线DME-9B 3.1个点；判别式嵌入总得分73.1，优于部分生成式基线；在包含Agent记忆检索、工具检索等场景的MMEB-v3基准上，AntEmbed-8B总得分55.6，位列所有对比模型第一。

值得记住的一句话：仅需单embedding token即可实现生成式与判别式嵌入的空间统一，用自蒸馏迁移推理信息，兼顾检索效率与精度。
