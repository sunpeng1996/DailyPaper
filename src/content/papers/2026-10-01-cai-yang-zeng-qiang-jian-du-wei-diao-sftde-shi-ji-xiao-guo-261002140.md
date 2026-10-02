---
title: 'Finetuning with Sampling: SFT Learns Better Than You Think'
title_zh: 采样增强监督微调：SFT的实际效果远超传统认知
authors:
- Aayush Karan
- Sitan Chen
- Yilun Du
affiliations:
- Harvard University
arxiv_id: '2610.02140'
url: https://arxiv.org/abs/2610.02140
pdf_url: https://arxiv.org/pdf/2610.02140
published: '2026-10-01'
collected: '2026-10-02'
category: Training
direction: LLM微调 · 采样式数据分布适配
tags:
- SFT
- MCMC
- LLM Finetuning
- On-policy Learning
- Catastrophic Forgetting
one_liner: 通过MCMC投影采样将离线专家数据转换为贴合基模型分布的数据，使SFT泛化性与能力保留优于RL等在线训练方法
practical_value: '- 垂域Agent/生成式推荐SFT微调可优先使用本方法重写专家数据，无需复杂RL调优即可提升新任务效果，同时降低灾难性遗忘

  - 若后续需做RLHF/GRPO训练，可先用采样增强SFT得到的checkpoint初始化，实验显示能进一步提升难样本泛化能力

  - 可借鉴分块MCMC采样思路做垂域文案/推荐理由改写，在保语义正确的前提下生成更符合模型原生表达习惯的内容'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
传统认知中SFT泛化性弱、易发生灾难性遗忘，RL泛化性好但依赖模型自行采样出有效轨迹，难任务下模型无法生成正确轨迹就会丢失学习信号；而SFT能利用离线专家的特权信息，但离线数据和基模型分布差异大导致训练效果差，亟需方法结合两者优势。

### 方法关键点
- 提出投影采样框架：目标生成和离线专家数据语义等价（同属正确集合C）、同时与基模型分布KL散度最小的训练数据
- 基于Metropolis-Hastings MCMC算法实现：初始化用专家轨迹，迭代对序列片段重采样，仅接受语义等价且更贴合基模型分布的候选，保证每步迭代后数据与基模型的KL散度单调下降
- 工程上分块处理长序列，用带专家上下文的prompt引导重采样过程保证语义正确性，仅需训练前一次性完成采样，无推理额外开销

### 关键实验
在化学、数学、医疗三个垂域任务测试，基线覆盖普通SFT、OPSD自蒸馏、GRPO/UFT等RL方法：化学任务相比普通SFT新任务准确率提升4.2pp，原有能力保留率仅降1.1pp，优于OPSD基线；数学任务相比最优RL基线UFT，MATH困难题准确率高2.5pp，MATH500准确率高26.9pp，采样SFT后再做RL可进一步提升8.3pp；医疗任务相比普通SFT原有能力平均保留率提升16.3pp，遗忘程度为所有基线最低。

**最值得记住的一句话**：与其修改训练目标适配离线数据，不如调整数据分布适配基模型，采样增强后的SFT就能达到甚至超过RL的效果，大幅降低垂域微调的落地成本。
