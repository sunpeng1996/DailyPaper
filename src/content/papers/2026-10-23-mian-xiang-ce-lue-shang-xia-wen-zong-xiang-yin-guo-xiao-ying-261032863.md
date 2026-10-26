---
title: A Foundation Model for Policy In-Context Longitudinal Causal Effect Estimation
title_zh: 面向策略上下文纵向因果效应估计的基础模型
authors:
- Wenxin Chen
- Kyra Gan
- Mingyu Lu
- Zilin Jing
- Fei Wang
- Hoifung Poon
- Tristan Naumann
- Peniel Argaw
affiliations:
- Cornell University
- University of Washington
- Columbia University
- Recursion Pharmaceuticals
- Microsoft Research
arxiv_id: '2610.32863'
url: https://arxiv.org/abs/2610.32863
pdf_url: https://arxiv.org/pdf/2610.32863
published: '2026-10-23'
collected: '2026-10-26'
category: Reasoning
direction: 纵向因果效应估计 · 基础模型
tags:
- Causal Inference
- Foundation Model
- Longitudinal Data
- In-Context Learning
- Policy Evaluation
one_liner: 提出首个支持动态治疗策略的纵向因果估计基础模型PICLE-PFN，无需任务调参即可单次前向输出结果
practical_value: '- 可复用「预训练+上下文泛化」范式解决电商多业务因果估计冷启动问题，避免每个活动/补贴策略单独拟合nuisance模型的高额成本

  - 针对动态流量分发、个性化补贴等动态策略的效应评估，可借鉴用in-context历史决策样例表征目标策略的统一接口设计，降低多策略适配开发成本

  - 业务上线阶段可参考该思路将因果估计的计算成本转移到预训练阶段，实现线上单次前向出结果的低延迟推理'
score: 7
source: arxiv-cs.AI
depth: abstract
---

### 动机
纵向因果效应估计受时变混淆、treatment-混淆因子反馈环问题限制，现有方法需针对单数据集拟合nuisance模型，且仅适配预设策略/预测窗口，部署阶段计算耗时极高。

### 方法关键点
提出PICLE-PFN，为首个支持动态治疗策略的纵向因果估计基础模型：
1. 用in-context历史-决策演示表征目标策略，为多类治疗策略提供统一适配接口；
2. 基于纵向结构因果模型生成的合成数据预训练，实现跨数据集、策略、预测窗口的因果估计能力复用；
3. 新场景下无需任务专属训练或超参调优，单次前向即可输出条件平均潜在结果（CAPOs）。

### 关键结果
在合成、半合成纵向基准数据集上，RMSE表现与SOTA持平，不确定性校准效果显著提升，部署runtime仅为逐数据集调优的传统SOTA估计器的极小比例。
