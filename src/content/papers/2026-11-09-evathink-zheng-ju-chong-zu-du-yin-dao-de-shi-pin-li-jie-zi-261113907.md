---
title: 'EVAThink: Evidence Sufficiency-Guided Training for Adaptive Thinking in Video
  Understanding'
title_zh: EVAThink：证据充足度引导的视频理解自适应思考训练方法
authors:
- Changti Wu
- Ruizhe Fan
- Bin Wang
- Lei Zhang
- Yuxiang Zhang
affiliations:
- East China Normal University
- Zhongguancun Academy
- Huawei Technologies Co., Ltd
arxiv_id: '2611.13907'
url: https://arxiv.org/abs/2611.13907
pdf_url: https://arxiv.org/pdf/2611.13907
published: '2026-11-09'
collected: '2026-11-12'
category: Multimodal
direction: 多模态视频理解 · VLM自适应推理优化
tags:
- VLM
- Video Understanding
- Reinforcement Learning
- Adaptive Reasoning
- Low-resource Training
one_liner: 提出证据充足度引导的自适应思考训练框架，小样本提升固定帧预算下VLM视频理解效果
practical_value: '- 稀疏/稠密双视图对比挖掘的思路可直接迁移到短视频电商的内容理解场景，在有限帧采样预算下提升高转化商品内容的识别准确率

  - 两阶段强化学习+首token正则防模式崩溃的训练范式，可复用在多模态生成式推荐的低资源训练场景，小样本即可实现基线效果提升

  - 基于证据充足度动态切换「直接输出/推理增强」模式的逻辑，可借鉴到多模态导购Agent的决策模块，兼顾推理效率和回答准确率'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
固定帧采样预算下，VLM做视频理解的效果高度依赖采样帧是否包含足够问答相关证据：证据充足时可直接输出准确结果，证据稀疏时直接回答准确率低，需引入推理链路提升有限信息的利用率。
### 方法关键点
1. 可恢复证据差挖掘：同帧预算下构造同一问答对的证据稠密/稀疏双视图，筛选出稀疏视图直接回答准确率低、但加显式推理后效果显著提升的样本对，为响应模式选择提供监督信号；
2. 证据引导两阶段强化学习：分阶段设置奖励，先引导模型基于证据充足度选择响应模式，再优化响应效率，同时引入首token优势正则缓解模式崩溃问题。
### 关键结果
仅用6.7K精编样本训练，在32帧、64帧两种预算下的所有视频理解基准上均优于基线模型，平均效果超过现有强基线。
