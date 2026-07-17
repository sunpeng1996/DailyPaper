---
title: Mask-Aware Policy Gradients for Diffusion Language Models
title_zh: 面向掩码扩散语言模型的掩码感知策略梯度算法
authors:
- Haran Raajesh
- Kulin Shah
- Adam Klivans
- Philipp Krähenbühl
affiliations:
- The University of Texas at Austin
arxiv_id: '2607.15200'
url: https://arxiv.org/abs/2607.15200
pdf_url: https://arxiv.org/pdf/2607.15200
published: '2026-07-16'
collected: '2026-07-17'
category: Training
direction: 扩散大语言模型 · RL训练优化
tags:
- Diffusion LLM
- Policy Gradient
- Reinforcement Learning
- MDLM
- LoRA
one_liner: 将掩码扩散语言模型生成建模为两阶段MDP，联合优化token预测与掩码位置选择实现多任务SOTA
practical_value: '- 若业务用MDLM做生成类任务（如电商文案、推荐理由生成），可直接复用该掩码感知策略梯度方法，仅将贪婪remask替换为概率采样版本，无需修改模型结构即可获得稳定效果提升，无额外参数开销

  - 做LLM/Agent RL微调的团队可复用两阶段MDP拆解思路：若生成/决策流程包含多步隐式决策（如推荐先选召回池再排序、Agent先选工具再生成参数），可将每步决策的log-prob加入策略梯度项，补全遗漏的优化信号

  - 工程层面可直接复用其LoRA+4-bit量化+StepMerge的训练配置，8卡H100即可完成8B规模MDLM的RL训练，收敛速度快于传统ELBO-based
  RL方法，适合算力有限的团队落地MDLM对齐'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
RL已被证明能大幅提升LLM的推理能力，但适配掩码扩散语言模型（MDLM）时存在log似然估计难以处理的问题，现有方法仅建模token预测损失，完全忽略生成过程中掩码位置选择的决策逻辑，丢失了大量优化信号，限制了MDLM在复杂任务上的表现。

### 方法关键点
- 将MDLM生成过程建模为两阶段动作MDP：每一步先预测所有掩码位置的token，再决策哪些位置保留、哪些重掩码，轨迹似然自然拆解为token项与掩码项两个可优化部分
- 替换原有确定性top-K remask为基于Plackett–Luce分布的概率采样，直接复用模型自身的token预测logit作为位置选择打分，无需新增参数或修改模型结构即可获得可微分的掩码梯度
- 联合优化两个梯度项，兼容所有主流策略梯度算法，搭配StepMerge近似计算轨迹似然，几乎无额外计算开销

### 关键实验
基座采用LLaDA-8B-Instruct，LoRA rank=128、4-bit量化训练，对比GDPO、SPG、StepMerge等SOTA基线：GSM8K最高准确率87.1%（+2.1%），MATH500最高44.2%（+2.4%），HumanEval最高44.0%（+2.9%），MBPP最高53.4%（+2.5%）；训练收敛速度比SPG快17%，达到同等精度的GPU成本仅为新增独立位置头同类方法的1/5。

最值得记住的一句话：对于包含多步决策的生成流程，不要仅优化最终输出的token似然，把每一步隐式决策都纳入策略梯度优化范围，往往能以极低的额外成本获得显著效果提升。
