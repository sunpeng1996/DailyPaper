---
title: How Much Training-Inference Mismatch Can On-Policy Distillation Tolerate?
title_zh: On-Policy蒸馏可容忍的训练-推理失配上限研究
authors:
- Cong Yu
- Ziting Wang
- Songlin Jiang
- Sitong Zhang
- Chengliang Chai
- Youhe Jiang
- Eiko Yoneki
- Tuo Shi
affiliations:
- Aalto University
- Nanyang Technological University
- Beijing Institute of Technology
- University of Cambridge
- Shenzhen University of Advanced Technology
arxiv_id: '2611.11450'
url: https://arxiv.org/abs/2611.11450
pdf_url: https://arxiv.org/pdf/2611.11450
published: '2026-11-07'
collected: '2026-11-10'
category: Training
direction: On-Policy蒸馏 · 训练推理一致性优化
tags:
- On-Policy Distillation
- Training-Inference Mismatch
- FP8 Quantization
- KV Cache
- LLM Training
one_liner: 量化OPD训练-推理失配容忍阈值，提出低成本准入校验，兼容FP8/异步rollout提效1.62倍
practical_value: '- 做生成式推荐/Agent的RLHF/OPD蒸馏时，无需过度追求训练推理完全一致，可在失配阈值内用FP8量化KV cache，最高提升1.93倍并发，不损训练质量

  - 异步rollout可直接复用，权重最多滞后8个版本仍不影响OPD效果，训练吞吐量提升1.62倍，大幅降低大模型蒸馏的时间成本

  - 可复用文中轻量准入校验方法：新rollout配置（量化/异步）无需全量训练，用少量样本算失配度即可快速判断可用性，单GPU仅需24分钟完成6种配置校验

  - 电商场景LLM生成文案/推荐结果的蒸馏场景，优先保留第一层KV cache为BF16，可避免93%+的量化失配，无需全层BF16浪费显存'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
On-Policy蒸馏（OPD）是大模型对齐的核心后训练步骤，rollout生成占单步训练时间76%，业界常用FP8量化、异步rollout降本，但两类优化都会引入训练-推理失配。RL场景下这类失配易导致训练崩溃，但OPD的失配容忍度一直缺乏量化研究，无法平衡降本收益与训练质量损耗。
### 方法关键点
- 统一失配度量：用rollout引擎与训练模型的next-token分布的每token KL散度（nats/token）作为统一指标，覆盖量化、权重滞后、数值精度差异所有失配来源
- 定义失配预算：OPD训练质量无明显劣化（held-out KL相对上升<20%）时的最大失配度阈值，不同模型单独校准
- 轻量准入校验：新rollout配置无需全量训练，仅生成少量样本离线计算与标准BF16引擎的失配度，乘以安全系数即可快速判断是否在预算内
### 关键实验
覆盖1.5B/3B/7B三类学生模型，测试6种量化配置、5种异步权重滞后梯度、4种权重噪声梯度，对比REINFORCE、GRPO两类RL方法：
- 7B模型OPD可容忍失配度达标准引擎的200倍，相同失配下REINFORCE、GRPO分别在12倍、60倍时即训练崩溃
- 失配预算内，FP8量化KV cache可承载1.93倍BF16的token容量，结合异步rollout比同步BF16训练提速1.62倍，训练质量无明显下降
- 第一层KV cache是量化失配核心来源，保留其为BF16可降低93%~99%的FP8量化失配

OPD天生比RL更耐受训练推理失配，只要在校准后的预算内，可大胆使用量化、异步等手段降本，无需过度追求训练推理完全一致
