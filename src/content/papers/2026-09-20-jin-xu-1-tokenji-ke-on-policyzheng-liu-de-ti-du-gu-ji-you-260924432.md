---
title: '1% of Tokens Can Be Enough: On Gradient Estimation in On-Policy Distillation'
title_zh: 仅需1% Token即可：On-Policy蒸馏的梯度估计优化研究
authors:
- Huanxin Sheng
- Zhiling Ye
- Haonan Wang
- Jian Wang
- Jinjie Gu
- Jian Kang
affiliations:
- MBZUAI
- Ant Group
arxiv_id: '2609.24432'
url: https://arxiv.org/abs/2609.24432
pdf_url: https://arxiv.org/pdf/2609.24432
published: '2026-09-20'
collected: '2026-09-22'
category: Training
direction: 大模型蒸馏 · 稀疏监督Token选择
tags:
- On-Policy Distillation
- Knowledge Distillation
- Gradient Estimation
- Sparse Supervision
- Token Selection
one_liner: 提出梯度可靠性度量IER，仅用0.1%-1% token即可在On-Policy蒸馏中达到全量监督效果
practical_value: '- 做业务场景LLM蒸馏（如客服话术、商品文案生成模型）时，可直接复用IER+现有有用性指标的token选择方案，仅用1%左右token就能达到全量蒸馏效果，大幅降低训练算力成本

  - 梯度估计可靠性是现有token选择逻辑的有效补充，生成式推荐、RAG问答的SFT/RLHF阶段可加入类似IER的梯度噪声筛选，避免噪声梯度带偏模型优化方向

  - IER的候选集近似计算方法可直接落地：仅取师生模型top-K logit+采样token计算，无需遍历全词表，工程实现门槛低，适配多数业务训练框架'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有稀疏On-Policy蒸馏仅基于token有用性（如熵、师生分歧、位置）筛选监督样本，但单采样token的梯度估计存在大量噪声，即使高有用性的token也可能因梯度偏差误导模型更新，在极低监督预算下这一问题会被放大，导致训练效率低、效果不稳定。
### 方法关键点
- 从信息几何角度对reverse KL梯度做信号-噪声分解，提出信息效率比（IER）：衡量最优标量基线下的梯度信噪比，表征梯度估计的可靠性，和现有有用性指标形成互补
- 工程化近似方案：取师生模型top-K logit + 当前采样token构建候选集，仅在候选集上归一化计算IER，避免全词表计算的高开销
- 两种融合算子：用IER-OR（软或，满足高有用性/高可靠性其一即可）和IER-AND（软与，两者均高才入选）结合IER排序与现有有用性指标，适配不同场景需求
### 关键结果数字
在数学推理（AIME 2025/2026、HMMT 2025/2026）、医疗推理（HealthBench）两个任务，强到弱、大到小两种蒸馏设置下：
1. 0.1% token预算下，IER单独使用效果接近全量OPD，医疗场景得分45.25 vs 全量OPD的45.77
2. 1% token预算下，IER结合现有有用性指标（如TIP、TA-OPD）的效果匹配甚至超过全量OPD
3. 0.1%预算下Prefix+IER-OR将医疗任务得分从38.30提升至44.98，远高于原有Prefix方法的效果
### 核心结论
On-Policy蒸馏的效果不随监督token数量单调提升，同时兼顾token有用性与梯度估计可靠性，仅用极少token即可达到全量监督的训练效果。
