---
title: 'Select-TTT: Query-Conditioned Selective Fast Weight Updates for In-Place Test-Time
  Training'
title_zh: Select-TTT：面向测试时训练的查询感知选择性快权重更新方法
authors:
- Yue Wu
- Yang Zhang
- Weinan Gan
- Chongming Gao
- Xinsen Guo
- Xiaoyuan Li
- Fuli Feng
affiliations:
- 中国科学技术大学
- 新加坡国立大学
- 华为诺亚方舟实验室
arxiv_id: '2610.36794'
url: https://arxiv.org/abs/2610.36794
pdf_url: https://arxiv.org/pdf/2610.36794
published: '2026-10-27'
collected: '2026-10-28'
category: Training
direction: LLM 测试时训练 · 长上下文QA优化
tags:
- Test-Time-Training
- Fast-Weights
- Long-Context
- QA
- In-Place-TTT
one_liner: 基于查询与上下文块的相关性动态调整IP-TTT快权重更新强度，提升长上下文QA效果
practical_value: '- 电商智能客服、导购Agent的长时对话记忆场景，可直接复用Select-TTT的查询感知权重更新逻辑，在IP-TTT基础上零额外参数优化记忆写入，降低无关历史上下文的噪声干扰

  - 长上下文召回、商品咨询QA场景，可复用logit空间query-CE相关性计算方法，无需额外训练重排器，直接用LM头原生输出做上下文块排序，效果优于cosine相似度和通用跨编码器

  - 长上下文推理工程实现中，可复用块级log-sum-exp、query token直取计算优化技巧，仅增加极小推理延迟和内存开销，即可获得稳定的长上下文效果提升'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有In-Place TTT（IP-TTT）通过复用MLP下投影层作为快权重实现测试时参数更新，大幅降低了LLM长上下文记忆的落地成本，但在真实长上下文QA场景中效果极差，甚至不如零样本基线。核心原因是IP-TTT对所有上下文块采用统一更新强度，无关内容的写入会稀释快权重中与查询相关的有效信息，在用户查询仅依赖小部分上下文的场景下问题尤为突出。

### 方法关键点
- 提出查询感知的选择性更新规则，为每个上下文块计算与用户查询相关的学习率乘数λ_i，动态缩放IP-TTT的块级快权重更新幅度，保留原IP-TTT的块级并行计算特性，无额外参数
- 相关性计算直接复用模型冻结的LM头：计算每个块隐状态对query token的交叉熵（cCE），通过top-k均值池化得到块级相关性得分，无需额外训练重排模型
- 相关性得分经温度缩放softmax转换为乘数，满足三个设计约束：软写入（所有块都有正权重不丢弃潜在有效信息）、预算守恒（平均学习率与原IP-TTT一致，总写入信息量不变）、稳定性（上限裁剪避免单个块权重过高）
- 工程优化：通过块级log-sum-exp和仅抽取query对应LM头参数计算，大幅降低相关性计算的内存与计算开销，额外推理开销可忽略

### 关键结果
在LongMemEval-S、LoCoMo两个长上下文QA基准上测试，对比零样本基线、原IP-TTT：
- Llama-3.1-8B上，LongMemEval-S准确率较IP-TTT提升3.8个百分点，较基线提升4个百分点；LoCoMo得分较IP-TTT提升1.52个百分点
- Qwen3-4B上，LongMemEval-S准确率较IP-TTT提升3.4个百分点，较基线提升1.6个百分点；LoCoMo得分较IP-TTT提升0.74个百分点
- 持续训练场景下，Select-TTT在LongMemEval-S上准确率达37.4%，较IP-TTT高1.8个百分点，较普通持续预训练高2.4个百分点

### 核心结论
测试时训练的快权重写入效率，核心取决于写入内容与下游任务的相关性，而非写入信息量的大小。
