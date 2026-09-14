---
title: Evaluating Time-Series Foundation Models and Multimodal Dietary Context for
  CGM Forecasting
title_zh: 时序基础模型与多模态饮食上下文的连续血糖预测效果评估
authors:
- Bowen Zhang
- Hsiu-Wen Cheng
- Hongyu Yang
- Evie L. Shen
- Joleen Vansomphone
- Yuna Li
- Kerry Zhou
- Zitian Qu
- Suning Zhao
- Xiangning Deng
affiliations:
- University of California, Los Angeles
- Tsinghua University
- Union County Magnet High School
- Huntington Beach High School
- Crean Lutheran High School
arxiv_id: '2609.11872'
url: https://arxiv.org/abs/2609.11872
pdf_url: https://arxiv.org/pdf/2609.11872
published: '2026-09-10'
collected: '2026-09-14'
category: Other
direction: 时序基础模型 · 多模态时序预测
tags:
- Time-Series Foundation Model
- Multimodal Fusion
- Lightweight Fine-tuning
- Time Series Forecasting
- Zero-shot Evaluation
one_liner: 系统性评估时序基础模型在连续血糖预测的表现，验证轻量微调及多模态饮食融合的性能增益
practical_value: '- 做用户行为时序预测、销量预测等电商时序类任务时，不要盲目依赖零-shot时序大模型，轻量微调后性能才能稳定超过传统任务专属基线

  - 多模态特征融合可优先采用残差式架构，针对大促、用户活跃时段等特定场景的效果增益远高于平均水平

  - 预训练时序基础模型的时序模式表征能力优于传统LSTM、树模型，即使后者加入额外特征也难以超越，可优先选型做下游微调'
score: 3
source: arxiv-cs.LG
depth: abstract
---

### 动机
连续血糖监测（CGM）短期预测是糖尿病管理的核心能力，但通用时序基础模型在该垂直任务的表现、多模态饮食上下文的实际增益尚未被系统性验证。
### 方法关键点
基于8个覆盖1型糖尿病、2型糖尿病、非糖尿病人群的公开CGM数据集，采用统一协议跨不同上下文长度、预测窗口开展评估；引入时序对齐的CGMacros多模态数据集，基于残差融合框架整合血糖信号、食物图像、宏量营养素记录三类特征。
### 关键结果数字
零-shot时序基础模型未稳定超过Elastic Net、PatchTST等任务专属基线；微调后Chronos-Bolt在1型糖尿病人群RMSE降低6.5%-18.4%，在2型/非糖尿病人群降低8.6%-18.2%，分布内/外测试增益一致；多模态融合较单血糖基线整体RMSE降约3%，餐后RMSE降约15%。
