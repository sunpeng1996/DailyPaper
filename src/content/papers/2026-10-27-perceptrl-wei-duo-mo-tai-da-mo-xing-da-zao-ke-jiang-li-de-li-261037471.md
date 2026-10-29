---
title: 'PerceptRL: Making Visual Perception Rewardable in MLLMs from Answers to Interactions'
title_zh: PerceptRL：为多模态大模型打造可奖励的视觉感知能力
authors:
- Tongkun Guan
- Zhibo Yang
- Mingkun Yang
- Haocheng Wang
- Wei Shen
- Xiaokang Yang
affiliations:
- Shanghai Jiao Tong University
- Qwen
arxiv_id: '2610.37471'
url: https://arxiv.org/abs/2610.37471
pdf_url: https://arxiv.org/pdf/2610.37471
published: '2026-10-27'
collected: '2026-10-29'
category: Multimodal
direction: 多模态大模型 · 视觉感知RL训练
tags:
- MLLM
- Reinforcement Learning
- Visual Perception
- Agentic Tool Use
- Reward Design
one_liner: 通过双层级RL框架与可验证感知奖励设计，大幅提升MLLM的细粒度视觉感知与工具交互能力
practical_value: '- 电商多模态商品理解任务可复用「从模型自身错误构造可验证QA对」的弱监督数据生成方法，大幅降低标注成本

  - 多模态Agent调用图像裁剪、OCR等视觉工具场景，可引入Coordinate Injection修正坐标漂移，搭配空间感知过程奖励提升工具调用准确率

  - 细粒度视觉识别类推荐场景（如同款匹配、穿搭属性识别）可参考感知能力分层训练范式，优先优化高频错误域的感知效果'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
MLLM的细粒度视觉感知是下游推理效果的核心瓶颈，预训练阶段的图文caption监督会被后续指令微调、RL等阶段的目标稀释；而caption本身主观性强、信息密度高，难以设计可验证的奖励函数用于感知优化，现有推理导向的RL方法无法解决感知层面的原生错误。
### 方法关键点
- 双层级RL框架：Level1单轮Perception RL通过多Agent流水线从模型生成的caption中提取交叉验证过的感知错误，生成带固定标签的QA对（关联错误构造链式QA、无关错误构造多选择QA），用规则化结果奖励训练；Level2多轮Perception Agentic RL针对小目标、复杂场景等单轮无法解决的细粒度感知场景，支持多轮视觉工具（裁剪、缩放、标注等）交互。
- 坐标漂移解决方案：通过Coordinate Injection修正冷启动轨迹中的空间操作坐标，搭配grounding-aware过程奖励，同时监督中间操作的空间准确性和最终答案正确性。
- 三阶段训练流程：共享冷启动SFT→单轮感知RL→多轮Agent感知RL顺序训练，无额外SFT插入。
### 关键实验
基于Qwen3.6-Flash 35B MoE基座训练，在8个公开感知基准上，单轮Perception RL将平均准确率从冷启动SFT的61.9%提升至69.8%；全流程在共享工具使用协议下的7个基准上平均准确率达71.6%，较同工具基线模型提升15.7pp，较最强前沿VLM Gemini-3-Flash提升5.2pp。
### 核心结论
针对难以直接设计奖励的感知类任务，从模型自身错误出发构造可验证的监督信号，效率远高于泛化的预训练数据优化。
