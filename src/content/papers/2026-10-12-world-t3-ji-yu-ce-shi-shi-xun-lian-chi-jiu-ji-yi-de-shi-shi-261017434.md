---
title: 'World-T3: Test-Time Training as Persistent Memory for Real-Time Video World
  Models'
title_zh: World-T3：基于测试时训练持久记忆的实时视频世界模型
authors:
- Junyi Wu
- Zekun Li
- Chenhongyi Yang
- Chen Guo
- Lingchen Yang
- Yongan Zhang
- Xinyi Zhang
- Hongbing Hu
- Bartek Rymkowski
- Srinath Sridhar
affiliations:
- Meta Reality Labs
- University of Illinois Chicago
- Brown University
arxiv_id: '2610.17434'
url: https://arxiv.org/abs/2610.17434
pdf_url: https://arxiv.org/pdf/2610.17434
published: '2026-10-12'
collected: '2026-10-17'
category: Other
direction: 实时视频世界模型 · 测试时训练记忆优化
tags:
- World Model
- Test-Time Training
- Persistent Memory
- Real-Time Generation
- Autoregressive Distillation
one_liner: 提出带测试时训练持久记忆的实时视频世界模型，提升长时序生成一致性与推理速度
practical_value: '- 可借鉴测试时训练增量更新专用记忆参数的思路，解决LLM4Rec/智能Agent长会话用户兴趣记忆衰减问题，无需扩展KV cache长度

  - 基于key索引的快速权重记忆读取方案，可迁移到推荐系统实时用户兴趣建模，实现常数级存储与计算开销，不受会话长度影响

  - 双教师分布匹配蒸馏自回归模型为少步生成器的方法，可用于生成式推荐/Agent交互的推理加速，平衡效果与延时要求'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有视频世界模型长时序生成依赖模型自身隐式存储观测信息，超出激活上下文后易出现空间记忆衰减，生成场景一致性差，自回归推理速度慢无法满足实时交互需求。
### 方法关键点
1. 引入测试时训练（TTT）持久记忆模块，将历史观测固化到专用模型参数中；
2. 设计递归最小二乘规则，基于相机姿态作为键在线增量更新记忆，实现常数级存储与单步计算开销；
3. 通过双教师分布匹配将自回归模型蒸馏为少步生成器，兼顾生成质量与推理速度。
### 关键结果
长时序回访基准上，相比最强基线PSNR从13.52提升至18.31dB，绝对旋转误差从3.344°降至1.075°，单张NVIDIA B200 GPU上1280×704分辨率下推理速度达20.6FPS。
