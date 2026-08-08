---
title: 'DyPES-VLA: Learning Shared Dynamics Priors and Embodiment-Specific Control
  for Cross-Embodiment Manipulation'
title_zh: DyPES-VLA：面向跨实体操控的共享动态先验与实体专属控制学习
authors:
- Junfeng Li
- Junjie He
- Zhide Zhong
- Yangyang Zheng
- Pingyue Sheng
- Jiayu Dong
- Ruixin Li
- Haodong Yan
- Jiaguan Zhu
- Tianran Zhang
affiliations:
- The Hong Kong University of Science and Technology (Guangzhou)
- COCO Matrix
arxiv_id: '2608.06374'
url: https://arxiv.org/abs/2608.06374
pdf_url: https://arxiv.org/pdf/2608.06374
published: '2026-08-05'
collected: '2026-08-08'
category: Other
direction: 跨实体机器人VLA操控模型优化
tags:
- VLA
- MoE
- Cross-Embodiment
- Robot Manipulation
- Dynamics Prior
one_liner: 提出跨实体VLA模型DyPES-VLA，通过共享动态先验+实体专属MoE头免手动动作对齐达成SOTA
practical_value: '- 多场景/多品类适配任务可复用「共享底层先验+场景专属MoE头」架构，无需手动对齐不同场景的输出空间，大幅降低预处理成本

  - 底层表征学习可引入未来预测辅助任务，驱动表征捕捉交互、状态变化等核心动态信息，有效提升跨场景迁移性

  - 异构任务输出头可参考“共享注意力层捕捉通用时序结构+专属FFN适配场景独特约束”的设计，兼顾模型泛化性与场景适配精度'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有跨实体VLA模型存在两大局限：一是未充分挖掘多源视觉、交互数据中的共享动态先验，跨实体迁移能力受限；二是需要大量手动预处理将不同实体的动作转换为统一格式，落地成本高。
### 方法关键点
1. 基于跨实体数据，以未来预测为目标训练VLM，学习共享动态先验，驱动共享query表征捕捉物体运动、接触、交互引发的场景变化；
2. 设计实体专属MoE动作头：共享注意力层捕捉通用时序动作结构，实体专属前馈专家适配不同实体的运动学约束与控制语义，可直接输出各实体原生动作空间的控制指令，无需手动对齐异构动作。
### 关键结果
跨仿真与真实世界评测均达到SOTA，LIBERO成功率98.0%，RoboCasa-GR1达59.25%，RoboTwin 2.0达89.02%
