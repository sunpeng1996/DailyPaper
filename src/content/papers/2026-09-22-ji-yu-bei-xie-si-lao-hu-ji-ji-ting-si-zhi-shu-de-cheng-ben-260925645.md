---
title: Efficient Cost-Aware LLM Evaluation via Bayesian Bandit Gittins Indices
title_zh: 基于贝叶斯老虎机吉廷斯指数的成本感知高效LLM评估方法
authors:
- Qian Xie
- Yueli He
- Nairen Cao
affiliations:
- Cornell University
- Columbia University
- New York University
- Shanghai University of Finance and Economics
arxiv_id: '2609.25645'
url: https://arxiv.org/abs/2609.25645
pdf_url: https://arxiv.org/pdf/2609.25645
published: '2026-09-22'
collected: '2026-09-23'
category: Eval
direction: LLM自适应评估 · 贝叶斯老虎机优化
tags:
- LLM Evaluation
- Bayesian Bandit
- Gittins Index
- Cost-Aware Optimization
- Adaptive Testing
one_liner: 将LLM配置选择建模为成本感知贝叶斯老虎机问题，提出GittinsEval大幅降低评估开销
practical_value: '- 做LLM4Rec/Agent的prompt、解码参数调优时，可复用GittinsEval框架替代全量测试，仅用1%-2%成本即可选出最优配置

  - 大流量场景下的召回/排序策略效果验证，可借鉴其成本感知贝叶斯老虎机逻辑做自适应流量分配，提前终止低潜力策略的实验

  - 多模型选型对比时，可复用其LCB置信区间得分规则平衡收益与不确定性，实现随时可输出最优候选的机制'
score: 7
source: arxiv-stat.ML
depth: abstract
---

### 动机
全量遍历所有LLM配置（模型、prompt、温度、解码策略等）在所有测试样本上的评估开销极高，现有自适应评估方法缺乏成本感知与统一的停止规则，难以平衡效果与效率。

### 方法关键点
1. 将LLM最优配置选择建模为成本感知贝叶斯老虎机问题，基于贝叶斯最优Gittins策略决策下一个评估的配置与停止时机
2. 引入LCB风格得分建模后验不确定性，支持对全/部分评估的配置随时输出最优推荐
3. 仅需离线预计算+轻量线上更新，计算效率高

### 关键结果
在GSM8K、PIQA、AlpacaEval、MMLU数据集上效果稳定优于贝叶斯优化与无成本感知老虎机基线，仅用1%-2%全量评估成本即可实现接近零的简单regret，自适应停止规则通常在1%-10%成本占比时触发。
