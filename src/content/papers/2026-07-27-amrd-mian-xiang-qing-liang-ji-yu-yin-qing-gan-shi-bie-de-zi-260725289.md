---
title: 'AMRD: Adaptive Multi-Teacher Relational Distillation for Lightweight Speech
  Emotion Recognition'
title_zh: AMRD：面向轻量级语音情感识别的自适应多教师关系蒸馏
authors:
- Yuqi Li
- Yi-Cheng Lin
- Xianglong Wang
- Kuo Yang
- Xiaoqin Feng
- Yixuan Wang
- Huiran Duan
- Yingli Tian
affiliations:
- The City College of New York
- National Taiwan University
- Wyze Inc.
- University of Minnesota - Twin Cities
arxiv_id: '2607.25289'
url: https://arxiv.org/abs/2607.25289
pdf_url: https://arxiv.org/pdf/2607.25289
published: '2026-07-27'
collected: '2026-08-01'
category: Training
direction: 知识蒸馏 · 端侧小模型训练优化
tags:
- Knowledge Distillation
- Multi-Teacher Learning
- Model Compression
- On-device Model
- Speech Emotion Recognition
one_liner: 提出自适应多教师关系蒸馏方法，解决多教师蒸馏的教师权重动态分配与样本关系丢失问题
practical_value: '- 多教师蒸馏时可复用动态加权策略：针对每个教师输出的相似度矩阵用one-class SVM打分，按batch动态分配教师权重，替代固定权重方案，适配不同batch的教师输出可靠性差异，可用于推荐排序大模型蒸馏小模型场景

  - 蒸馏损失可新增关系对齐项：除常规logit/feature对齐外，新增师生样本间相似度矩阵对齐损失，保留更多数据结构信息，可迁移到Agent动作模型、端侧推荐模型的蒸馏优化

  - 整套蒸馏框架可直接用于端侧业务模型压缩：解决端侧推理算力受限、大模型无法部署的问题，适配电商端侧个性化推荐、智能客服交互等场景'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
端侧语音情感识别（SER）对实时交互类业务至关重要，但现有性能优异的自监督SER模型参数量达94M级，无法直接部署在边缘设备；传统多教师知识蒸馏存在两大痛点：不同batch下教师可靠性波动大，仅logit级蒸馏会丢失样本间关系结构信息。
### 方法关键点
1. 为每个教师的logit相似度矩阵训练one-class SVM，按batch动态分配教师权重，优先给输出一致性更高的教师更高权重；
2. 新增关系蒸馏损失，对齐教师与学生的样本相似度矩阵，捕捉logit匹配遗漏的样本间结构信息。
### 关键结果
在IEMOCAP、CREMA-D两个公开数据集，覆盖4种学生架构的实验中，AMRD在绝大多数场景下性能优于单教师蒸馏基线；消融实验验证两个核心组件的增益互补
