---
title: 'MVP-Nav: Multi-layer Value Map Planner Navigator'
title_zh: MVP-Nav：多层价值地图规划导航框架
authors:
- Wenyuan Xie
- Shaokai Wu
- Yijin Zhou
- Yanbiao Ji
- Guodong Zhang
- Bayram Bayramli
- Qiuchang Li
- Xunchu Zhou
- Yue Ding
- Hongtao Lu
affiliations:
- Shanghai Jiao Tong University
arxiv_id: '2606.31919'
url: https://arxiv.org/abs/2606.31919
pdf_url: https://arxiv.org/pdf/2606.31919
published: '2026-06-30'
collected: '2026-07-01'
category: Agent
direction: 具身Agent 零样本视觉导航优化
tags:
- EmbodiedAgent
- ZeroShotNavigation
- 3DFoundationModel
- SpatialSemanticRepresentation
- RGBPerception
one_liner: 提出物理感知的仅RGB零样本物体导航框架，融合语义与几何约束实现无深度传感器方案的SOTA性能
practical_value: '- 电商仓储/线下导购具身Agent可复用2D语义实例转3D包围盒的方案，无需深度传感器即可实现物理感知，降低硬件成本

  - 多约束融合的推荐/搜索场景可借鉴多层价值地图的统一成本空间设计，同时兼顾语义优先级与底层业务/物理约束

  - 高成本感知输入受限的Agent推理场景，可参考结构化先验补全缺失信息的思路，降低对传感器/全量特征的依赖'
score: 7
source: arxiv-cs.AI
depth: abstract
---

### 动机
仅采用RGB感知的Zero-shot Object Goal Navigation (ZSON) 缺失深度信息，存在严重物理不确定性与语义-物理错位问题；现有方案要么无几何grounding仅做高层语义推理，要么端到端策略缺乏显式物理约束，易输出语义合理但物理不安全的行为。
### 方法关键点
1. 基于3D foundation model将单目观测的2D语义实例投影为3D定向包围盒，重建显式物理占用信息，构建全局空间语义表征；
2. 提出Multi-layer Value Map (MVM)，将语义优先级与重建几何信息整合到统一成本空间，实现具备物理grounding的几何规划，对齐感知、规划、控制与真实3D世界。
### 关键结果
在零样本物体导航基准上大幅领先所有现有无深度方法，达到SOTA性能，验证结构化物理先验可有效补偿主动深度传感器的缺失。
