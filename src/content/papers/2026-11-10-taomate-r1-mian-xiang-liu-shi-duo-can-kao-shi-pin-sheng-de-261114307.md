---
title: 'TaoMate-R1: Temporal Role Specialization for Streaming Multi-Reference Video
  Generation'
title_zh: TaoMate-R1：面向流式多参考视频生成的时序角色专业化方法
authors:
- Qijun Gan
- Chenwei Zhang
- Xinyang Li
- Meiguang Jin
- Junfeng Ma
affiliations:
- Alibaba Group
arxiv_id: '2611.14307'
url: https://arxiv.org/abs/2611.14307
pdf_url: https://arxiv.org/pdf/2611.14307
published: '2026-11-10'
collected: '2026-11-12'
category: Multimodal
direction: 多模态生成 · 流式多参考视频生成优化
tags:
- LoRA
- Video Generation
- Streaming Generation
- Adapter Tuning
- Multi-reference Generation
one_liner: 通过时序角色分配独立LoRA结合自梯度强迫，提升流式多参考视频生成连贯性
practical_value: '- 电商直播AIGC场景可直接复用时序角色拆分思路，给场景初始化、后续续播阶段分配独立LoRA，可大幅降低视频片段边界跳变，提升直播生成流畅度

  - Self Gradient Forcing训练策略无需额外标注，可利用生成历史自动对齐前后片段特征，有效降低多阶段生成任务的训练数据成本

  - 冻结主干仅调整LoRA参数的适配方案，可快速复用现有开源视频生成底座，兼顾生成效果与部署成本，适合电商短平快的AIGC内容生产需求'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
流式多参考视频生成需基于指定人/物构建初始场景后跟随动态指令连续生成，现有方案存在片段边界跳变、时序连贯性差的问题，无法适配电商直播等长时连续生成场景需求。
### 方法关键点
1. 提出时序角色专业化机制，在冻结预训练主干的基础上，为场景初始化、场景续播两个阶段分别分配独立LoRA适配器，每个适配器同时承担对应阶段的去噪与上下文写入任务；
2. 设计Self Gradient Forcing训练策略，利用模型自身生成的历史信息联合训练两个阶段的适配器，保证前后片段特征对齐。
### 关键结果
在2分钟时长的指令驱动流式生成任务中，平均边界亮度跳变从1.96降至0.613，边界特征相似度显著提升；短交互、长流、公开基准集上的CLIP、DINO时序相似度均优于基线方案。
