---
title: Attending to Multimodal Generation One Token at a Time
title_zh: 逐Token视角下多模态生成过程的注意力机制研究
authors:
- Varun Gupta
- Vineet Gandhi
- Makarand Tapaswi
affiliations:
- CVIT, IIIT Hyderabad
arxiv_id: '2607.03738'
url: https://arxiv.org/abs/2607.03738
pdf_url: https://arxiv.org/pdf/2607.03738
published: '2026-07-03'
collected: '2026-07-09'
category: Multimodal
direction: 多模态大模型 · 注意力机制可解释性
tags:
- MLLM
- Attention Mechanism
- Multimodal Generation
- Interpretability
- Test-time Intervention
one_liner: 揭示MLLM逐token注意力切换规律，提出轻量化测试时干预方法提升多模态任务性能
practical_value: '- 多模态商品导购Agent/多模态推荐场景中，可参考逐token注意力规律，在生成依赖商品图像的内容（如外观、配色描述）时拉高图像模态注意力权重，降低幻觉

  - 涉及单轮回复内跨模态切换的场景（如先讲商品文本参数再讲视觉特征），可在任务切换节点重注入指令token注意力，避免生成偏离需求

  - 提出的测试时动态调整模态注意力的方法无需重新训练模型，可快速落地适配多模态生成类业务的细分场景'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有MLLM可解释性研究多聚焦层/注意力头级的静态实现机制，未覆盖生成过程中逐token的多模态计算动态规律，无法支撑生成过程的精准优化。
### 方法关键点
提出OTaT（One Token at a Time）分析框架，逐步骤追踪生成过程中模型对图像、文本、指令、历史生成token的注意力偏移规律；设计需在单条回复内显式切换视觉/文本上下文的多模态任务，在2类主流模型架构、4个不同规模开源MLLM上开展验证，通过因果注意力阻断干预验证规律的功能性。
### 关键结果
验证得到3类稳定注意力模式：需图像信息的token位置图像注意力达峰、任务切换阶段会重访指令token、生成过程中对历史生成token的注意力逐步上升；基于该规律设计的测试时干预方法可显著提升多模态任务性能，注意力被破坏时模型会出现依赖语言先验、跨模态泄露等问题。
