---
title: 'Encoded Early, Used Late: Where Transformers Begin to Act on an Inferred Partner''s
  Expertise'
title_zh: 早编码晚使用：Transformer何时处理推断出的对话伙伴专业度
authors:
- Mika Okamoto
- Gabriele Sarti
affiliations:
- Georgia Institute of Technology
- Northeastern University
arxiv_id: '2609.07139'
url: https://arxiv.org/abs/2609.07139
pdf_url: https://arxiv.org/pdf/2609.07139
published: '2026-09-06'
collected: '2026-09-10'
category: LLM
direction: LLM 推断属性的编码与生效层间隔机制
tags:
- Transformer Mechanism
- Probing
- Counterfactual Patching
- Attribute Representation
- Dialogue Agent
one_liner: 揭示Transformer对对话推断的关系属性存在早编码、晚因果生效的层间间隔规律
practical_value: '- 做电商导购/客服对话Agent时，若需基于用户专业度适配输出话术，干预节点选中后层而非早层，可大幅提升干预有效性

  - 做LLM4Rec的用户隐式属性探测时，不能仅以早层高可解码性判定属性会影响推荐输出，需结合因果干预验证生效层

  - 微调/注入用户推断属性时，可直接将属性注入中后层，降低对模型整体生成逻辑的干扰，减少无关输出偏差'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
过往研究仅证实输入直接给出的属性在Transformer中存在「可解码层早于实际影响输出层」的gap，尚未验证对话过程中逐步推断的关系属性（如对话伙伴专业度）是否存在相同规律。
### 方法关键点
基于覆盖4档专业度人设的多轮研究规划对话语料ExpertCollab，结合线性探测、反事实补丁干预、无探针诊断三类方法，逐层分析专业度属性的可解码性与因果生效性差异。
### 关键结果
1. 对话伙伴专业度在Transformer早层解码准确率最高，到网络中点前就降至接近随机水平；
2. 在早层峰值解码点注入专业度差异对最终输出影响不足10%，中点后注入的影响接近100%，效果差超过1个数量级；
3. 静态给定的属性全程保持高可解码性，无上述间隔效应。
