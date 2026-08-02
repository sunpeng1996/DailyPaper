---
title: 'πR^2: Reactive Real-time Flow Policies'
title_zh: πR²：响应式实时流策略
authors:
- Sungjae Park
- Shubham Tulsiani
affiliations:
- Carnegie Mellon University
arxiv_id: '2607.26055'
url: https://arxiv.org/abs/2607.26055
pdf_url: https://arxiv.org/pdf/2607.26055
published: '2026-07-27'
collected: '2026-08-02'
category: Other
direction: 机器人基础模型 · 实时推理优化
tags:
- Real-time Inference
- Flow Matching
- Diffusion
- Robot Foundation Model
- Low Latency
one_liner: 通过快慢条件通道拆分与延迟自适应流调度，实现大模型驱动流策略的实时响应优化
practical_value: '- 快慢通道拆分思路可复用在推荐/Agent系统的特征处理链路：高新鲜度实时特征（用户实时点击、会话行为）走轻量快速通道直接输入推理层，低时效语义特征（用户长期画像、物品多模态embedding）走异步预计算慢通道更新，兼顾实时响应精度与速度

  - 延迟自适应调度可迁移至大模型驱动的生成式推荐/Agent服务：将已生成的中间结果作为inpainting条件，流量高峰/算力不足时动态减少去噪步数，单次调用单步出结果，无需全链路重跑，大幅降低推理延迟

  - 预训练模型轻量微调适配方案可复用：无需重构原有大模型架构，仅修改条件输入逻辑与推理调度流程即可适配低延迟实时场景，大幅降低落地改造成本'
score: 4
source: huggingface-daily
depth: abstract
---

### 动机
基于大预训练backbone的动作分块流策略采用开环执行，无法响应执行过程中输入的感知信息，而高频重规划受限于大模型+多步去噪的高延迟，无法适配动态闭环控制场景。
### 方法关键点
1. 拆分条件输入为快通道（本体感知数据每tick更新）和异步更新慢通道（视觉-语言特征），可在动作块内响应实时感知，同时容忍视觉特征延迟；
2. 提出延迟自适应流调度，将执行中的动作作为inpainting条件，单次调用仅需1步去噪即可输出动作，单模型可适配不同硬件延迟；仅需对现有架构做极小修改，可从预训练策略直接微调。
### 关键结果
在xArm6+XHand平台基于GR00T-N1.7测试，闭环重规划速度比基线快4倍，A5000 GPU上可达25Hz，单观测响应仅40ms；仿真任务成功率最高提升23%，真实场景最高提升30%。
