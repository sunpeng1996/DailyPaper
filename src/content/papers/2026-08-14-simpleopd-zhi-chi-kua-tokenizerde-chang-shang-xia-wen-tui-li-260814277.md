---
title: 'SimpleOPD: Simple Tokenizer-Agnostic On-Policy Distillation for Long-Context
  Reasoning'
title_zh: SimpleOPD：支持跨Tokenizer的长上下文推理无偏策略蒸馏方法
authors:
- Haonan He
- Haodi Lei
- Yun Luo
- Haoran Zhang
- Shunkai Zhang
- Yizhuo Li
- Shengji Tang
- Zhilin Wang
- Runzhe Zhan
- Lei Bai
affiliations:
- Shanghai Artificial Intelligence Laboratory
arxiv_id: '2608.14277'
url: https://arxiv.org/abs/2608.14277
pdf_url: https://arxiv.org/pdf/2608.14277
published: '2026-08-14'
collected: '2026-08-17'
category: Training
direction: LLM训练 · 跨Tokenizer策略蒸馏
tags:
- On-Policy Distillation
- Cross-Tokenizer
- Long-Context Reasoning
- Knowledge Distillation
- LLM Training
one_liner: 提出跨Tokenizer对齐与训练稳定策略，高效将长上下文大模型推理能力迁移到不同架构小模型
practical_value: '- 跨模型蒸馏时可复用共享文本空间对齐方法，无需对齐Tokenizer就能把大模型的推理/决策能力迁移到业务侧小模型，大幅降低适配成本

  - 做LLM蒸馏/RLHF时可引入终止Token优势掩码+学生初始策略KL正则，解决生成长度爆炸、训练不稳定问题，适合业务侧长文案生成、多步推理Agent训练场景

  - 策略蒸馏训练时可根据师生模型差异调整KL正则系数，差异越大正则系数越高，平衡能力迁移与原有能力保留，适合业务侧定制化小模型快速迭代

  - 蒸馏长上下文能力时，在学生上下文窗口允许范围内适当提高蒸馏序列长度，能更完整迁移多步推理能力，可应用在搜索推荐长用户行为建模、多轮导购Agent训练中'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有On-Policy Distillation（OPD）默认师生模型同架构同Tokenizer，无法直接将长上下文大模型的推理能力迁移到不同架构的短上下文小模型；直接跨Tokenizer蒸馏会出现Token对齐难、师生分布不匹配、响应长度爆炸、训练不稳定等问题，严重限制大模型能力的下沉落地。

### 方法关键点
- 跨Tokenizer对齐：在共享文本空间做蒸馏，仅对齐师生Token中对应完全相同文本片段的位置，未对齐位置回退到学生自身的log概率，无需人工构建Token映射关系
- 训练稳定优化：一是掩码`</think>`、`<|im_end|>`等终止Token的优势损失，避免教师长输出抑制学生正常终止；二是加入学生初始策略的参考KL损失，约束策略漂移，缓解长度爆炸
- 蒸馏目标：基于PPO clipped loss优化，仅在对齐Token位置施加教师监督，支持同家族/跨家族模型的无偏蒸馏

### 关键结果
教师用长上下文数学推理模型SU-01，学生覆盖Qwen3、Qwen3.5、Intern-S2、GLM-4.7、Gemma-4等多架构模型，在推理基准测试中：Intern-S2-Preview在ProofBench上提升21.2个点达到55.2，超过Gemini-2.5-Pro；跨家族模型GLM-4.7-Flash的ProofBench提升8.96个点，Gemma-4提升8.7个点；蒸馏能力可泛化到未训练的科学推理基准，HiPhO提升2.5个点。

**最值得记住的一句话**：跨Tokenizer策略蒸馏不需要完全对齐词汇表，仅通过相同文本片段的局部对齐就能传递大部分模型能力，搭配简单的稳定trick即可实现高效的大模型能力下沉。
