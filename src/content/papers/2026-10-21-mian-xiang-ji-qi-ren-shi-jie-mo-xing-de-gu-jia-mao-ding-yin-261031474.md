---
title: Skeleton-Grounded Latent Action Model for Robot World Models
title_zh: 面向机器人世界模型的骨架锚定隐式动作模型
authors:
- Qi Lv
- Jiayi Lin
- Yuxin Jiang
- Jianzong Wang
- Xiang Deng
- Mike Shou Zheng
affiliations:
- HIT (Shenzhen)
- Show Lab, NUS
- Ping An Tech
arxiv_id: '2610.31474'
url: https://arxiv.org/abs/2610.31474
pdf_url: https://arxiv.org/pdf/2610.31474
published: '2026-10-21'
collected: '2026-10-26'
category: Other
direction: 机器人世界模型 · 跨模态隐式动作建模
tags:
- World_Model
- Latent_Action
- Cross_Modal
- Skeleton_Guidance
- Robotics
one_liner: 将隐式动作拆解为骨架锚定运动分量与残差视觉分量，提升机器人世界模型可控性与预测精度
practical_value: '- 隐式表征拆分思路可复用：生成式推荐/多模态召回中，可将用户/物品表征拆分为显式规则锚定的核心分量+残差补充分量，平衡模型效果与可控性

  - 跨模态互换重建trick可落地：多模态表征对齐任务中，用跨模态表征互换重建约束，可降低模态gap，提升跨域召回/推荐的一致性

  - 分支dropout训练策略可借鉴：序列推荐/Agent轨迹预测任务中，对依赖未来信息的分支加dropout，可有效缓解训练推理不一致问题'
score: 4
source: huggingface-daily
depth: abstract
---

### 动机
现有隐式动作模型通过重建学习视觉动态，得到的隐式动作混合了机器人运动、物体响应等多种场景变化，与实际机器人控制信号对应关系弱，世界模型可控性不足。
### 方法关键点
1. 提出SkeLAM框架，将隐式动作拆解为两部分：机器人骨架监督锚定的运动分量、保留补充视觉动态的残差分量
2. 引入跨模态互换重建约束，要求RGB与骨架衍生的运动表征在视频重建中可互换；双通路输入世界模型，搭配分支dropout降低模型对未来衍生残差信息的依赖
3. 用轻量Adapter映射机器人动作到运动空间，微调后支持基于当前观测+机器人动作生成未来观测
### 关键结果
在DROID数据集上，相比基准DreamDojo，末端执行器ADE降低19.5%，LPIPS降低11.1%；支持零样本人-机器人运动迁移，策略评估预测成功率与真实机器人执行结果高度一致
