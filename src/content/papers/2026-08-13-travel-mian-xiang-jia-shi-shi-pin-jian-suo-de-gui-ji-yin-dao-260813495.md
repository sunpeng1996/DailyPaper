---
title: 'TraVEL: Trajectory-Guided Video Embedding Learning for Driving-Video Retrieval'
title_zh: TraVEL：面向驾驶视频检索的轨迹引导视频嵌入学习方法
authors:
- Yi-Chung Chen
- Philip Jacobson
- Tom Lampo
- Yiren Lu
- Jin Yao
- David I. Inouye
- Jing Gao
- Danhua Guo
- Burhan Yaman
affiliations:
- Uber AV Labs
- Purdue University
arxiv_id: '2608.13495'
url: https://arxiv.org/abs/2608.13495
pdf_url: https://arxiv.org/pdf/2608.13495
published: '2026-08-13'
collected: '2026-08-14'
category: Multimodal
direction: 多模态视频检索 · 嵌入微调
tags:
- Multimodal-Embedding
- Video-Retrieval
- GRPO
- Motion-Understanding
- Fine-tuning
one_liner: 提出轨迹引导的视频嵌入学习框架，用轨迹相似度作为GRPO奖励提升驾驶视频运动事件检索效果
practical_value: '- 特定领域多模态检索场景可采用「通用SFT+领域特权信号RL微调」范式，特权信号仅训练用，推理无额外开销，适配电商短视频检索等低延迟线上场景

  - 细粒度行为/运动类检索任务，可引入物理层面客观相似度作为RL奖励，替代纯文本caption监督，解决文本标注粒度不足问题，可复用在电商短视频用户动作、商品操作类检索

  - Group Relative Policy Optimization（GRPO）相比传统PPO训练更稳定，可复用在多模态嵌入微调的RL阶段，降低调参成本'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
大规模驾驶日志检索是自动驾驶数据治理核心需求，传统规则式检索依赖专家规则与多阶段感知pipeline成本高，通用多模态嵌入模型依赖静态场景捷径，无法区分转向、加减速等细粒度运动类事件，纯caption监督的SFT也难以满足运动理解要求。

### 方法关键点
1. 先基于Qwen3-VL-Embedding用nuReasoning数据集的视频-推理轨迹对做InfoNCE损失预微调；
2. 提出TraVEL运动感知微调框架，将自车轨迹相似度作为奖励接入Group Relative Policy Optimization（GRPO）做RL微调，轨迹仅作为训练阶段特权监督，推理阶段仅用单向量视频embedding检索，无需额外输入；
3. 基于nuReasoning构建驾驶视频检索基准。

### 关键结果
相比SFT基线，2B参数模型纵向、横向运动类检索mAP分别提升9.8、4.7个百分点，8B参数模型对应提升7.2、1.5个百分点，跨模型规模均有稳定收益。
