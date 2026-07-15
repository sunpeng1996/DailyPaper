---
title: 'Deep4ge: DNN Training Trajectories for Fault Detection and Diagnosis'
title_zh: Deep4ge：面向故障检测与诊断的DNN训练轨迹数据集
authors:
- Sigma Jahan
arxiv_id: '2607.12868'
url: https://arxiv.org/abs/2607.12868
pdf_url: https://arxiv.org/pdf/2607.12868
published: '2026-07-14'
collected: '2026-07-15'
category: Training
direction: DNN训练故障检测基准数据集
tags:
- DNN Training
- Fault Detection
- Benchmark Dataset
- Training Trajectory
- Fault Diagnosis
one_liner: 发布含1.4万余条带标注DNN训练轨迹的基准数据集Deep4ge，支撑训练故障检测诊断任务
practical_value: '- 可复用论文提出的27种故障注入方法，针对电商推荐/LLM微调训练场景模拟常见训练故障，优化训练监控告警规则，降低线上模型训练故障率

  - 可借鉴其设计的26维训练行为特征体系，搭建自有推荐/大模型训练健康度巡检工具，覆盖权重、梯度、硬件占用等多维度异常识别

  - 做推荐模型预训练/微调的early stop故障预判时，可参考其基于部分训练轨迹做故障预测的思路，减少无效训练的算力浪费'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有DNN训练故障检测与诊断研究缺乏公开的带完备标注的逐epoch训练轨迹基准数据集，无法支撑相关任务的标准化开发与效果验证。
### 方法关键点
1. 基于Stack Overflow收集的59个TensorFlow/Keras DNN项目，通过27种源代码变换注入7类已知故障，生成可控基准数据集Deep4ge
2. 每条训练运行记录逐epoch的4个评估指标、26维训练行为特征，覆盖权重、梯度、激活、精度损失趋势、学习率、硬件占用等维度
3. 支持三类任务：二分类故障检测、多分类故障诊断、基于部分训练轨迹的早期故障预测
### 关键结果
数据集共包含14227条训练运行记录，其中9845条为故障运行、4382条为正常基线运行，配套开源故障注入框架。
