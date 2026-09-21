---
title: Detecting Pretraining Data in Large Language Models from a Free-Energy Perspective
title_zh: 基于自由能视角的大语言模型预训练数据成员检测方法
authors:
- Chenye Ke
- Zirui Liu
- Qi Liu
- Yan Zhuang
- Jintao Zhang
- Zhenya Huang
- Shijin Wang
affiliations:
- State Key Laboratory of Cognitive Intelligence, University of Science and Technology
  of China
- Institute of Artificial Intelligence, Hefei Comprehensive National Science Center
- College of Artificial Intelligence, Nanjing University of Aeronautics and Astronautics
- iFLYTEK AI Research (Central China), iFLYTEK Co., Ltd
arxiv_id: '2609.21888'
url: https://arxiv.org/abs/2609.21888
pdf_url: https://arxiv.org/pdf/2609.21888
published: '2026-09-18'
collected: '2026-09-21'
category: LLM
direction: 大语言模型 · 预训练数据成员检测
tags:
- LLM
- Membership Inference
- Free Energy
- Pretraining Data Audit
- Data Contamination Detection
one_liner: 提出熵校正的自由能检测框架ETD，显著提升LLM预训练数据成员检测性能
practical_value: '- 做LLM4Rec/Agent推理生成时，可借鉴熵校正逻辑修正生成置信度阈值，降低对通用高置信非训练样本的误判

  - 业务侧自有预训练语料的版权审计、下游测试集数据污染排查，可直接复用开源ETD工具快速完成检测

  - 训练垂直领域LLM（如电商文案生成、商品语义理解模型）时，可用该方法校验预训练数据覆盖度，优化语料配比'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
仅基于似然的LLM预训练数据成员检测器仅用预测损失作为判定边界，无法区分高似然来自训练暴露还是模型强泛化，容易将可预测的非成员样本误判为成员。
### 方法关键点
1. 在预测损失+预测熵联合空间引入倾斜判定边界，用预测熵对损失做校正，保留成员信号的同时降低其方差，提升成员-非成员的区分度
2. 该熵校正得分符合亥姆霍兹自由能解释，提出Energy Transfer Detection（ETD）框架，从宏观残余自由能转移视角实现检测
### 关键结果
ETD取得最优平均检测性能，平均AUROC最高提升3.5%，TPR@5%FPR最高提升5.1%，跨不同设置下均保持优异鲁棒性
