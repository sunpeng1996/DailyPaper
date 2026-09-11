---
title: Decoupled Self-Forcing Distillation for Streaming Talking Head Generation
title_zh: 面向流式说话头生成的解耦自强制蒸馏框架
authors:
- Yanru An
- Ruiyan Wang
- Wenwu Wei
- Rui Bu
- Qi Wang
- Hongwei Hu
- Zhengxue Cheng
- Rong Xie
- Li Song
- Wenjun Zhang
affiliations:
- Shanghai Jiao Tong University
- Ant Group
arxiv_id: '2609.10317'
url: https://arxiv.org/abs/2609.10317
pdf_url: https://arxiv.org/pdf/2609.10317
published: '2026-09-09'
collected: '2026-09-11'
category: Multimodal
direction: 多模态生成 · 流式数字人推理优化
tags:
- Streaming Generation
- Knowledge Distillation
- Video Diffusion
- Autoregressive Transformer
- Multimodal Fusion
one_liner: 提出解耦自强制蒸馏的双流流式说话头生成方案，兼顾高保真与低延迟推理
practical_value: '- 电商虚拟主播/直播带货场景可直接复用双流解耦架构，将运动生成与渲染分层部署，大幅降低大模型推理延迟，满足实时流式输出要求

  - 解耦蒸馏思路可迁移至多模态生成类业务（如数字人带货话术+动作联动生成），用单一冻结教师模型分别监督不同子模块，规避流式推理的曝光偏差问题

  - 低维解耦特征空间融合多模态条件的方案，可复用在语音/文本驱动的生成式内容推荐场景，在降低计算开销的同时提升生成内容的一致性'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
流式说话头生成面临保真度与效率的核心权衡：端到端音频驱动视频扩散模型质量高但参数量大、推理延迟高，无法满足实时流要求；两阶段方法先生成中间运动表示再渲染，生成质量显著落后。同时流式推理的因果约束易引发曝光偏差，没有对应双向教师模型可用于蒸馏优化。
### 方法关键点
1. 将生成流程解耦为ID无关的低维运动隐空间生成、块因果扩散渲染两个并行流，按时间粒度路由音频/文本caption条件，用小参数量因果自回归Transformer生成运动隐向量，再送入预训练扩散渲染器生成视频
2. 提出解耦自强制蒸馏机制，仅用一个冻结的预训练教师模型，分别监督渲染器的因果蒸馏、运动生成器的输出质量，解决曝光偏差问题
### 关键结果
推理速度达15.4FPS，端到端延迟仅1.3s，无生成质量下降
