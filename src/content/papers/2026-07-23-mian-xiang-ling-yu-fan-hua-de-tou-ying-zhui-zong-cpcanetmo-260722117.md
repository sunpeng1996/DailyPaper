---
title: Projection Pursuit CPCANet for Domain Generalization
title_zh: 面向领域泛化的投影追踪CPCANet模型
authors:
- Yu-Hsi Chen
- Abd-Krim Seghouane
affiliations:
- The University of Melbourne
arxiv_id: '2607.22117'
url: https://arxiv.org/abs/2607.22117
pdf_url: https://arxiv.org/pdf/2607.22117
published: '2026-07-23'
collected: '2026-07-30'
category: Training
direction: 领域泛化 · 训练稳定性优化
tags:
- Domain Generalization
- Projection Pursuit
- CPCANet
- Covariance-free
- Stable Training
one_liner: 提出无协方差的PP-CPCANet解决小批量训练下CPCANet秩亏问题，实现领域泛化任务SOTA
practical_value: '- 电商推荐/广告跨域（不同品类/流量域）场景遇分布偏移时，可引入PP-CPCANet无协方差正交基学习方法，避免小批量训练下协方差秩亏问题，提升跨域泛化性能

  - 模型训练需约束参数正交性时，可复用Cayley变换的联合优化方案，保证正交约束下训练过程稳定

  - 特征对齐的优化目标设计可借鉴detached-median对称破缺色散目标，获得更稠密鲁棒的优化信号'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
领域泛化（DG）目标是学习抗分布偏移的鲁棒表征，现有CPCANet类几何对齐方法依赖批量协方差估计提取域不变结构，小批量训练下特征维度高于批量大小时会出现协方差秩亏问题，严重限制可恢复的公共子空间规模。
### 方法关键点
1. 提出无协方差框架PP-CPCANet，在Stiefel流形上学习全局正交基，通过Cayley变换实现正交基与网络参数的端到端联合优化
2. 引入对称破缺的detached-median投影追踪色散目标，提取公共主成分时提供更稠密、鲁棒的优化信号
### 关键结果
在4个DG基准数据集上取得SOTA性能，同时训练稳定性显著优于基线CPCANet
