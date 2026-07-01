---
title: Geometry-Preserving Orthonormal Initialization for Low-Rank Adaptation in RLVR
title_zh: 面向RLVR场景低秩适配的保几何正交初始化方法
authors:
- Ruijia Zhang
- Jiacheng Zhu
- Hanqing Zhu
- Laixi Shi
affiliations:
- Johns Hopkins University
- Meta
- The University of Texas at Austin
arxiv_id: '2606.31813'
url: https://arxiv.org/abs/2606.31813
pdf_url: https://arxiv.org/pdf/2606.31813
published: '2026-06-30'
collected: '2026-07-01'
category: Training
direction: 大模型参数高效微调 · LoRA初始化优化
tags:
- LoRA
- RLVR
- PEFT
- Orthonormal Initialization
- SVD
one_liner: 设计两种保几何正交初始化LoRA变体，稳定RLVR训练且性能优于标准LoRA
practical_value: '- 做LLM的RLHF/RLVR类微调（如Agent工具调用能力优化、推荐个性化文案生成RL微调）时，避免直接使用PiSSA/MiLoRA等带奇异值缩放的SVD初始化LoRA，防止训练不稳定崩溃

  - 可直接复用LoRA-RLPO/RLMO初始化方案：B矩阵初始化为0，A矩阵从预训练权重SVD的右奇异向量提取（主成分或尾子空间），无需奇异值缩放，既能缩小与全量微调的差距，又能保证训练稳定，性能比标准LoRA高1~3个百分点

  - 若暂不修改初始化逻辑，使用DCT/Haar小波等随机正交矩阵初始化A矩阵，也可稳定RL类微调，且性能优于标准随机初始化LoRA'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
SFT场景下表现优异的PiSSA、MiLoRA等SVD初始化LoRA变体，在RLVR（基于可验证奖励的强化学习微调）场景下会出现训练不稳定、性能甚至低于标准LoRA的问题；而RLVR是当前推理、代码、Agent能力优化的核心微调范式，亟需适配RLVR的LoRA初始化方案。
### 方法关键点
- 理论证明当B矩阵初始化为0时，A矩阵行正交初始化可最小化LoRA与全量微调的效果差距，同时控制更新幅度避免突破RLVR的隐式KL约束
- 设计两种保几何正交初始化变体：LoRA-RLPO取预训练权重SVD的前r个右奇异向量作为A初始值，LoRA-RLMO取后r个右奇异向量作为A初始值，均保持B初始为0，无奇异值缩放
### 关键实验
在DeepSeek-R1-Distill-Qwen-1.5B上用DAPO算法微调数学推理任务，对比标准LoRA、PiSSA、MiLoRA：LoRA-RLPO平均准确率达65.03%，LoRA-RLMO达63.76%，分别比标准LoRA高2.63、1.36个百分点；训练过程KL散度低于标准LoRA，无训练崩溃问题。
最值得记住的结论：RLVR场景下LoRA初始化的核心是避免奇异值缩放带来的梯度放大，正交初始化+无缩放是兼顾性能和稳定性的最优选择。
