---
title: Probe-Space Preconditioning for Fast and Stable Zero-Order Training
title_zh: 面向快速稳定零阶训练的探针空间预处理方法
authors:
- Francois Chaubard
- Mykel J. Kochenderfer
- Chris Ré
affiliations:
- Stanford University
arxiv_id: '2609.38095'
url: https://arxiv.org/abs/2609.38095
pdf_url: https://arxiv.org/pdf/2609.38095
published: '2026-09-29'
collected: '2026-09-30'
category: Training
direction: 大模型零阶训练效率优化
tags:
- Zero-Order Optimization
- SPSA
- LLM Fine-tuning
- Memory Efficient Training
- Distributed Training
one_liner: 提出1.5-SPSA零阶优化器，显存较BP降10倍，比MeZO少3个数量级步骤达SOTA
practical_value: '- 显存不足的大模型微调场景（如30B级LLM做推荐文案生成、Agent工具调用微调）可直接用1.5-SPSA，仅推理级显存（OPT-30B仅需60GB），单A100就能跑全参数微调，无需复杂模型分片

  - 零阶优化计算分配可直接复用结论：固定总前向传播预算下，优先提升单步batch size和扰动数、减少迭代步数，配合分布式并行能大幅降低墙钟时间，适合业务快速迭代需求

  - 轻量预条件trick可复用：单步加1次无扰动前向传播计算探针空间曲率权重，无需额外O(d)内存就能提升训练稳定性，允许更大学习率，病态Loss场景收敛速度最多提7倍

  - 工程实现可直接复用8-bit打包扰动+Triton融合核方案，比原生PyTorch实现提速2.76倍，降低单步开销'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
反向传播（BP）训练大模型显存开销极高，OPT-30B用Adam训练需约600GB显存，普通硬件无法支持，且依赖复杂分布式分片。现有零阶优化（ZOO）方法如MeZO收敛速度慢，需10万级迭代步，训练稳定性差，无法满足业务快速微调需求。
### 方法关键点
- 计算预算重分配：固定总前向传播次数下，将资源从多迭代步转向单步更大有效batch、更多扰动，大幅减少迭代步数，单步计算可全并行，墙钟时间随GPU数量线性下降
- 1.5-SPSA算法：在1SPSA基础上每步加1次无扰动前向传播，计算每个扰动方向的局部曲率，采用α=0.1的饱和权重下调高曲率方向的更新步长，无需存储O(d)级优化器状态，仅推理级显存即可实现预条件加速
- 工程优化：采用8-bit打包Rademacher扰动生成、Triton融合解包/应用核、种子式分布式并行，仅传输标量损失，通信开销极低
### 关键实验结果
在OPT、Qwen3两个模型族的GLUE/SuperGLUE等6个下游任务对比MeZO、BP+Adam等基线：
- OPT-13B SST-2任务：1.5-SPSA仅70步达94.5%准确率，比MeZO（10万步）高3.1%，比BP高2.5%，总前向传播次数少44倍
- 病态Loss场景（条件数κ=1000）下，收敛速度比1SPSA最高快7倍，单8xA100节点即可支持OPT-30B全参数训练
### 核心结论
零阶优化无需盲目堆迭代步数，合理分配单步计算量+轻量探针空间预条件，即可实现显存、速度、效果的三赢
