---
title: 'Knowing When to Stop: Bayesian Optimal Stopping for LLM Evaluations'
title_zh: 知止：面向大语言模型评估的贝叶斯最优停止框架
authors:
- Toby D. Pilditch
affiliations:
- UK AI Security Institute, London, UK
arxiv_id: '2608.14425'
url: https://arxiv.org/abs/2608.14425
pdf_url: https://arxiv.org/pdf/2608.14425
published: '2026-08-14'
collected: '2026-08-17'
category: Eval
direction: 大语言模型评估 · 算力优化
tags:
- LLM Evaluation
- Bayesian Inference
- Adaptive Sampling
- Compute Optimization
- Optimal Stopping
one_liner: 提出基于贝叶斯推断的自适应停止框架optstop，大幅降低LLM评估的冗余算力消耗
practical_value: '- LLM4Rec/Agent效果评估可复用optstop自适应采样逻辑，无需固定每个测试case的重复次数，按不确定性分配算力，最高可省97%评估成本

  - 冷启动推荐、极端case召回等低性能边界场景的评估，可复用其近零性能时的谨慎采样策略，避免漏判稀有成功案例

  - 线上A/B测试分流可参考该框架逻辑，对效果不确定的策略组多分配流量，效果稳定后提前切量，降低线上实验风险'
score: 7
source: arxiv-cs.AI
depth: abstract
---

### 动机
当前LLM评估普遍采用固定采样预算，每个测试项重复相同次数，即使估算精度已经达标仍继续采样，造成大量算力浪费，大模型批量评估、多轮测试场景下成本压力尤为突出。
### 方法关键点
1. 提出optstop精度导向的自适应停止框架，将评估建模为序列测量问题：对不确定性高的测试项持续采样，估算精度达标即停止
2. 基于层次贝叶斯推断实现，支持二分类、序数、连续三类评估结果，无需预校准测试项库，可实时运行也可回溯计算
3. 新增安全机制：当模型性能接近0（稀有成功场景）时自动提高采样谨慎度，避免低估模型能力
### 关键结果
在200项、10轮的基准评估中，9种验证场景下可削减57%-97%的计划测试量，最终评估结论与全量运行完全一致
