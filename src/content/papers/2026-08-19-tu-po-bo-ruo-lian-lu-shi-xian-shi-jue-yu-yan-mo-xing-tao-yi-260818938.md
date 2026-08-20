---
title: Breaking the weakest link to evade vision language models
title_zh: 突破薄弱链路实现视觉语言模型逃逸攻击
authors:
- Ilan Zini
- Boussad Addad
- Katarzyna Kapusta
affiliations:
- ESILV
- Thales
- Thales cortAIx Labs
arxiv_id: '2608.18938'
url: https://arxiv.org/abs/2608.18938
pdf_url: https://arxiv.org/pdf/2608.18938
published: '2026-08-19'
collected: '2026-08-20'
category: Multimodal
direction: 多模态大模型 · 对抗攻击安全
tags:
- VLM
- Adversarial Attack
- Evasion Attack
- Vision Encoder
- Multimodal Security
one_liner: 仅优化VLM视觉编码器生成人眼不可察对抗扰动，低成本实现高有效性的VLM逃逸攻击
practical_value: '- 电商多模态内容审核场景需重点加固VLM视觉编码器链路，该模块是对抗逃逸攻击的核心薄弱点，可避免恶意商品图绕过审核规则

  - 对线上部署的VLM做鲁棒性自测时，可复用仅优化视觉编码器的梯度生成方法，无需全模型反传，能大幅降低对抗样本生成的计算成本

  - 用VLM做商品图文匹配、多模态内容理解的推荐系统，需新增微小扰动检测前置模块，避免人眼不可察的图像扰动导致匹配错误、推荐效果下降'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
VLM已成为多模态AI系统核心组件，广泛落地于关键场景，但针对多模态对齐的逃逸攻击鲁棒性研究存在缺口，现有全架构优化的攻击方案计算成本极高，难以规模化验证。
### 方法关键点
梯度驱动的攻击方案仅对VLM的视觉编码器做优化生成对抗扰动，无需调整整个多模态架构，覆盖两类攻击场景：无目标攻击扰乱模型对原图的语义解读，有目标攻击强制模型输出与原图无关的指定语义描述。
### 关键结果
在Qwen2.5-VL、Granite-Vision、FastVLM、Phi-3.5-VL等多个主流开源VLM上验证，人眼不可察的微小扰动即可大幅改变模型的文本输出，攻击成功率稳定，同时计算资源需求较全架构优化方案显著降低。
