---
title: 'SyncWorld: Visual Calibration Enables World Models as Zero-Shot Simulators'
title_zh: SyncWorld：视觉校准支撑世界模型作为零样本模拟器
authors:
- Yuncong Yang
- Zhengtao Han
- Furkan Ozyurt
- Zeyuan Yang
- Han Yang
- Junyi Cao
- Haoyu Zhen
- Yilun Du
- Chuang Gan
affiliations:
- UMass Amherst
- UC Berkeley
- NYU
- Harvard
arxiv_id: '2609.09155'
url: https://arxiv.org/abs/2609.09155
pdf_url: https://arxiv.org/pdf/2609.09155
published: '2026-09-07'
collected: '2026-09-13'
category: Agent
direction: 具身Agent · 世界模型零样本迁移
tags:
- World Model
- Zero-Shot Transfer
- Visual Calibration
- Embodied Agent
- Simulation
one_liner: 提出基于视觉校准的动作条件世界模型SyncWorld，支持跨未知环境零样本模拟无需额外训练
practical_value: '- 跨域迁移场景可复用视觉校准思路：引入少量源-目标域配对样本做上下文映射，无需全量重训即可适配新场景，可落地于跨品类/跨站点推荐迁移

  - 仿真环境搭建可借鉴零样本适配逻辑：针对新业务场景的用户行为仿真、推荐策略预演，仅需少量历史交互样本校准即可生成可靠模拟结果

  - 测试时策略优化思路可复用：上线前基于校准后的仿真环境做多轮策略迭代，无需额外训练即可提升策略效果，降低线上AB实验成本'
score: 4
source: huggingface-daily
depth: abstract
---

### 动机
现有动作条件世界模型作为具身Agent的想象仿真环境时，动作与像素空间的映射不具备通用性：环境、相机视角、机器人位姿/形态变化会导致相同数值动作的视觉表现完全不同，混合训练易产生监督冲突，部署泛化性极差，无法直接跨未知场景使用。
### 方法关键点
1. 提出SyncWorld动作条件世界模型，引入视觉校准片段（覆盖所有可控自由度的帧-动作配对数据），在上下文内注入场景专属的动作-视觉映射规则；
2. 训练阶段加入视觉校准上下文数据，引导模型学会通过视觉证据解读动作含义，无显式校准数据时可利用历史交互补全映射关系。
### 关键结果
可在完全未见过的场景下零样本完成动作结果仿真，无需任何额外训练；基于其多步rollout仿真能力，可直接在测试阶段优化策略效果，无需额外参数更新。
