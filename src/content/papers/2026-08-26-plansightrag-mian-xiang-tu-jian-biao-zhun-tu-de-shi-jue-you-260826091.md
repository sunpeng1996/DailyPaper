---
title: 'PlanSightRAG: A Visual-First Multimodal RAG for Automating Question Answering
  and Compliance Checking for Civil Standard Plans'
title_zh: PlanSightRAG：面向土建标准图的视觉优先多模态RAG问答与合规校验框架
authors:
- Nabaraj Subedi
- Shuvo Dip Datta
- Ahmed Abdelaty
- Shivanand Venkanna Sheshappanavar
affiliations:
- University of Wyoming
arxiv_id: '2608.26091'
url: https://arxiv.org/abs/2608.26091
pdf_url: https://arxiv.org/pdf/2608.26091
published: '2026-08-26'
collected: '2026-08-27'
category: RAG
direction: 多模态RAG · 视觉文档合规校验
tags:
- Multimodal RAG
- VLM
- Agentic Pipeline
- Visual Grounding
- Zero-shot Retrieval
one_liner: 提出无需OCR的视觉优先多模态RAG，实现土建工程图高准确率检索与合规校验
practical_value: '- 做多模态商品/广告素材审核时，可复用视觉优先RAG架构，跳过OCR直接对图像建索引推理，避免OCR丢失布局/几何信息

  - 针对结构化视觉文档（海报、资质图、商品详情图）合规校验场景，可借鉴Planner-Retriever-Auditor-Synthesizer的Agent流水线设计

  - 零样本跨域检索效果达标时可省略LoRA微调步骤降低部署成本，同时可引入MaxSim热图作为检索证据链提升可解释性'
score: 6
source: arxiv-cs.IR
depth: abstract
---

### 动机
土建基建合规校验长期依赖人工读图，基于OCR的自动化方案会丢失解读图纸必需的几何、布局信息，现有方案准确率不足。

### 方法关键点
提出视觉优先的多模态RAG框架PlanSightRAG，直接对图纸图像做索引与推理，整合ColNomic-3B多向量检索、Planner-Retriever-Auditor-Synthesizer Agent流水线，搭配MaxSim热图作为证据链路；支持无需人工输入规则，直接从规范语料提取数值阈值完成视觉规则grounding。

### 关键结果
在4056对、5个州DOT标准图的自建基准上零样本Recall@5达91.47%，跨域到未见过的密歇根DOT语料仍达91.40%，LoRA微调无收益；搭配Qwen2.5-VL-72B的流水线在给定预解析规则阈值时，合成合规图纸verdict准确率达100%，远高于非VLM OCR基线的76.4%。
