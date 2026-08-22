---
title: 'ForgeWM: Progressive Causal Training for Few-Step Action-Conditioned Video
  World Models'
title_zh: ForgeWM：面向少步动作条件视频世界模型的渐进式因果训练
authors:
- Xinye Li
- Lingshuai Lin
- Lei Wang
- Liuzhou Zhang
- Jialin Cui
- Qingshan Li
- Guanchu Wang
- Qingbin Liu
- Xi Chen
- Jiang Bian
affiliations:
- CUHK
- Tencent PCG
- FDU
- Shanghai AI Laboratory
- HKUST
arxiv_id: '2608.14022'
url: https://arxiv.org/abs/2608.14022
pdf_url: https://arxiv.org/pdf/2608.14022
published: '2026-08-14'
collected: '2026-08-22'
category: Agent
direction: Agent 动作条件视频世界模型优化
tags:
- World Model
- Causal Training
- Controllable Generation
- Video Generation
- Knowledge Distillation
one_liner: 提出渐进式因果训练框架ForgeWM，实现低延迟高可控的少步动作条件视频世界模型
practical_value: '- 渐进式师生蒸馏+分布匹配的训练范式可迁移到GenRec场景，用双向大模型蒸馏1-4步轻量生成模型，兼顾推理 latency
  与生成效果

  - 双路径部署方案可复用在实时广告/商品短视频生成场景，在线用1步轻量模型满足RT要求，离线用重放优化生成高质感素材

  - 动作与生成结果对齐的约束思路可用于交互可控内容生成，比如电商带货短视频按用户交互动作生成对应画面的对齐优化'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
动作条件视频世界模型需同时满足低延迟因果生成、生成内容与用户操作精准对齐的要求，现有因果蒸馏方法适配交互式场景时，存在离散键盘/连续鼠标动作与时序压缩隐向量对齐困难的问题。
### 方法关键点
1. 四阶段渐进式训练流程：领域适配→教师强制因果训练→因果一致性蒸馏→与双向教师的同策略分布匹配，蒸馏出1、2、4步去噪的轻量学生模型；
2. 双路径部署协议：低延迟交互场景用1步学生模型输出，回放场景可基于已生成草稿重噪优化，兼顾实时性和生成质量。
### 关键结果
在Minecraft数据集上，成像质量、动作对齐度、鼠标控制精度均为SOTA，LPIPS最低；重放优化效果对齐4步模型质量，与真实轨迹偏差比随机噪声重建低约2/3；训练流程可直接迁移到手柄控制的FPS游戏场景。
