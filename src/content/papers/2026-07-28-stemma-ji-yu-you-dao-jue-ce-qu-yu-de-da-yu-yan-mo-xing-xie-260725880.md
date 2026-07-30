---
title: 'Stemma: Induced Decision Regions Reveal LLM Provenance'
title_zh: Stemma：基于诱导决策区域的大语言模型血统溯源方法
authors:
- Keyu Zhang
- Vadim Safronov
- Andrew Martin
affiliations:
- Department of Computer Science, University of Oxford
arxiv_id: '2607.25880'
url: https://arxiv.org/abs/2607.25880
pdf_url: https://arxiv.org/pdf/2607.25880
published: '2026-07-28'
collected: '2026-07-30'
category: LLM
direction: LLM安全 · 黑盒血统溯源
tags:
- LLM Provenance
- Black-box Detection
- Decision Region
- Model Fingerprinting
- Model Security
one_liner: 通过诱导决策区域消除输出表面差异，实现高鲁棒性黑盒LLM血统溯源检测
practical_value: '- 自研LLM的知识产权保护场景可复用诱导决策区域+多原则探针筛选思路生成专属模型指纹，防范未经授权的模型蒸馏/微调盗用

  - 业务侧集成第三方LLM做推荐/Agent推理时，可基于该方法快速校验第三方LLM血统合规性，规避IP风险

  - 生成式推荐场景下如需校验生成内容的模型来源，可借鉴开放输出映射到有限决策空间的思路，降低表面文本差异对溯源的干扰'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有LLM血统溯源黑盒方法依赖响应表层特征，模型经过微调、压缩、部署参数调整后特征易偏移，导致溯源可靠性大幅下降。

### 方法关键点
1. 提出诱导决策区域概念，将开放式输出映射到有限决策空间，消除表层文本差异，将溯源问题转化为决策区域继承度的度量；
2. 设计Stemma黑盒溯源方法，基于稳定性、鲁棒性、特异性三个互补原则筛选探针，可靠估计决策区域的继承关系。

### 关键结果
在770组来自56个公开checkpoint的源-嫌疑模型对（覆盖多种模型权重变换场景）上，AUC达0.967，1% FPR下TPR达87.8%，显著优于4个代表基线；在覆盖91个部署实例的1260组测试对上，AUC达0.995，1% FPR下TPR达93.5%，对各类推理部署配置鲁棒性极强。
