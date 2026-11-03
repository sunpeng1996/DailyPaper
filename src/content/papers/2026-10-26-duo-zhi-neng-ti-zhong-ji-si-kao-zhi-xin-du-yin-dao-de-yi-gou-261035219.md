---
title: Multi-Agent Relay Thinking
title_zh: 多智能体中继思考：置信度引导的异构模型协作推理框架
authors:
- Xu Liu
- Jungang Qiao
- Guikun Chen
- Xiaojuan Qi
- Wenguan Wang
affiliations:
- Zhejiang University
- Nanyang Technological University
- The University of Hong Kong
arxiv_id: '2610.35219'
url: https://arxiv.org/abs/2610.35219
pdf_url: https://arxiv.org/pdf/2610.35219
published: '2026-10-26'
collected: '2026-11-03'
category: Agent
direction: 多智能体协作 · 置信度引导中继
tags:
- Multi-Agent Collaboration
- Confidence Calibration
- Relay Reasoning
- Heterogeneous Models
- Inference Efficiency
one_liner: 提出置信度校准的异构多智能体中继协作机制，精度追平传统多智体方案，token开销降低6倍
practical_value: '- 异构模型调度可复用滑动窗口置信度校准方法，无需硬编码路由规则，适配电商商品审核、营销文案生成、用户多轮咨询等复杂推理场景的动态模型选路

  - 现有多智能体系统可将群思考模式替换为中继模式，在效果持平的前提下最高降低6倍token开销，适合大流量推荐文案生成、Query改写等成本敏感场景

  - 工程实现可直接复用各模型独立维护KV cache的设计，接力生成时无需重复prefill，大幅降低推理延迟

  - 推荐多阶段链路可借鉴中继逻辑，召回/粗排/精排阶段对应不同专长模型，置信度不足时自动切换，兼顾效果与算力效率'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有多智能体协作大多采用群思考模式，多模型并行生成完整结果后聚合，虽然效果不错但token开销极高；且异构模型的置信度分布存在偏移，无法直接比较，难以实现推理权的动态调度，导致算力浪费严重，复杂推理场景的落地成本居高不下。

### 方法关键点
1. 离线置信度校准：采用滑动窗口计算每个模型的局部生成置信度，基于历史基准数据集统计每个模型的置信度均值与标准差，做Z-score标准化对齐异构模型的置信度分布，ANOVA F值从13.31降至1.01，实现跨模型置信度可比。
2. 在线中继调度：采用「初始化-监控-竞标-中继」闭环流程：初始阶段各模型生成短序列竞标，选置信度最高的模型启动推理；实时监控当前生成模型的窗口置信度，低于阈值即触发全模型竞标，选置信度最高的模型接力生成；各模型独立维护KV cache，避免重复prefill降低延迟。

### 关键实验
在MathVista、MMStar、HallusionBench、LogicVista 4个多模态基准上测试：对比最强单模型方案，精度分别提升3.3%、3.9%；对比传统多智体方案H-DMAD，精度基本持平，token开销降低6倍，投入产出比IBC最高提升18.5倍。

### 最值得记住的一句话
异构模型的架构级能力互补性远高于同模型角色扮演、温度采样带来的模拟多样性，基于置信度的动态中继是兼顾效果与成本的最优多智能体协作路径之一。
