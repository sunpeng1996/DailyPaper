---
title: 'MoE--LoRA Methods for Multilingual Adaptation: A Systematic Empirical Study'
title_zh: MoE-LoRA多语言适配方法的系统性实证研究
authors:
- Nikit Srivastava
- Joel Dag
- René Speck
- Axel-Cyrille Ngonga Ngomo
affiliations:
- Paderborn University
- Heinz Nixdorf Institute
arxiv_id: '2611.23158'
url: https://arxiv.org/abs/2611.23158
pdf_url: https://arxiv.org/pdf/2611.23158
published: '2026-11-17'
collected: '2026-11-18'
category: Training
direction: 大模型训练 · MoE-LoRA多语言适配
tags:
- LoRA
- MoE
- PEFT
- Multilingual LLM
- Empirical Study
one_liner: 在200种语言、9000+评估设置下对比8种LoRA方法，明确多语言适配的效果边界与配置规律
practical_value: '- 多语言LLM适配优先选低rank（r=2）LoRA配置，参数量仅为r=64方案的1/32，效果优于更高rank配置，适合跨境电商、多语言推荐等场景的低成本适配

  - 小范围预实验仅能筛选可行配置，无法预测大规模训练时的效果排名，最终上线方案必须在目标语言量级的训练集上验证，避免小范围实验选到的最优配置大规模拉跨

  - MoE-LoRA适配效果存在明显任务偏移：对翻译、多语言生成类任务增益稳定，对阅读理解、推理类任务会显著降分，选择适配方案前需对齐业务场景

  - 低资源语言从LoRA适配中获益最多，针对小语种跨境用户的推荐、客服Agent场景可直接复用该方案快速补全语言能力，无需重新训练基座模型'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前主流LLM训练数据英语占比极高，低资源语言效果远差于英语，MoE-LoRA被认为是低成本扩展LLM多语言能力的核心方案，但始终缺乏统一评测协议下的系统性实证验证，不同方法的效果边界、最优配置规律完全不明确。

### 方法关键点
- 基于冻结的Llama-3.1-8B基座，对比8种LoRA/MoE-LoRA方法（含AdaMoE、MOELoRA、HydraLoRA、普通LoRA等），覆盖10/96/200三种语言量级的训练集
- 分三阶段实验：单因素搜索（遍历rank、专家数超参）→ 混合配置验证筛选Top5可行方案 → 大规模多语言训练验证效果
- 覆盖4类多语言基准：阅读理解（Belebele）、翻译拟合（FLORES）、主题分类（SIB-200）、文本分类（Taxi1500），总计10842个评测项

### 关键结果数字
- 低rank（r=2）配置效果最优，平均排名2.49，参数量仅为r=64方案的1/32；专家数对效果影响远小于rank，相关一致性系数仅为rank的1/4
- 小范围10语言实验筛选的配置排名与200语言大规模实验排名的Spearman相关系数仅为-0.1，几乎无相关性
- 所有适配方案在翻译拟合任务上相对提升0.4~1.4%，在阅读理解任务上准确率平均下降1.4~3.4个点，低资源语言的效果增益是高资源语言的2倍以上

### 核心结论
MoE-LoRA不是LLM多语言能力的通用升级方案，而是针对特定生成类任务、低资源语言的定向优化工具
