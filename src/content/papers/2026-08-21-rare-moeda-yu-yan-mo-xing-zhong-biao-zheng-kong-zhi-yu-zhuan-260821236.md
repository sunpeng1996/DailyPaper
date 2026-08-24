---
title: 'RARE: Decoupling Representation Steering from Expert Routing in Mixture-of-Experts
  Language Models'
title_zh: 《RARE：MoE大语言模型中表征控制与专家路由的解耦框架》
authors:
- Zhibo Zhang
- Zhen Ouyang
- Ling Shi
- Kailong Wang
affiliations:
- Huazhong University of Science and Technology
- AIDX TECH PTE. LTD.
- National University of Singapore
arxiv_id: '2608.21236'
url: https://arxiv.org/abs/2608.21236
pdf_url: https://arxiv.org/pdf/2608.21236
published: '2026-08-21'
collected: '2026-08-24'
category: LLM
direction: MoE LLM · 表征控制 路由优化
tags:
- MoE
- Representation Engineering
- Model Steering
- Null Space Projection
- Behavior Control
one_liner: 提出路由无关的MoE表征控制框架RARE，将扰动投影到路由矩阵零空间，大幅提升多场景行为控制效果
practical_value: '- 业务中使用MoE架构做生成式推荐、Agent决策控制时，若需做表征干预（如调整推荐风格、控制回复合规性），可先将扰动投影到路由矩阵零空间，避免改变原生专家分配路径导致效果下降

  - MoE模型行为控制优先选用AffineGaussian扰动估计器，可在合规性控制、事实编辑、真实性提升三类场景下获得最优干预效果；若需平衡干预副作用，LDA估计器是更优选择

  - 验证了MoE路由对输入语义的敏感度远高于对输出行为的敏感度，电商场景下做个性化风格生成、合规性控制时，无需修改路由分配，仅修改选中专家处理的隐状态即可达到效果，降低工程复杂度'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有表征工程在稠密LLM上行为控制效果优异，但直接迁移到MoE模型时，扰动会改变路由逻辑，导致token被分配到错误专家，控制效果大幅下降；现有MoE控制方法直接修改专家选择，会破坏原有输入相关的计算路径，降低模型通用能力和响应相关性，因此需要协调表征控制与MoE路由机制的矛盾。

### 方法关键点
- 实证发现MoE路由对输入语义的敏感度远高于对输出行为/意图的敏感度，同一输入下不同输出行为可在几乎不变的专家路径上生成，因此表征控制应保留原生路由
- 核心框架将原始行为扰动投影到路由矩阵的零空间，移除路由可见的扰动分量，仅保留路由不可见的部分注入隐状态，避免改变当前层的路由逻辑
- 增加下游路由漂移校正：对路由保护层，每次计算时仅保留与参考路由的偏差中路由不可见的分量，抑制扰动传播导致的后续层路由变化
- 对比5种扰动估计器，AffineGaussian（基于正负类协方差的白化重着色）获得最优控制效果，LDA估计器则有更优的副作用平衡性

### 关键实验
在6种不同架构的开源MoE模型（DeepSeek、Mixtral、Qwen3等）上，覆盖有害性控制、真实性提升、事实编辑三个场景，对比RepE、SAFEx、SteerMoE等基线：有害性控制平均攻击成功率53.3%，同时保留67.8%的MMLU准确率，效果和能力保留均优于基线；TruthfulQA MC1准确率从41.0%提升到58.6%；CounterFact事实编辑有效率从16.8%提升到96.3%。

### 核心结论
MoE的路由主要匹配输入语义，行为控制完全可以在不改变原生专家分配的前提下实现，路由一致性是MoE表征工程的核心设计原则。
