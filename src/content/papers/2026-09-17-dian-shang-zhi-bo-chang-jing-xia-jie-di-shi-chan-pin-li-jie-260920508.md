---
title: Grounded Product Understanding in Livestream Videos
title_zh: 电商直播场景下接地式产品理解基准与统一模型
authors:
- Xinyu Zhang
- Junjie Chen
- Jiawei Ge
- Qianlong Li
- Libin Ma
- Baokun Pan
- Yahui Luo
affiliations:
- Kuaishou Technology
- Institute of AI for Industries, Chinese Academy of Sciences
arxiv_id: '2609.20508'
url: https://arxiv.org/abs/2609.20508
pdf_url: https://arxiv.org/pdf/2609.20508
published: '2026-09-17'
collected: '2026-09-18'
category: RecSys
direction: 电商直播 · 多模态产品理解
tags:
- Multimodal Understanding
- E-commerce Livestream
- Product Retrieval
- Temporal Grounding
- Benchmark
- LLM4Rec
one_liner: 提出电商直播接地式产品理解基准GPUB与联合识别定位统一模型UniPro
practical_value: '- 直播电商多模态理解场景可复用ASR过滤方案：用视觉条件轻量话语选择器过滤闲聊、促销类无关ASR内容，降低冗余噪声，相比全量ASR可提升0.74%
  Pair mAP@0.3

  - 多任务联合建模可复用双路表示架构：共享多模态编码器分别输出全局产品对齐表示用于检索、时序结构化表示用于时段定位，避免单表示无法兼顾两类任务的性能损失

  - 细粒度产品识别任务可复用硬负例构造方法：用语义Embedding检索Top29相似产品作为硬负例构造候选集，贴合业务中区分相似款的真实场景，提升模型细粒度区分能力

  - 直播切片自动化业务可直接复用GPUB的Pair mAP、Joint Recall评估指标，避免单独测评检索和定位时的效果虚高问题'
score: 8
source: arxiv-cs.CV
depth: full_pdf
---

### 动机
现有电商直播产品理解相关任务将产品检索与时段定位拆分评估，无法验证识别出的产品与定位到的证据时段是否对应，导致模型在两个子任务单独测评表现优异，但在直播切片、产品导购等真实落地场景中效果虚高，同时缺乏覆盖多时段分散证据、细粒度相似品的大规模高质量基准，阻碍技术迭代。
### 方法关键点
- 基准GPUB：包含3000条直播样本、31831个细粒度时尚品目录、8975条质量校验的多时段证据标注，设置3个任务：子任务1产品检索（给定片段匹配全库商品）、子任务2产品时段定位（给定查询定位对应时段）、主任务接地式产品理解（无查询时联合识别候选集中目标产品+定位所有对应证据时段），提出Pair mAP、Joint Recall两类联合评估指标，避免拆分评估的偏差。
- 统一模型UniPro：基于Qwen3-VL-Embedding-2B搭建，首先用轻量视觉条件话语选择器过滤ASR中闲聊、促销等无关内容，共享多模态编码器输出两类适配表示：全局池化的产品对齐表示用于检索、时序锚定交叉注意力生成的结构化表示用于时段定位，三阶段训练优化对齐与定位能力。
### 关键实验
对比7款主流多模态大模型，通用模型在主任务上最高仅取得10.13% Pair mAP@0.3，UniPro将该指标提升至21.53%，Joint R@1@0.3达37.23%；产品检索全库R@1达33.47%，时段定位mAP@0.3达47.72%，所有指标均大幅领先基线。
### 核心结论
单独评测产品检索和时段定位的结果存在显著虚高，必须联合验证产品与对应证据时段的匹配关系，才能真实反映模型在直播电商产品理解场景的落地效果。
