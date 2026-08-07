---
title: 'M$^3$Prune: Hierarchical Collaborative Pruning for Efficient Multi-Modal Multi-Agent
  Retrieval-Augmented Generation'
title_zh: M³Prune：面向多模态多智能体RAG的分层协同通信剪枝框架
authors:
- Taolin Zhang
- Weizi shao
- Zijie Zhou
- Chen Chen
- Daiyang Yu
- Tingyuan Hu
- Chengyu Wang
- Xiaofeng He
affiliations:
- Hefei University of Technology
- East China Normal University
- China University of Petroleum (Beijing)
- Guangdong University of Finance and Economics
- Alibaba Group
arxiv_id: '2608.05967'
url: https://arxiv.org/abs/2608.05967
pdf_url: https://arxiv.org/pdf/2608.05967
published: '2026-08-06'
collected: '2026-08-07'
category: MultiAgent
direction: 多智能体 · mRAG通信效率优化
tags:
- Multi-Agent
- mRAG
- Communication Pruning
- Graph Sparsification
- Multimodal
one_liner: 通过分层剪枝多模态多智能体通信边，同时提升mRAG任务精度与token效率
practical_value: '- 多模态多Agent系统通信优化可复用分层剪枝思路：先做模态内连接剪枝再做跨模态连接剪枝，可直接降低token开销，同时提升推理精度，适配电商多模态商品咨询、内容生成等成本敏感场景

  - 可复用模态对齐损失设计：在跨模态（商品图+标题/属性/评论）Agent协作中加入语义对齐约束，减少跨模态信息冲突导致的推理错误，提升商品问答、多模态推荐准确率

  - 鲁棒性设计可迁移到业务高风险场景：通过动态剪枝低质量/恶意Agent的通信边，降低错误信息对系统的干扰，适配大促场景下的智能客服、内容审核链路

  - 剪枝拓扑仅需几十条训练样本即可收敛，业务冷启动成本低，无需大量标注数据即可落地'
score: 8
source: arxiv-cs.MM
depth: full_pdf
---

### 动机
现有多模态多智能体RAG（mRAG）系统普遍采用固定通信拓扑，存在大量冗余交互，既推高token与计算成本，还会引入噪声干扰推理导致准确率下降，难以大规模落地到电商、搜索等对时延、成本敏感的业务场景。

### 方法关键点
- **模态内图稀疏化**：为文本、视觉模态分别构建时空通信图，用Gumbel-Softmax初始化可学习软邻接矩阵，基于边对最终任务的贡献动态评估重要性，稀疏化低价值连接
- **跨模态图稀疏化**：构建跨模态时空通信图，学习跨模态边权重的同时加入模态对齐损失，约束跨模态语义理解一致性，减少冲突信息对推理的干扰
- **渐进式边剪枝**：训练阶段按衰减的剪枝率逐步移除低权重边，推理阶段直接使用剪枝后的固定拓扑，无需额外计算开销

### 关键结果
在ScienceQA（领域专用）、Vidoseek、MultimodalQA（通用）三个mRAG基准上测试，对比单Agent、固定拓扑多Agent等强基线，相比最优多模态多Agent baseline，准确率提升9.4%，token效率提升23.8%，且对抗扰动下性能下降幅度仅为基线的1/3左右，鲁棒性显著提升。

### 核心结论
多智能体系统效率优化的核心不是盲目增加Agent数量，而是通过剪枝保留高价值通信链路，才能实现效果与成本的最优平衡。
