---
title: 'WorldCycle: Self-Verifiable Reinforcement Learning for Long-Horizon Video
  World Models'
title_zh: WorldCycle：面向长时序视频世界模型的自验证强化学习
authors:
- Bohai Gu
- Yueyang Yuan
- Taiyi Wu
- Dazhao Du
- Jian Liu
- Xiaoyi Pang
- Jie Zhang
- Xiaocheng Lu
- Haobin Zhong
- Xiaotong Zhao
affiliations:
- The Hong Kong University of Science and Technology
- Wuhan University
- AI Technology Center, Tencent Video, Tencent
arxiv_id: '2608.04964'
url: https://arxiv.org/abs/2608.04964
pdf_url: https://arxiv.org/pdf/2608.04964
published: '2026-08-04'
collected: '2026-08-06'
category: Agent
direction: 长时序视频世界模型自验证RL优化
tags:
- World Model
- Reinforcement Learning
- Self-Supervised Learning
- Long-Horizon Planning
- Video Generation
one_liner: 提出基于可逆动作闭环的自验证RL框架，解决长时序视频世界模型误差累积问题
practical_value: '- 长时序Agent任务无标注优化可复用可逆闭环思路：构造正向+逆向操作序列，无需ground truth即可监督序列生成的长期正确性，降低标注成本

  - 双奖励设计可迁移到序列生成类任务：空间对称+时序一致性的奖励组合，可用于用户行为序列建模、长文案生成等场景的漂移抑制

  - 电商虚拟交互场景（如3D商品预览、虚拟试穿的交互世界模型）可直接引入该框架，减少长时序交互操作的误差累积'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
交互式视频世界模型支撑长时序规划与探索，但自回归生成存在严重的误差累积问题，传统RL后优化方案无长时序漂移的ground truth标注，面临验证瓶颈。

### 方法关键点
核心思路是利用可逆动作闭环的天然约束：任意动作序列拼接其逆序列，必然回归初始状态，可提供无标注的长时序正确性监督。基于普通动作序列生成闭环节点及重复执行样本，优化两个互补奖励：空间闭合奖励约束正向、反向生成段的对称性，时序一致性奖励对齐多次闭环执行的状态。同时开源CycleBench基准，用于测试复杂动作结构下的状态回归能力。

### 关键结果
相比基线模型，状态回归漂移最高降低44%，复合动作准确率提升近4倍
