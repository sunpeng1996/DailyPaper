---
title: 'ACLArena: Agent Continue Learning in Multi-stage Post-training'
title_zh: ACLArena：多阶段后训练场景下的智能体持续学习研究框架
authors:
- Haixin Wang
- Xiaoxuan Wang
- Junkai Zhang
- Han Zhang
- Renliang Sun
- Alexander K Taylor
- Yidan Shi
- Haoran Deng
- Chenguang Wang
- Jason Cong
affiliations:
- University of California, Los Angeles
- University of California, Santa Cruz
arxiv_id: '2609.23989'
url: https://arxiv.org/abs/2609.23989
pdf_url: https://arxiv.org/pdf/2609.23989
published: '2026-09-20'
collected: '2026-09-23'
category: Agent
direction: Agent 多阶段后训练持续学习
tags:
- Continual Learning
- LoRA
- Post-training
- Distillation
- Model Merging
- Agent
one_liner: 提出ACLArena框架分析Agent多阶段后训练遗忘机制，基于LoRA专家的方案大幅降低跨能力干扰
practical_value: '- 电商/广告Agent多能力集成可复用SDFT+多LoRA专家架构：用SFT统一训练通用能力，不同领域（搜索/导购/客服）能力用独立LoRA做RL微调，仅新增少量参数即可避免训练时的能力遗忘

  - 多阶段训练后恢复遗忘能力优先选MMOPD范式：针对高熵决策token（如工具调用、query改写节点）加入正向KL约束，比纯SFT更稳定，可在保留新习得能力的同时恢复90%以上的旧领域表现

  - 多任务蒸馏/微调必须采用跨任务均衡采样策略，避免高数据量任务梯度覆盖小领域，相比随机混洗可平均提升跨任务表现2~5个百分点'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
工业级Agent需要在多阶段后训练中依次集成推理、工具调用、指令遵循等能力，但现有持续学习方案要么依赖昂贵的环境重放，要么存在严重的跨阶段能力遗忘，且缺乏统一的测试框架和不同范式的横向对比，无成熟可复用的训练范式指导落地。

### 方法关键点
- 搭建ACLArena基准，采用Math→搜索→电商→指令遵循的四阶段训练流程，从模型层（参数位移）和token层（预测一致性）两个维度拆解遗忘机制
- 系统对比三类主流能力整合范式：多教师混合策略蒸馏（MMOPD）、自蒸馏微调（SDFT）、模型合并（MM）的优劣势与适用场景
- 提出Mixture of Low-Rank Experts（MLE）方案：先通过SDFT训练共享主干整合通用能力，再为每个阶段独立训练LoRA专家做RL微调，推理时根据环境路由对应专家，避免参数干扰

### 关键实验
基于Qwen3-8B-Base验证，对比单任务专家、顺序训练、MMOPD、SDFT、MM等基线，MLE方案在跨领域表现上全面优于基线：相比顺序训练基线，AIME26数学得分从10.21提升到21.04，搜索NQ得分从33.5提升到49.7，电商τ3-Retail得分从29.6提升到32.9，同时保留85.0的IF-Eval指令遵循能力，接近各单任务专家的水平。

**最值得记住的一句话**：SFT负责建立任务行为范式，RL负责精细化优化能力，二者互补，强行把多领域能力压缩到单一共享参数空间必然存在不可避免的权衡，参数隔离的轻量专家架构是更优的多能力整合路径
