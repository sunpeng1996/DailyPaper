---
title: 'Miles v0.1: Production-Level Post-Training'
title_zh: Miles v0.1：面向生产环境的全栈大模型后训练系统
authors:
- RadixArk
- Tom Chen
- Mao Cheng
- Shi Dong
- Kangrui Du
- Yanbin Jiang
- Jiajun Li
- Yiming Li
- Tao Lin
- Yusheng Su
affiliations:
- RadixArk
arxiv_id: '2609.08368'
url: https://arxiv.org/abs/2609.08368
pdf_url: https://arxiv.org/pdf/2609.08368
published: '2026-09-07'
collected: '2026-09-09'
category: Training
direction: 大模型分布式后训练系统优化
tags:
- RLHF
- Distributed Training
- LoRA
- MoE
- Production System
one_liner: 推出全栈生产级大模型后训练系统，覆盖RL、LoRA微调等场景，支持大规模分布式部署
practical_value: '- 做Agent RL微调（如电商导购Agent、广告文案生成Agent）的团队可直接复用异步rollout+训练解耦架构，采用session亲和路由+最低负载分配策略，可将KV
  cache前缀命中率提升至96%，大幅降低多轮对话rollout耗时

  - 用MoE大模型做生成式推荐/RLHF的团队可复用R3（Rollout Routing Replay）机制，训练阶段直接复用rollout记录的专家路由结果，避免路由数值差异导致的训练漂移甚至崩溃

  - 显存资源紧张的场景可复用训练状态离线卸出、优化器状态流式加载设计，优化器状态流加载可将训练actor卸出时间从24s降至5.2s，重载时间从8.9s降至1.3s，支撑更大模型的RL训练

  - 搭建生产级LLM训练平台的团队可参考三级权重同步传输设计，根据集群网络条件选择NCCL广播/P2P RDMA/共享存储delta同步，大集群下P2P RDMA比广播提速85%以上'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
前沿大模型后训练尤其是多轮Agent RL、万亿参数MoE模型RLHF面临三大痛点：一是rollout和训练串行导致GPU利用率低、空泡多；二是rollout和训练的token一致性、MoE路由一致性差，容易出现训练漂移甚至崩溃；三是缺乏全栈可定制、可验证的生产级系统，普通团队难以落地大规模RL训练。

### 方法关键点
- 架构拆分为rollout、训练、权重同步三个异步解耦模块，支持全异步RL模式，rollout基于SGLang实现，通过session亲和路由绑定同一会话到同一引擎
- 引入TITO（Token-In-Token-Out）会话服务，全程记录rollout阶段的精确token ID，避免多轮对话中消息解析、模板渲染导致的token不一致
- 针对MoE模型提供R3机制，训练阶段直接复用rollout记录的专家路由结果，解决路由数值差异导致的训练不稳定
- 训练层支持Megatron-LM、PyTorch FSDP双后端，覆盖全参数/ LoRA RL、监督微调、蒸馏等多种后训练范式，配套优化器状态流式加载、训练状态卸出等显存优化手段
- 权重同步支持NCCL广播、P2P RDMA、共享存储delta三种传输方式，适配不同集群网络条件

### 关键结果
在64张NVIDIA GB300 GPU上跑GLM-5.2 744B-A40B的终端编码任务Agent RL训练，单步中位数耗时263秒；大集群下P2P RDMA权重同步比NCCL广播提速85%以上；优化器状态流加载可将训练actor卸出时间从24s降至5.2s，重载时间从8.9s降至1.3s。

> 最值得记住的一句话：大模型RL后训练的核心瓶颈从来不是算法，而是全栈系统的精度、效率、可靠性和可扩展性的协同优化
