---
title: Teaching Vision-Language-Action Models to Stop Safely
title_zh: 视觉-语言-动作模型的安全停止机制研究
authors:
- Zheyuan Liu
- Chuhan Wang
- Jinduo Guo
- Yue Huang
- Xiangchi Yuan
- Ningshan Ma
- Meng Jiang
affiliations:
- University of Notre Dame
- Georgia Tech
- MIT
arxiv_id: '2611.26239'
url: https://arxiv.org/abs/2611.26239
pdf_url: https://arxiv.org/pdf/2611.26239
published: '2026-11-18'
collected: '2026-11-21'
category: Other
direction: 多模态机器人VLA安全控制
tags:
- VLA
- Safety Control
- Multimodal
- Imitation Learning
- Robot Policy
one_liner: 提出状态感知回退模仿SAFI方法，实现VLA模型执行禁止任务时的安全终止且保留原有能力
practical_value: '- 可借鉴SAFI双阶段策略，给执行类Agent（如电商客服Agent、履约调度Agent）设计中途违规操作的安全回退逻辑，避免执行错误造成资损

  - 联合适配原有任务+安全回退目标的训练范式可复用，保证Agent新增安全能力时不损失原有业务性能

  - 安全评估不能仅看任务是否终止，需额外评估终止后的次生问题（如推荐流截断后的用户体验、客服断联后的客诉），补充多维度安全评估指标'
score: 4
source: huggingface-daily
depth: abstract
---

### 动机
现有VLA模型仅能在初始状态抑制禁止任务，执行中途接管时仍可能完成违规操作，就算未完成也易出现掉落持握物品等次生安全事故，仅用任务未完成作为安全评估指标存在显著缺陷。

### 方法关键点
提出State-Aware Fallback Imitation（SAFI）双阶段框架：
1. 回退目标构建：给禁止任务的演示样本全程分配静止机械臂指令与一致的夹爪目标，明确中途终止的标准安全动作
2. 联合策略适配：在保留原有正常任务动作学习的同时，同步学习上述安全回退目标，确保不损失原有业务技能

### 关键结果
在LIBERO任务集上测试，SAFI将接管后禁止任务的整体完成率降至1.3%，无物理事故或动作饱和记录，同时保留了原有正常任务的高成功率。
