---
title: 'Sylvas: Synergistic Learning Value based Device Scheduling in Federated Continual
  Learning'
title_zh: Sylvas：基于协同学习价值的联邦持续学习设备调度框架
authors:
- Yuxuan Sun
- Yuxuan Bai
- Tan Chen
- Sheng Zhou
- Zhisheng Niu
arxiv_id: '2609.15763'
url: https://arxiv.org/abs/2609.15763
pdf_url: https://arxiv.org/pdf/2609.15763
published: '2026-09-14'
collected: '2026-09-15'
category: Training
direction: 联邦持续学习 · 训练调度优化
tags:
- Federated Continual Learning
- Device Scheduling
- Edge Intelligence
- Semi-supervised Learning
- Learning Value
one_liner: 定义双维度协同学习价值指标，实现资源约束下FCL高价值设备调度
practical_value: '- 跨域联邦推荐训练可复用双维度价值评估逻辑，从数据分布差异、伪标签质量两个维度筛选高质量参与方，降低通信开销提升训练效率

  - 流式非平稳数据的模型更新场景可参考价值优先的调度策略，资源受限下优先选择覆盖时空分布缺口、标注质量高的数据源做增量训练

  - 半监督联邦训练场景可借鉴伪标签数量与可靠性的权衡方案，平衡未标注数据的利用率和训练噪声'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
联邦持续学习（FCL）可实现全局模型适配分布式非平稳数据流，广泛适用于边缘智能场景，但面临两大痛点：一是时空数据分布动态偏移，二是标注数据稀缺；现有方案无法量化边缘设备对全局训练的贡献，资源约束下难以调度最优设备完成及时的模型更新。

### 方法关键点
Sylvas调度框架定义双维度协同学习价值量化指标：
1. 分布价值：从时空分布维度评估设备数据对全局模型的贡献，优先选择能补全全局数据分布缺口的设备
2. 标签价值：权衡伪标注数据的数量与可靠性，降低半监督训练引入的噪声
整合两类价值得分，在通信、计算资源约束下筛选高价值设备参与训练。

### 关键结果
案例验证表明，Sylvas可支撑时空分布动态变化下的模型快速适配，大幅提升未标注数据的利用效率。
