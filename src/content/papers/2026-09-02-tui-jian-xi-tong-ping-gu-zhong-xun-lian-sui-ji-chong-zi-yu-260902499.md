---
title: Training seeds and model-selection stability in recommender-system evaluation
title_zh: 推荐系统评估中训练随机种子与模型选择的稳定性分析
authors:
- Juan Manuel Rodriguez
- Oleg Lesota
- Antonela Tommasel
affiliations:
- Aalborg University
- Johannes Kepler University Linz
- ISISTAN, CONICET-UNCPBA
arxiv_id: '2609.02499'
url: https://arxiv.org/abs/2609.02499
pdf_url: https://arxiv.org/pdf/2609.02499
published: '2026-09-02'
collected: '2026-09-03'
category: Eval
direction: 推荐系统评估 · 可复现性优化
tags:
- Recommender-System
- Evaluation
- Reproducibility
- Model-Selection
- Random-Seed
one_liner: 量化训练随机种子对推荐系统评估的多维度影响，明确需将种子纳入标准化评估协议
practical_value: '- 业务迭代做A/B实验前，先做多种子重复训练验证模型效果波动阈值，避免单种子跑出的虚高效果上线后不及预期

  - 离线评估时将训练种子作为超参数的一部分做验证，至少选择3个不同种子的平均指标作为模型效果的判定依据

  - 线上模型选择时，优先选择不同种子下推荐列表重合度更高的模型，降低种子随机性带来的线上效果波动'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
推荐系统实验普遍默认单训练种子的结果稳定，忽略参数初始化、负采样、mini-batch排序等环节的随机性对评估结论的干扰，易导致复现性差、模型选择错误。
### 方法关键点
固定数据划分与评估协议，在不同超参数配置下仅改变训练种子，从三个维度量化种子影响：用户级指标敏感度、基于验证集的模型选择正确率、不同种子输出推荐列表的重合度。
### 关键结果
种子带来的效果波动普遍可检测，单种子结果会高估评估稳定性；种子影响大小取决于超参数配置的效果区分度、验证到测试集的效果迁移性、同分数模型的推荐列表相似度；仅当不同配置的效果差距>5%时，单种子的模型选择结论才相对可靠。
