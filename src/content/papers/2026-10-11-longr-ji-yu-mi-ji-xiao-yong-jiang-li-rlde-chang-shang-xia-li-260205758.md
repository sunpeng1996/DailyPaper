---
title: 'LongR: Unleashing Long-Context Reasoning via Reinforcement Learning with Dense
  Utility Rewards'
title_zh: LongR：基于密集效用奖励RL的长上下文推理优化框架
authors:
- Qize Yu
- Zijun Chen
- Chen Wu
- Yue Chen
- Yiyao Yu
- Tingfeng Hui
- Bowen Ping
- Junchi Yan
- Baobao Chang
affiliations:
- Peking University
- Shanghai Jiao Tong University
- Tsinghua University
- Beijing University of Posts and Telecommunications
arxiv_id: '2602.05758'
url: https://arxiv.org/abs/2602.05758
pdf_url: https://arxiv.org/pdf/2602.05758
published: '2026-10-11'
collected: '2026-10-14'
category: Reasoning
direction: 长上下文推理 · RL密集奖励设计
tags:
- Long-Context Reasoning
- Reinforcement Learning
- Dense Reward
- Information Gain
- Curriculum Learning
one_liner: 提出结合Think-and-Read机制与相对信息增益密集奖励的RL框架，无标注提升长上下文推理性能
practical_value: '- 做电商Agent长会话理解、长商品文档RAG问答场景时，可复用相对信息增益的密集奖励设计，无需额外证据标注即可让模型更精准定位有效上下文，相比稀疏最终奖励可提升约4%的准确率

  - 训练适配长上下文的垂域LLM时，可采用渐进式上下文长度的课程学习策略，先在短文本上训练基础能力再逐步扩展到长文本，无需专门构造长上下文SFT数据，降低数据工程成本

  - 做用户长评论分析、商品说明书信息提取等场景时，可借鉴Think-and-Read的Prompt范式，引导模型在推理过程中显式引用原文片段，既提升结果准确率也便于结果可解释性校验'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有长上下文推理的RL优化方案要么依赖文档硬分块、预定义输出格式，破坏信息完整性且适配性差；要么仅使用最终结果的稀疏奖励，信号太弱无法有效引导长上下文下的证据查找，还需要额外的证据标注成本，落地门槛高。
### 方法关键点
- 动态Think-and-Read机制：将证据查找自然嵌入CoT流程，模型可在推理过程中直接引用原文片段，无需对输入文档做预分块，也不用强制输出chunk ID，完全兼容标准自回归生成范式
- 无标注密集奖励：基于相对信息增益计算引用片段的效用，用冻结的小参数量验证模型分别计算引用片段的先验NLL和上下文条件NLL，差值归一化后作为密集奖励，无需额外标注
- 渐进式课程学习：训练时从短上下文逐步扩展到长上下文，无需专门构造长上下文SFT数据，降低数据构造成本
### 关键结果
在LongBench v2上相比仅用稀疏奖励的DAPO基线，8B模型提升3.39个百分点，4B模型提升5.03个百分点，整体相比SFT基线提升超9%；在RULER、InfiniteBench上均有一致的性能提升；相对信息增益奖励设计比纯稀疏奖励高约4个百分点，4B规模验证器即可获得接近32B验证器的效果，平衡性能与训练成本。
### 核心结论
长上下文推理的RL优化中，基于相对信息增益的无标注密集奖励，能有效解决稀疏奖励信号不足的问题，同时避免额外标注成本，适配性远高于硬分块的长上下文RL方案
