---
title: Efficient Sequential Evaluation of Large Language Models
title_zh: 大语言模型的高效序列评估方法
authors:
- Chia-Yu Hsu
- Shubhanshu Shekhar
affiliations:
- EECS Department, University of Michigan
arxiv_id: '2607.17409'
url: https://arxiv.org/abs/2607.17409
pdf_url: https://arxiv.org/pdf/2607.17409
published: '2026-07-19'
collected: '2026-07-22'
category: Eval
direction: LLM评估 · 主动采样优化
tags:
- LLM Evaluation
- Active Sampling
- Confidence Sequence
- Sequential Testing
- Query Rule
one_liner: 利用历史LLM性能数据构建置信序列与主动查询规则，降低基准评估所需测试样本量
practical_value: '- 上线新LLM驱动的推荐/Agent/生成式文案服务前，可复用本文的序列评估框架，用更少测试样本快速验证模型能力，大幅降低预上线评估成本

  - 自定义业务benchmark评估时，可借鉴混合查询规则设计思路，将基于历史预测的定向采样与均匀探索结合，平衡评估效率与偏差控制

  - 评估模型时优先将均匀采样作为baseline，避免过度设计复杂自适应采样策略，反而因预测偏差导致评估效率下降'
score: 7
source: arxiv-stat.ML
depth: abstract
---

### 动机
当前LLM基准测试常包含数千道题目，全量评测成本高、耗时长，亟需可复用历史LLM测试数据的少样本高效评估方案。

### 方法关键点
1. 基于逆测试上鞅构建两类置信序列（CS）：反向信息投影（RIPr）法和博弈测试法，验证RIPr法在oracle设置下的最优性；
2. 提出增长导向查询规则，最大化当前CS端点的单步最差预期对数增量，基于历史数据学习的题目正确率预测构建查询策略；
3. 针对预测不匹配、查询分布尖峰两个拖慢CS收敛的核心问题，提出融合增长导向查询、预测修正、均匀探索的混合查询规则。

### 关键结果
实验显示混合查询规则可降低30%以上的评估样本量，同时简单的均匀采样有时性能优于复杂的自适应采样策略。
