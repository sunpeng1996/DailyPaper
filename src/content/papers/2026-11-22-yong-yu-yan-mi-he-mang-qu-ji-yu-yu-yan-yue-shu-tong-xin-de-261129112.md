---
title: 'Bridging Blind Spots With Words: Decentralized Multi-View Spatial Reasoning
  via Language-Constrained Communication'
title_zh: 用语言弥合盲区：基于语言约束通信的去中心化多视角空间推理
authors:
- Soumyabrata Chaudhuri
- Joydeep Ghosh
affiliations:
- The University of Texas at Austin
arxiv_id: '2611.29112'
url: https://arxiv.org/abs/2611.29112
pdf_url: https://arxiv.org/pdf/2611.29112
published: '2026-11-22'
collected: '2026-11-24'
category: Agent
direction: 多Agent协作 · 语言约束空间推理
tags:
- MultiAgent
- SpatialReasoning
- MLLM
- LoRA
- MARL
- Communication
one_liner: 提出N智能体多视角空间推理基准，证明语言通信去中心化成本极低，RL可大幅缩小区间
practical_value: '- 多Agent分布式信息融合场景下，优先用自然语言通信替代原始特征传输，兼顾隐私、带宽和跨模型兼容性，可直接复用单轮广播+无视图listener的架构降低耦合

  - 搭建多Agent协作任务测评体系时，可复用双模型认证的数据集分层方法，拆分无需协同、单视角可解、需多视角协同的样本，避免测评结果被简单样本稀释

  - 多Agent RL训练时，优先选用removal credit（留一法信用分配）方案，效果优于joint credit/substitution credit，可复用跨模型迁移的LoRA微调策略降低训练成本'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有多模态大模型（MLLM）的空间推理多基于中心化全视角假设，和多机器人、AR/VR、隐私敏感场景下的分布式局部观测部署存在明显gap，此前语言介导的空间协同仅局限于双智能体简单场景，缺乏通用场景的基准和量化评估。

### 方法关键点
- 通用化N智能体多视角空间推理框架：N个speaker各持1个局部视角，在单条消息词量预算约束下发送自然语言描述，无视图的listener仅基于通信文本回答空间问题，和中心化全视图基线的准确率差定义为去中心化gap
- 双认证多视角基准：整合6个公开多视角数据集共10007条QA，用Qwen3-VL-32B、InternVL3.5-38B两个大模型做分层过滤，拆分盲答可解（A）、单视角可解（B）、需多视角协同（C）三个样本分层，避免文本捷径干扰
- 多智能体RL优化：共享LoRA微调speaker，对比3种信用分配方案（joint/removal/substitution），用团队相对奖励做策略优化

### 关键实验
在5款开源MLLM上测评，90%的场景下语言通信的去中心化gap<4个百分点，部分模型（LLaVA-OV-7B）分布式方案甚至优于中心化基线；best-of-K oracle准确率比中心化基线高20.2个百分点，说明语言通信本身无本质信息损失；用removal credit微调后可缩小60%-65%的gap，和中心化基线差仅3.5个百分点。

最值得记住的一句话：多智能体分布式信息融合的瓶颈不是语言通信的带宽限制，而是如何引导智能体输出任务相关的低冗余有效信息。
