---
title: 'ES-VP : Energy-Shaped Dynamic Visual Prompting for Efficient Model Adaptation'
title_zh: ES-VP：面向高效模型适配的能量塑形动态视觉提示方法
authors:
- Can Jin
- Ying Li
- Jingchen Sun
- Hongwu Peng
- Jiahui Zhao
- Yang Zhou
- Lei Li
- Dimitris N. Metaxas
affiliations:
- Rutgers University
- Zhejiang University
- University at Buffalo, SUNY
- Adobe Research
- University of Connecticut
arxiv_id: '2608.21194'
url: https://arxiv.org/abs/2608.21194
pdf_url: https://arxiv.org/pdf/2608.21194
published: '2026-08-21'
collected: '2026-08-24'
category: Multimodal
direction: 多模态模型 · 高效视觉Prompt适配
tags:
- Visual Prompting
- Parameter-Efficient Tuning
- CLIP
- Low-Rank Initialization
- Dynamic Adaptation
one_liner: 通过低秩初始化+能量引导生成图像专属视觉提示，兼顾参数效率与精度优于现有SOTA
practical_value: '- 电商多模态召回/搜广推场景的CLIP适配可复用低秩初始化+能量引导动态Prompt方案，相比固定Prompt大幅提升个性化匹配精度，比额外加辅助网络的方案参数量降2个数量级，推理开销几乎无上涨

  - 图像类下游任务适配（如电商商品图分类、违规图识别）可直接套用ES-VP框架，无需引入额外子网络，避免过拟合小流量业务数据集，泛化性更优

  - 可扩展到文本Prompt生成场景，借鉴能量引导动态适配思路，替代固定Prompt或LoRA+Prompt方案，进一步压缩参数规模'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有视觉Prompt（VP）适配方案存在灵活性与效率的核心矛盾：固定Prompt忽略单图像特性效果受限；引入辅助网络生成个性化Prompt的方案参数量大、易过拟合业务小数据集，泛化性与扩展性差。
### 方法关键点
ES-VP不新增额外辅助网络，直接复用预训练模型本身能力，通过低秩初始化+能量引导的动态适配流程，生成每张输入图像专属的定制化Prompt，兼顾参数效率与泛化表现。
### 关键结果
在5种模型架构、15个数据集上全面超越现有SOTA单Prompt与差异化Prompt方案；基于CLIP架构在4个数据集测试，相比SOTA DAM-VP平均精度提升2.6%，同时VP参数量减少590倍，刷新高效模型适配基准。
