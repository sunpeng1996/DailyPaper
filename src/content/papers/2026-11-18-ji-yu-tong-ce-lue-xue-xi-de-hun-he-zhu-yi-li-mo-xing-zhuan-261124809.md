---
title: On-Policy Morphing into Hybrid Attention Models
title_zh: 基于同策略学习的混合注意力模型转换方法FlashMorph2
authors:
- Disen Lan
- Xuanda Wang
- Jianbin Zheng
- Huafeng Kuang
- Wei Tang
- Yu Cheng
affiliations:
- Fudan University
- ByteDance Seed
- Nanyang Technological University
arxiv_id: '2611.24809'
url: https://arxiv.org/abs/2611.24809
pdf_url: https://arxiv.org/pdf/2611.24809
published: '2026-11-18'
collected: '2026-11-19'
category: LLM
direction: LLM效率优化 · 混合注意力层选择
tags:
- Hybrid Attention
- On-Policy Learning
- Long Context LLM
- Model Compression
- FlashMorph2
one_liner: 提出同策略层选择方法FlashMorph2，实现Transformer到混合注意力模型的高效高质量转换
practical_value: '- 业务中使用LLM做推荐文案生成、多轮Agent推理的场景，可直接用FlashMorph2将现有预训练LLM转为混合注意力模型，无需从头预训练即可降低KV
  cache开销、提升长上下文吞吐量

  - 层选择trick可复用：采用Gumbel-TopK采样离散架构+联合优化层选择分数与模型权重，比固定插层、逐层敏感性评估效率高数倍，适合快速迭代不同混合比例的业务模型

  - 同策略优化思路可迁移到推荐系统结构搜索：比如召回/排序层的结构选择，直接在候选结构上做端到端前向+权重自适应，比离线打分更贴合上线后实际效果'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
混合注意力模型仅在少量层保留全注意力、其余层使用线性注意力，可兼顾长上下文建模能力和推理效率，大幅降低KV cache开销，已在工业界LLM落地中广泛采用。但现有Transformer转混合注意力的层选择方法存在两个off-policy偏差：一是连续门插值、教师强制隐状态和实际部署的离散混合计算逻辑不一致；二是层选择时权重冻结，未考虑后续恢复训练的参数自适应，导致选出的层配置性能不及预期。

### 方法关键点
- 采用Gumbel-TopK采样满足全注意力层预算的离散混合架构，端到端前向传播使用模型自身生成的隐状态，解决计算逻辑的off-policy偏差
- 层选择阶段联合优化层选择分数和模型权重，采用和后续恢复训练相同的logits蒸馏目标，让层选择结果适配权重自适应后的实际性能
- 用带预算约束的直通估计器解决离散TopK选择的不可导问题，实现层选择分数的梯度回传

### 关键实验
在Qwen3 0.6B/1.7B/8B系列模型、Lightning/GLA/GDN三种线性注意力变体上测试，对比Uniform、PostNAS、KL-LS、HALO、FlashMorph等基线：RULER平均分比FlashMorph高+2.42，LongBench高+1.08，召回密集型任务高+0.76；0.6B到8B模型层选择仅需0.72~3.57 GPU小时，比HALO快8.4~20.8倍，比KL-LS快560~854倍。

**最值得记住的一句话**：混合注意力层选择必须同时考虑部署时的离散计算逻辑和恢复训练的权重自适应，同策略优化能以极低额外成本大幅提升转换后模型的长上下文和召回性能。
