---
title: 'Information Abundance Paradox: Long-Context Training Undermines Parametric
  Knowledge'
title_zh: 信息丰度悖论：长上下文训练会削弱模型的参数化知识
authors:
- Arda Uzunoglu
- Benjamin van Durme
- Daniel Khashabi
affiliations:
- Johns Hopkins University
arxiv_id: '2608.12218'
url: https://arxiv.org/abs/2608.12218
pdf_url: https://arxiv.org/pdf/2608.12218
published: '2026-08-12'
collected: '2026-08-13'
category: LLM
direction: LLM训练 · 长上下文能力优化
tags:
- Long-Context Training
- Parametric Knowledge
- Context Addiction
- LLM Pretraining
- SFT
one_liner: 揭示长上下文训练的信息丰度悖论，量化其对参数知识内化的负向影响及机制
practical_value: '- 做垂直领域LLM-SFT时，不要盲目堆砌训练样本的相关上下文：若业务存在无上下文、上下文冲突的推理需求，需控制训练时的上下文信息丰度，避免上下文依赖导致的线上鲁棒性下降

  - 电商/广告Agent训练可监控FFN/SA梯度比值：要让模型内化领域规则（如商品合规、活动价计算）需保证FFN梯度占比足够高；要让模型优先用RAG实时上下文（如库存、优惠券）可适当增加训练相关上下文占比

  - 长上下文LLM适配无需盲目追求超大窗口，需根据业务推理平均输入长度选择最优训练窗口，超过拐点后不仅浪费算力，还会降低模型零/少shot任务性能'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前行业默认长上下文训练仅能提升模型能力，忽略了上下文窗口对学习模式的影响——实际观测到同系列模型长上下文版本的零/少shot性能反而弱于短上下文版本，无法仅用数据质量解释，需明确长上下文训练的潜在副作用。

### 方法关键点
- 预训练实验：固定token预算、模型配置、优化策略，仅改变训练上下文窗口（512~32768token），在4种模型规模（20M~750M）上做控制变量测试
- SFT实验：固定上下文长度，仅改变训练样本中任务相关文档占比（0/4/8篇目标领域文档），在Qwen3的5种参数规模（0.6B~14B）上测试
- 机制分析：从解复杂度、模块梯度分配、token级注意力分配三个维度拆解效应成因

### 关键结果
- 预训练性能呈倒U型：SuperGLUE、闭书MCQA在2048token窗口达峰值，超过后性能最高下降3.2%；语言建模任务在8192token达峰值
- SFT场景下，训练时任务相关文档从0增至8篇时，支持上下文场景性能最高提升14.2%，但无上下文场景性能最高下降19.1%，冲突上下文场景错误率最高提升27.4%
- 机制上，长上下文训练会将梯度压力从FFN（负责参数知识）向注意力模块转移，推理时上下文注意力占比最高提升18%

### 核心结论
长上下文不是无成本的扩容维度，其本质是在参数内化知识和上下文依赖能力之间做权衡，需要根据业务场景选择最优的训练上下文信息丰度
