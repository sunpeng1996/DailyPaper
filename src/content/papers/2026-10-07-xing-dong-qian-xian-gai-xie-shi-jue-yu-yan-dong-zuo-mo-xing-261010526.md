---
title: 'Rephrase Before You Act: Characterizing and Mitigating Language Sensitivity
  in Vision-Language-Action Models'
title_zh: 《行动前先改写：视觉语言动作模型的语言敏感性表征与缓解》
authors:
- Mikey Watts
- Yuchen Cui
arxiv_id: '2610.10526'
url: https://arxiv.org/abs/2610.10526
pdf_url: https://arxiv.org/pdf/2610.10526
published: '2026-10-07'
collected: '2026-10-08'
category: Agent
direction: Agent 指令理解鲁棒性优化
tags:
- VLA
- Instruction Rewriting
- Robustness
- LLM Distillation
- Zero-Shot
one_liner: 无需重训视觉语言动作模型，通过LLM蒸馏改写规则预处理指令，大幅提升跨分布任务成功率
practical_value: '- 电商导购Agent/智能客服场景可复用该无重训改写方案：对少量业务样本的不同表述打分后用LLM蒸馏规则，低成本提升用户指令匹配准确率

  - 搜索/推荐的Query改写环节可借鉴「样本打分→规则蒸馏→部署改写」的pipeline，显著降低OOV Query的召回、排序误差

  - 多模态商品搜索场景可复用单编辑波动统计方法，定位模型敏感的表述特征，针对性优化Query理解模块的鲁棒性'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
视觉语言动作模型（VLA）未继承基座VLM的语言鲁棒性，对指令措辞高度敏感，单字修改即可导致成功率波动超60个点，传统重训、改写增强方案无法有效弥合21点的分布内/跨分布任务性能gap。
### 方法关键点
1. 采用统计检验的单编辑波动分析+ oracle短语搜索，表征VLA的语言敏感性规律，证实仅靠措辞优化即可基本消除分布间性能差
2. 无需修改原有VLA策略：先对少量训练任务的多种表述打分，用LLM蒸馏出10-20条改写规则，部署时仅对输入指令做一次规则改写即可
### 关键结果
冻结的π0模型在12个留出任务上相对性能提升16%-27%，增益集中在跨分布任务；在π0.5和LIBERO基准上，微调内成功率从93.6%升至97.8%，支持零样本泛化到未知任务与指令，无额外重训、逐步骤校验成本
