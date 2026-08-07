---
title: 'OneEmo: A Unified Multimodal Reasoning Model for Emotion Perception, Understanding,
  and Interaction'
title_zh: OneEmo：面向情感感知、理解与交互的统一多模态推理模型
authors:
- Jiahao Huang
- Zheng Lian
- Jingyi Zhang
- Zhide Chen
- Xiaojiang Peng
- Shaonan Wang
arxiv_id: '2608.06013'
url: https://arxiv.org/abs/2608.06013
pdf_url: https://arxiv.org/pdf/2608.06013
published: '2026-08-06'
collected: '2026-08-07'
category: Multimodal
direction: 多模态大模型 · 情感推理
tags:
- MLLM
- Multimodal
- Multi-task Learning
- Reinforcement Learning
- Affective Computing
one_liner: 提出统一多模态情感通用模型，配套专用数据集与RL训练策略，同等参数量下达SOTA
practical_value: '- 电商导购/客服Agent可复用Emo-Chord多任务奖励分配策略，同步优化用户情绪识别、共情回复生成等任务，降低训练波动

  - 短视频/直播内容推荐场景可借鉴多任务情感知识蒸馏思路，统一构建用户多模态情感标注数据集，提升内容情感匹配精准度

  - 垂类情感小模型SFT可参考human-in-the-loop构建带推理轨迹的数据集，用更少参数量达到接近商用大模型的效果'
score: 7
source: arxiv-cs.HC
depth: abstract
---

### 动机
现有MLLM情感相关研究多聚焦单任务专项优化，忽略任务间协同效应，推理潜力未被充分挖掘。

### 方法关键点
1. 构建EmoWorld-130K数据集，通过human-in-the-loop流程将专业情感知识蒸馏为显式推理轨迹，基于该数据集的监督微调验证了多任务学习的显著增益
2. 推出Emo-Chord强化学习策略，通过统一多任务奖励分配稳定优化过程，充分释放模型推理潜力

### 关键结果
同等参数量下在绝大多数情感基准测试中达到SOTA，参数量远小于商用模型的前提下仍具备极具竞争力的表现
