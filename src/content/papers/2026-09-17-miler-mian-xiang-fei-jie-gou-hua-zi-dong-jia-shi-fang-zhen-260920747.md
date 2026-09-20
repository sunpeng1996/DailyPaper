---
title: 'MILER: Semantic Mid-Level Representation for Sim-to-Real Reinforcement Learning
  in Unstructured Autonomous Driving'
title_zh: MILER：面向非结构化自动驾驶仿真到现实迁移的语义中层表示方法
authors:
- Thomas Steinecker
- Denis Trescher
- Alexander Bienemann
- Thorsten Luettel
- Mirko Maehlisch
affiliations:
- Chair of Machine Perception for Autonomous Driving, University of the Bundeswehr
  Munich
arxiv_id: '2609.20747'
url: https://arxiv.org/abs/2609.20747
pdf_url: https://arxiv.org/pdf/2609.20747
published: '2026-09-17'
collected: '2026-09-20'
category: Other
direction: 自动驾驶 · RL 仿真到现实跨域迁移
tags:
- Reinforcement Learning
- Sim-to-Real
- Semantic Representation
- Zero-Shot Transfer
- Autonomous Driving
one_liner: 提出基于语义中层表示的MILER框架，实现非结构化自动驾驶RL策略零样本sim-to-real迁移
practical_value: '- 跨域迁移时统一训练/部署侧中间语义表示的思路，可复用解决推荐系统离线仿真到线上的领域Gap问题，减少分布偏移导致的效果折损

  - 策略输出前增加对齐校准层的设计，可借鉴到LLM4Rec/Agent生成结果的上线适配环节，降低仿真训练结果到真实业务的落地落差

  - 端到端轻量化推理栈的优化思路，可复用在边缘端推荐、端侧Agent等资源受限场景的模型部署'
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
RL在真实场景落地面临试错成本高的问题，自动驾驶非结构化场景下sim-to-real迁移的领域Gap始终缺乏有效解决方案，限制了RL的实际应用。
### 方法关键点
1. 提出MILER端到端策略框架，离线训练阶段基于自定义语义中层表示（MLR）模拟器训练RL策略，输出直接对接自行车运动模型；
2. 部署阶段用BEVFusion处理摄像头、LiDAR多模态传感数据，生成与训练侧对齐的语义鸟瞰图表示；
3. 新增轨迹对齐策略，RL生成的动作经适配后再下发到真实车辆，实现感知、控制全链路零样本迁移。
### 关键结果
在含障碍物、急弯、越野路段的3km测试赛道（最高时速33.6km/h）上，两款车辆累计无人工干预行驶17.3km，全栈可在Jetson AGX Orin上运行。
