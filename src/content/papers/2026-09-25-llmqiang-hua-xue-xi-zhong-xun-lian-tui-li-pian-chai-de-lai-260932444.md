---
title: 'Rethinking Training-Inference Mismatch in LLM Reinforcement Learning: Where
  It Arises and How to Correct It'
title_zh: LLM强化学习中训练推理偏差的来源分析与校准修正方法
authors:
- Tianrun Yu
- Kaixiang Zhao
- Shangzhe Li
- Yuxiao Yang
- Porter Jenkins
- Weitong Zhang
- Taylor W. Killian
affiliations:
- Brigham Young University
- University of North Carolina at Chapel Hill
arxiv_id: '2609.32444'
url: https://arxiv.org/abs/2609.32444
pdf_url: https://arxiv.org/pdf/2609.32444
published: '2026-09-25'
collected: '2026-09-29'
category: Training
direction: LLM强化学习 · 训练推理偏差修正
tags:
- Reinforcement Learning
- Training-Inference Mismatch
- Importance Sampling
- MoE
- GRPO
- RLVR
one_liner: 提出校准重要性采样CIS，解决LLM强化学习训练推理概率不一致导致的训练不稳定问题
practical_value: '- 做LLM4Rec、Agent的RLHF/RLVR训练时，尤其使用MoE模型，可替换原有TIS/IcePop为CIS，降低梯度方差、避免训练崩溃，实测MoE场景下平均精度比基线高0.6~2个点

  - CIS置信度感知的动态权重截断思路可迁移到推荐系统off-policy评估、样本重加权场景，解决低置信样本偏差集中的问题

  - 工程实现极轻量，仅需逐token计算置信度p_t，将权重截断为min(k_t, 1+λ*max(1-p_t, κ))，无额外前反向开销，可无缝接入现有RL训练框架'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前LLM强化学习（尤其RLVR）为提升吞吐量，普遍将rollout生成（推理引擎）与梯度计算（训练引擎）解耦，即使加载完全相同的参数，二者因内核实现、数值精度、MoE路由差异会对同token给出不同概率，导致名义on-policy训练实际变为off-policy。传统重要性采样会因个别token权重过大导致梯度方差爆炸，固定阈值截断（TIS）又会让偏差集中在低置信token，MoE模型尤其容易出现训练不稳定甚至崩溃。
### 方法关键点
- 提出ratio-displacement恒等式，将重要性权重k_t拆解为token置信度p_t和仅反映引擎偏差的log-odds位移ε_t，实测ε_t分布几乎不随p_t变化，权重爆炸仅由ε_t的重尾上侧导致
- 设计CIS算法：仅对ε_t上侧做固定阈值截断，映射回权重空间后得到随p_t升高而收紧的动态截断阈值，避免低置信token承担过多截断偏差
- 加入数值floor κ=5e-3，避免高置信token阈值过小误截断rounding error，无额外计算开销
### 关键实验
在3个MoE模型（Qwen1.5-MoE-A2.7B、DeepSeek-V2-Lite、Qwen3-30B-A3B）、5个数学推理基准上测试，对比TIS、IcePop、KPop等9种基线：
- CIS在所有3个模型上均取得最高的5基准平均精度，比无修正方法高1.62~3.79个点，比次优基线高0.6~0.65个点
- 相比固定阈值的TIS，CIS整体截断偏差低18%，梯度方差控制在合理范围
### 核心结论
训练推理偏差的修正要从偏差本身的统计特性出发，而非直接对最终权重加固定阈值，置信度感知的动态截断能实现更优的偏差-方差权衡。
