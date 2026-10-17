---
title: Routing Policy Optimization for Online Diffusion Reinforcement Learning
title_zh: 面向扩散模型在线强化学习对齐的路由策略优化
authors:
- Qiuhong Shen
- Yiding Yang
- Yuxin Zhang
- Xinwei Huang
- Minxuan Lin
- Bo Liu
- Hao Kang
- Haotian Yang
- Yizhi Wang
- Chongyang Ma
affiliations:
- National University of Singapore
- ByteDance
arxiv_id: '2610.22282'
url: https://arxiv.org/abs/2610.22282
pdf_url: https://arxiv.org/pdf/2610.22282
published: '2026-10-15'
collected: '2026-10-17'
category: Training
direction: 扩散模型 · 强化学习对齐训练优化
tags:
- Reinforcement-Learning
- Diffusion-Model
- Attention-Routing
- Training-Optimization
- Efficiency-Optimization
one_liner: 提出基于注意力路由的扩散模型RL对齐方法，训练效率较Flow-GRPO提升近4倍
practical_value: '- 生成式推荐/营销素材生成场景，可复用RPO的注意力路由随机探索机制，提升扩散类文生图/文生视频模型RL对齐的训练效率，降低训练成本

  - 大模型在线微调场景可借鉴双rollout估计器设计，通过控制变量仅保留核心动作差异计算优势信号，减少冗余计算量同时稳定梯度更新

  - 需要保留原有推理链路的RL对齐场景，可复用RPO「训练引入随机路由、推理恢复原生结构」的设计思路，无需改动线上推理逻辑即可完成对齐优化'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有扩散模型RL对齐方法通过扰动反向去噪轨迹引入随机性，依赖大量rollout计算，训练成本极高，且会破坏原生采样器结构。
### 方法关键点
1. 提出RPO算法，将注意力路由作为随机探索动作，仅在部分选定去噪层级采样注意力路径，保留原生采样器结构；
2. 设计高斯似然损失对路径扰动打分，保证移除路由后训练更新依然有效；
3. 采用受控双rollout估计器，仅在采样注意力路由上存在差异，用奖励差计算优势信号，推理阶段恢复稠密注意力，完全保留原有确定性采样逻辑。
### 关键结果
文生图、文生视频实验显示，RPO在提升生成质量的同时，训练效率较Flow-GRPO类方法提升近4倍。
