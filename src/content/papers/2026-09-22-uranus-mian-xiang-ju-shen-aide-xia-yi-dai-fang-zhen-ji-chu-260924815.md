---
title: 'Uranus: Building the Next-Generation Simulation Infrastructure for Embodied
  AI'
title_zh: Uranus：面向具身AI的下一代仿真基础设施
authors:
- Wenkang Qin
- Yukun Zhou
- Noah Shen
- Jisong Cai
- Dongxiao Mao
- Baicheng Li
- Yue Zhang
- Wei Sui
affiliations:
- D-Robotics Large Model Team
arxiv_id: '2609.24815'
url: https://arxiv.org/abs/2609.24815
pdf_url: https://arxiv.org/pdf/2609.24815
published: '2026-09-22'
collected: '2026-09-25'
category: Agent
direction: 具身Agent · 仿真基础设施构建
tags:
- Embodied AI
- Diffusion Model
- World Model
- Simulation
- Autoregressive Generation
one_liner: 提出基于关节轨迹条件自回归扩散模型的低延迟可扩展具身AI仿真器Uranus
practical_value: '- 低延迟自回归生成的推理优化trick（24FPS实现方案）可直接复用在实时生成式推荐、直播互动文案生成等对延迟敏感的业务场景

  - 多实体统一控制接口的设计思路可迁移到跨品类电商推荐的多模态item表征对齐模块

  - 开放域无固定horizon流式生成方案可优化Agent导购的多轮实时交互响应链路'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
具身AI的数据生成、策略训练、评估与安全迭代高度依赖可扩展仿真能力，但真实世界交互成本极高，传统仿真器构建需投入大量人工劳动，缺乏通用低延迟方案。
### 方法关键点
基于关节轨迹条件的自回归扩散模型构建数据驱动仿真器Uranus，核心设计包括：1. 流式开放推演：支持在线接收未来关节位置轨迹，每步自回归生成对应4帧RGB的1个latent帧，无固定horizon限制；2. 低延迟推理优化；3. 统一控制接口：适配多形态机器人、多相机配置的同步多视图生成需求。
### 关键结果
推理优化后生成帧率达24FPS，在分布内/分布外数据上完成全面定性定量验证，已开源代码、1.3B SFT/蒸馏模型权重、SDK及demo数据集。
