---
title: Multiplayer Interactive World Models with Representation Autoencoders
title_zh: 基于表征自编码器的多玩家交互式世界模型
authors:
- Anthony Hu
- Václav Volhejn
- Adrien Ramanana Rahary
- Chris Mulder
- Aditya Makkar
- Amélie Royer
- Manu Orsini
- Alyx Liao
- Adam Jelley
- Eloi Alonso
affiliations:
- Kyutai
- Epic Games
arxiv_id: '2607.05352'
url: https://arxiv.org/abs/2607.05352
pdf_url: https://arxiv.org/pdf/2607.05352
published: '2026-07-05'
collected: '2026-07-08'
category: Agent
direction: 多智能体 · 世界模型构建
tags:
- Multi-Agent
- World Model
- Latent Diffusion
- Autoencoder
- Generative Modeling
one_liner: 提出首个支持多智能体动作条件的50亿参数潜扩散世界模型，可实时生成高动态物理交互场景
practical_value: '- 多智能体条件建模思路可迁移到电商多角色交互仿真，比如模拟商家、平台、用户三方博弈的流量变化场景

  - 长时序生成稳定性优化方案可复用在直播/短视频内容生成、用户长期行为序列预测等业务场景

  - 仅用短片段训练、长rollout不崩溃的训练trick可借鉴到生成式推荐的长序列用户兴趣建模'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有单玩家世界模型将其他智能体归为环境一部分，无法精准归因多智能体共同作用下的场景变化，无法支撑高动态多角色交互场景的仿真需求。
### 方法关键点
基于表征自编码器构建多玩家世界模型，以多智能体动作流为输入条件，学习将场景变化归因到对应玩家，同时系统优化了视频编解码器、生成目标、多玩家条件机制三大核心设计模块。
### 关键结果
基于1万小时公开机器人对战数据训练的50亿参数潜扩散模型，单张Nvidia B200 GPU可实时生成4人对战画面，帧率达20FPS；仅用短片段训练即可实现5分钟稳定生成，实测可连续生成数小时无模式崩溃，同时支持针对性评估物理理解能力而非仅视觉效果。
