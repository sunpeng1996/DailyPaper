---
title: Towards Mechanistically Understanding Why Memorized Knowledge Fails to Generalize
  in Large Language Model Finetuning
title_zh: 大模型微调中记忆知识泛化失效的机制性解释
authors:
- Lu Dai
- Ziyang Rao
- Yili Wang
- Hanqing Wang
- Hao Liu
- Hui Xiong
affiliations:
- HKUST(GZ)
- HKUST
arxiv_id: '2607.08393'
url: https://arxiv.org/abs/2607.08393
pdf_url: https://arxiv.org/pdf/2607.08393
published: '2026-07-09'
collected: '2026-07-10'
category: LLM
direction: 大模型微调 · 知识注入泛化优化
tags:
- Fine-tuning
- Knowledge Injection
- Generalization
- Mechanistic Interpretability
- Activation Patching
- LoRA
one_liner: 提出知识-电路错位假说，用自修补诊断泛化失效，简单启发式恢复58-75%泛化headroom
practical_value: '- 做LLM+电商知识注入（商品参数、活动规则、商家规则微调）时，不要在记忆准确率达标后就停止微调，可额外增加少量梯度更新促进知识向中间层渗透，提升多轮导购、复杂优惠计算等下游推理准确率

  - 若业务允许推理阶段轻量干预，可参考固定启发式策略，将实体相关的早/晚层表示迁移到中间层，无需额外训练即可提升多跳推理效果

  - 用LoRA微调垂域LLM时，若模型能答单跳事实但答不出组合式问题，优先排查知识-电路错位问题，不要盲目增加训练数据或调大LoRA rank'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前LLM微调注入新知识时普遍存在「记得到但用不了」的问题：模型可快速记忆新事实，但无法将其用于多跳推理等下游任务，即存在Knowing-Using Gap，既有泛化准确率远低于记忆准确率的差距，也存在泛化能力显著滞后于记忆的时间差，现有研究缺乏对该现象的机制性解释与低成本修复方案。

### 方法关键点
- 提出知识-电路错位假说：记忆的知识被存储在易拟合的早/晚层（支持直接召回），但未被路由到多步推理所需的中间层计算路径，导致泛化失效
- 设计self-patching干预技术：将源层锚定实体的隐层表示替换到目标层对应位置，通过准确率变化定位知识存储位置与有效计算层的映射关系
- 提出低成本修复启发式：无需逐实例搜索，固定将总层数10%位置的早层、80%位置的晚层表示迁移到45%位置的中间层，即可实现泛化提升

### 关键实验
- 数据集：基于生物医学STaRK-Prime、学术STaRK-MAG知识库构造，预训练模型零-shot准确率<6%，确保注入知识全新，任务包含单跳记忆、多跳链式推理、交集推理三类
- 效果：Oracle自修补比CoT基线在链式推理上提升1.5~6倍，比无干预的准确率提升1.5~6倍；固定启发式可恢复58~75%的Oracle提升空间，跨Qwen、LLaMA全系列模型、跨领域效果稳定
- 附加结论：全量微调比LoRA记忆更快，但泛化效果无显著优势；模型规模增大无法消除Knowing-Using Gap，注入知识越多准确率差距越大

### 核心结论
LLM微调时记忆知识泛化失效不是容量问题，而是知识存储位置与推理电路的路由对齐问题，属于可低成本修复的工程问题而非本质能力缺陷
