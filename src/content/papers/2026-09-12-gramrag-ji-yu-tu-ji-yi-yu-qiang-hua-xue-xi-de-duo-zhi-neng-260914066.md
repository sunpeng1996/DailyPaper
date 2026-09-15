---
title: 'GraMRAG: Orchestrating Multi-Agent Multi-Step Reasoning via Graph Memory with
  Reinforcement Learning'
title_zh: GraMRAG：基于图记忆与强化学习的多智能体多步推理框架
authors:
- Zhongyu Wang
affiliations:
- Beihang University
arxiv_id: '2609.14066'
url: https://arxiv.org/abs/2609.14066
pdf_url: https://arxiv.org/pdf/2609.14066
published: '2026-09-12'
collected: '2026-09-15'
category: Agent
direction: 多Agent RAG · 图记忆强化学习推理
tags:
- Multi-Agent
- RAG
- Graph Memory
- Reinforcement Learning
- Multimodal Reasoning
one_liner: 提出融合动态多模态记忆图与拓扑感知策略优化的多Agent RAG框架，提升长程跨模态推理性能
practical_value: '- 电商导购、商品信息查询等多轮交互Agent可复用多模态记忆图设计，将用户交互、检索动作、结果的依赖关系建模为DAG，减少重复检索，缓解上下文膨胀，提升长会话推理稳定性。

  - Agent RL训练阶段可复用TAPO策略优化思路，基于推理轨迹拓扑做梯度掩码，避免正样本无效探索被强化、负样本有效检索被惩罚，降低训练成本、提升收敛速度。

  - 以图搜商品等跨模态多跳推理场景可借鉴视觉-文本桥接范式，将多尺度实体裁剪+ReAct视觉工具链结合，把图像信息转成结构化文本后接入文本深搜链路，减少跨模态推理断点。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有多Agent RAG系统在长程多模态推理场景存在三大痛点：一是检索轮次有限，易提前终止探索漏采关键证据；二是线性/迭代摘要式内存结构缺乏推理状态显式建模，交互轮次增多后易出现状态盲、重复检索、上下文膨胀问题；三是基于最终结果的稀疏奖励机制无法做细粒度credit assignment，易误判有效/无效推理步骤，训练收敛慢、效果差。

### 方法关键点
- 视觉-文本桥接推理范式：整合多尺度实体裁剪与ReAct式视觉工具链，先通过分层视觉实体定位、多轮检索收集有效跨模态证据，再将图像转成结构化描述，无缝衔接文本深搜链路，支持数十步长程跨模态推理。
- 多模态记忆图：将多Agent推理过程建模为动态DAG，显式编码不同模态动作、观察的时间与逻辑依赖，从根本上缓解状态盲与冗余检索问题，同时为RL优化提供拓扑结构支撑。
- 拓扑感知策略优化（TAPO）：基于记忆图拓扑做关键路径识别与节点裁剪：正样本中仅给最终答案贡献的关键路径节点分配正奖励，屏蔽无效探索节点；负样本中屏蔽已验证有效的检索节点的惩罚，实现步级细粒度credit assignment。

### 关键实验
在HotpotQA、ViDoSeek、LVBench等9个覆盖文本、视觉文档、长视频的跨模态基准上测试，对比ReAct、Vanilla RAG、Mem1、VimRAG等SOTA基线：基于Qwen3-VL-8B-Instruct backbone时，GraMRAG整体准确率达53.5%，比次优基线VimRAG高3.4个百分点；TAPO相比传统GRPO优化带来4.2个百分点的性能提升，同时训练收敛速度提升30%以上。

**值得记住的一句话**：长程多模态Agent推理的性能瓶颈，本质上不是推理步数不够，而是缺乏结构化的记忆管理与细粒度的奖励信号分配机制。
