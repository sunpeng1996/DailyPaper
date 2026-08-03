---
title: 'HierDoc: Hierarchical Page-to-Region Evidence Routing for Long-Document Visual
  Question Answering'
title_zh: HierDoc：面向长文档视觉问答的分层页到区域证据路由框架
authors:
- Rongjian Gu
- Wengang Zhou
- Junyu Xiong
- Yonghui Wang
- Bing Yin
- Bei Wang
- Houqiang Li
affiliations:
- University of Science and Technology of China
- iFLYTEK Research
- Anhui Transport Consulting & Design Institute Co. Ltd.
arxiv_id: '2607.29638'
url: https://arxiv.org/abs/2607.29638
pdf_url: https://arxiv.org/pdf/2607.29638
published: '2026-07-31'
collected: '2026-08-03'
category: Multimodal
direction: 多模态长文档理解 · 分层证据路由
tags:
- Multimodal-VQA
- Hierarchical-Routing
- GRPO
- Long-Document-Understanding
- Evidence-Retrieval
one_liner: 提出两阶段GRPO优化的分层页-区域证据路由框架，达成开源长文档VQA最优性能
practical_value: '- 电商多模态文档（商品详情页、物流单据、合规合同）的智能问答场景可直接复用分层路由架构：先做页级粗筛再做区域精排，相比全页输入token成本降低60%以上，同时精度更高

  - 用GRPO优化结构化集合选择的奖励设计可迁移到推荐召回、广告素材筛选场景：针对不同粒度任务设置召回、F1、格式的加权奖励，无需端到端训练即可快速提升选品/选素材的准确率

  - 分层路由的反射精简机制适合线上低延迟RAG场景：第一次选择后若结果超阈值触发二次精简，既保证证据召回率，又严格控制输入长度，平衡效果和耗时

  - 全局上下文+局部细粒度证据融合的思路可复用在长用户行为建模：保留全量行为的全局分布特征，同时提取高相关的局部行为细节，优于仅用短序列或全序列的方案'
score: 8
source: arxiv-cs.CV
depth: full_pdf
---

### 动机
现有长文档视觉问答方法要么聚焦页级检索忽略细粒度区域证据，要么区域选择依赖上游预先选好的页面，两级决策割裂，无法同时兼顾全局上下文感知和细粒度证据定位，易出现证据冗余、关键信息遗漏的问题，在长PDF、多页幻灯片、表格类文档上精度不足。
### 方法关键点
- 两阶段分层证据路由：第一阶段页策略将长文档拆分为固定窗口，用GRPO优化选相关页，奖励平衡召回率、F1、格式规范，选页超阈值时触发二次反射精简，降低冗余
- 第二阶段区域策略基于MinerU解析的语义区域（段落、表格、图片等）构建离散动作空间，同样用GRPO优化，奖励额外增加精度惩罚，避免输出无关区域
- 最终回答阶段同时输入选中的完整页面、区域裁剪图、对应OCR文本，既保留全局布局上下文，又突出局部高相关证据
### 关键结果
在MMLongBench-Doc、LongDocURL、SlideVQA等5个长文档VQA基准测试，对比Doc-V*、MoLoRAG+等主流基线，基于Qwen3-VL的HierDoc在LongDocURL上相对最强开源基线精度提升16.87%，MMLongBench-Doc精度提升27.36%；区域选择相比仅用页级输入的方案精度提5.51%、F1提4.82%，页级检索F1相对基线最高提56.76%，平均选页量仅2.1，大幅降低输入成本。

长文档理解中，粗粒度路由做召回、细粒度路由做精准定位，两级独立优化+全局局部证据融合的收益远高于单粒度检索方案
