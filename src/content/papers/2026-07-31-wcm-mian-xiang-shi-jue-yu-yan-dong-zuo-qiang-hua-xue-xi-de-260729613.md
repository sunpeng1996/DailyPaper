---
title: 'WCM: A World Critic Model for Vision-Language-Action Reinforcement Learning'
title_zh: WCM：面向视觉-语言-动作强化学习的世界评判模型
authors:
- Senyu Fei
- Xiaopeng Yu
- Siyin Wang
- Xianzhong Zhao
- Jingjing Gong
- Xipeng Qiu
affiliations:
- Tongji University
- Shanghai Innovation Institute
- Fudan University
arxiv_id: '2607.29613'
url: https://arxiv.org/abs/2607.29613
pdf_url: https://arxiv.org/pdf/2607.29613
published: '2026-07-31'
collected: '2026-08-04'
category: Agent
direction: VLA Agent 强化学习时序建模优化
tags:
- Reinforcement Learning
- VLA
- World Model
- Critic Model
- JEPA
- Robotics
one_liner: 提出联合预测未来隐态与价值估计的WCM，解决VLA模型RL后训练的时序建模缺陷
practical_value: '- 多模态Agent/推荐系统用户行为序列建模可复用双目标设计：在价值/打分回归之外加入未来隐态预测辅助任务，低额外成本提升表征时序捕捉能力

  - 多模态交互场景RL优化可直接复用轻量LeJEPA作为critic底座，兼容现有SOTA多模态backbone，无需大幅改造现有训练pipeline

  - 部分可观测场景（如用户行为序列截断、多模态交互信息不全）下，优先给价值估计模块增加显式时序建模目标，性价比高于单纯堆叠历史输入'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
VLA模型RL后训练在机器人操纵场景潜力突出，但现有基于critic的RL方法仅依赖单帧观测或单帧VLM隐态做价值估计，与机器人控制的部分可观测特性存在本质 mismatch；直接引入观测历史会随高维视觉空间指数级提升复杂度，且纯标量回报回归无法为跨时序动态学习提供足够监督，核心问题是critic表征缺乏显式世界建模目标，无法捕获价值估计所需的时序结构。
### 方法关键点
提出基于轻量LeJEPA架构的WCM，联合执行未来隐态预测与价值估计双任务，显式训练critic表征捕捉时序动态而非仅做标量回报回归；可无缝接入on-policy、off-policy训练流程，兼容Pi0、Pi0.5、OpenVLA-OFT等现有SOTA VLA backbone。
### 关键结果
在4个基准共149个任务上达到SOTA性能，分布内、分布外场景均有稳定提升，泛化增益尤其显著；7个真实世界操纵任务验证可跨场景稳定部署。
