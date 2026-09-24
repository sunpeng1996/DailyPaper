---
title: 'DCRL: Decoupling and Coupling Reinforcement Learning via Policy-Reward Manifold
  Alignment'
title_zh: DCRL：基于策略-奖励流形对齐的解耦耦合强化学习框架
authors:
- Henan Sun
- Zehua Li
- Haitao Hu
- Qifan Zhang
- Jianfeng Zhang
- Nuo Chen
- Jia Li
affiliations:
- The Hong Kong University of Science and Technology (Guangzhou)
- The Hong Kong University of Science and Technology
- Huawei Noah’s Ark Lab
- Tencent HY
arxiv_id: '2609.27572'
url: https://arxiv.org/abs/2609.27572
pdf_url: https://arxiv.org/pdf/2609.27572
published: '2026-09-23'
collected: '2026-09-24'
category: Training
direction: LLM RL训练 · 策略奖励流形对齐
tags:
- Reinforcement Learning
- Manifold Alignment
- Reward Modeling
- LLM Alignment
- Small LLM
one_liner: 提出融合动态奖励规则进化与策略奖励同步的RL框架，大幅提升小参数LLM通用推理能力
practical_value: '- 落地基于RL的电商导购Agent、query改写Agent时，可复用「每轮训练后同步奖励模型与策略模型参数」的策略，解决静态奖励模型漂移、奖励过优化问题，降低人工对齐成本

  - 设计电商/广告场景的多维度奖励规则时，可借鉴三层分级prompt结构：公理层（通用规则固定）、定理层（品类/场景规则跨域调整）、推论层（按业务表现动态迭代），减少奖励hack风险

  - 搜索/推荐垂域小参数LLM落地时，可参考DCRL范式做RL微调，用4B级模型逼近几十倍大模型效果，兼顾推理性能与部署成本，适配低延时业务场景'
score: 9
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前LLM的RL训练存在两大核心痛点：规则类奖励适配性差易被模型hack，静态奖励模型易随策略迭代出现分布漂移，导致优化不稳定、奖励信号与真实业务目标不匹配，小参数模型性能难以追平大模型，落地成本居高不下。

### 方法关键点
- 从几何视角将LLM推理建模为逻辑推导、评估、表征三个耦合子流形，现有RL训练的本质问题是策略-奖励流形不匹配
- 设计三段式分级奖励prompt结构：公理层（通用评估规则全程固定）、定理层（领域规则仅在跨域时调整）、推论层（每轮训练根据当前策略表现动态迭代），动态优化奖励评估的表征流形
- 每轮策略更新后直接将奖励模型参数同步为最新的策略模型参数，实现策略-奖励流形的重耦合，保证奖励评估的一致性

### 关键实验
在数学、代码、常识3大类10个推理基准上测试，对比规则奖励、静态奖励模型、ReasonFlux等多个SOTA基线，基于Qwen3-4B训练的DCRL-4B全面超过Qwen3-32B，在GSM8K、CodeContest、MMLU-Pro核心基准上pass@5分别达到95.59%、36.84%、71.20%，性能接近Qwen3-235B，训练稳定性也显著优于基线。

**最值得记住的一句话**：策略与奖励的动态协同进化，是用极低成本大幅提升LLM推理能力的可行路径。
