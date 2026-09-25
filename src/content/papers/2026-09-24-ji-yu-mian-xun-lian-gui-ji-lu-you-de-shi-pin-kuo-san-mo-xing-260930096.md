---
title: Accelerating Video Diffusion via Training-Free Trajectory Routing
title_zh: 基于免训练轨迹路由的视频扩散模型推理加速方法
authors:
- Mustafa Munir
- Huy Vu
- Shreyas Misra
- Rohit Jena
- Sajad Norouzi
- Ali Taghibakhshi
- Anis Ahmad
- Anjul Patney
- Pavlo Molchanov
- Nima Tajbakhsh
arxiv_id: '2609.30096'
url: https://arxiv.org/abs/2609.30096
pdf_url: https://arxiv.org/pdf/2609.30096
published: '2026-09-24'
collected: '2026-09-25'
category: Multimodal
direction: 多模态生成 · 推理加速优化
tags:
- Diffusion Model
- Inference Acceleration
- Training-Free
- Model Routing
- Video Generation
one_liner: 提出免训练TRACK路由策略，在视频扩散去噪步骤切换大小模型，实现最高2.73倍推理加速且质量相当
practical_value: '- 大小模型分步骤路由的思路可直接迁移到电商AIGC业务（如商品短视频、营销文案生成）的推理部署，无需重训即可大幅降低推理成本

  - 离线基于大小模型预测偏差生成路由阈值的校准方法，可复用在所有异构模型混合部署场景，快速平衡推理质量与latency

  - 免训练异构路由逻辑可迁移到LLM驱动的推荐Agent流程，不同推理环节（如用户意图理解、候选排序、文案生成）可切换不同参数量模型降本'
score: 7
source: arxiv-cs.AI
depth: abstract
---

### 动机
视频扩散模型推理需执行多步去噪，每步都调用大模型计算成本极高，即使经过步骤蒸馏，推理成本仍难以支撑规模化落地。
### 方法关键点
提出TRACK免训练异构去噪路由策略：1. 离线校准阶段用大模型生成参考去噪轨迹，逐步骤对比同输入下小模型与大模型的预测偏差，生成各步骤的偏差得分映射；2. 推理路由规则：高偏差的质量敏感步骤保留大模型，低偏差步骤切换为小模型；3. 推理阶段无需双模型并行、无需修改模型架构/调度器、无需重训。
### 关键结果
在Wan 2.1、Cosmos 3、TurboDiffusion、FastVideo四个主流视频扩散模型上分别实现1.95×、2.04×~2.73×、2.69×、2.17×的推理加速，生成质量与全大模型推理相当，同时保留高生成多样性。
