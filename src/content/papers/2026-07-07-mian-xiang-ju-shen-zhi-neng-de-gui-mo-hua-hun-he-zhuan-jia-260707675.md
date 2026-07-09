---
title: Scaling Mixture-of-Experts Video Pretraining for Embodied Intelligence
title_zh: 面向具身智能的规模化混合专家（MoE）视频预训练框架
authors:
- Shuailei Ma
- Jiaqi Liao
- Xinyang Wang
- Jingjing Wang
- Chaoran Feng
- Zijing Hu
- Chong Bao
- Zichen Xi
- Yuqi Gan
- Weisen Wang
affiliations:
- Robbyant Technology
arxiv_id: '2607.07675'
url: https://arxiv.org/abs/2607.07675
pdf_url: https://arxiv.org/pdf/2607.07675
published: '2026-07-07'
collected: '2026-07-09'
category: Agent
direction: 具身Agent · MoE视频基础模型预训练
tags:
- MoE
- Video Foundation Model
- Embodied Agent
- Pretraining
- DiT
one_liner: 推出首个开源大规模MoE视频基础模型LingBot-Video，适配具身场景的物理合理性与推理效率需求
practical_value: '- 垂直场景基础模型研发可复用「MoE替代稠密架构」的设计思路，平衡模型容量与推理效率，适配低延时业务（如实时内容生成、端侧Agent）需求

  - 垂直领域预训练可参考专属数据增强引擎思路，补充场景特有的样本（如电商可补充商品实拍、用户第一人称交互视频），强化模型对场景逻辑的理解

  - 模型对齐训练可引入多维度奖励体系，在通用指标外叠加业务专属指标（如电商内容生成加点击率、转化率相关指标），提升落地适配性'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有视频生成模型以内容创作为核心目标，设计上优先保障视觉保真度与创意性，忽视计算效率与物理真实性，落地具身智能场景时存在严重域不匹配问题。
### 方法关键点
1. 架构层：采用MoE替代传统稠密DiT结构，从零实现规模化训练，在保障建模容量的同时兼顾推理效率；
2. 数据层：搭建专属数据画像引擎，在通用互联网视频基础上补充大量机器人视角的操作、导航、第一人称交互 footage，让模型内置动作逻辑与世界动力学常识；
3. 训练层：设计多维度奖励对齐机制，在美学、指令跟随、运动一致性等通用指标外，额外增加物理合理性、任务完成度两个垂直场景专属对齐目标。
### 关键结果
是全球首个开源的大规模MoE视频基础模型，综合评测验证其在具身场景下的性能与效率优势，成功打通数字内容生成与物理动作执行的技术链路。
