---
title: 'LynnReal-Omni: Native multi-modal Video Generation for Agentic Visual Workflows'
title_zh: LynnReal-Omni：面向智能体视觉工作流的原生多模态视频生成
authors:
- Xiaofeng Mao
- Peijia Lin
- Shaohao Rui
- Yibo Zhang
- Haibin Wan
- Weijie Ma
affiliations:
- LynnReal AI
arxiv_id: '2609.15863'
url: https://arxiv.org/abs/2609.15863
pdf_url: https://arxiv.org/pdf/2609.15863
published: '2026-09-13'
collected: '2026-09-15'
category: Agent
direction: Agent 多模态可控视频生成框架
tags:
- Multi-modal Generation
- Diffusion Transformer
- Video Generation
- Agent Workflow
- Real-time Inference
one_liner: 提出适配Agent视觉工作流的统一多模态视频生成框架，兼顾可控性、质量与推理效率
practical_value: '- 电商商品短视频生产场景可复用该框架的参考引导+结构控制能力，输入商品图+3D渲染素材生成可控种草短视频，降低素材制作成本

  - 实时互动Agent场景（虚拟导购、直播数字人）可直接复用Flash版本的轻量VAE+加速方案，单H100即可实现亚秒级视频生成，满足实时交互要求

  - 多模态内容评估可借鉴MSAVP评估体系，从指令遵循、视觉质量、时序一致性等多维度衡量生成内容效果，适配业务内容质检需求'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有视频扩散模型随机性强、可控性差，长时序场景易出现内容漂移，而Agent视觉生成方案虽可控但对象保真度不足，二者融合是实现稳定高质量视频生成的核心路径。
### 方法关键点
1. 基于32B共享多模态Diffusion Transformer构建统一框架，覆盖文生视频、图像条件生成、参考引导、结构控制、视频修复、长视频生成等多任务，兼容3D渲染、游戏录屏等异质输入，支持Agent自定义组合视觉条件；
2. 推出27B参数Flash版本，搭配轻量VAE解码器实现推理加速；
3. 搭建系统化数据清洗、多模态标注pipeline，提出覆盖100条prompt、20项指标的MSAVP评估体系，多维度衡量生成效果。
### 关键结果
单H100上生成22帧540p视频，标准版耗时843ms，Flash版本仅需377ms，可支撑实时流视频生成需求。
