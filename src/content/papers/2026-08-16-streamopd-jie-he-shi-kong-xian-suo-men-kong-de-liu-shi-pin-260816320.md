---
title: 'StreamOPD: A Post-Training Recipe with Spatio-Temporal Cue Gating for Streaming
  Video Understanding'
title_zh: StreamOPD：结合时空线索门控的流视频理解后训练方案
authors:
- Keming Wu
- Baoyi Wang
- Kaichen Zhang
- Xiang An
- Zuhao Yang
- Sudong Wang
- Haowei Zhu
- Tingxuan Huang
- Hongcheng Gao
- Bin Wang
affiliations:
- Tsinghua University
- Zhejiang University
- The University of Hong Kong
- LMMs-Lab
- Nanyang Technological University
arxiv_id: '2608.16320'
url: https://arxiv.org/abs/2608.16320
pdf_url: https://arxiv.org/pdf/2608.16320
published: '2026-08-16'
collected: '2026-08-19'
category: Multimodal
direction: 多模态大模型 · 流视频理解后训练
tags:
- Multimodal-LLM
- Streaming-Video-Understanding
- Post-Training
- Knowledge-Distillation
- Spatio-Temporal-Modeling
one_liner: 提出无额外推理内存的流视频理解后训练方案StreamOPD，搭配时空线索门控，性能逼近9B大模型
practical_value: '- 直播实时推荐/审核场景可复用无额外推理内存的后训练范式，无需改动推理架构即可提升流内容理解精度，适配低延迟要求

  - 小模型落地时可采用on-policy自蒸馏方案，用自身初始冻结策略做教师无需额外大模型资源，保留大部分性能增益的同时降低成本

  - 时空线索门控的损失重加权思路可迁移到时序用户行为序列推荐的蒸馏流程，解决时序信号权重分配不合理问题'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有流视频理解方案依赖推理侧额外内存、检索模块，但无训练的滑动窗口基线性能已与这些方案持平；同时强化学习奖励稀疏易生成长「先想后答」内容，on-policy蒸馏（OPD）仅在思考模式下训练稳定，亟需轻量化后训练方案提升流视频理解性能。
### 方法关键点
1. 提出StreamOPD后训练范式，融合可验证流视频数据、思考模式OPD、指令模式部署三段流程
2. 新增ST-CueGate模块，聚合教师模型有无线索的似然比得到组相对响应得分，对OPD损失重加权
3. 支持无外部教师的自蒸馏变体，用学生初始策略的冻结副本做教师
### 关键结果
- StreamingBench准确率从77.9%提升到83.9%，仅比9B教师模型低0.3个点
- OVO-Bench（排除幻觉检测子任务）准确率提升9.1个点
- 自蒸馏变体幻觉检测任务准确率达57.0%，超过未训练学生模型和9B教师模型，是唯一在四个基准上全优于基线的变体
