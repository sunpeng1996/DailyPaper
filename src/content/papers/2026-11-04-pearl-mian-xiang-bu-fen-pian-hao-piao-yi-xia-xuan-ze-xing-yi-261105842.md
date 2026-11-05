---
title: 'PEARL: Prediction Error-Adaptive Regularized Learning for Selective Forgetting
  under Partial Preference Drift'
title_zh: PEARL：面向部分偏好漂移下选择性遗忘的预测误差自适应学习框架
authors:
- Rashmi Gangadharaiah
- Balakrishnan Narayanaswamy
affiliations:
- AWS
arxiv_id: '2611.05842'
url: https://arxiv.org/abs/2611.05842
pdf_url: https://arxiv.org/pdf/2611.05842
published: '2026-11-04'
collected: '2026-11-05'
category: RecSys
direction: 偏好漂移 · 在线自适应个性化推荐
tags:
- Contextual Bandit
- Preference Drift
- Selective Forgetting
- Online Learning
- Personalized Recommendation
one_liner: 针对用户部分偏好漂移问题提出定向选择性遗忘的神经上下文赌博机框架PEARL
practical_value: '- 电商个性化推荐场景遇到用户偏好漂移时，可复用双向Gram矩阵更新机制，仅在预测误差超标的特征维度回注不确定性，避免全维度遗忘丢失有效信息，效果比滑动窗口、折扣学习等统一遗忘方案高3~10个点

  - 探索率配置可复用误差自适应策略：基于用户维度的预测误差EMA动态调整探索权重，稳定偏好用户走近贪心策略，漂移用户自动提升探索强度，解决固定探索率无法兼顾稳定态和漂移态性能的痛点

  - 工程实现上仅需100K左右参数的MLP即可运行在CPU上，无需更新底层大模型权重，适合API调用类LLM服务的个性化响应选择场景，推理延迟在毫秒级'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
用户偏好并非静态，会随需求、场景变化发生漂移，现有非平稳赌博机方法采用全维度统一遗忘策略，浪费大量已学习的有效偏好信息；神经上下文赌博机的Gram矩阵仅能单向累积置信度，一旦偏好漂移，模型会持续利用过时预测结果，且无法定向校正置信度最高但已失效的特征方向，导致个性化推荐、LLM响应选择等场景性能严重下降。

### 方法关键点
- 误差自适应探索：维护每个用户的预测误差EMA，动态调整UCB探索bonus，预测准确的用户探索权重趋近于0走近贪心策略，漂移用户误差飙升后自动提升探索强度
- 双向Gram矩阵更新：常规更新收缩置信度之外，当预测误差超过用户历史平均时，仅在当前出错的特征方向回注不确定性，其余方向置信度保持不变，同时加光谱上限避免不确定性无限膨胀
- 仅需轻量MLP奖励模型，底层LLM/推荐权重完全冻结，可适配任意API类模型

### 关键结果
在PRISM个性化LLM响应选择基准（1500用户、21个LLM）中等偏好漂移场景下，PEARL比贪心策略高+4.0分，比最优神经赌博机基线高+2.5分（p<0.001），比统一遗忘方案高3~10分；偏好稳定场景下性能与贪心持平，CPU推理毫秒级。

### 核心结论
偏好漂移大多是局部而非全局的，定向选择性遗忘的效率比全维度统一遗忘高d/s倍（d为总特征维度，s为漂移维度），真实场景通常能带来10倍以上效率提升
