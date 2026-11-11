---
title: 'Precision on Demand: Escalating Weight Bits at Uncertain Decoding Steps in
  a Small Local Model'
title_zh: 按需精度：小尺寸本地模型不确定解码步的权值位宽动态提升
authors:
- Mohammed Nayeem Khan
- Logesh L
- Aliyas Ahmad Misri
affiliations:
- Intel Corporation
arxiv_id: '2611.14418'
url: https://arxiv.org/abs/2611.14418
pdf_url: https://arxiv.org/pdf/2611.14418
published: '2026-11-10'
collected: '2026-11-11'
category: LLM
direction: LLM量化 · 动态精度推理优化
tags:
- Quantization
- Dynamic Precision
- LLM Inference
- Uncertainty Gating
- Nested Quantization
one_liner: 提出面向本地小LLM的动态权值位宽策略，仅在不确定解码步升为8bit，兼顾推理成本与精度
practical_value: '- 端侧电商导购/私域客服类小模型Agent可复用不确定性门控逻辑，仅在生成价格、优惠、商品参数等关键信息的不确定步提升权值位宽，降低内存带宽开销，提升端侧推理速度

  - 生成式推荐场景用小模型做候选生成/营销文案生成时，可复用logit margin/熵的门控信号，15%的升位预算即可覆盖94%的精度损失点，在几乎不损失生成质量的前提下降低推理成本

  - LLM推理框架优化可复用嵌套位量化存储设计，一份8bit权重可同时支持4bit/8bit推理，无需存储多份权重副本，节省端侧/边缘侧存储开销'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
本地小LLM推理通常采用固定全局权值位宽的方案，低bit位宽易出现推理精度损失，全高bit位宽则会带来过高的内存读取开销，而内存带宽正是端侧/边缘侧LLM推理的核心瓶颈，亟需兼顾精度与成本的动态精度优化方案。
### 方法关键点
- 采用嵌套位量化设计：仅存储1份8bit权值副本，常规解码步仅读取权值的高4bit做推理，大幅降低内存访问量
- 不确定性门控触发升位：低4bit推理完成后，若输出分布熵超过阈值、或top1与top2 logit的差值低于阈值，则重跑该步的全8bit推理，保证精度
- 成本模型以每token读取的权值字节数为核心指标，剔除硬件负载、计算核心占用等干扰因素，客观衡量优化收益
### 关键实验
基于Qwen3-0.6B模型、GSM8K数学推理benchmark测试：回放36724个解码步时，熵门控预测高低bit argmax翻转的AUC为0.93，margin门控AUC达0.96；15%升位预算下，margin门控可覆盖94%的精度翻转点，熵门控覆盖78%；实测150道测试题时，16%升位率的熵门控方案仅消耗全8bit方案87%的权值读取量，精度仅比全8bit低1.3个百分点，比全4bit方案高7.3个百分点。
### 核心结论
小模型推理中仅不到4%的解码步会出现高低bit精度翻转，用极低成本的不确定性门控筛选这些步骤升位，即可用接近全低bit的成本获得接近全高bit的精度。
