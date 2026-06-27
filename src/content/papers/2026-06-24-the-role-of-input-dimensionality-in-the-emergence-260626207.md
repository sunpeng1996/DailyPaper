---
title: The Role of Input Dimensionality in the Emergence and Targeted Control of Adversarial
  Examples
title_zh: The Role of Input Dimensionality in the Emergence
authors:
- Nasrin Malekzadeh Goradel
- Niccolo Pancino
- Yaser Gholizade Atani
- Benedetta Tondi
- Giovanni Bellettini
- Mauro Barni
arxiv_id: '2606.26207'
url: https://arxiv.org/abs/2606.26207
pdf_url: https://arxiv.org/pdf/2606.26207
published: '2026-06-24'
collected: '2026-06-27'
category: Multimodal
direction: Multimodal
tags:
- Multimodal
- LLM
one_liner: Several theoretical works have tried to explain the adversarial vulnerability
  of deep neural ne...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 摘要

Several theoretical works have tried to explain the adversarial vulnerability of deep neural networks through properties of high-dimensional geometry. However, the assumptions underlying these works are rarely examined empirically, and systematic evidence remains limited. In this work, we present a systematic study of the role of input dimensionality in both the emergence and the targeted control of adversarial examples. We first analyse the scope and limitations of existing theoretical frameworks based on concentration of measure, showing that real image classes exhibit strong empirical localization, beyond what such theories typically assume. We then conduct an extensive empirical evaluation across hierarchical image datasets spanning a wide range of input dimensionalities and diverse neural architectures. Our results consistently show that adversarial examples become easier to construct as dimensionality increases. We also investigate how input dimensionality affects the additional difficulty of crafting targeted adversarial examples. In particular, we provide theoretical arguments showing that high-dimensional geometry implies that enforcing a specific target label entails only a limited additional distortion compared to untargeted attacks. We corroborate this insight through extensive experiments, demonstrating that the gap between targeted and untargeted perturbations remains small and further narrows as input dimensionality increases. While, taken together, our findings establish high input dimensionality as a fundamental factor underlying the emergence and targeted control of adversarial examples, whether this phenomenon primarily arises from the interplay between high-dimensional geometry and data distributions or from the architectural properties of deep neural networks remains an open question.

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。
