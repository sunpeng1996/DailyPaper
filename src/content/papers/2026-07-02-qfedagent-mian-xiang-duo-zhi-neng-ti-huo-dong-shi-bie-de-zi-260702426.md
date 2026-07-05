---
title: 'QFedAgent: Quantum-Enhanced Personalized Federated Learning for Multi-Agent
  Activity Recognition'
title_zh: QFedAgent：面向多智能体活动识别的量子增强个性化联邦学习框架
authors:
- Quoc Bao Phan
- Tuy Tan Nguyen
affiliations:
- Department of Electrical and Computer Engineering, FAMU-FSU College of Engineering,
  Florida State University
arxiv_id: '2607.02426'
url: https://arxiv.org/abs/2607.02426
pdf_url: https://arxiv.org/pdf/2607.02426
published: '2026-07-02'
collected: '2026-07-05'
category: Agent
direction: 多智能体 · 联邦学习优化
tags:
- Federated Learning
- Multi-Agent
- Variational Quantum Circuit
- Non-IID
- Activity Recognition
one_liner: 提出面向多智能体的混合量子-经典个性化联邦学习框架，参数量较传统MLP融合降10倍，精度超传统联邦基线
practical_value: '- 端侧联邦学习场景下的多模态特征融合，可参考变分量子电路思路大幅压缩参数量，降低跨端通信成本

  - 处理non-IID分布的分布式数据训练任务时，可尝试量子-经典混合架构，在保障精度的前提下降低参数 overhead

  - 多智能体端侧协同任务中，量子编码与纠缠方案可迁移用来建模异源特征的高阶交互关系'
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
联邦学习适配分布式多智能体隐私保护训练需求，但传统方案处理non-IID多模态传感器流时精度退化严重，且经典多模态融合模块参数量大、通信成本高，难以适配端侧部署约束。
### 方法关键点
1. 设计混合量子-经典的个性化联邦学习框架QFedAgent，适配多智能体活动识别场景
2. 引入变分量子电路融合模块，通过量子态编码与纠缠建模异源传感器数据交互，大幅压缩融合模块参数量
### 关键结果
- 融合模块仅需72个量子旋转参数，相较传统MLP融合的3.3万参数量实现约10倍总参数缩减
- 在OPPORTUNITY数据集subject-based non-IID划分下，平均测试精度达97.7%，性能优于传统联邦基线
