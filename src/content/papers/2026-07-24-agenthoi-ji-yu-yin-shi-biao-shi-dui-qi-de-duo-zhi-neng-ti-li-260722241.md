---
title: 'AgentHOI: Multi-Agent Reasoning for Human-Object-Interaction Video Generation
  via Implicit Representation Alignment'
title_zh: AgentHOI：基于隐式表示对齐的多智能体推理人-物交互视频生成
authors:
- Ziyao Huang
- Shunkai Li
- Juan Cao
- Chenyu Li
- Youliang Zhang
- Zixiang Zhou
- Cong Wang
- Yuan Zhou
- Qinglin Lu
- Fan Tang
affiliations:
- University of Chinese Academy of Sciences
- Tencent HunYuan
arxiv_id: '2607.22241'
url: https://arxiv.org/abs/2607.22241
pdf_url: https://arxiv.org/pdf/2607.22241
published: '2026-07-24'
collected: '2026-07-27'
category: Agent
direction: 多智能体推理 · 人-物交互视频生成
tags:
- Multi-Agent
- Diffusion Model
- Video Generation
- Implicit Alignment
- HOI
one_liner: 提出先思考后生成的多Agent推理HOI视频生成方法，无需显式运动输入即可提升合成效果
practical_value: '- 电商商品展示短视频生成可复用「先思考后生成」框架：先用多Agent拆解脚本时序动作，再生成对应视频，降低动作逻辑错误率

  - 文本驱动内容生成场景可借鉴隐式文本-运动对齐策略，将动作先验蒸馏到底层生成模型，推理时无需额外显式运动输入，降低部署成本

  - 多Agent分工（感知/交互/运动规划）的任务拆解思路可迁移到复杂文案生成、广告创意生成等需要多步逻辑的生成任务'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有HOI（人-物交互）视频生成方法高度依赖显式运动控制，跨不同物体、交互场景的扩展性与泛化性差，难以对齐高层文本意图与底层动作逻辑。

### 方法关键点
1. 采用「先思考后生成」框架，通过感知、交互、运动规划三类Agent的协同推理，自动生成细粒度秒级时序交互动作计划，打通文本意图到物理执行的链路；
2. 提出隐式文本-运动对齐策略，将文本到运动的先验蒸馏到视频扩散模型中，推理阶段无需输入显式运动信号即可完成HOI视频合成。

### 关键结果
在穿戴、骑行等复杂物体中心场景下，交互自然度、物体外观保留度、复杂文本指令遵循度均实现显著提升。
