---
title: 'DAIN: Dynamic Agent-Based Interaction Network for Efficient and Collaborative
  Multimodal Reasoning'
title_zh: DAIN：基于动态Agent的交互网络实现高效协作多模态推理
authors:
- Xinxin Chen
- Yuchen Li
- Zihan Wang
- Haoyu Zhang
- Ruixin Liu
- Mingyuan Zhao
affiliations:
- University of Chinese Academy of Sciences
arxiv_id: '2606.30189'
url: https://arxiv.org/abs/2606.30189
pdf_url: https://arxiv.org/pdf/2606.30189
published: '2026-06-29'
collected: '2026-06-30'
category: Agent
direction: Agent 多智体多模态推理优化
tags:
- MultiAgent
- MoE
- Multimodal Reasoning
- Sparse Activation
- Interpretability
one_liner: 将多模态融合重构为动态多Agent协作过程，实现性能与推理效率的双重提升
practical_value: '- 电商多模态商品/广告推荐场景，可复用三类Agent分工设计替代原有MoE专家，通过Meta-Controller动态激活30%-60%的Agent，在不损失效果的前提下降低推理时延

  - Agent间通信的低秩压缩+动态图正则设计，可直接迁移至多Agent协作的推荐系统中，减少跨模块信息传递的冗余开销，适配高QPS在线服务

  - 多目标损失中的Agent专用性正则+稀疏激活正则，可用于优化现有大参数量MoE推荐模型，解决专家坍塌、推理成本高的问题

  - Agent激活分布可作为多模态推荐的可解释性依据，快速定位影响推荐结果的核心模态（如商品图/标题/属性），提升badcase排查效率'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有基于静态MoE架构的多模态融合方法缺乏动态自适应协作能力，无法针对性建模单模态独有、跨模态协同、多模态冗余三类不同的信息交互模式，全量激活专家的设计导致计算成本高，且难以适配复杂场景下的性能效率平衡需求。

### 方法关键点
- 基于Partial Information Decomposition（PID）理论将交互Agent分为三类：Synergy Agent建模跨模态协同信息，Uniqueness Agent提取单模态独有特征，Redundancy Agent捕捉多模态共享冗余信息
- 引入Meta-Controller，基于多模态聚合的上下文向量动态生成稀疏激活向量，仅调度相关Agent子集执行计算，同时生成上下文感知的通信图控制Agent间信息流动强度
- 激活的Agent之间通过低秩投影压缩通信消息，状态更新后经多头注意力共识模块融合输出最终预测
- 多目标损失联合优化任务效果、Agent专用性、激活与通信稀疏性，在提升性能的同时约束计算开销

### 关键实验
在ADNI、MIMIC-IV、MM-IMDB、CMU-MOSI、ENRICO 5个跨领域多模态基准上，对比Early Fusion、静态MoE、MMoE等基线，ADNI数据集准确率提升2.6%，MIMIC-IV提升1.7%，MM-IMDB提升2.1%；单卡A100训练最快2小时收敛，有效参数量仅5.8M，比同规模静态MoE低53%。

### 核心结论
多模态融合不需要全量激活所有计算单元，基于输入上下文动态调度专用Agent+轻量化通信，能同时实现性能提升和推理成本下降。
