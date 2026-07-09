---
title: 'HIVE: Understanding Post-Hallucination Reasoning in Vision Language Models'
title_zh: HIVE：视觉语言模型幻觉后推理机制研究
authors:
- Feng He
- Zhenting Wang
- Qifan Wang
- Qiang Guan
- Dongfang Liu
- Ruixiang Tang
- Qiankun Li
affiliations:
- Purdue University
- Rutgers University
- Meta AI
- Kent State University
- Imperial College London
arxiv_id: '2607.07507'
url: https://arxiv.org/abs/2607.07507
pdf_url: https://arxiv.org/pdf/2607.07507
published: '2026-07-08'
collected: '2026-07-09'
category: Multimodal
direction: 多模态大模型 · 幻觉推理机制评估
tags:
- VLM
- Hallucination
- Multimodal Reasoning
- Evaluation Framework
- PHR
one_liner: 提出HIVE评估基础设施，系统揭示VLM幻觉进入推理上下文后对下游任务的影响规律
practical_value: '- 做多模态商品理解/导购Agent时，无需完全压制所有低置信度幻觉补全，合理的幻觉扩展语义覆盖反而可提升跨模态检索、商品问答准确率

  - 构建多模态推荐/搜索的效果评估体系时，可复用HIVE的控制变量思路，对比真实语义与幻觉语义对下游排序、召回效果的量化影响

  - 多模态客服Agent的推理链路可做模态差异化优化：过滤纯文本任务中的幻觉输入，保留视觉任务中有益的幻觉补全提升应答效果'
score: 7
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有VLM幻觉研究集中在生成阶段的检测与抑制，完全忽略幻觉语义进入推理上下文后对下游预测的影响，该阶段的作用规律尚未被系统探明。
### 方法关键点
提出HIVE（Hallucination Inference and Verification Engine）评估基础设施，通过严格控制变量对比忠实字幕和幻觉字幕输入下的模型表现，覆盖9类任务、9个主流VLM开展大规模对照实验。
### 关键结果数字
观测到清晰的模态依赖规律：幻觉字幕可提升多数视觉语言任务的准确率，对纯文本任务的影响有限且不稳定；进一步分析显示幻觉提示可拓宽语义覆盖范围、重塑推理动态，同时保持推理过程稳定，证实幻觉语义一旦进入上下文就会显著影响下游推理效果。
