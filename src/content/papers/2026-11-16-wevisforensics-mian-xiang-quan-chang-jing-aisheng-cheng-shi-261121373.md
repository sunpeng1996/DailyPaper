---
title: 'WeVisForensics: Self-Evolving Agent for Omni AI-Generated Video Detection'
title_zh: WeVisForensics：面向全场景AI生成视频检测的自进化智能体
authors:
- Yipeng Du
- Yuxi Li
- Ying Zhang
- Chong Sun
- Chen Li
- Jing Lyu
- Ying Tai
affiliations:
- Nanjing University
- WeChat Vision, Tencent Inc.
arxiv_id: '2611.21373'
url: https://arxiv.org/abs/2611.21373
pdf_url: https://arxiv.org/pdf/2611.21373
published: '2026-11-16'
collected: '2026-11-17'
category: Agent
direction: 多Agent协同 · 自进化策略优化
tags:
- MultiAgent
- ReinforcementLearning
- AIGCDetection
- PolicyOptimization
- VideoUnderstanding
one_liner: 提出双时间尺度优化的自进化多Agent框架，实现可溯源的高精度AI生成视频检测
practical_value: '- 双时间尺度DTPO优化策略可直接复用：主调度Agent用快速RL调协同策略，子专家Agent慢迭代优化垂直能力，适配多Agent推荐/内容审核类场景

  - 自进化子Agent能力库的架构思路可迁移到电商内容风控、虚假营销素材检测系统，快速适配新增的造假/作弊手法

  - 融合角色专属标注与交互轨迹的数据集构建方法，可用于多Agent协同业务系统的训练，降低冷启动阶段的策略优化成本'
score: 7
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有AI生成视频检测方法存在两类缺陷：单轮CoT推理易遗漏局部/短时伪影，预定义多Agent工作流检测选择灵活性不足，且仅优化调度策略无法提升固定子专家的检测能力。
### 方法关键点
1. 构建WeVisForensics多Agent框架：主调查Agent协调覆盖视觉、音频维度的自进化检测子Agent库，自主决策检测的伪影类型、时间窗口与终止时机，交互数据为两层Agent提供共享反馈
2. 提出双时间尺度策略优化（DTPO）：主Agent通过快速RL优化调度策略，子Agent基于标注伪影区间慢迭代优化检测能力，形成能力提升闭环
3. 开源ForenCue-30K数据集，包含角色专属标注、交互轨迹与RL训练池，支撑模型训练
### 关键结果
跨域、基准测试集平均检测准确率达95.2%，较此前最优方案高出9.0%，同时可输出本地化的检测证据支撑判定结果
