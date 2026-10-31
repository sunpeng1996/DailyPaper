---
title: 'HiFOR: Hierarchical Foresight with Action-Guided World Grounding for Vision-Language-Action
  Model'
title_zh: HiFOR：面向视觉-语言-动作模型的动作引导世界接地分层前瞻框架
authors:
- Rongxing Ding
- Hongyu Qu
- Kehong Wu
- Xudong Wang
- Fan Zhang
- Xinguang Xiang
- Xiangbo Shu
affiliations:
- Nanjing University of Science and Technology
- National University of Singapore
- Shenyang Institute of Automation, Chinese Academy of Sciences
- The Chinese University of Hong Kong
arxiv_id: '2610.40373'
url: https://arxiv.org/abs/2610.40373
pdf_url: https://arxiv.org/pdf/2610.40373
published: '2026-10-29'
collected: '2026-10-31'
category: Agent
direction: 多模态Agent 动作生成优化
tags:
- VLA
- Hierarchical Prediction
- World Modeling
- Action Generation
- Latent Retrieval
one_liner: 提出分层前瞻框架HiFOR，通过动作引导的世界检索提升VLA模型机器人操纵任务性能
practical_value: '- 分层依赖掩码（HDM）可迁移到长序列推荐的用户行为建模，同时建模短期点击、中期加购、长期复购的跨时间尺度依赖关系，提升长周期推荐精度

  - 动作引导的因子化检索思路可用于生成式推荐的RAG流程，根据当前生成的Item候选动态召回适配的用户历史/上下文信息，降低无关信息干扰

  - 多维度结构化隐空间建模方法可复用在多模态检索系统，沿时间、模态、空间维度组织隐向量，降低细粒度检索的计算开销'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有VLA模型的未来预测模块存在两类缺陷：一是短期环境动态与长期任务目标独立建模，缺少跨时间尺度的依赖关联；二是预测的未来信息未结合当前动作需求筛选就直接注入策略，有效信息利用率低。
### 方法关键点
1. 设计分层前瞻预测模块，通过Hierarchical Dependency Mask（HDM）联合预测短期状态演化、语义里程碑、最终目标状态，打通不同时间尺度的建模依赖；
2. 构建结构感知隐式世界模型，沿时间、视角、空间三个维度组织未来隐向量，支撑细粒度检索；
3. 提出动作引导的因子化世界检索机制，在去噪过程中根据实时更新的动作表征自适应召回相关未来信息，精准指导动作生成。
### 关键结果
在2个仿真基准、6个真实世界机器人操纵任务上性能全面超越现有SOTA VLA模型。
