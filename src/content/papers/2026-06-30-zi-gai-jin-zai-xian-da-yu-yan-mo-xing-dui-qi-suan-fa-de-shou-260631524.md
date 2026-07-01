---
title: On the Convergence of Self-Improving Online LLM Alignment
title_zh: 自改进在线大语言模型对齐算法的收敛性分析与优化
authors:
- Xudong Wu
- Pangpang Liu
- Vaneet Aggarwal
- Jiayu Chen
affiliations:
- The University of Hong Kong
- Yale University
- Purdue University
arxiv_id: '2606.31524'
url: https://arxiv.org/abs/2606.31524
pdf_url: https://arxiv.org/pdf/2606.31524
published: '2026-06-30'
collected: '2026-07-01'
category: Training
direction: 在线LLM对齐 · 收敛性优化
tags:
- LLM Alignment
- Online RLHF
- Convergence Analysis
- Reverse KL
- SAIL
- Sample Complexity
one_liner: 为在线LLM对齐的SAIL算法引入RevKL正则，证明全局收敛，样本复杂度与实际效果均优于基线
practical_value: '- 做LLM驱动的电商导购、客服Agent对齐时，可直接引入RevKL正则替代普通KL约束，有效缓解在线迭代的分布漂移问题，减少性能震荡，提升对齐效果

  - 在线RLHF迭代调优场景下，可参考论文给出的γ系数、步长、batch size设置逻辑，将样本复杂度从Õ(ε^-3)降至Õ(ε^-1 log ε^-1)，大幅降低用户反馈/标注成本

  - 算力有限的业务场景可采用论文验证的仅最后层微调+RevKL方案，对齐效果接近LoRA微调，且稳定性更高，适合中小模型的快速迭代上线'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有在线LLM对齐算法SAIL将双层对齐优化简化为单层，有效降低了计算开销，但缺乏正式收敛性保证：原始目标函数海森矩阵无法保证强凹性，仅在初始化附近局部收敛，迭代过程中易受分布漂移影响导致性能不稳定甚至退化，亟需优化优化地形以实现全局收敛。
### 方法关键点
- 提出SAIL-RevKL，在原始SAIL目标中加入Reverse KL散度正则项，引入费舍尔信息矩阵的正曲率重塑优化地形，证明正则后目标在有界参数空间满足Polyak-Lojasiewicz（PL）条件
- 采用投影随机梯度上升框架，保证迭代参数始终落在有界可行域内，理论证明全局线性收敛，样本复杂度达Õ(ε^-1 log ε^-1)，相比通用双层RLHF的Õ(ε^-3)大幅降低
- 量化了正则系数γ的权衡关系：γ足够大时可覆盖全可行域的强凹性，引入的正则偏差有明确上界，可通过调参平衡稳定性与对齐效果
### 关键实验
- MuJoCo连续控制任务上，SAIL-RevKL对比PEBBLE、vanilla SAIL，Cohen's d效应量最高达0.872（大效应），学习稳定性与最终奖励显著提升
- LLM对齐实验覆盖Qwen-0.5B、Phi-3-3.8B、LLaMA-3-8B等模型，在PKU-SafeRLHF上pairwise win率达43%，较DPO提升17pct、较vanilla SAIL提升14pct，GPT打分差缩小1.124；UltraFeedback上跨模型win率平均提升11pct
- 仅最后层微调（符合理论对数线性假设）场景下，适度γ时win率较vanilla SAIL最高提升8pct，验证了理论结论的落地有效性
### 核心结论
在线LLM对齐中，反向KL正则可将SAIL的局部收敛扩展为全局收敛，在降低样本复杂度的同时显著提升迭代稳定性与对齐效果
