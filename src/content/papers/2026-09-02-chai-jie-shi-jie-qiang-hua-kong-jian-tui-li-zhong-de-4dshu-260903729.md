---
title: 'Unfold The World: Factorize 4D Properties in Reinforcing Spatial Reasoning'
title_zh: 拆解世界：强化空间推理中的4D属性因子分解
authors:
- Yijun Yang
- Shenghe Zheng
- Wenbo Li
- Jianhui Liu
- Haoze Sun
- Yanbing Zhang
- Jiaxiu Jiang
- Lin Song
- Haoyang Huang
- Nan Duan
affiliations:
- The Hong Kong University of Science and Technology (Guangzhou)
- Joy Future Academy
- The Hong Kong University of Science and Technology
- The University of Hong Kong
arxiv_id: '2609.03729'
url: https://arxiv.org/abs/2609.03729
pdf_url: https://arxiv.org/pdf/2609.03729
published: '2026-09-02'
collected: '2026-09-08'
category: Reasoning
direction: 多模态大模型 · 4D空间推理优化
tags:
- VLM
- Spatial Reasoning
- Reinforcement Learning
- 4D Perception
- Factorized Learning
one_liner: 提出因子化强化学习框架FactoSR，通过拆解4D子目标提升VLM空间推理性能
practical_value: '- 电商3D商品展示、虚拟试穿等多模态场景VLM推理优化时，可借鉴XY/Z/T三维子目标拆解思路，替代单一大目标优化，降低训练难度

  - 复杂多模态任务优化可复用「分治+约束强化」范式，将不可控的隐式学习拆解为可验证的子步骤，提升效果稳定性

  - 跨帧/多视角商品内容理解（如短视频商品识别、AR场景推理）场景，可加入时间可逆性、深度一致性显式约束，提升识别准确率'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有VLM基于2D投影训练，对物理世界的空间推理存在维度错配瓶颈，直接优化4D时空目标计算复杂度过高，常规SFT或新增空间Token无法构建连贯的隐式世界模型。
### 方法关键点
采用分治范式设计FactoSR因子化强化学习框架，将整体世界一致性推理问题拆解为三个正交几何子目标：平面对应（XY）、深度一致性（Z）、时间可逆性（T），在统一策略学习机制中优化这些可验证约束，将病态的投影恢复问题转化为可落地的推理步骤。
### 关键结果
在多视角和视频基准上大幅提升3D/4D推理能力，VSI-Bench上性能提升5.9%，All-Angles-Bench上提升4.5%，验证了显式因子化4D一致性约束是VLM具备世界感知能力的关键路径。
