---
title: Hand-Object Interaction in the Age of Large Foundation Models:Reconstruction,
  Generation, and Embodied Transfer
title_zh: 大模型时代的手物交互：重建、生成与具身迁移
authors:
- Weiquan Lin
- Yu Deng
- Shiyang Liu
- Luping Xiao
- Xu Tang
- Junzhi Yu
- Jiaolong Yang
- Lei Zhang
- Xingyu Chen
affiliations:
- Xidian University
- Zhongguancun Academy
- Microsoft Research Asia
- Peking University
- Visincept
arxiv_id: '2607.28394'
url: https://arxiv.org/abs/2607.28394
pdf_url: https://arxiv.org/pdf/2607.28394
published: '2026-07-30'
collected: '2026-08-01'
category: Other
direction: 具身智能 · HOI大模型先验综述
tags:
- HOI
- Foundation Model
- Embodied AI
- Survey
- Robot Learning
- 3D Vision
one_liner: 首个系统梳理大模型先验在HOI领域应用的综述，建立分类框架与具身迁移路径
practical_value: '- 开发具身电商Agent（如智能拣货、AR试穿交互）可直接复用文中8种大模型先验分类框架，按需匹配几何/语义/视觉先验解决交互建模问题

  - 实体导购、机器人带货场景的技能迁移，可参考HOI到机器人的3类具身迁移路径，降低技能训练的标注数据成本

  - 多模态推荐中AR/VR商品交互内容生成场景，可复用HOI生成任务的大模型先验注入方法，提升交互内容的真实度'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
手物交互（HOI）建模需同时推理手部关节、物体几何、接触语义、动力学特性，受视觉不确定性干扰大，现有大模型HOI相关研究零散，未系统梳理先验类型、注入方式与解决的问题边界。
### 方法关键点
1. 首个大模型HOI方向综述，将HOI任务划分为重建、生成2大类共6个子任务
2. 建立8种大模型子先验分类体系，归为几何、语义、视觉3个家族，明确不同先验在HOI pipeline的表示、注入、适配逻辑
3. 梳理HOI知识到机器人学习的3类具身迁移路径，汇总公开数据集与评估协议，维护持续更新的开源方法基准库
### 关键结果
提出的分类框架可覆盖当前所有主流大模型HOI方案，开源库已收录领域最新方法与基准，大幅降低后续HOI系统研发的选型成本
