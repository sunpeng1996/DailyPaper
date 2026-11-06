---
title: 'VFlash: Fast, Accurate Visual Planning via Flash Primitive Decoding'
title_zh: VFlash：基于Flash基元解码的快速精准视觉规划
authors:
- Yu-Cheng Chou
- Shihao Wang
- Jin Huang
- Chi-Pin Huang
- Chiao-An Yang
- Xianzhe Fan
- Jing Wang
- Zhiqi Li
- Yuanguo Kuang
- Ruijie Zheng
arxiv_id: '2611.08449'
url: https://arxiv.org/abs/2611.08449
pdf_url: https://arxiv.org/pdf/2611.08449
published: '2026-11-04'
collected: '2026-11-06'
category: Agent
direction: Agent 视觉规划解码优化
tags:
- Visual Planning
- Decoding Optimization
- VLM
- Autoregressive Decoding
- Robotics
one_liner: 提出基于视觉基元结构化特征的并行解码框架VFlash，大幅降低视觉规划延迟同时提升精度
practical_value: '- 结构化输出场景（如电商广告素材坐标标注、商品展示框生成、用户行为轨迹预测）可复用基元并行解码思路，替代逐token自回归生成，大幅降低推理延迟

  - 训练时仅要求输出结构合法、无需严格匹配目标token序列的思路，可迁移到生成式推荐的结构化输出（如Semantic ID序列、多商品组合推荐）训练，兼顾效果与效率

  - 轻量级drafter单步生成完整基元的架构，可落地于推荐/广告系统的实时召回、端侧个性化展示等低延迟要求场景'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
机器人、自动驾驶等物理AI场景的视觉规划需输出坐标、边界框、轨迹等结构化信息，传统自回归VLM逐token生成坐标，推理延迟随输出复杂度线性上升，落地成本过高。
### 方法关键点
1. 利用视觉基元的已知结构化特征，设计轻量级drafter单次前向生成完整基元，布局自适应基元的类型、维度、长度，同时保留验证模块保证输出合法性；
2. 训练时无需对齐自回归模型的token序列，只要结构有效即可接受预测，不损失空间精度。
### 关键结果
3D点运动预测生成速度较自回归解码提升25倍；2D/3D机器人轨迹任务预测误差普遍低于自回归基线；基于VFlash规划的世界动作模型在4个MolmoSpaces任务集上平均成功率达70.2%，较基线62.6%提升7.6pct；在NVIDIA Jetson Thor、DGX Spark平台上解码延迟较自回归降低80%以上。
