---
title: 'ExpBoN: Exponential-Noise Best-of-$n$ for Efficient Test-Time LLM Alignment'
title_zh: ExpBoN：基于指数噪声的高效测试时LLM对齐Best-of-n方法
authors:
- Yanxiao Liu
- Sicheng Wan
- Deniz Gündüz
affiliations:
- Imperial College London
- University of Washington
arxiv_id: '2609.21899'
url: https://arxiv.org/abs/2609.21899
pdf_url: https://arxiv.org/pdf/2609.21899
published: '2026-09-18'
collected: '2026-09-21'
category: LLM
direction: LLM测试时对齐 · 推理效率优化
tags:
- Best-of-n
- Test-time Alignment
- Exponential Noise
- Speculative Inference
- LLM Alignment
one_liner: 提出基于指数噪声的软Best-of-n对齐方法ExpBoN，结合GSI实现推理对齐效率最高提升45%
practical_value: '- LLM驱动的电商推荐文案生成、智能客服Agent回答对齐场景中，可将原有Gumbel噪声软BoN替换为ExpBoN，用更少候选量达到同等对齐效果，降低推理成本

  - 搭建小模型生成候选、大模型打分的推测推理流水线时，可集成ExpBoN的早期退出机制，在不损失效果的前提下降低计算开销，适配高并发业务场景

  - 代理奖励模型存在过优化风险时，ExpBoN的指数收敛特性可在更小候选规模下达到目标奖励分布，降低reward hacking出现概率'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有硬Best-of-n（BoN）测试时LLM对齐方法对奖励-KL tradeoff控制粒度粗，易出现reward hacking；传统软BoN（SBoN）收敛速度为多项式级，候选量需求大，推理成本高，且难以适配推测推理框架做效率优化，亟需更高效的软BoN方案。

### 方法关键点
1. 提出ExpBoN，将SBoN的Gumbel噪声替换为指数噪声，可实现有限n下的精确分布分解，对最优倾斜分布的收敛速度为指数级，远快于SBoN的O(1/n)多项式收敛
2. 理论证明ExpBoN在总变差、双向KL散度、期望奖励上的收敛界，同等候选量下期望奖励高于SBoN，且具备更优的代理奖励鲁棒性
3. 结合引导式推测推理（GSI）框架提出ExpGSI，新增奖励截断trick，支持分布无损的早期退出机制，进一步降低计算开销

### 关键结果
在MATH500、MMLU-STEM、Minerva Math数据集上测试，对比GSI、SBoN、RSD等基线，ExpGSI在Qwen2.5-Math上降低14%-39%计算量，Qwen3 n=16时最高降低45%计算量，精度与GSI基本持平，差异小于0.8个百分点。

> 最值得记住的一句话：指数噪声软BoN的收敛速度比传统Gumbel噪声方案快指数级，结合推测推理可在几乎无损效果的前提下大幅降低LLM测试时对齐的推理成本
