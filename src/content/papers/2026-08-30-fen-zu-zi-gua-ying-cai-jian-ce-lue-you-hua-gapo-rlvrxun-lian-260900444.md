---
title: Group Adaptive Clipping Policy Optimization
title_zh: 分组自适应裁剪策略优化（GAPO）：RLVR训练的轻量优化方法
authors:
- Sheng Jia
- Xiao Wang
- Shiva Prasad Kasiviswanathan
- Rein Houthooft
affiliations:
- University of Toronto
- Amazon
arxiv_id: '2609.00444'
url: https://arxiv.org/abs/2609.00444
pdf_url: https://arxiv.org/pdf/2609.00444
published: '2026-08-30'
collected: '2026-09-07'
category: Training
direction: 大模型RLVR训练 · 自适应裁剪优化
tags:
- RLVR
- PPO
- Adaptive Clipping
- Policy Optimization
- Mathematical Reasoning
- Code Generation
one_liner: 提出RLVR场景下插件式自适应裁剪策略优化方法，跨模型稳定提升数学与代码任务pass@1和pass@k
practical_value: '- 做Agent、LLM驱动电商文案生成的RLHF/RLVR训练时，可直接复用GAPO的自适应裁剪逻辑，针对低成功率的稀有正确样本放开裁剪阈值，保留高价值探索梯度，避免固定裁剪压制难任务优化信号，尤其适合复杂业务场景的冷启动训练

  - 现有GRPO/GSPO训练流程可无侵入接入GAPO，仅需修改裁剪阈值计算逻辑，无需调整损失函数、新增超参数，改动成本极低即可获得性能提升

  - 电商搜索/推荐场景下，对稀有点击/转化样本、长尾query召回样本的模型训练，可借鉴该思路分配更大的更新权重，平衡易/难样本的梯度占比，避免模型过早收敛到头部样本的局部最优'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有GRPO、GSPO等组相对RLVR方法采用固定重要性采样（IS）比率裁剪边界，对低成功率难任务的稀有正确样本（携带强探索梯度信号）和高成功率易任务的大量正确样本一视同仁裁剪，导致高价值梯度被过度压制；均匀调宽裁剪边界无法解决不同优势样本的更新头room错配问题，还可能破坏信任域约束，甚至出现pass@k崩塌。
### 方法关键点
- 基于反向KL信任域推导，最优IS比率与样本优势值呈指数正相关，高优势的稀有正确样本应获得更大的更新头room
- 仅修改裁剪阈值，保留PPO/GSPO原有代理目标，无需奖励/优势整形，直接优化pass@1，避免整形带来的pass@1漂移
- 自适应裁剪阈值公式：$\epsilon_{hi}(c) = \epsilon_{lo} + (\epsilon_{max}^{hi} - \epsilon_{lo}) \cdot \frac{k-c}{k-1}$，其中k为每组rollout数，c为组内正确样本数，仅复用原有裁剪上下界参数
### 关键实验
跨Qwen2.5-Math-1.5B、Llama-3.2-3B-Instruct、DeepSeek-R1-Distill-Qwen-1.5B三个模型测试，对比GRPO、Dr.GRPO、对称/非对称GSPO等基线：AIME24数学任务pass@1最高提升2.7%，代码任务HumanEval+ pass@1提升3.5%；训练后期IS比率与优势值的Pearson相关性保持在0.8以上，远高于基线的负相关水平，同时保留更多问题的求解能力。
### 核心结论
RLVR训练中无需改动损失函数，仅通过自适应调整裁剪阈值为高价值稀有样本分配更大更新空间，就能在不牺牲pass@k的前提下稳定提升pass@1
