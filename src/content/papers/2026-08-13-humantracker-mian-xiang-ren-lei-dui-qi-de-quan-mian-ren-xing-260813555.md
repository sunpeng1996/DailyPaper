---
title: 'HumanTracker: Towards Comprehensive and Human-Aligned Motion Tracking Benchmark'
title_zh: HumanTracker：面向人类对齐的全面人形动作跟踪基准
authors:
- Dairu Liu
- Zekun Qi
- Jiayu Zeng
- Ruixi Yu
- Yu Guan
- Yintianrun Zhang
- Xuchuan Chen
- Sikai Liang
- Zekai Li
- Chenghuai Lin
affiliations:
- Nankai University
- Tsinghua University
- Galbot
- Shanghai Jiao Tong University
- Peking University
arxiv_id: '2608.13555'
url: https://arxiv.org/abs/2608.13555
pdf_url: https://arxiv.org/pdf/2608.13555
published: '2026-08-13'
collected: '2026-08-16'
category: Other
direction: 人形机器人动作跟踪基准与评估
tags:
- Humanoid Robot
- Motion Tracking
- Benchmark
- Evaluation Metric
- Human Alignment
one_liner: 推出含153小时动作轨迹的HumanTracker基准，以及对齐人类偏好的评估指标HumanScore
practical_value: '- 偏好对齐的评估指标构建思路可复用：推荐/广告效果评估可基于用户成对偏好数据训练判别式指标，替代传统点击率等单点指标，捕捉用户隐性体验

  - 大规模基准的分层标注思路可迁移：推荐系统benchmark可按场景/行为类型分层打标签，支持算法效果的细粒度诊断

  - 时序Transformer做序列级偏好打分的架构可复用：长会话推荐的用户满意度评估，可基于整会话序列建模输出综合满意度得分'
score: 4
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有动作跟踪的运动学评估指标仅计算逐帧姿态差，漏检脚滑、落地时机错误、支撑不稳定等人类感知敏感的物理缺陷；主流测试集规模小、多样性不足，无法覆盖多接触、长时序复杂行为场景。

### 方法关键点
1. 构建HumanTracker基准，包含153小时专业表演者的光学运动轨迹，分为4类动作族并配套文本标签，支持细粒度效果诊断；
2. 提出HumanScore偏好对齐评估指标，基于12K共24K条动作的成对偏好数据，用时序Transformer训练得到序列级综合打分。

### 关键结果
在主流SOTA跟踪器上的测试显示，HumanScore对人类偏好的预测效果优于传统指标，可识别运动学指标常漏判的接触、稳定性故障。
