---
title: 'LLaDA MoE v2: Scaling Mixture-of-Experts Diffusion Language Models'
title_zh: LLaDA MoE v2：混合专家扩散语言模型的规模化训练方法
authors:
- Fengqi Zhu
- Shaoxuan Xu
- Jingyang Ou
- Zebin You
- Yipeng Xing
- Huabin Liu
- Xiaolu Zhang
- Jun Zhou
- Zhenzhong Lan
- Yankai Lin
affiliations:
- Renmin University of China
- Beijing Key Laboratory of Research on Large Models and Intelligent Governance
- Engineering Research Center of Next-Generation Intelligent Search and Recommendation,
  MOE
- Ant Group
arxiv_id: '2608.03457'
url: https://arxiv.org/abs/2608.03457
pdf_url: https://arxiv.org/pdf/2608.03457
published: '2026-08-03'
collected: '2026-08-05'
category: LLM
direction: 扩散大语言模型 · MoE缩放定律
tags:
- MoE
- Diffusion LLM
- Scaling Law
- Pretraining
- LLaDA
one_liner: 提出MoE扩散语言模型专属缩放定律，训练出性能接近同规模AR模型的30B-A3B LLaDA MoE v2
practical_value: '- 业务侧MoE LLM架构可直接复用本文最优配置：专家粒度取8~16、共享专家比例固定为33.3%，规模化时优先降低激活比例扩大专家池，可在相同激活算力下提升模型效果

  - 训练扩散LLM时可直接套用本文超参缩放公式：最优batch size随算力增长更快、学习率衰减更快，算力分配略向训练数据侧倾斜，可显著提升训练性价比

  - 扩散LLM支持并行解码，可替代AR模型用于电商推荐的实时生成场景（如个性化推荐理由、实时query改写），降低推理延迟，本文SFT方案可直接复用提升下游任务性能'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
扩散语言模型（dLLM）支持多token并行解码，是自回归（AR）语言模型的重要替代方向，但现有MoE架构的dLLM完全沿用AR模型的缩放经验，缺乏针对性的训练、架构设计指导，规模化训练效率低、效果不达预期。

### 方法关键点
1. 校准MoE dLLM超参缩放规律：拟合得到最优batch size、学习率随训练算力变化的幂律公式，相比AR模型，最优batch size增速更快、学习率衰减速率更快
2. 算力分配规则：IsoFLOP分析显示最优token预算增速略高于激活模型计算量，算力分配应小幅向数据侧倾斜
3. MoE架构最优配置：规模越大越适合更低的激活比例，专家粒度G=8~16跨规模鲁棒，共享专家比例稳定为33.3%
4. 基于上述规律训练30B总参、3B激活参的LLaDA MoE v2，预训练token量23.5T，仅为同规模Qwen3的65%

### 关键结果
预训练后在15项通用、推理、编码基准上平均得分58.6，为当前最优dLLM，性能接近同规模AR MoE模型Qwen3；仅经SFT后，在8项推理/编码基准中7项超越SDAR Chat 30B，多语言编码任务MultiPL-E超越Qwen3。

### 最值得记住的结论
MoE扩散语言模型的缩放规律不能直接复用AR模型经验，经针对性校准后可在仅用65%预训练数据的条件下达到同规模AR MoE模型的相近性能。
