---
title: 'Weaving Visual Narratives: Agentic Image Bundle Composition Beyond Atomic
  Visual Matching'
title_zh: 智能体驱动的图像束组合：构建超越原子匹配的视觉叙事
authors:
- Rong Shan
- Tianyi Xu
- Congmin Zheng
- Wenteng Chen
- Jiachen Zhu
- Junjie Wu
- Teng Wang
- Weiwen Liu
- Changwang Zhang
- Weinan Zhang
affiliations:
- Shanghai Jiao Tong University
- Shanghai Innovation Institute
- OPPO
arxiv_id: '2608.28695'
url: https://arxiv.org/abs/2608.28695
pdf_url: https://arxiv.org/pdf/2608.28695
published: '2026-08-26'
collected: '2026-09-01'
category: Agent
direction: Agent驱动多模态检索 图像束组合
tags:
- Agentic Retrieval
- Multimodal Retrieval
- Image Bundle Composition
- VLM
- Hypergraph Discovery
one_liner: 提出图像束组合新检索范式，配套开源基准与智能体框架，较SOTA基线F1提升27.5%
practical_value: '- 电商商品组合/搭配推荐场景可直接复用该框架逻辑：针对「海边度假全套装备」「生日宴布置全流程」这类需要多商品协同满足的查询，从单品池动态组合符合语义关联的成套结果，替代传统单粒度排序

  - 内容类产品（社区晒单、智能相册、消费账单叙事生成）中，可借鉴增量超边发现思路，基于用户历史内容自动生成符合时序/场景关联的视觉叙事集合，降低用户手动整理成本

  - 工程上可复用「多样种子初始化+上下文候选剪枝+自适应子查询生成+全束VLM重排」的组合类检索架构，有效解决组合爆炸问题，同时平衡单步匹配精度和整体语义一致性

  - 做组合类召回时可落地多样种子初始化trick：从初始召回结果中选择语义/特征差异最大的多个起始项并行搜索，避免陷入局部最优，提升召回结果的多样性和完整性'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
传统文本到图像检索采用原子级单图匹配范式，仅能返回独立打分的离散图像列表，无法满足用户查找连贯视觉叙事（如演唱会全程高光、景观从昼到夜变化、旅行路线节点）的需求：这类需求的目标是具备内在关联（时序、空间、事件）的图像束，其联合相关性无法通过单图得分聚合得到，且候选组合空间爆炸，传统方法完全无法适配。

### 方法关键点
- 提出Image Bundle Composition（IBC）全新检索范式，目标是从大规模无结构图像池中动态生成满足查询的连贯图像束，而非单图排序
- 开源IBCBench基准数据集：通过半自动化标注流水线（时空会话挖掘→VLM验证→人工标注）构建，包含109467张图像、667条验证查询，覆盖同地点动态、跨地点结构两类核心关联
- 提出BundleWeaver智能体框架：将IBC转化为查询条件下的增量超边发现任务，核心流程为：多样种子初始化锚定全局搜索空间，并行束搜索下LLM自适应生成子查询补全缺失的关联角色，最后用VLM做全束重排验证整体一致性

### 关键结果
在IBCBench上对比四类基线（多模态嵌入、文本嵌入+字幕、元数据启发式、VLM两阶段分解重排），BundleWeaver F1达30.28%，较最优基线（Claude Sonnet 4.5两阶段方案）提升27.5%，Exact Match提升380%；ablation验证所有核心组件均有正向贡献，且框架兼容任意VLM底座，替换不同开源/闭源VLM均稳定优于两阶段基线。

### 核心结论
未来检索系统需要从被动的点式排序器，进化为具备主动推理能力的构造器，实现 inline 关联内容组合。
