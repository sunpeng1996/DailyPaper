---
title: 'Asuka-FM: A System-Architectural Co-Design Framework for Efficient Text-to-Image
  Pretraining on Consumer Hardware'
title_zh: Asuka-FM：消费级硬件上高效文生图预训练的系统架构协同设计框架
authors:
- Víctor Rodrigo González
- Pablo M. Olmos
- Ignacio Peis
- Alejandro Lancho
affiliations:
- Universidad Carlos III de Madrid
- Technical University of Denmark
- Universidad de Granada
arxiv_id: '2611.26437'
url: https://arxiv.org/abs/2611.26437
pdf_url: https://arxiv.org/pdf/2611.26437
published: '2026-11-19'
collected: '2026-11-21'
category: Training
direction: 文生图预训练 · 低算力硬件效率优化
tags:
- Text-to-Image
- Diffusion Transformer
- Efficient Pretraining
- Consumer GPU
- RoPE
- Sparsification
one_liner: 提出系统架构协同优化方案，单张RTX4090即可低成本从头预训练效果达标的文生图DiT模型
practical_value: '- 电商商品图生成小团队可直接复用该框架，无需大集群即可在消费级GPU上预训练垂类文生图模型，算力成本可降低90%以上

  - SPRINT结构化序列稀疏化、无AdaLN双流DiT架构可迁移到垂类文生图微调场景，降50%以上注意力FLOPs，同时减少显存占用

  - 连续长宽比归一化RoPE+偏移方形裁剪方案，可解决电商多尺寸商品图训练的JIT编译中断问题，提升训练吞吐'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
当前前沿文生图基础模型依赖数十亿参数DiT与超大规模计算集群预训练，中小团队准入门槛极高；单张24G RTX4090从头训DiT存在三大瓶颈：二次复杂度注意力成本、可变长宽比分桶导致JIT编译中断、冻结VAE运算占比过高拖慢单步延迟。
### 方法关键点
1. 采用无AdaLN的双流DiT backbone减少参数量；2. 引入SPRINT结构化序列稀疏化，降低注意力FLOPs超50%；3. 提出连续长宽比归一化RoPE+偏移方形裁剪训练，保证静态张量形状同时支持零样本虚拟相机控制；4. 新增10M参数Patch Detailer Head做像素适配，采用v-prediction训练。
### 关键结果
206M参数模型单张RTX4090预训练仅需~160GPU小时，总成本低于55美元；256px分辨率下GenEval 0.588/DPG 78.96，512px下GenEval 0.609/DPG 78.51，达到效率帕累托最优。
