---
title: 'LODESTAR: Trustworthy Entropy Is Navigated, Not Merely Measured -- Reinforced
  Polarizer Keeps a Frozen LLM from Being Confidently Misled by the Wrong Evidence'
title_zh: LODESTAR：强化极化器引导定向熵，避免冻结LLM被误导证据欺骗
authors:
- Po-Jen Ko
- Che-Cheng Wu
- Hung-Chun Hsu
- Li-Yang Chang
- Chuan-Ju Wang
affiliations:
- Research Center for Information Technology Innovation, Academia Sinica, Taiwan
arxiv_id: '2608.11922'
url: https://arxiv.org/abs/2608.11922
pdf_url: https://arxiv.org/pdf/2608.11922
published: '2026-08-12'
collected: '2026-08-13'
category: RAG
direction: RAG优化 · 冻结LLM置信度校准
tags:
- RAG
- Entropy Calibration
- Reinforcement Learning
- Frozen LLM
- Hallucination Reduction
one_liner: 通过RL训练固定自然语言极化器插入prompt，修正RAG中最低熵选择的置信错误问题
practical_value: '- 电商/广告RAG场景可直接复用极化器思路：无需微调LLM，仅插入RL训练的固定提示串，就能降低误导性召回内容的选中率，工程落地成本极低

  - 熵选策略优化可参考定向熵设计：同一query下主动抬升误导性召回片段的生成熵，避免「自信错误」的召回片段被优先选中，适配搜索/导购问答的召回排序场景

  - 可复用首token熵的工程优化：仅计算生成首token的熵即可完成片段排序，比全序列熵计算省数倍推理开销，适配高QPS的线上推荐/搜索业务

  - 跨模型迁移可参考同家族适配逻辑：极化器在同模型家族下迁移效果较好，业务中可先基于小模型训练极化器，再迁移到线上大模型，降低训练成本'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
RAG系统中现有基于最低熵的召回片段选择规则存在致命缺陷：误导性片段会让冻结LLM生成更自信（熵更低）的错误答案，反而被优先选中；且更强的召回/重排模型会提升误导性片段的占比，传统熵选的误导率甚至高于随机选片段，亟需解决置信度和正确性脱钩的问题。

### 方法关键点
- 提出LODESTAR框架，不微调冻结LLM，仅在召回片段和问题之间插入一个GRPO训练的固定自然语言极化器（polarizer），定向抬升误导性片段的生成熵、压低正确片段的熵，让熵选规则能正确选出优质片段
- 训练奖励函数为单query下误导性片段和正确片段的熵差，推理阶段无需标注、采样或额外模型，仅需保留极化器字符串即可运行
- 工程上仅计算生成首token的熵即可完成排序，比全序列熵计算大幅降低推理开销

### 关键结果
在5个开源QA数据集共5008个问题上测试，对比14种已发表的RAG选择方法，LODESTAR的平均F1达0.5339，比传统最低熵选提升3.71%，比召回top1提升11.95%；Exact Match达0.4136，GPT-4o打分达0.6435，所有指标均为最优；误导性片段选中率从30.3%降至26.0%，优于随机选择的28.9%。

**最值得记住的一句话**：熵是RAG片段选择的有效信号，但必须经过定向干预而非被动测量，仅一个短提示串就能在不修改LLM的前提下大幅提升RAG效果。
