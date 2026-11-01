---
title: A Pretrained Model for Bayesian Filtering in Heterogeneous Dynamical Systems
title_zh: 面向异质动态系统的贝叶斯滤波预训练模型FilterFM
authors:
- Ke Fan
- Wen Wu
- Haitao Su
- Yilin Wang
- Yuan Zhou
- Chao Zhang
affiliations:
- Shanghai AI Laboratory
- Tsinghua University
arxiv_id: '2610.40437'
url: https://arxiv.org/abs/2610.40437
pdf_url: https://arxiv.org/pdf/2610.40437
published: '2026-10-29'
collected: '2026-11-01'
category: Other
direction: 贝叶斯滤波 · 跨域预训练基础模型
tags:
- Bayesian Filtering
- Foundation Model
- Pretraining
- Zero-shot Generalization
- State Estimation
one_liner: 推出首个跨异质动态系统的贝叶斯滤波预训练模型FilterFM，支持未知动态系统零样本状态估计
practical_value: '- 分层双级编码器适配不同维度输入的设计，可迁移到跨域推荐中处理多域异构用户/物品特征

  - 分位数预测建模不确定性的方法，可用于推荐流量预估、冷启动打分的置信度建模

  - 单checkpoint跨异质任务预训练的范式，可复用在多场景统一推荐模型的训练流程中'
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有贝叶斯滤波方案存在两类局限：经典在线算法需输入已知动态规则，学习类神经滤波需针对单系统/参数族从零训练，核心瓶颈是异质动态系统的结构差异（控制逻辑、物理尺度、噪声水平不同），无法构建可复用滤波器的共享表征空间。
### 方法关键点
FilterFM是首个单checkpoint跨异质动态系统做隐状态估计的贝叶斯滤波预训练模型：1）采用分层双级观测序列编码器+先验到后验状态重建模块，适配不同系统的观测、状态维度差异；2）通过分位数预测建模状态不确定性；3）在混合异质滤波任务上完成预训练。
### 关键结果
域内任务上估计精度、运行效率、噪声鲁棒性均显著优于现有基线；首次实现未知动态系统上的零样本滤波，突破状态估计的泛化瓶颈；验证了基础模型范式下贝叶斯滤波的缩放定律，消融实验证明结构设计最优
