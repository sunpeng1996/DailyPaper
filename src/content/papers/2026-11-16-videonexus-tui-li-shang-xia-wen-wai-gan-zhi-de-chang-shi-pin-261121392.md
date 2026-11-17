---
title: 'VideoNexus: Video Perception Beyond the Reasoning Context'
title_zh: VideoNexus：推理上下文外感知的长视频智能体框架
authors:
- Yancheng Long
- Xuanyu Zheng
- Wei Chen
- Luoyuan Zhang
- Haoyang Xu
- Bin Wen
- Tingting Gao
affiliations:
- The Chinese University of Hong Kong
- The Hong Kong University of Science and Technology
- KlingAI Research
arxiv_id: '2611.21392'
url: https://arxiv.org/abs/2611.21392
pdf_url: https://arxiv.org/pdf/2611.21392
published: '2026-11-16'
collected: '2026-11-17'
category: Agent
direction: 长视频Agent · 感知规划解耦优化
tags:
- VideoAgent
- Long-Video-Understanding
- Decoupled-Perception
- Zero-Training
- Cost-Optimization
one_liner: 无训练长视频Agent框架，解耦规划与感知，降本提效提升长视频理解准确率
practical_value: '- 电商短视频/直播理解、用户长行为序列建模等场景可直接复用感知-规划解耦架构：将高token成本的原生多模态处理下沉到独立子Agent，仅返回结构化紧凑结果，避免挤占推理上下文，同时降本提效

  - 结构化输出协议可直接复用：给子任务返回结果增加时间戳、状态字段、明确证据项，方便上层规划模块做信息聚合、不确定性判断，也便于结果可解释性回溯

  - 多模态Agent成本优化可参考该思路：仅保留少量关键证据卡（如直播核心商品帧）做校验，平衡效果与成本，该架构无需训练即可适配不同基座，迁移成本低，适合快速上线长视频理解类业务'
score: 8
source: arxiv-cs.CV
depth: full_pdf
---

### 动机
当前长视频Agent存在两类问题：一是将原始帧/剪辑直接塞入推理上下文，导致context膨胀、调用成本高；二是感知委托给独立模块但稀疏采样易漏关键细节，逐帧描述仍会导致上下文线性增长，难以同时兼顾准确率与成本。

### 方法关键点
- 完全解耦规划与感知：Planner全程不接收视频流，仅负责制定感知任务、选择时间区间与采样率、聚合证据、决策停止时机，所有原生音视频处理交给独立感知子Agent，子Agent上下文用完即弃
- 三类标准化感知工具：Transcribe返回带时间戳的ASR结果（跨查询缓存复用）；Overview做全局稀疏扫描，最多返回8个候选区间（仅做定位不做判断）；Inspect按指定帧率采样目标区间，返回结构化Finding（带状态、结论、锚定绝对时间的证据项），可选返回最多6帧的证据卡做校验
- 输出规模约束：Finding输出与感知帧数亚线性相关，避免context随采样密度线性膨胀，所有时间锚定原视频 timeline 方便跨调用信息对齐

### 关键实验结果
- LVBench（1549道长视频选择题）上，Gemini 3.8 Flash基座准确率达88.6%，比静态全量输入高3.6个点，比Gemini自带Agent模式高1.1个点，仅为后者API成本的44%
- Kimi K3基座下，Video-GAIA数据集上比官方ReAct baseline准确率高8.5个点
- 解耦设计相比耦合架构减少32%的Planner输入token，同时准确率提升2.5个点

### 核心结论
长视频Agent的优化核心不是一味扩充上下文容量，而是拆解感知与推理链路，让推理上下文仅存储高价值结构化证据，而非原始多模态数据
