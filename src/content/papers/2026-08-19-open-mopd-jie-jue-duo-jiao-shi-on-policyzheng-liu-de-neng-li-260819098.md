---
title: 'Open-MOPD: Diagnosing and Fixing Capability Imbalance in Multi-Teacher On-Policy
  Distillation'
title_zh: Open-MOPD：解决多教师On-Policy蒸馏的能力不平衡问题
authors:
- Huan-ang Gao
- Haohan Chi
- Yong Yan
- Shiyuan Feng
- Hanlin Wu
- Zheng Jiang
- Bingxiang He
- Wei-Ying Ma
- Ya-Qin Zhang
- Hao Zhou
affiliations:
- SIA-Lab of Tsinghua AIR and ByteDance Seed
- Institute for AI Industry Research, Tsinghua University
- Department of Computer Science and Technology, Tsinghua University
arxiv_id: '2608.19098'
url: https://arxiv.org/abs/2608.19098
pdf_url: https://arxiv.org/pdf/2608.19098
published: '2026-08-19'
collected: '2026-08-20'
category: Training
direction: 多教师On-Policy蒸馏 · LLM能力整合
tags:
- Knowledge Distillation
- On-Policy Distillation
- Multi-Teacher Distillation
- LLM Post-Training
- RLHF
one_liner: 提出三种针对性机制将多教师OPD的能力恢复率从35.6%提升至83.4%
practical_value: '- 多领域Agent/通用大模型蒸馏时，不要只平衡prompt采样比例，要按响应token数加权调整loss权重，避免短回复任务（如query改写、指令响应）得不到足够训练信号

  - 多任务RL/蒸馏训练可采用gap-aware动态预算分配，将训练资源倾斜到当前与教师差距大的任务，避免收敛任务浪费算力，同时裁剪权重防止训练崩溃

  - 多轮minibatch复用rollout的PPO类训练流程中，可复用教师log概率，仅刷新学生侧概率计算reward，几乎无额外开销即可解决reward stale问题

  - 整合多个垂直领域专家模型（如电商搜推广、客服、内容生成专家）到通用模型时，可直接复用Open-MOPD开源训练配方，降低试错成本'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
多教师on-policy蒸馏（M-OPD）是将多个垂直领域RL专家能力整合到单个通用学生模型的主流方案，但之前存在严重的能力整合缺口，朴素实现仅能恢复混合域SFT到RouteRL提升的35.6%，尤其短回复类任务（如指令跟随）性能退化严重、提前停滞，且业界缺乏可复现的开源实现。

### 方法关键点
- 搭建基于SmolLM3-3B的可控M-OPD基准，采用oracle路由隔离路由误差与能力整合问题，覆盖数学、代码、指令跟随三个领域
- token-share balancing：按目标预算比例加权各域loss，消除不同域响应长度差异导致的梯度token分配失衡，无需过采样短回复任务
- gap-aware动态预算分配：根据各域当前与教师的剩余差距动态调整权重，将更多资源分配给未收敛任务，同时做权重裁剪避免训练崩溃
- student reward refresh：复用缓存的教师log概率，每轮inner update前重新计算学生侧log概率生成reward，几乎无额外开销解决多轮minibatch导致的reward stale问题

### 关键结果
在三个领域共6个基准数据集上测试，对比朴素M-OPD，Open-MOPD将能力恢复率从35.6%提升至83.4%，总得分从28.05提升至31.24，仅比RouteOPD（分域部署多个模型）低0.31分；其中指令跟随域得分提升5.94分，解决了短回复任务的性能退化问题。

### 核心结论
多教师OPD的核心瓶颈不是教师间的梯度冲突，而是token级优化预算的错配
