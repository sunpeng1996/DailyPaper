---
title: How Do VLMs Fail? Vision-Operation Misalignment in Compositional VQA
title_zh: 多模态VQA任务中VLM的视觉-操作错位失效机制分析
authors:
- Navya Gupta
- Bingjie Xu
- Avinash Anand
- Timothy Liu
- Zhengchen Zhang
affiliations:
- Singapore Institute of Technology
- NVIDIA
arxiv_id: '2607.16094'
url: https://arxiv.org/abs/2607.16094
pdf_url: https://arxiv.org/pdf/2607.16094
published: '2026-07-17'
collected: '2026-07-21'
category: Reasoning
direction: 多模态推理 · VLM失效机制分析
tags:
- VLM
- Compositional VQA
- Failure Analysis
- Transformer
- Causal Intervention
one_liner: 拆解组合式VQA任务中VLM的四类失效模式，定位不同失效对应的Transformer内部计算路径
practical_value: '- 电商多模态商品问答、多模态Agent客服场景可复用该框架拆解VLM badcase，降低问题排查成本，针对性制定调优策略

  - 不同失效对应不同Transformer模块的结论可用于定向优化：grounding类错误优先优化FFN，多步推理类错误优先优化后层attention

  - 多模态商品检索推荐场景的badcase分类可复用4类失效模式划分，指导训练数据增强与模型微调方向'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
组合式VQA要求VLM执行对象选择、空间关系解析、属性校验等多步推理，当前VLM整体性能表现不错，但失效的底层机制尚未被充分挖掘，难以支撑定向优化。

### 方法关键点
提出以操作为核心的机制分析框架，从推理操作源头、内部计算传播路径两个维度拆分失效，结合覆盖全Transformer层的三类互补因果干预，定位不同失效的传播路径。

### 关键结果
识别出4类机制独立的失效模式：grounding失效、推理失效、属性提取失效、语言先验主导失效，每类对应独特的视觉grounding强度与答案正确率的关联关系；验证了路径分离特性：grounding失效仅通过FFN传播，推理失效对应后层attention，属性提取失效定位在答案位置的FFN计算，不同失效类型需匹配完全不同的修复策略。
