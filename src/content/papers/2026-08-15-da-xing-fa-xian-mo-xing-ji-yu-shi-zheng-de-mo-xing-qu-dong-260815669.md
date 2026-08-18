---
title: 'Large Discovery Models: Empirically-grounded Model-Based Open-Ended Search'
title_zh: 大型发现模型：基于实证的模型驱动开放式搜索架构
authors:
- Zhongwei Yu
- Yan Song
- Xue Yan
- Anjie Liu
- Xingyu Lu
- Yihang Chen
- Huichi Zhou
- Siyuan Guo
- Luoyang Sun
- Sihan Chen
affiliations:
- University College London
- The Hong Kong University of Science and Technology (GZ)
- Institute of Automation, CAS
- Jilin University
- AI Lab, The Yangtze River Delta
arxiv_id: '2608.15669'
url: https://arxiv.org/abs/2608.15669
pdf_url: https://arxiv.org/pdf/2608.15669
published: '2026-08-15'
collected: '2026-08-18'
category: Other
direction: 开放式假设空间 · 通用搜索引擎
tags:
- Open-Ended-Search
- Bayesian-Surrogate
- Generative-Model
- LLM
- Uncertainty-Aware
one_liner: 耦合生成模型与贝叶斯非参数奖励代理，实现开放式假设空间的高效搜索
practical_value: '- 可复用「生成模型+贝叶斯奖励代理」架构，做电商长尾/新品的开放式召回，用不确定性感知值过滤低潜力候选，降低试错成本

  - 可借鉴「记忆库+代理模型持续迭代更新」逻辑，优化搜索推荐冷启动探索流程，基于用户反馈动态调整生成偏好，提升冷门候选挖掘效率

  - 多目标优化场景下，可复用不确定性引导生成逻辑，替代纯LLM反思方案，在广告文案生成、商品标题优化等场景提升多指标效果'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
科学发现、分子设计等场景需在超大开放式假设空间优化高评估成本的目标，现有LLM生成候选的自评估可靠性低，对分布外新颖候选的不确定性校准能力差，纯LLM反思或传统统计搜索效率极低。

### 方法关键点
Large Discovery Model (LDM) 为经验驱动的循环架构，耦合生成模型与贝叶斯非参数奖励代理模型：生成模块负责提出、优化候选设计，代理模块预测候选性能并量化不确定性，输出不确定性感知价值信号指导候选的生成、优化与选择；每次新实验观测结果输入后，持续更新发现记忆库与代理模型，实现迭代优化。

### 关键结果
在神经网络训练、抗体设计、分子优化三个跨模态场景验证，对比纯LLM反思、传统统计搜索方案：验证BPB降低幅度提升2.4倍，抗体结合能相对降低18.2%，分子多目标优化性能相对提升超60%。
