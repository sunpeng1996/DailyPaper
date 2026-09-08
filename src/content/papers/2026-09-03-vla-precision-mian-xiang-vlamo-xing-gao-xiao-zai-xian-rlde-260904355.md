---
title: 'VLA-Precision: Asymmetric Co-Bootstrapping for Efficient Real-World Online
  RL of Vision-Language-Action Models'
title_zh: VLA-Precision：面向VLA模型高效在线RL的非对称协同自举框架
authors:
- Chenyu Su
- Zhaolong Shen
- Yuan Qian
- Chen Qian
- Rui Zhang
- Feng Yan
- Weixing Chen
- Fei Zhang
- Jiamin Wang
- Shuang Cong
affiliations:
- University of Science and Technology of China
- State Key Laboratory of Precision and Intelligent Chemistry
- Beihang University
- Zhongguancun Academy
- Hefei SpinX Technology
arxiv_id: '2609.04355'
url: https://arxiv.org/abs/2609.04355
pdf_url: https://arxiv.org/pdf/2609.04355
published: '2026-09-03'
collected: '2026-09-08'
category: Other
direction: 视觉语言动作模型 · 在线强化学习优化
tags:
- VLA
- Online RL
- Policy Optimization
- Asymmetric Bootstrapping
- Robotics
one_liner: 提出非对称协同自举框架，解决VLA模型在线RL的策略漂移与效率瓶颈
practical_value: '- 非对称多时间尺度自举思路可迁移到推荐系统在线RL迭代场景：小流量干预快速调优策略，全量回流数据校准价值信号，避免策略漂移

  - 不变状态解耦+按需流计算的架构设计可复用在大模型驱动的在线推荐/Agent服务中，提升推理吞吐量、降低延迟

  - 参考正则化的相对优势策略更新方法可用于GenRec在线微调，解决纯RL微调导致的生成输出分布漂移问题'
score: 6
source: arxiv-cs.HC
depth: abstract
---

### 动机
预训练VLA模型在高精度、高重复性任务上可靠性不足，引入真实世界在线RL微调时存在两大瓶颈：不可靠价值信号易引发策略漂移，大VLA的计算开销限制吞吐量与样本效率。
### 方法关键点
1. 提出非对称协同自举（ACoB）算法：跨时间尺度分层优化，早期用干预引导的行为学习快速提升策略质量，累积自主经验后通过全局回报传播+局部偏好排序校准价值估计，结合参考正则化抑制策略漂移
2. 设计ACoB-Stream闭环架构，采用不变状态解耦、按需流设计原则，适配大VLA的在线迭代需求
### 关键结果
在9个高精度化学任务、4种机器人实体上测试，平均成功率达98.3%，单任务平均耗时45.8min，单episode耗时27.6s；吞吐量与计算效率最高提升10.9倍，运行速度是VLA baseline的1.2倍、RL baseline的1.8倍。
