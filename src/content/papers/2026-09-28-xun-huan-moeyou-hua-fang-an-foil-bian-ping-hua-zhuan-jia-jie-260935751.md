---
title: 'How to Loop MoE: Flatten the Experts, Untie the Attention'
title_zh: 循环MoE优化方案Foil：扁平化专家，解耦注意力
authors:
- Shouren Wang
- Chuang Ma
- Mohsen Hariri
- Debargha Ganguly
- Wang Yang
- Xiaoqing Tong
- Qianying Liu
- Xiaotian Han
- Vipin Chaudhary
affiliations:
- Case Western Reserve University
- Kyoto University
- NII LLMC
arxiv_id: '2609.35751'
url: https://arxiv.org/abs/2609.35751
pdf_url: https://arxiv.org/pdf/2609.35751
published: '2026-09-28'
collected: '2026-09-29'
category: Training
direction: MoE架构优化 · 循环Transformer
tags:
- MoE
- Looped Transformer
- Expert Utilization
- Model Efficiency
- Routing Optimization
one_liner: 固定参数量与计算量下，通过扁平化专家、解耦注意力提升循环MoE效果与路由质量
practical_value: '- 自研MoE大模型（用于生成式推荐/Agent推理）时，可复用Foil的扁平化设计：总专家参数量、单token计算量固定的前提下，减少循环块层数、增加单层专家数、提升循环次数，可无额外成本获得效果增益

  - 循环MoE的注意力层不要跨循环步共享，给每个循环步分配独立的注意力参数，不会增加计算量，还能同时提升路由均衡度和置信度，下游任务效果更优

  - MoE专家健康度评估不要只看负载均衡，新增MMR（路由置信度）指标，当MMR随循环步出现峰值时，说明循环次数已达最优，继续增加不会有收益，可作为调优停止信号'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
Looped Transformer通过重复调用单块层提升参数利用率，MoE通过稀疏激活用少量计算支撑超大参数量，二者结合的循环MoE可让单token在不同循环步路由到更多专家，大幅提升专家利用率，但此前没有研究在固定参数量和计算量的约束下，如何最优设计循环MoE的专家分布和参数共享策略。

### 方法关键点
- 提出Foil架构，核心两个优化：1）扁平化专家：将循环块的层数减半、单层专家数翻倍、循环次数翻倍，保证总专家参数量、单token专家调用量、有效深度完全不变，仅扩大每次路由的可选专家池；2）解耦注意力：专家和路由层跨循环步共享，每个循环步分配独立的注意力参数，不增加额外计算量，仅补全扁平化过程中损失的注意力参数量
- 提出三个评估专家利用率的指标：单token触达的distinct专家数、负载均衡B2、路由置信度MMR（第一选择概率与中位专家概率的比值）

### 关键实验
在FineWeb-Edu数据集上训练，基线是未扁平化的循环MoE，参数量均为553.7M：20B token预训练时所有Foil模型损失均低于基线；100B token训练时损失随扁平化程度单调下降，最扁平的Foil-1比基线低0.012 nat，下游零样本效果持平或更优；相同结构下，解耦注意力比共享注意力的模型100B token时损失低0.049 nat，路由更健康。

### 最值得记住的话
循环MoE的扁平化扩宽专家层和增加循环次数是互补的，二者收益互相放大，固定预算下优先选择少层多专家+多循环+解耦注意力的设计。
