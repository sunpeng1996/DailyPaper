---
title: 'SLAI T-Rex: Full-Parameter Post-training of the DeepSeek-V4 Family on Ascend
  SuperPOD'
title_zh: 面向昇腾SuperPOD的DeepSeek-V4系列全参数后训练框架SLAI T-Rex
authors:
- Dongfang Li
- Xiaodong Luo
- Ruoyu Sun
- Xuhui Chen
- Linyuan Qiu
- Jian Meng
- Zhengxuan Lu
- Yiting Wang
- Yucheng Xie
- Tao Guo
affiliations:
- Shenzhen Loop Area Institute
arxiv_id: '2607.20145'
url: https://arxiv.org/abs/2607.20145
pdf_url: https://arxiv.org/pdf/2607.20145
published: '2026-07-21'
collected: '2026-07-23'
category: Training
direction: 万亿参数MoE训练 · 昇腾全栈优化 · 领域后训练
tags:
- MoE
- Post-training
- Ascend NPU
- MFU Optimization
- Domain Specialization
one_liner: 在昇腾SuperPOD上实现万亿参数MoE训练2.93倍MFU提升，配套OR领域后训练流程
practical_value: '- 领域模型微调可复用CPT+SFT两阶段流程：先通过CPT注入领域先验，再用SFT做任务对齐，参考OR领域实验，比直接SFT可带来10%+的结构正确性指标提升

  - 大模型训练性能调优可参考分层优化思路：先做并行策略（如ETP、VPP）和通信计算调度优化，再针对性优化Top瓶颈算子，最后做长尾小算子融合，可快速提升MFU

  - 非CUDA硬件的算子优化可借鉴AuraKernel思路：先通过OR建模确定最优tiling初值，再基于实测反馈闭环迭代，减少无效搜索，降低算子调优的专家依赖'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有万亿参数MoE大模型训练多基于GPU/TPU集群，昇腾等SIMD架构NPU的全参数后训练缺乏成熟的全栈优化方案，同时运筹优化（OR）等工业决策类领域的大模型专项训练pipeline不完善，难以支撑复杂推理类任务的效果要求。

### 方法关键点
- 系统层分层优化：采用专家张量并行（ETP）降低通信开销、虚拟流水线并行（VPP）控制内存占用、MoE调度做同步与计算重叠、双缓冲交换优化器降低内存压力，从并行策略、通信调度层面提升训练效率
- 算子层优化：提出AuraKernel算子优化Agent，基于OR建模做最优tiling初始化，结合实测反馈的闭环迭代优化瓶颈算子；同时做长尾小算子融合，消除冗余内存访问和启动开销
- 领域后训练流程：面向OR任务构建CPT+SFT两阶段流程，CPT阶段用领域数据注入OR建模先验，SFT阶段用求解器验证的高质量样本做任务对齐，配套自蒸馏数据飞轮、CoT增强等数据优化策略

### 关键结果
- 训练效率：1.6T参数的DeepSeek-V4-Pro在昇腾SuperPOD上MFU达到34.22%，比开源基线提升2.93倍，训练稳定性达标
- 领域效果：OR专项微调后的模型零样本Pass@1达到71.81%，比GPT-5.4-Mini高3.98个百分点，比基线DeepSeek-V4-Flash高11.27个百分点；CPT+SFT相比直接SFT在OR结构正确性指标上提升10.66个百分点

### 核心洞察
大模型全栈优化要从并行策略、通信调度、算子性能分层切入，领域专项微调优先做CPT注入领域先验再做SFT对齐，可实现效率与效果的双重提升
