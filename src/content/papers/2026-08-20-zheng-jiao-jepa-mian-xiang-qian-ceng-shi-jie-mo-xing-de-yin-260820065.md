---
title: 'Orthogonal JEPA: Factorized Predictive States for Latent World Models'
title_zh: 正交JEPA：面向潜层世界模型的因子化预测状态表示
authors:
- Taoyong Cui
- Pheng Ann Heng
- Wanli Ouyang
affiliations:
- The Chinese University of Hong Kong (CUHK)
arxiv_id: '2608.20065'
url: https://arxiv.org/abs/2608.20065
pdf_url: https://arxiv.org/pdf/2608.20065
published: '2026-08-20'
collected: '2026-08-21'
category: Agent
direction: Agent 潜层世界模型表示学习
tags:
- JEPA
- World Model
- Representation Learning
- Factorization
- Latent State
one_liner: 提出基于正交预测因子化的潜层世界建模框架Orthogonal JEPA，解决标准JEPA单通路预测的容量冗余与梯度冲突问题
practical_value: '- 可将正交因子化思路迁移到用户行为序列建模，拆分用户兴趣的不同维度，避免主流兴趣压制长尾兴趣梯度，提升小众物品召回效果

  - 四类正则化策略（正交约束、因子活跃度正则、在线方差正则、预测回归约束）可直接复用在多兴趣表征、Semantic ID生成的训练环节，缓解表征坍塌问题

  - 因子化预测分支架构可用于推荐系统长时序行为预测，拆分不同时间跨度的预测任务，提升长周期用户转化预估准确率'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
标准JEPA采用单嵌入单预测通路的整体式状态设计，在复杂系统中会给主导信号分配冗余容量，同时给非主导预测结构传递弱梯度甚至冲突梯度，无法适配多场景预测、规划需求。

### 方法关键点
1. 基于正交预测因子化设计框架，用学习到的基矩阵将目标状态拆分为多个独立分量，每个分量对应专属预测分支从共享上下文表征中估计；
2. 加入四类约束优化：预测回归保留因子幅值、正交约束避免方向重叠、因子活跃度正则保证目标投影多样性、在线方差正则缓解编码器逐维坍塌；
3. 预测分量可合成完整潜态，支持时序预测、空间补全、局部观测补全等多类任务。

### 关键结果
在视觉、单细胞转录组、纵向健康记录、连续控制、分子动力学5类任务上，表征质量、预测精度、规划性能、长时序稳定性均优于标准JEPA。
