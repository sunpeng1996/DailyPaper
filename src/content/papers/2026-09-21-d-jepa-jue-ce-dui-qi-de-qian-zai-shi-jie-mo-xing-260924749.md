---
title: 'D-JEPA: A Decision-Aligned Latent World Model'
title_zh: D-JEPA：决策对齐的潜在世界模型
authors:
- Shuaijun Liu
- Chengyu Wu
- Qifu Wen
- Feiyang You
- Chenglong Zhang
- Shuyang Hao
- Xi Lin
- Ningxin Su
affiliations:
- The Hong Kong University of Science and Technology (Guangzhou)
- Boston University
- Shanghai Jiao Tong University
arxiv_id: '2609.24749'
url: https://arxiv.org/abs/2609.24749
pdf_url: https://arxiv.org/pdf/2609.24749
published: '2026-09-21'
collected: '2026-09-22'
category: Agent
direction: Agent 世界模型决策对齐优化
tags:
- World_Model
- Decision_Alignment
- Latent_Representation
- JEPA
- Sequential_Decision
one_liner: 提出决策对齐的潜在世界模型D-JEPA，修正预测潜空间偏差，大幅提升多场景动作选择性能
practical_value: '- 电商导购Agent、搜索推荐候选排序场景可复用「预测特征+序贯执行证据联合推理」逻辑，修正仅靠语义相似度匹配的决策偏差，比如推荐路径选择时加入实际转化序贯信号调整潜空间权重

  - 预训练表示微调可借鉴「受限预测器适配+共享序贯接口」设计，无需全量微调即可在保留预训练几何结构的前提下实现下游决策对齐，降低LLM4Rec/生成式推荐的微调成本

  - 多候选排序任务可复用排列等变算子设计，同时建模单个item的目标匹配度与候选间的相对优劣关系，提升排序效果'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有潜在世界模型仅关注预测精度，预测潜空间与目标的距离无法反映候选动作的实际执行效果，存在决策局部预测gap：潜空间更靠近目标的候选反而实际执行结果更差。
### 方法关键点
1. 设计有界、排列等变算子，联合推理目标相关预测特征与序贯执行证据，在动作选择的高影响区域微调预训练预测几何结构
2. 采用受限预测器适配+共享序贯接口，无需破坏原预训练结构即可跨多预测几何实现决策对齐
3. 把学习到的决策结构写入JEPA兼容的未来表示，可直接通过原生latent-distance规划部署
### 关键结果
PushT任务成功率达87.89%，RoboTwin数据集平均性能提升15.04pt，实体机器人任务性能提升17pt
