---
title: 'SituRecBench: Evaluating Frontier Models as Situated Recommendation Assistants
  in 3D Environments'
title_zh: SituRecBench：3D环境下具身推荐助手的前沿模型评测基准
authors:
- Jingtong Yang
- Dongding Lin
- Jian Wang
- Wenjie Li
affiliations:
- The Hong Kong Polytechnic University
- Sichuan University
arxiv_id: '2611.10349'
url: https://arxiv.org/abs/2611.10349
pdf_url: https://arxiv.org/pdf/2611.10349
published: '2026-11-07'
collected: '2026-11-10'
category: Agent
direction: 具身推荐 · 多模态Agent评测
tags:
- Situated Recommendation
- VLM
- 3D Environment
- Benchmark
- User Simulation
- Embodied Agent
one_liner: 首个支持3D购物场景下具身推荐助手多维度交互评测的基准
practical_value: '- 线下零售/AR导购类Agent研发可直接复用其3D场景构建+用户模拟+多维度评测的框架，无需从零搭建测试环境

  - 具身推荐的动作空间设计可直接迁移，将对话、推荐、导航、交互四类动作解耦，适配AR导购、线下智慧门店等场景

  - LLM用户模拟的设计方法可复用在对话推荐离线评测环节，用带profile+购物目标的模拟用户替代大量真人测试，降本提效

  - 多维度评测指标（任务成功率、对话质量、推荐效用、导航效果）可套用到交互式推荐系统评估，补足现有仅看点击/转化指标的不足'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有推荐系统正从静态检索引擎转向物理环境下的交互式助手，但现有基准无法同时覆盖空间导航、visual grounding、多轮交互三个核心维度的联合评测，无法支撑线下零售、AR导购等场景下具身推荐助手的研发。

### 方法关键点
- 基于UE5构建超市、家居店两个高保真3D购物场景，标注455个商品的属性、位置等元数据，支持60个导航目标点
- 设计带用户profile、购物目标、行为特征的VLM驱动用户模拟器，支持自然语言交互+行走、取货等物理动作
- 提出统一交互式评测协议，从任务结果、对话质量、推荐效用、导航效果四个维度综合评估助手表现
- 引入Set-of-Mark (SoM)视觉标注方案，模型无需预测坐标即可直接指定交互目标，降低VLM接入门槛

### 关键实验结果
测试7款前沿VLM在200个任务上的表现：最优模型Gemini 3.1 Pro在超市场景成功率80%、R@5 64.4%，在家居场景成功率66%、R@5 49.8%；小模型Qwen3-VL-8B超市成功率仅34%，比最优模型低46个百分点；真人评测与模拟用户评测的成功率相关系数达0.8，证明模拟评测可有效替代真人测试做相对效果排序。

### 核心结论
当前前沿VLM在具身推荐场景下仍存在空间grounding差、偏好elicitation不足、全局上下文与局部观察融合能力弱的问题，是后续优化的核心方向。
