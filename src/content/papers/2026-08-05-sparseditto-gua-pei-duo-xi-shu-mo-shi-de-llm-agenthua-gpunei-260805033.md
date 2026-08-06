---
title: 'SparseDitto: Customizing GPU Kernels for Different Sparsity Patterns with
  LLM-Based Agentic System'
title_zh: SparseDitto：适配多稀疏模式的LLM Agent化GPU内核定制系统
authors:
- Shiyang Li
- Guangyan Sun
- Jinwei Tang
- Yanzhi Wang
- Mingyi Hong
- Caiwen Ding
affiliations:
- University of Minnesota
- Northeastern University
arxiv_id: '2608.05033'
url: https://arxiv.org/abs/2608.05033
pdf_url: https://arxiv.org/pdf/2608.05033
published: '2026-08-05'
collected: '2026-08-06'
category: Agent
direction: Agent 代码生成 · GPU算子优化
tags:
- LLM Agent
- GPU Kernel
- Sparse Matrix
- SpMM
- Code Generation
one_liner: 基于LLM Agent的框架为不同稀疏模式、算子、GPU自动生成最优稀疏运算GPU内核，性能远超cuSPARSE等方案
practical_value: '- 可复用「结构特征预筛选 + 领域先验排序 + LLM代码生成 + 硬件实测迭代」的Agent优化范式，落地到推荐系统常用的GNN推理/训练、稀疏Embedding查表等GPU算子优化，无需从零构建代码生成Agent工作流

  - 论文提出的36维稀疏算子结构特征（行分布、块占用、中间计算量等）可直接复用，用于判断业务稀疏数据适配的算子类型，避免踩cuSPARSE不同格式350×性能差的坑

  - 多Agent分工（规划/编码/验证）+ 分层搜索（先策略再参数再实测）的设计可迁移到其他硬件相关的LLM代码生成任务，比如端侧推理算子优化，降低无效生成成本'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
稀疏矩阵运算（SpMV/SpMM/SpGEMM）是GNN召回、大模型稀疏推理的核心算子，现有库（如cuSPARSE）和专用优化方案对稀疏模式、算子、GPU架构的适配性极差，同矩阵同算子不同存储格式性能差可达350×，无统一方案能跨场景保持最优性能。

### 方法关键点
- 预提取36维稀疏矩阵结构特征（含固有模式、存储格式开销、算子专属计算特征三类），用离线训练的可解释加性能量模型对成熟优化策略排序，大幅缩小搜索空间
- 分层架构感知规划器：先匹配GPU硬件参数（SM数、缓存、寄存器限制），再确定数据表示、执行策略，最后绑定Tile大小、启动参数等硬件专属配置
- 多Agent协作：编码Agent自动生成CUDA代码，验证Agent做正确性校验和目标GPU实测，基于性能反馈迭代优化，支持跳出预设策略集生成定制化方案

### 关键结果
在60个SuiteSparse稀疏矩阵上验证，覆盖SpMV、4种宽度的SpMM、SpGEMM，对比cuSPARSE等5种SOTA方案：RTX PRO 6000上几何平均提速2.68×，最高146.61×；H200上几何平均提速2.79×，最高78.5×；用于GCN训练最高提速3.39×；36%的最优方案不在预设策略集内，平均提速比预设集高26%。

### 核心启示
硬件相关的代码优化类Agent，必须用「领域先验约束搜索空间 + 目标环境实测反馈迭代」的设计，而非放任LLM自由生成，才能兼顾探索性和落地效率。
