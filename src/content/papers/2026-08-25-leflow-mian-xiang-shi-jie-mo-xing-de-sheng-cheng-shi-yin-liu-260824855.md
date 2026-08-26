---
title: 'LeFlow: Generative Latent Flow Planning for World Models'
title_zh: LeFlow：面向世界模型的生成式隐空间流规划方法
authors:
- Hsiang-Wei Huang
- Jianxu Shangguan
- Junbin Lu
- Jenq-Neng Hwang
affiliations:
- University of Washington
arxiv_id: '2608.24855'
url: https://arxiv.org/abs/2608.24855
pdf_url: https://arxiv.org/pdf/2608.24855
published: '2026-08-25'
collected: '2026-08-26'
category: Agent
direction: Agent 世界模型隐式规划优化
tags:
- World Model
- Generative Planning
- Rectified Flow
- Amortized Planning
- Inverse Dynamics
one_liner: 在冻结隐式世界模型上学习可复用轨迹先验，替代在线迭代规划，提速一个数量级且提升成功率
practical_value: '- 做电商导购Agent、多步营销路径规划时，可复用「离线训练隐空间轨迹先验+在线小批量rollout选优」范式，替代CEM类在线迭代优化，大幅降低端到端时延，适配线上高QPS要求

  - 业务已有冻结的预训练大模型（比如用户兴趣向量模型、召回语义模型）时，可直接在其隐空间训练轻量生成式规划模块，无需微调原有大模型，改造成本极低

  - 生成多步序列（比如推荐路径、营销动作序列）时，优先在低维平滑的隐空间做生成，再解码为可执行的原始动作/物品序列，比直接生成原始序列效果更稳定、泛化性更强'
score: 8
source: arxiv-cs.CV
depth: full_pdf
---

### 动机
现有隐式世界模型的规划环节依赖CEM等在线迭代优化方法，每个状态-目标对都需要从零开始搜索最优动作序列，完全不复用历史规划经验，在线计算成本极高，无法落地时延要求严格的真实业务场景。
### 方法关键点
- 全程冻结预训练世界模型权重，仅训练两个轻量模块：1）条件Rectified Flow隐式规划器，以当前状态、目标状态的隐向量为固定锚点，生成中间的连续隐状态轨迹；2）逆动力学解码器，输入相邻隐状态及其位移特征，解码为可执行的动作块；
- 在线推理引入rollout重排：批量生成N条候选隐轨迹，解码为动作后用冻结世界模型做自回归推演，选择最终推演状态离目标最近的候选执行；
- 训练新增一致性损失，约束生成的隐状态跳转经过动作解码、世界模型推演后与原值一致，保证轨迹的动态可达性。
### 关键实验
在4个主流目标条件像素控制基准上对比LeWM+CEM baseline，成功率最高提升26.7个百分点，端到端规划时间降低4.5~14.4倍；适配冻结DINO-WM后，比其原生CEM规划提速14.7倍，成功率高出2个百分点，泛化到未见过的目标对无性能衰减。
### 核心结论
离线学习隐空间的规划先验，是大幅降低世界模型在线规划成本、同时提升效果的可行路径。
