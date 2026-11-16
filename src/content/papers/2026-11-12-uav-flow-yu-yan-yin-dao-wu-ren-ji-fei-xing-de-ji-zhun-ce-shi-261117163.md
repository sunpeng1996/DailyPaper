---
title: 'UAV-Flow++: A Unified Suite for Benchmarking and Learning Language-Guided
  UAV Flight'
title_zh: UAV-Flow++：语言引导无人机飞行的基准测试与学习统一套件
authors:
- Donglin Yang
- Xiangyu Wang
- Yantong Zhong
- Wenhao Zheng
- Zihan Ding
- Yue Liao
- Hongsheng Li
- Ke Xu
- Si Liu
affiliations:
- Beihang University
- National University of Singapore
- MMLab, The Chinese University of Hong Kong
arxiv_id: '2611.17163'
url: https://arxiv.org/abs/2611.17163
pdf_url: https://arxiv.org/pdf/2611.17163
published: '2026-11-12'
collected: '2026-11-16'
category: Agent
direction: 语言引导无人机Agent动作控制
tags:
- Language-Guided Control
- Vision-Language Agent
- Reinforcement Learning
- Benchmark Dataset
- Robotics
one_liner: 定义语言引导短程无人机飞行动作任务Flow，配套基准数据集与TGRPO优化的FlowVLA模型
practical_value: '- 多模态Agent做指令到动作对齐时，可借鉴虚实混合演示数据预训练+在线强化学习后调的范式，降低真实场景下的高质量样本采集成本

  - 强化学习优化策略时可参考TGRPO的分组奖励分布思路，强化高奖励序列的学习效率，可迁移至推荐排序多目标reward优化场景

  - 低资源垂类Agent任务可借鉴其基准构建思路，覆盖基础操作+复杂交互双维度的测试用例设计，提升评测完备性'
score: 4
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有语言引导无人机导航研究集中于长程路径规划，短程、物体相关的飞行动作控制领域存在研究空白，缺乏标准化任务定义、基准数据集与高效学习框架。
### 方法关键点
1. 定义Flow任务，要求无人机结合自然语言指令、第一视角视觉观测、当前状态输出连续飞行动作，覆盖基础运动指令和复杂物体交互行为；
2. 发布UAV-Flow数据集，包含30692条真实世界专家飞行轨迹、10109条仿真轨迹，配套带任务完成判定标准的UAV-Flow-Sim仿真环境；
3. 提出FlowVLA模型，先在虚实混合演示数据上做模仿预训练，再通过Tail-Aware GRPO（TGRPO）做在线后训练，利用分组奖励分布强化高奖励动作序列学习。
### 关键结果
仿真环境273个测试样本上，预训练FlowVLA成功率达75.58%，超最优基线6.72个百分点；经TGRPO后调后成功率升至93.16%，样本效率更优，真实室内外场景实验均验证了模型鲁棒性。
