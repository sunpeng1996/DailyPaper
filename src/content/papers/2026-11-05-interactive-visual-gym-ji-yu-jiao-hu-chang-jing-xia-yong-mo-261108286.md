---
title: 'Interactive Visual Gym: Evaluating Visual Interaction Models with Simulated
  Users in Interactive Worlds'
title_zh: Interactive Visual Gym：基于交互场景下用模拟用户评估视觉交互模型
authors:
- Chenhao Zheng
- Zixian Ma
- Kai Li
- Kanchana Ranasinghe
- Jieyu Zhang
- Artemis Panagopoulou
- Weikai Huang
- Jianxu Shangguan
- Yuanyuan Tan
- Silvio Savarese
affiliations:
- University of Washington
- Salesforce AI Research
arxiv_id: '2611.08286'
url: https://arxiv.org/abs/2611.08286
pdf_url: https://arxiv.org/pdf/2611.08286
published: '2026-11-05'
collected: '2026-11-06'
category: Eval
direction: 多模态交互模型 · 闭环评估基准
tags:
- VLM
- Evaluation Benchmark
- Simulated User
- Closed-loop Training
- Multimodal Agent
one_liner: 提出视觉交互模型闭环评估训练框架，含3类任务模拟器和315个场景的IVG-Bench基准
practical_value: '- 交互型电商导购、操作指引类Agent评估可复用「模拟用户+可执行环境」的闭环范式，替代离线回放，更贴近真实交互场景下的效果度量

  - 多模态交互Agent训练可参考GRPO闭环训练方法，基于环境反馈优化任务成功率与交互体验，小参数模型即可获得明显收益

  - 构建场景化用户模拟可引入persona条件、可控执行误差、非计划行为的设计思路，提升模拟用户的真实度，适配电商个性化导购等场景'
score: 7
source: arxiv-cs.CV
depth: abstract
---

### 动机
视觉交互模型需在闭环场景下评估才能捕捉响应对后续用户行为、任务结果的影响，现有基准依赖离线回放，无法还原真实交互的动态效应。
### 方法关键点
提出Interactive Visual Gym框架，联合仿真可执行任务环境与人类用户，覆盖烹饪、家居操作、移动界面3类日常任务，提供人类对齐的动作空间；配套persona条件化的用户模拟模块，支持注入可控执行误差、非计划行为，还原真实用户特性；落地为包含315个交互场景的IVG-Bench基准，同时支持模型评估与训练。
### 关键结果
SOTA VLM Gemini 4 Argon限时任务完成率仅53.4%，事实grounding、可执行指导能力存在明显短板，响应延迟过高易错过用户操作纠错窗口；评估指标与人类偏好一致性达78.5%；基于GRPO的闭环训练可显著提升Qwen3.5-4B在烹饪场景的任务成功率与交互质量。
