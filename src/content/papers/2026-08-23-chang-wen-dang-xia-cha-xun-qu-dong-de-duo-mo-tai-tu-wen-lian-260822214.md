---
title: Query-Driven Multimodal Information Extraction from Long Documents
title_zh: 长文档下查询驱动的多模态图文联合抽取
authors:
- Yikai Gao
- Ding Xia
- Xi Yang
affiliations:
- Jilin University
- The University of Tokyo
arxiv_id: '2608.22214'
url: https://arxiv.org/abs/2608.22214
pdf_url: https://arxiv.org/pdf/2608.22214
published: '2026-08-23'
collected: '2026-08-25'
category: Agent
direction: 多Agent协作 · 长文档多模态抽取
tags:
- Multi-Agent
- Multimodal Extraction
- Long Document
- VLM
- Benchmark
one_liner: 提出首个长文档图文联合抽取基准ITJoint与三阶段多Agent框架Q2IT，性能远超单VLM
practical_value: '- 长文档多模态信息抽取可复用「证据收集→页面定位→图像绑定」三阶段Agent拆分架构，比直接调用VLM精度提升超40%，适合电商商品手册、品牌介绍PDF的结构化信息自动抽取

  - 图文对齐场景可借鉴三级校验（证据校验/页校验/图校验）逻辑，大幅降低图像绑定幻觉，尤其适配电商商品属性与主图/详情图的自动匹配场景

  - 跨页图文关联任务可采用「关键词匹配+页号映射+相对偏移+源页fallback」的多策略定位方案，解决长文档下图文跨页分散的关联问题'
score: 8
source: arxiv-cs.MM
depth: full_pdf
---

### 动机
现有DocVQA范式仅支持输出文本答案或证据区域，无法满足查询驱动的按需抽取文本属性+对应图像的需求；而领域长文档（如电商商品册、专业手册）图文耦合度高、布局非线性、跨页分散，规则抽取鲁棒性差，全人工标注成本极高，亟需自动化的按需抽取方案。

### 方法关键点
1. 构建首个长文档图文联合抽取基准ITJoint，覆盖多领域2455页文档、316个查询、910个标注实例，支持查询级（单实例/集合查询）、实例级（1对1/1对多/1对0、跨页/内页、显式/隐式对齐）的细粒度评测
2. 提出Q2IT三阶段多Agent框架：Evidence Agent通过混合检索+GMM聚类召回相关文本与图像线索；Page Agent采用多策略（关键词/页号/相对偏移/源页fallback）定位目标页；Figure Agent基于Grounding DINO检测候选框+VLM完成图文绑定
3. 设计图文联合评测指标，同时校验文本正确性、图像IoU、图文对齐准确性，明确惩罚无对应图像时的绑定幻觉

### 关键实验
对比GPT-5.4、Gemini-3.1-Pro、Qwen3-VL、GLM-4.5V四款SOTA VLM，直接调用时Gemini性能最优，Strict Joint F1仅为0.507；接入Q2IT后Gemini的Strict Joint F1提升至0.722，其中单实例正查询准确率提升24.4%，1对N多图实例准确率提升18.5%，1对0无图场景的幻觉率降低7.7个百分点。

### 核心结论
长文档多模态复杂任务通过分阶段多Agent拆解+专用工具调用，比直接调用通用大模型的性能提升幅度可达40%以上，是当前落地性价比最高的技术路径
