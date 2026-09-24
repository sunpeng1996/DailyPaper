---
title: Complementary Roles of Activation and Parametric Memory in Few-Shot Learning
title_zh: 少样本学习中激活记忆与参数记忆的互补作用研究
authors:
- Miaohe Niu
- Runsong Zhao
- Xinyu Liu
- Bo Jin
- Yucheng Qiao
- Chunliang Zhang
- Jingbo Zhu
- Tong Xiao
affiliations:
- Northeastern University
- NiuTrans Research
arxiv_id: '2609.28250'
url: https://arxiv.org/abs/2609.28250
pdf_url: https://arxiv.org/pdf/2609.28250
published: '2026-09-23'
collected: '2026-09-24'
category: LLM
direction: 大语言模型 · 记忆机制与少样本学习
tags:
- LLM
- Few-Shot Learning
- KV Cache
- Test-Time Training
- Memory Mechanism
one_liner: 通过控制实验明确LLM激活与参数记忆的适用场景，揭示复合任务下二者的协同机制
practical_value: '- 电商/Agent的事实类查询（如用户历史订单、商品属性召回）优先用KV cache的激活记忆，准确率接近100%，比测试时微调参数的效率、效果都高得多

  - 涉及多步骤复合任务（如智能客服的规则判断+金额计算、个性化推荐的用户规则匹配+商品召回）时，可将激活记忆与轻量参数更新（如LoRA）结合，能大幅提升任务效果

  - 少样本任务方案选型时不要默认参数微调优于上下文学习，简单规则类任务上下文学习的效果甚至更好，可节省大量微调成本'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
此前业界默认激活记忆（KV cache）适合事实召回、参数记忆（测试时更新参数）适合新任务学习，但二者的分工边界、协同机制缺少系统对照验证，无法为少样本任务的记忆方案选型提供明确指导。

### 方法关键点
- 构造6类无预训练知识泄漏的合成任务，分为事实召回、基础规则学习、条件算术复合任务三类，所有规则与事实仅通过测试时历史提供
- 设置三组对照变量：仅激活记忆（ACT，固定参数，历史存入KV cache）、仅参数记忆（PARA，测试时更新参数，不保留历史激活）、二者结合（COMBO，先更新参数再重编码历史到激活）
- 从神经元层面定位两类记忆分别激活的功能神经元，拆解协同的底层机制

### 关键实验
在Qwen3 1.7B/4B/8B、Llama-3.2 1B四个模型上测试，每类任务300个测试样本：
1. 事实召回任务ACT准确率100%，PARA即使做200步更新准确率仅4.67%
2. 基础规则学习任务中ACT与PARA效果各有优劣，无稳定胜负关系
3. 条件算术复合任务中，COMBO在20步更新时准确率最高达99.3%，远高于ACT的66%、PARA的32.3%；历史规模达2000条时COMBO仍保持83%准确率，远高于单记忆的37%/12%

### 核心结论
不要刻板认为参数更新一定优于上下文学习，多步骤复合任务结合两种记忆才能实现最优效果
