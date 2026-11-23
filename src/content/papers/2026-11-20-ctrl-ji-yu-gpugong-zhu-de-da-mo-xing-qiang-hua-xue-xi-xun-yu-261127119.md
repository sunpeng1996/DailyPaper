---
title: 'CTRL: Concurrent Training and Rollout for LLM Reinforcement Learning via GPU
  Co-Residency'
title_zh: CTRL：基于GPU共驻的大模型强化学习训练与Rollout并行调度框架
authors:
- Ruijia Yang
- Ruikai Li
- Zeyi Wen
affiliations:
- The Hong Kong University of Science and Technology (Guangzhou)
arxiv_id: '2611.27119'
url: https://arxiv.org/abs/2611.27119
pdf_url: https://arxiv.org/pdf/2611.27119
published: '2026-11-20'
collected: '2026-11-23'
category: Training
direction: LLM RL训练 · GPU资源调度优化
tags:
- LLM
- Reinforcement Learning
- GPU Scheduling
- Training System
- Rollout
one_liner: 实现LLM RL训练与Rollout单GPU共驻执行，相比现有异步基线吞吐量最高提升2.24倍
practical_value: '- 开展生成式推荐、商品文案RL优化、智能Agent对齐的RL训练时，可复用CTRL的GPU共驻架构，无需拆分GPU池，相比现有异步训练方案提升1.1~2.24倍训练吞吐量

  - 小显存GPU（如RTX 4090）跑LLM RL微调时，可复用「优化器状态放主机+层流式滑动窗口加载」的显存优化trick，节省的显存可分配给KV cache，支持更大的rollout
  batch size

  - 推荐系统/Agent的线上模型迭代流程可借鉴publication gate调度思路：新版本训练完成后不立即切流，先等待旧版本在途请求满足陈旧度约束再发布，既不阻塞训练进度，也不会丢失样本或影响线上效果'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
LLM RL后训练（如GRPO、RLHF）包含两个硬件需求互补的阶段：Rollout解码为访存密集型，batch随响应完成动态缩小，GPU计算资源利用率低；learner训练为计算密集型，占显存高。现有方案要么时间分片串行执行两个阶段，浪费硬件资源，要么将GPU拆为独立的训练/推理池，仅支持整卡分配，资源利用率低，小显存GPU甚至无法承载完整工作流。

### 方法关键点
- 每块GPU通过CUDA MPS同时运行learner进程和常驻rollout引擎，两个阶段的内核共享GPU算力，无需切换上下文
- 优化器状态、所有策略版本均存储在主机内存，采用层流式滑动窗口将模型层逐一流入GPU执行，无需全量加载模型，大幅降低GPU显存占用
- 设计publication gate调度机制，训练完成的新版本先等待旧版本在途请求满足staleness bound再发布，不丢样本也不阻塞训练执行
- 基于step-time bound自动探测learner与rollout的最优算力分配比例，平衡两个阶段的耗时

### 关键实验
在H100、A800、RTX 4090三个硬件平台测试Qwen3系列模型的数学、代码RL训练任务，对比verl的异步时间分片、GPU拆分两种主流基线：CTRL吞吐量达到更强基线的1.11~2.24倍；相同learner配置下，比时间分片方案快1.10~1.26倍，比最优整卡拆分方案快1.10~1.30倍，训练精度与基线完全持平。

### 核心结论
Rollout与learner的硬件资源需求天然互补，单GPU共驻执行可充分利用解码阶段空闲的计算资源，资源利用率显著高于时间分片、整卡拆分两种传统方案。
