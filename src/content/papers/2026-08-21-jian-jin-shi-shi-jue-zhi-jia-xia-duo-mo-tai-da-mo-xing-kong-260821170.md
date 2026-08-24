---
title: Is Visual Prompting All You Need? Studying VLM Spatial Reasoning under Progressive
  Visual Scaffolds
title_zh: 渐进式视觉支架下多模态大模型空间推理能力研究
authors:
- Lars Benedikt Kaesberg
- Tianyu Yang
- Florian Valentin Wunderlich
- Terry Ruas
- Jan Philip Wahle
- Daniel Kurzawe
- Bela Gipp
affiliations:
- University of Göttingen, Germany
arxiv_id: '2608.21170'
url: https://arxiv.org/abs/2608.21170
pdf_url: https://arxiv.org/pdf/2608.21170
published: '2026-08-21'
collected: '2026-08-24'
category: Reasoning
direction: 多模态大模型 · 空间推理能力优化
tags:
- VLM
- Spatial Reasoning
- Visual Prompting
- Visual Scaffold
- GRPO
one_liner: 通过输入侧轻量视觉支架大幅提升VLM空间推理准确率，明确视觉呈现对VLM能力评估的核心影响
practical_value: '- 做多模态商品理解、货架陈列识别、线下空间布局分析等业务时，可在VLM输入侧加轻量视觉支架（如网格线、区域边界标注），无需微调即可大幅降低视觉grounding错误，提升推理准确率

  - VLM下游任务表现不达预期时，优先排查是否为视觉感知环节瓶颈，而非直接优化推理逻辑或做全量微调，可通过优化视觉输入快速验证性能上限

  - 训练多模态Agent（如电商实景导购、仓储巡检Agent）时，视觉输入优化可搭配GRPO等对齐训练策略，获得额外性能增益，效率高于单独做训练优化'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
VLMs多模态推理性能提升快，但推理任务固定时，视觉呈现形式对模型性能、错误模式的影响机制尚不明确，难以区分VLM失败是源于感知还是推理能力缺陷。

### 方法关键点
基于网格类视觉空间规划基准SPaRC，在输入侧新增轻量视觉支架，保留原视觉模态的同时强化空间结构可辨识度，支架为针对任务结构的诊断性干预，而非通用prompt策略。

### 关键结果
- 多款VLM上，视觉支架相比原始视觉输入最高提升34.0pp任务准确率，Qwen 3.5 397B单靠输入优化就实现33.4pp准确率提升
- 搭配GRPO训练时，视觉支架组可额外获得4.6pp准确率增益，原始输入组训练增益接近0
- 性能提升核心来自grounding类错误降低，规则推理仍为VLM的相对短板
