---
title: 'AGE: Adaptive-masking for Graph Embedding in Graph Retrieval-Augmented Generation'
title_zh: AGE：面向GraphRAG的自适应掩码图嵌入方法
authors:
- Bao Long Nguyen Huu
- Atsushi Hashimoto
affiliations:
- OMRON Corporation
- OMRON SINIC X Corporation
arxiv_id: '2607.00052'
url: https://arxiv.org/abs/2607.00052
pdf_url: https://arxiv.org/pdf/2607.00052
published: '2026-06-30'
collected: '2026-07-02'
category: RAG
direction: GraphRAG · 自适应掩码图嵌入
tags:
- GraphRAG
- Self-Supervised Learning
- Reinforcement Learning
- JEPA
- Knowledge Graph
one_liner: 提出RL引导的自适应掩码图嵌入框架AGE，在冻结LLM下显著提升GraphRAG问答精度
practical_value: '- 电商/广告场景的知识图谱RAG可直接复用AGE的自适应掩码策略，替代随机掩码提升图嵌入与冻结LLM的特征对齐度，无需全量微调LLM，大幅降低部署成本

  - 可复用RL驱动的关键节点采样思路，在商品/用户/内容关系图谱中自动识别核心节点（如爆款商品、高价值用户），优化子图检索和嵌入质量

  - 三类损失优化disjoint参数的设计可直接复用，无需手动调整损失权重，降低训练调参成本，适配小参数量LLM的边缘部署场景'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
GraphRAG可补充普通RAG缺失的结构化关系表征能力，但存在图嵌入与冻结LLM文本特征空间对齐差的问题；针对文本设计的随机掩码SSL在冗余度极低的图结构上训练效率低下，关键节点被掩码会严重降低训练效果，而全量微调LLM或训练可学习检索器的计算成本过高，不适用于业务落地场景。

### 方法关键点
- 架构对齐文本嵌入编码器的掩码SSL思路，采用JEPA框架避免Token级细节重建，提升嵌入的语义表征能力
- 新增RL训练的节点采样器，自适应识别图中的关键节点，仅对辅助节点做掩码预测，解决随机掩码的低效问题，最优关键节点采样率ρ=0.3
- 设计三类无权重冲突的损失函数：prompt tuning loss优化目标编码器，target loss优化编解码器实现JEPA蒸馏，sampling loss用REINFORCE优化节点采样器，三者优化参数无重叠，无需手动调整损失权重

### 关键实验结果
在ExplaGraphs、SceneGraphs、WebQSP、CWQ四个GraphQA基准数据集上测试，基线为G-Retriever、AMAR等SOTA方法。冻结Llama3.2-1B时，AGE比G-Retriever在ExplaGraphs上精度提升26.72个百分点，WebQSP上Hit@1提升2.02个百分点；结合LoRA时Llama2-7B+AGE+AMAR在CWQ上Hit@1达85.2，远超基于GPT-4的LLM检索器方法ReKnoS的68.2。

### 核心结论
图结构的冗余度远低于文本，针对文本设计的随机掩码SSL不直接适配图嵌入场景，通过自适应保留关键节点的掩码策略，可在仅优化图嵌入模块、冻结LLM的低计算成本下，大幅提升GraphRAG的下游任务性能。
