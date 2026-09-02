---
title: 'LatentPress: Context Compression Beyond Text and Vision'
title_zh: 《LatentPress：超越文本与视觉的上下文压缩方法》
authors:
- Zhengze Zhou
- Hejian Sang
affiliations:
- Cornell University
- Arizona State University
arxiv_id: '2609.01507'
url: https://arxiv.org/abs/2609.01507
pdf_url: https://arxiv.org/pdf/2609.01507
published: '2026-09-01'
collected: '2026-09-02'
category: LLM
direction: LLM上下文压缩 · 连续软令牌
tags:
- Context Compression
- Soft Token
- Frozen LLM
- Long Context
- Efficient Inference
one_liner: 训练仅占LLM参数量~0.1%的适配模块，将长上下文压缩为软令牌供冻结LLM直接读取，压缩4-16倍仍保精度提效率
practical_value: '- 电商客服Agent会话历史压缩可复用角色感知策略：保留用户输入原token、压缩助理回复，在压缩率4-8倍下不丢失用户核心需求，降低长会话推理成本

  - RAG系统的召回后文档压缩阶段可替换现有文本摘要/LLMLingua方案：仅需训练占目标LLM参数量~0.1%的专属适配模块，4-8倍压缩下精度不低于原始上下文，推理速度提升5-9倍

  - 生成式推荐的用户长行为序列建模可借鉴软令牌压缩思路：将长行为序列映射为LLM embedding空间的连续软令牌，无需文本重构即可直接输入LLM完成推理，降低长序列处理耗时'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有LLM上下文压缩依赖文本摘要、OCR重构或整模型微调，要么精度损失大，要么推理/训练成本高，且压缩结果仍需转为人类可读文本才能输入LLM，浪费算力；长会话Agent、长文档QA等场景需要更高效的机器专属上下文表示，无需人类可读即可被LLM直接读取。

### 方法关键点
- 架构分为Writer和Reader两步：Reader是完全冻结的下游LLM，Writer仅由复用的LLM底部2层冻结Transformer层+极小线性适配模块组成，参数量仅为LLM的~0.1%
- 压缩策略支持两种：面向会话的角色感知压缩（用户输入无损保留，助理回复按比例压缩）、面向长文档的均匀压缩
- 训练目标结合重建损失和前向KL散度蒸馏，让压缩后的软令牌对齐原始上下文的LLM输出分布，推理时无需重构文本，直接将软令牌拼接问题嵌入后输入冻结LLM

### 关键实验结果
- 会话记忆任务LongMemEval上，7.7倍压缩时准确率达0.504，超过原始上下文的0.490，远高于文本摘要的0.184和OCR压缩的0.312；单会话写入耗时仅43ms，比文本摘要/OCR快9-22倍
- 长文档QA任务LongBench-QA上，域内训练的Writer在4-8倍压缩时精度超过原始上下文，16倍压缩时略低于原始；推理速度比原始上下文/缓存OCR快5-9倍

### 核心结论
机器专属的连续软令牌上下文表示，无需人类可读即可被冻结LLM直接读取，是兼顾精度和效率的长上下文处理可行路径。
