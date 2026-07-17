---
title: Improving Text-to-Audio Instruction Following via Fine-Grained Feedback from
  Audio-Aware Large Language Models
title_zh: 基于音频感知大模型细粒度反馈的文本转音频指令跟随优化
authors:
- Chun-Yi Kuan
- Siwon Kim
- Byeonggeun Kim
- Suyoun Kim
- Bo-Ru Lu
- Qinming Tang
- Ankur Gandhe
- Hung-yi Lee
- Chieh-Chi Kao
- Chao Wang
affiliations:
- National Taiwan University
- Amazon
arxiv_id: '2607.13408'
url: https://arxiv.org/abs/2607.13408
pdf_url: https://arxiv.org/pdf/2607.13408
published: '2026-07-15'
collected: '2026-07-17'
category: Other
direction: 文本转音频生成 · LLM细粒度反馈优化
tags:
- Text-to-Audio
- LLM Feedback
- DPO
- Instruction Following
- Benchmark
one_liner: 用音频感知LLM细粒度反馈优化文本转音频的多事件时序指令跟随能力，配套发布S3Bench评测集
practical_value: '- 做生成类任务（如电商广告文案/商品素材生成）的指令对齐时，可复用「领域感知LLM做细粒度评判→构建偏好对→DPO优化」的pipeline，替代仅靠全局相似性的弱监督信号

  - 针对多约束生成任务（如电商推广内容需同时满足卖点完整性、时序逻辑合规），可设计面向具体约束的细粒度评判维度，而非仅评估整体生成质量

  - 构建自定义生成任务评测集时，可参考S3Bench的设计思路，针对任务核心痛点（如多约束满足）构造测试用例，避免通用评测集的适配性不足'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有文本转音频（TTA）模型全局生成质量优异，但处理包含多声音事件、时序约束的用户指令时，指令遵循准确率低，核心原因是训练、评估信号仅关注全局相似性/感知质量，缺乏指令级的细粒度监督。
### 方法关键点
1. 引入音频感知大模型（ALLM）作为细粒度评判器，专门校验生成音频中目标事件是否存在、时序关系是否符合指令要求；
2. 经基准测试、人工验证确认ALLM评判可靠性后，用其反馈构造偏好对，采用DPO优化TTA模型；
3. 发布S3Bench叙事类评测集，专门用于评估多事件时序指令跟随能力。
### 关键结果
在现有公开基准、S3Bench上，TTA模型的事件完整性、时序排序准确率、联合指令遵循准确率均显著提升，同时音频质量无下降。
