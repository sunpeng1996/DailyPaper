---
title: 'Hy-Embodied-VLM-1.0: Efficient Physical-World Agents'
title_zh: Hy-Embodied-VLM-1.0：高效物理世界具身智能体
authors:
- Ziyi Wang
- Xumin Yu
- Yongming Rao
- Yonggen Ling
- Yunheng Li
- Oran Wang
- Mingqi Gao
- Yuchen Zhou
- Yves Liang
- Zuyan Liu
arxiv_id: '2607.12894'
url: https://arxiv.org/abs/2607.12894
pdf_url: https://arxiv.org/pdf/2607.12894
published: '2026-07-14'
collected: '2026-07-15'
category: Agent
direction: 具身智能体 · VLM基座优化
tags:
- Embodied Agent
- VLM
- MoE
- Multi-turn Interaction
- Long-horizon Reasoning
one_liner: 基于动作中心能力分层构建高效具身VLM基座，3B激活参数量接近上代32B模型性能
practical_value: '- 线下电商场景（门店导购Agent、仓储拣货Agent、AR试穿交互）可直接复用其动作中心能力分层框架，拆解感知-推理-交互全链路任务模块，降低定制开发成本

  - 低延迟要求的端侧Agent（线下广告互动屏、移动端AR导购）可借鉴其MoE架构设计思路，用小激活参数量实现接近大模型的性能，兼顾效果与部署成本

  - 面向长周期用户交互任务（如全链路线下逛店导购、家装设计Agent）可复用其预训练+后训练的系统化数据pipeline，快速构建领域适配的微调数据集'
score: 8
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有具身Agent基座普遍能力偏科，仅侧重多模态感知，缺乏适配物理世界交互的动作导向推理能力，同时难以在保证性能的前提下满足低延迟部署要求。
### 方法关键点
1. 定义动作中心能力分层框架，覆盖动作相关状态理解、动作转移推理、序列自适应推理三个递进维度，从预训练阶段植入具身能力
2. 基于框架搭建系统化数据pipeline，构建覆盖预训练、后训练全阶段的混合数据集
3. 采用Hy3-A3B语言基座+Hy-ViT2视觉编码器架构，搭配高效MoE设计平衡模型容量与推理效率
### 关键结果
- 在38项覆盖具身感知、物理世界理解、具身推理的基准测试中，19项取得同体量模型最优性能，大幅优于Qwen3.6-A3B、Cosmos 3等竞品
- 平均性能较上代Hy-Embodied-0.5 MoT-2B提升8.4%，仅激活3B参数量即可接近上代32B激活参数量模型的性能
- 在需多轮交互、长周期推理的具身任务上表现优异
