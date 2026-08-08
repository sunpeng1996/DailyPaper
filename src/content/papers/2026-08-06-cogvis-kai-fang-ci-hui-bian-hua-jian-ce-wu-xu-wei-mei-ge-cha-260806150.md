---
title: 'CogVis: Must Open-Vocabulary Change Detection Perceive the Scene Anew for
  Every Query?'
title_zh: CogVis：开放词汇变化检测无需为每个查询重新感知场景
authors:
- Zijie Wang
- Chen Zhong
- Wei He
affiliations:
- Key Laboratory of Information Engineering in Surveying, Mapping and Remote Sensing,
  Wuhan University
arxiv_id: '2608.06150'
url: https://arxiv.org/abs/2608.06150
pdf_url: https://arxiv.org/pdf/2608.06150
published: '2026-08-06'
collected: '2026-08-08'
category: Other
direction: 开放词汇变化检测 · 认知记忆范式优化
tags:
- Open-Vocabulary Change Detection
- Cognitive Memory
- Inference Acceleration
- Dynamic Threshold
- Scene Perception
one_liner: 提出认知记忆引导的CogVis框架，解耦开放词汇变化检测时序与语义计算，实现SOTA性能与推理效率双提升
practical_value: '- 多Query查询场景可复用共性前置计算：将与query无关的无类别特征提取/感知步骤预计算缓存，避免每query重复计算，可直接迁移到电商多query检索、RAG多轮查询等场景提升推理吞吐量

  - 动态阈值校准思路可解决类目标分偏移问题：针对不同query/类目动态调整决策阈值，适配电商多类目下召回、排序的得分分布差异，提升跨类目效果稳定性

  - 多维度候选过滤方案可复用：综合语义、时序、结构多维度可靠性过滤候选，可应用于电商推荐异常结果过滤、候选去重等环节'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有开放词汇变化检测（OVCD）方法耦合时序感知、语义判别、区域校验环节，存在结果不稳定、多查询场景计算冗余的问题，无法适配开放世界落地需求。
### 方法关键点
1. 重构OVCD为感知-记忆-校验三阶段范式，首先通过Scene Change Perceptron（SCP）从冻结双时相特征提取可复用的无类别变化先验，解耦时序证据与语义类别决策
2. 引入Semantic Memory Calibrator（SMC）动态估计图像-query专属决策阈值，补偿类别相关的得分偏移
3. 用Adaptive Region Filter（ARF）结合语义、时序、结构三类可靠性特征过滤连通候选
### 关键结果
在7个覆盖语义变化检测、二值变化定位、建筑损毁评估的基准数据集上取得SOTA性能，通过共享场景级变化感知能力，推理吞吐量提升28.50%
