---
title: Data-Free Reservoir Features for Efficient Long-Horizon Cold-Start Continual
  Learning
title_zh: 面向高效长时程冷启动持续学习的无数据储层特征方法
authors:
- Augustinas Jučas
- Yangchen Pan
affiliations:
- University of Oxford
arxiv_id: '2606.27095'
url: https://arxiv.org/abs/2606.27095
pdf_url: https://arxiv.org/pdf/2606.27095
published: '2026-06-25'
collected: '2026-06-27'
category: Training
direction: 持续学习 · 冷启动无回放训练优化
tags:
- Continual Learning
- Cold Start
- Feature Extraction
- Class Incremental Learning
- Training Efficiency
one_liner: 提出采用无数据训练固定特征提取器的CIRCLE方案，实现低开销无回放冷启动持续类别增量学习
practical_value: '- 电商新商品/新用户冷启动分类场景可复用固定无训练随机特征提取器思路，省去预训练或backbone反复微调开销，适配流式新类增量需求

  - 新类持续接入的推荐召回/广告分类任务可借鉴特征层+预测层双集成策略，在低训练成本下平衡偏差方差，缓解灾难性遗忘

  - 流式更新场景可复用SLDA流式闭式更新头，无需反向传播即可实现样本级增量更新，大幅降低长时程任务训练算力成本'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有无样例冷启动类别增量学习方法要么全流程训练backbone需反复做语义漂移补偿，算力开销随任务量增长陡增；要么首任务后冻结backbone，特征偏向初始类别效果差，两类方案均存在效果与效率难以兼顾的矛盾。

### 方法关键点
CIRCLE类别增量分类器采用完全无需在数据上训练的固定双向二维储层特征提取器，搭配流式线性判别分析(SLDA)头；通过多组随机储层特征集成、独立SLDA头softmax输出平均的双集成策略，可灵活调节偏差-方差权衡；特征提取器固定+分类头支持流式闭式更新，无需回放、任务边界信息与backbone反向传播即可实现样本级训练。

### 关键结果
在CIFAR-100、TinyImageNet等数据集上，10-20任务拆分下效果与基线相当；50/100/500长任务拆分下大幅优于CS-EFCIL强基线，训练速度远高于带漂移补偿的backbone训练方案。
