---
title: 'Agora: Enhancing LLM Agent Reasoning Via Auction-Based Task Allocation'
title_zh: Agora：基于拍卖机制的LLM Agent推理任务分配框架
authors:
- Kaiji Zhou
- Ales Leonardis
- Yue Feng
affiliations:
- University of Birmingham
arxiv_id: '2607.09600'
url: https://arxiv.org/abs/2607.09600
pdf_url: https://arxiv.org/pdf/2607.09600
published: '2026-07-10'
collected: '2026-07-13'
category: Agent
direction: Agent 多智体任务分配优化
tags:
- Multi-Agent
- Task Allocation
- Auction Mechanism
- Confidence Calibration
- Reasoning
one_liner: 提出基于校准置信度的拍卖机制，动态分配子任务给最优Agent，兼顾推理效果与成本
practical_value: '- 多模型/多工具路由场景可直接复用这套拍卖机制：将推荐/搜索的子任务（如意图识别、召回、排序、文案生成）作为拍卖单元，基于校准后的模型真实准确率+归一化成本（token费用、latency）计算出价，动态选最优执行方，是无需改动现有Agent内部逻辑的可插拔路由层。

  - 解决Agent过自信问题的两层校准方案可复用：先在通用多领域数据集训练静态Confidence Calibration函数映射模型自报的虚高置信度，再用业务真实反馈（如电商点击/转化、搜索点击率）在线更新校准参数，避免被模型幻觉误导。

  - 成本质量单旋钮调优设计可借鉴：通过调整成本权重β参数，可在效果优先、平衡、成本优先三种模式间一键切换，无需重训路由模型，适配大促低延迟、高价值 query
  高准确率等不同业务场景需求。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有多Agent推理框架的任务路由多为查询级粗粒度匹配，或依赖模型自报置信度，忽略了功能相似Agent间的效果差异、调用成本，还容易被模型的过自信幻觉误导，将关键子任务分配给实际能力不足但虚高报置信度的Agent，导致推理链路失败。

### 方法关键点
1. 任务拆分：Planner将复杂查询拆解为带依赖的原子步骤，合并耦合度高的节点为可执行任务单元
2. 两层置信度校准：先基于通用多领域数据集训练静态校准器，对模型自报的原始置信度做分桶映射；再用在线执行的对错反馈动态调整校准参数，过滤幻觉带来的虚高置信度
3. 拍卖分配：Agent出价 = 校准后置信度的幂变换值 - 成本权重β × 归一化成本（含token费用、latency），选最高出价的Agent执行任务
4. 单旋钮调优：调整β参数即可在效果优先、平衡、成本优先三种模式切换，无需重训

### 关键结果
在5个基准（MuSiQue-Ans多跳QA、MMLU-Pro知识推理、SciCode科学代码、SPIQA多模态科研QA、MathVision视觉数学推理）上对比单模型、FrugalGPT、Hybrid LLM等基线：效果优先模式下，MMLU-Pro准确率达71.9%，较最优单模型提升3.8个百分点；SPIQA严格推理准确率（≥0.8）达56.9%，较最优单模型提升8.7个百分点；调整β可在准确率损失不到1个百分点的前提下，将低成本Agent使用率提升近一倍。

### 核心结论
拍卖机制的核心不是规则本身，而是校准后的置信度：没有可靠的能力评估，动态分配反而会因为过自信问题效果差于静态路由。
