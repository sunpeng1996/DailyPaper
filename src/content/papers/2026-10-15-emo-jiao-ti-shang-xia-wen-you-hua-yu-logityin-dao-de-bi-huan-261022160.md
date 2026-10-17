---
title: 'EMO: A Closed-Loop Test-Time Computation Framework via Alternating Context
  Optimization and Logits Steering'
title_zh: EMO：交替上下文优化与Logit引导的闭环线测试时计算框架
authors:
- Wei Xia
- Yehui Tang
- Zhi-Hong Deng
affiliations:
- Peking University
- Samsung Research, Beijing
arxiv_id: '2610.22160'
url: https://arxiv.org/abs/2610.22160
pdf_url: https://arxiv.org/pdf/2610.22160
published: '2026-10-15'
collected: '2026-10-17'
category: LLM
direction: LLM测试时自适应 · 无训练推理优化
tags:
- test-time adaptation
- logit steering
- context optimization
- zero-shot inference
- frozen LLM
one_liner: 训练无关的LLM测试时自适应框架，交替优化上下文与logit，提升零样本推理效果
practical_value: '- 对于Agent类应用的闭环迭代，可复用E-M交替逻辑：先用外部judge反馈优化prompt，再用新旧prompt的token分布差修正logit，无需微调即可提升商品文案生成、用户query理解等任务的效果

  - 工程上可复用confidence-constrained logit修正trick：仅保留优化后上下文下概率高于阈值α的token做引导，避免无关token干扰，平衡效果与计算开销

  - 预算受限的推理场景可参考：同等生成算力预算下，该框架的oracle覆盖率优于独立采样best-of-N，适合推理成本敏感的推荐文案生成、智能客服等场景'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有测试时上下文优化仅通过修改prompt适配frozen LLM，但无法独立控制上下文更新对token分布的影响强度，优化收益受限，且未将生成反馈闭环到后续上下文迭代中，难以最大化测试时算力的投入产出比。

### 方法关键点
- 类EM迭代框架，分两步执行：E-step用外部judge的文本反馈迭代优化系统上下文，无需金标答案；M-step对比同一前缀下新旧上下文的next-token分布，构造置信度约束的logit修正向量，引导解码走向更符合优化后上下文的分布
- 理论上统一了参数优化和上下文优化的目标，均为最小化与目标分布的KL散度，推导证明在上下文优化有效、引导方向对齐的假设下，足够小的引导强度可保证单轮KL下降
- 工程上仅需维护两个上下文对应的KV cache，logit修正计算复杂度为O(|V|)每步，无需模型反向传播

### 关键实验
在8个3B-32B参数的LLM、6个推理基准（AIME、GPQA-Diamond、GSM8K、MATH-500、MMLU-Pro）上测试：比零样本基线在39/40的场景下提升，平均涨点9.10pp；比仅做上下文优化的TextGrad平均涨点1.53pp，所有模型在MMLU-Pro上均有稳定收益；同等生成算力预算下，oracle覆盖率优于best-of-N独立采样，尤其在Llama系列模型上优势明显。

### 核心结论
测试时算力分配应将生成和验证耦合，根据当前推理瓶颈动态调整上下文迭代、logit引导强度和验证投入，而非单纯堆采样数量。
