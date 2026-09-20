---
title: Learning Foresight without Explicit Trajectories for 3D Diffusion Policies
title_zh: 无需显式轨迹的3D扩散策略前瞻性学习方法
authors:
- Zhongbo Zhang
- Zaibin Zhang
- Yifan Wang
- Changbo Yan
- Lijun Wang
- Huchuan Lu
affiliations:
- Dalian University of Technology
arxiv_id: '2609.20669'
url: https://arxiv.org/abs/2609.20669
pdf_url: https://arxiv.org/pdf/2609.20669
published: '2026-09-17'
collected: '2026-09-20'
category: Other
direction: 3D扩散策略 · 机器人交互预判
tags:
- Diffusion Policy
- 3D Perception
- Robot Manipulation
- Latent Representation
- FiLM
one_liner: 提出运动趋势引导方法，无需显式轨迹即可为3D扩散策略引入前瞻交互预判能力
practical_value: '- 可借鉴「稀疏未来信号监督隐态」思路：生成式推荐/Agent决策场景无需完整未来轨迹标注，仅用稀疏未来目标监督隐表示即可提升长期决策连贯性，大幅降低标注成本

  - 可复用「仅在UNet瓶颈层加门控FiLM分支」的轻量改造方案：对现有扩散生成架构做最小侵入修改，仅增少量参数即可实现全局条件注入，适配大模型微调、生成式推荐等增量迭代场景

  - 「历史观测压缩为前瞻隐态作为推理条件」范式可迁移：适用于搜索推荐用户行为序列建模、Agent多轮交互决策等依赖上下文的场景，平衡推理效率与长期效果'
score: 4
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有3D扩散策略仅基于当前观测生成几何可行的动作，缺乏对交互发展趋势的前瞻性预判，依赖隐式学习的前瞻能力效果有限，引入显式规划又会大幅提升系统复杂度。
### 方法关键点
1. 提出Movement Trend Guidance模块，从短时序观测历史学习交互演化的紧凑latent representation，训练阶段用稀疏未来夹爪状态监督该隐态，推理阶段仅保留该隐态作为全局前瞻条件，与当前观测共同输入
2. 仅在UNet瓶颈层新增门控FiLM分支注入全局条件，对原DP3架构侵入极小，仅增加3.52%参数，保留原有密集动作、滚动时域范式不变
### 关键结果
在RoboTwin2.0 50任务混合训练中准确率达62.8%（基线DP3为56.1%），LIBERO-40数据集达71.93%（基线37.08%），5个真实机器人任务达72.0%（基线49.0%），全场景大幅领先基线
