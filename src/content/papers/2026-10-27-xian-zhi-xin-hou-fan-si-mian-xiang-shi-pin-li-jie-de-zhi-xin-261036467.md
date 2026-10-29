---
title: 'Confident First, Reflective Second: Reinforcement Learning of Confidence-Preserving
  Reflection for Video Understanding'
title_zh: 先置信后反思：面向视频理解的置信度保留反思强化学习
authors:
- Zihao Lin
- Jingyuan Liu
- Yucheng Zhang
- Yuguang Yao
- Lifu Huang
affiliations:
- University of California, Davis
- Independent Researcher
- Intuit
arxiv_id: '2610.36467'
url: https://arxiv.org/abs/2610.36467
pdf_url: https://arxiv.org/pdf/2610.36467
published: '2026-10-27'
collected: '2026-10-29'
category: Reasoning
direction: 多模态推理 · RL优化反思机制
tags:
- Reinforcement Learning
- Video Understanding
- Reflection Mechanism
- Multimodal LLM
- Confidence Preservation
one_liner: 提出CoFire方法解决视频理解RL反思流程的置信度侵蚀问题，同步提升初始与最终回答准确率
practical_value: '- 搭建带反思链路的电商内容Agent（如短视频带货标签抽取、商品咨询多轮解答）时，可引入置信度保底机制，避免RL训练后初始回答准确率下降，平衡反思增益与基础响应效率

  - 针对长序列内容理解任务（如用户长行为序列召回、长视频种草内容语义解析），可参考三通道防侵蚀方案（奖励设计、参数漂移抑制、梯度隔离）优化RL训练目标

  - 资源受限场景下的多模态生成任务，可复用「初始输出保底+反思增量优化」的架构，在控制计算成本的前提下提升最终输出准确率'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有视频理解模型基于采样帧回答易遗漏关键片段，基于RL的反思优化流程存在**置信度侵蚀**问题：因错误可在后续反思阶段修复，初始正确回答获得的奖励偏低，导致初始回答准确率停滞，最终准确率提升受限。
### 方法关键点
提出「先置信后反思」原则，要求初始回答准确率不低于参考策略的保底阈值，反思仅做增量优化；设计CoFire方法针对三类置信度侵蚀通道分别优化：调整奖励函数激励初始正确回答、抑制参数漂移避免初始能力退化、隔离梯度避免反思阶段梯度干扰初始回答模块。
### 关键结果
在Video-MME、MLVU、LongVideoBench三个基准上平均准确率达67.0%，比最优7B参基线高1.7个百分点；相比传统结果奖励RL，初始回答准确率平均提升4.1pct，最终准确率平均提升3.7pct
