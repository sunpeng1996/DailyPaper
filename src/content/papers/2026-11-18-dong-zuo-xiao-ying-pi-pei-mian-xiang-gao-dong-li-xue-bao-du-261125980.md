---
title: 'Learning What Actions Change: Action Effect Matching for Dynamics-Faithful
  World Models'
title_zh: 动作效应匹配：面向高动力学保真度世界模型的训练方法
authors:
- John Won
- Yonghoon Dong
- Jinwoo Shin
affiliations:
- KAIST
- RLWRLD
arxiv_id: '2611.25980'
url: https://arxiv.org/abs/2611.25980
pdf_url: https://arxiv.org/pdf/2611.25980
published: '2026-11-18'
collected: '2026-11-21'
category: Agent
direction: Agent 世界模型动力学保真度优化
tags:
- World_Model
- Auxiliary_Training
- Dynamics_Fidelity
- Policy_Planning
- Robotics
one_liner: 提出AFFECT辅助训练目标，无需同初始状态重复执行即可提升世界模型动力学保真度
practical_value: '- 电商Agent做促销策略、流量调控模拟时，可引入动作扰动+真实响应对齐的辅助训练目标，提升虚拟仿真环境对真实业务效果的拟合度，减少线下试错成本

  - 推荐/广告反事实预估场景可复用其无需同初始状态重复采样的训练思路，降低对多组对照AB实验的依赖

  - 生成式内容保真度对齐逻辑可迁移到广告文案、商品展示生成的效果校验环节，提升生成结果与目标动作的相关性'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有世界模型虽可生成高逼真度视频，但无法准确捕捉微小动作扰动对未来观测的影响，无法满足策略评估、基于模型的规划等场景需求，这类场景中相近动作往往会带来完全不同的结果。
### 方法关键点
提出AFFECT辅助训练目标：对基于任务无关人类遥操作训练的策略动作注入时间相关噪声，训练世界模型使其生成视频对噪声的响应与真实录制视频对齐，无需相同初始状态下的重复执行数据。
### 关键结果
- 在OGBench仿真、真实DROID、ALOHA-2场景下均提升世界模型推演保真度
- DROID数据集上，世界模型与真实机器人的策略成功率皮尔逊相关系数从0.47升至0.79，FVD最高降低23%
- 规划场景下采用AFFECT训练的世界模型选点，任务成功率最高提升8.3%
