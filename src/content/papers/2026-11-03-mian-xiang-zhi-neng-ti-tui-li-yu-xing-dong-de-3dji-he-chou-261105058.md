---
title: Do Agentic Policies Need to Look at Every Step? Geometric Abstraction for Reasoning
  and Action
title_zh: 面向智能体推理与行动的3D几何抽象，无需逐步重解析视觉观测
authors:
- Yihang Liu
- Yiming Chen
- Mingzhe Zheng
affiliations:
- Independent Researcher
- Georgia Institute of Technology
- The Hong Kong University of Science and Technology
arxiv_id: '2611.05058'
url: https://arxiv.org/abs/2611.05058
pdf_url: https://arxiv.org/pdf/2611.05058
published: '2026-11-03'
collected: '2026-11-04'
category: Agent
direction: 具身智能体 · 空间推理中间表示
tags:
- Agentic Reasoning
- Spatial Reasoning
- Geometric Abstraction
- Embodied AI
- LLM Interface
one_liner: 提出文本符号化3D几何抽象接口，降低智能体多模态调用开销同时提升多步操作任务成功率
practical_value: '- 可借鉴「符号引用+动态数值绑定」的中间表示设计，替代LLM逐步处理高冗余原始输入（如用户行为序列、商品图像特征），大幅降低推理token开销

  - 可复用结构化符号与动态刷新场景/用户状态分离的设计，可直接迁移到多轮对话式推荐Agent，避免重复召回冗余用户历史行为

  - 「常规推理走中间表示、异常场景按需调用多模态」的混合调度策略，可用于电商导购Agent实时响应优化，平衡推理效果和延迟

  - 状态证据标识（观测/推断/不可用）的设计可复用在推荐系统用户状态建模中，降低推断状态带来的决策误差'
score: 8
source: arxiv-cs.CV
depth: full_pdf
---

### 动机
当前多模态LLM驱动的具身智能体需逐步重解析原始视觉观测，既引入推理不确定性，又带来极高的计算开销和延迟；现有视觉接口要么保留全量冗余信息，要么仅输出粗粒度物体级特征，无法平衡表达效率和推理可靠性。

### 方法关键点
- 设计带证据状态的3D几何抽象层，将RGB-D观测映射为带类型、时间戳、证据标识（观测/推断/不可用）的物体部件（中心、顶点、面等）结构化表示
- 提供两类LLM访问接口：可组合的符号引用（如`red.bottom_face`）+几何算子（对齐、支撑检查等），以及动作执行后输出的紧凑文本检查点（包含更新后的3D坐标、目标残差、证据状态）
- 采用混合推理调度：常规空间推理直接基于文本符号完成，仅当抽象状态不足以解释故障时按需调用多模态视觉推理

### 关键实验
在MuJoCo仿真环境3类机器人操作任务上，对比逐步处理图像的Pixel Reasoning基线：
1. 策略合成场景：3轮迭代后三立方体堆叠任务成功率达81.4%（基线70.8%），token开销降低10.6%；Ring-on-peg任务基线成功率为0，本方法达38%
2. 在线执行场景：Bridge-tower任务成功率提升133%（从24%到56%），Tower relocation任务成功率提升180%（从30%到84%），平均模型调用时间降低49.4%~60.5%，单轮请求附加图像数减少75%以上

### 核心结论
将可复用的结构化符号与动态刷新的场景数值解耦，是降低多模态智能体推理开销、提升决策可靠性的核心路径。
