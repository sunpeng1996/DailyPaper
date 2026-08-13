---
title: 'GRASP: Granularity-Aware Region Alignment and Semantic Prototype Learning
  for Fine-Grained Cross-Modal Understanding in Drone Views'
title_zh: GRASP：面向无人机视角细粒度跨模态理解的粒度感知学习框架
authors:
- Jiahui Cui
- Yan Zhao
- Kan Wei
- Enze Zhu
- Peirong Zhang
- Lei Wang
- Yiru Wang
affiliations:
- Aerospace Information Research Institute, Chinese Academy of Sciences
- Key Laboratory of Target Cognition and Application Technology (TCAT)
- University of Chinese Academy of Sciences
- School of Electronic, Electrical and Communication Engineering, University of Chinese
  Academy of Sciences
arxiv_id: '2608.09270'
url: https://arxiv.org/abs/2608.09270
pdf_url: https://arxiv.org/pdf/2608.09270
published: '2026-08-10'
collected: '2026-08-13'
category: Multimodal
direction: 细粒度跨模态理解 · 图文匹配
tags:
- Cross-Modal Retrieval
- Fine-Grained Understanding
- Vision-Language Matching
- Prototype Learning
- Drone View
one_liner: 提出含区域对齐与语义扰动匹配双策略的GRASP框架，解决无人机视角细粒度跨模态理解的两大痛点
practical_value: '- 电商商品跨模态图文匹配（如图与标题/卖点匹配）场景，可复用RFA思路过滤商品图背景噪声，聚焦商品本身提升匹配准确率

  - 处理同品类细粒度商品区分需求时，可借鉴SPEM方案，基于提纯的商品语义原型构造难负样本，增强模型对细微属性差异的判别能力

  - 跨模态检索任务中可引入Semantic Prototype Codebook设计，降低同类样本歧义性，提升检索召回的精准度'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
无人机视角宽视野、俯视拍摄的特性带来两大跨模态理解瓶颈：宏观层面背景杂乱导致跨模态聚焦错位，模型优先匹配全局环境特征而非目标对象细节；微观层面视觉同构引发歧义，候选样本几何结构高度相似仅存在细微属性差异，现有方案难以适配细粒度匹配需求。
### 方法关键点
提出GRASP框架，通过两大协同策略增强判别能力：1. Region-Focused Alignment（RFA）：实现以对象为中心的跨模态对齐，抑制背景干扰；2. Semantic Perturbation Enhanced Matching（SPEM）：基于前景提纯的Semantic Prototype Codebook（SPC）构造语义扰动难负样本，强化细粒度语义区分能力。
### 关键结果
在GeoText-1652基准集与未见数据集ERA上取得SOTA级无人机视角细粒度图文检索性能
