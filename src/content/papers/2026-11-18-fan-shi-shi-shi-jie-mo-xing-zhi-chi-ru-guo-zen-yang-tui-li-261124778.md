---
title: 'Counterfactual World Models: JEPAs That Reason About "What If"'
title_zh: 反事实世界模型：支持「如果怎样」推理的JEPA架构
authors:
- Randall Balestriero
- Yann LeCun
- Kerda Varaku
affiliations:
- Brown University
- AMI Labs
- New York University
- Independent Researcher
arxiv_id: '2611.24778'
url: https://arxiv.org/abs/2611.24778
pdf_url: https://arxiv.org/pdf/2611.24778
published: '2026-11-18'
collected: '2026-11-19'
category: Agent
direction: Agent世界模型 · 反事实推理
tags:
- World Model
- JEPA
- Counterfactual Reasoning
- Causal Inference
- Autonomous Agent
one_liner: 无需反事实数据与模型重训，基于物理平滑假设实现JEPA高精度反事实推理
practical_value: '- 电商推荐/广告投放的反事实效果预估场景，若符合「干预动作与隐干扰（如流量波动、用户临时偏好）作用通道独立」假设，可直接复用残差修正公式，无需收集反事实标注数据、无需重训现有预估模型，即可快速得到反事实结果

  - 已部署的预测模型做反事实扩展时，仅需新增两次不同动作的预测调用、加观测结果残差修正步骤，工程改造成本极低，可快速落地归因、复盘类需求

  - 做决策归因时，可直接用该方法区分决策错误与运气因素（如不可观测的外部干扰），无需额外做AB实验即可快速复盘运营策略效果'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有世界模型仅能完成事实预测，无法回答「如果采取其他动作会发生什么」的反事实问题，而这类问题是Agent决策归因、复盘优化的核心。理论证明仅用事实数据训练的模型天然存在反事实耦合歧义，现有反事实推理方法要么需要昂贵的反事实标注数据，要么要求重训模型，落地成本极高。

### 方法关键点
- 基于「自然无跳跃」物理假设，当动作与隐干扰作用通道独立时，反事实结果等价于观测结果加世界模型对两种动作的预测差值，无需额外参数、反事实数据或模型重训
- 推导了该残差修正方法的误差上界为O(h²)（h为动作执行时长），且是仅用事实数据下的最小最大最优估计
- 支持直接在预训练视觉编码器（DINOv2/MAE等）输出的特征空间或物理量读出空间做修正，兼容任意冻结预训练编码器

### 关键实验
在5个物理仿真环境（含水下机器人场景）测试，对比普通JEPA基线：
- 反事实R²从38~46%提升到86~96%，水下机器人场景用16倍事实数据可达90~94%
- 事后规划任务中，找到最优动作的比例从14~23%提升到35~69%
- 兼容7种不同的冻结预训练编码器，反事实R²均可达到81~95%

### 核心结论
仅用事实数据训练的世界模型本身无法解决反事实耦合歧义，但借助合理的场景结构假设（如动作与隐干扰独立），通过残差修正可以低成本实现高精度反事实推理
