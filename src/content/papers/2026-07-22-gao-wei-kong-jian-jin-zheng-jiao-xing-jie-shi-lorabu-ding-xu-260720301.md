---
title: 'The Blessing of Dimensionality: How Near-Orthogonality in High-Dimensional
  Spaces Explains Temporal Portability'
title_zh: 高维空间近正交性解释LoRA补丁跨持续预训练的时间可移植性
authors:
- Abigail Woodring
- Adrian Chan
- Rana Muhammad Shahroz Khan
- Sukwon Yun
- Chau-Wai Wong
- Tianlong Chen
affiliations:
- NC State University
- University of North Carolina at Chapel Hill
- Independent Researcher
arxiv_id: '2607.20301'
url: https://arxiv.org/abs/2607.20301
pdf_url: https://arxiv.org/pdf/2607.20301
published: '2026-07-22'
collected: '2026-07-23'
category: Training
direction: LLM微调 · LoRA时间可移植性
tags:
- LoRA
- PEFT
- PortLLM
- Continual Pretraining
- Temporal Portability
one_liner: 通过实验与理论分析揭示高维近正交性是LoRA补丁长期时间可移植性的核心原因
practical_value: '- 业务中上游基座LLM定期迭代时，已训好的下游任务（如商品文案生成、用户意图识别、推荐理由生成）LoRA补丁无需重新训练，直接复用在新版本基座上，性能损失可忽略，可节省大量算力与标注数据成本

  - 多LoRA组合部署时，利用高维空间近正交特性，不同任务的LoRA补丁互相干扰极小，可放心叠加使用，无需额外做融合训练

  - Agent的专用技能LoRA（如工具调用、订单查询、售后话术）在基座迭代后无需重新适配，大幅降低Agent的维护成本'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
大厂商通常会定期对基座LLM做持续预训练以更新知识，下游资源有限的开发者若每次基座更新后重新训练业务LoRA补丁，算力与数据成本极高。现有PortLLM方法可直接将旧LoRA复用在新基座上，但仅验证了最多4步的短期可移植性，长期效果不明，且缺乏理论解释。
### 方法关键点
- 大规模实验覆盖10步持续预训练，测试Mistral-7B、Gemma3-12B、Qwen2-0.5B三个基座，Fineweb、Cosmopedia两个预训练数据集，以及常识推理、阅读理解、数学推理等多个下游任务
- 提出两种理论分析框架：① 基于损失landscape的1-D切片，将不同LoRA适配策略的性能差转化为单个内积计算；② 基于持续预训练迭代关系，推导PortLLM跨时间步的性能波动上界
- 定义ϵ-准正交性量化标准，从高维空间特性出发解释性能稳定的根因
### 关键结果
- 10步持续预训练后，PortLLM相比无补丁基线性能提升4~11个百分点，与每步重新微调的Oracle策略性能差距可忽略
- 12组测试中仅3组存在统计显著的性能下降，单步性能下降斜率最高仅为1e-3，性能波动极小
### 核心结论
高维参数空间的“维度诅咒”反而成为LoRA补丁可移植性的“维度祝福”，高维向量的近正交性让预训练更新与下游微调的梯度几乎不产生干扰，是LoRA长期时间可移植性的核心原因。
