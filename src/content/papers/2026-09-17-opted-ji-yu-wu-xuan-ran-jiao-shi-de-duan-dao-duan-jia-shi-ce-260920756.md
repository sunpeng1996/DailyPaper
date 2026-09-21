---
title: 'OPTED: On-Policy Fine-Tuning for End-to-End Driving using a Render-Free Teacher'
title_zh: OPTED：基于无渲染教师的端到端驾驶同策略微调方法
authors:
- Damiano Da Col
- Maximilian Igl
- Peter Karkus
- Kashyap Chitta
- Boris Ivanovic
- Marco Pavone
- Konrad Schindler
- Christos Sakaridis
arxiv_id: '2609.20756'
url: https://arxiv.org/abs/2609.20756
pdf_url: https://arxiv.org/pdf/2609.20756
published: '2026-09-17'
collected: '2026-09-21'
category: Other
direction: 自动驾驶 · 端到端策略闭环优化
tags:
- Reinforcement-Learning
- On-Policy-Finetuning
- Teacher-Student
- End-to-End-Driving
- Autonomous-Vehicle
one_liner: 通过特权向量输入教师模型指导端到端驾驶模型闭环微调，大幅降低RL交互成本
practical_value: '- 跨模态蒸馏架构可复用：推荐场景可先用全量用户/物品特权特征训练教师模型，指导输入受限的学生模型（如仅用公开特征的召回模型）微调，降低闭环优化成本

  - 同策略微调范式参考：解决模仿学习（如排序模型的行为克隆）开环训练、闭环部署误差累积问题时，可先在抽象向量空间做RL优化，再蒸馏到下游业务模型，避免直接RL的高流量成本

  - 训练效率优化思路：当直接RL交互成本过高时，采用「特权教师RL优化→监督学生微调」两段式架构，可降低3个数量级的交互成本，适配广告/推荐场景流量贵的现状'
score: 3
source: arxiv-cs.LG
depth: abstract
---

### 动机
端到端自动驾驶策略采用开环行为克隆预训练，存在分布偏移问题，闭环部署时误差累积易引发安全事故；直接RL闭环微调依赖大量高成本仿真交互，落地难度高。
### 方法关键点
两段式OPTED框架解耦RL优化与端到端策略训练：
1. 基于HD地图、bounding box等特权向量输入训练RL教师模型，完成同策略闭环优化
2. 用无渲染教师的输出作为监督信号，指导摄像头输入的预训练学生模型做闭环微调
### 关键结果
在TransFuser、VaVAM两个相机驾驶模型上，驾驶得分分别提升1.6×、9.5×；达到同等闭环性能所需仿真交互量比直接RL微调低3个数量级，且策略更贴近人类驾驶行为。
