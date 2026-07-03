---
title: 'Learning to Move Before Learning to Do: Task-Agnostic pretraining for VLAs'
title_zh: 先学移动再学执行：面向视觉语言动作模型的任务无关预训练
authors:
- Junhao Shi
- Siyin Wang
- Xiaopeng Yu
- Li Ji
- Jingjing Gong
- Xipeng Qiu
affiliations:
- Fudan University
- Shanghai Innovation Institute
arxiv_id: '2607.02466'
url: https://arxiv.org/abs/2607.02466
pdf_url: https://arxiv.org/pdf/2607.02466
published: '2026-07-01'
collected: '2026-07-03'
category: Agent
direction: 具身Agent · VLA预训练优化
tags:
- VLA
- Pre-training
- Embodied AI
- Self-supervised Learning
- Transfer Learning
one_liner: 提出两阶段任务无关预训练框架，大幅降低VLA模型对高成本标注演示数据的依赖并提升鲁棒性
practical_value: '- 任务拆分思路可迁移：将复杂多模态Agent任务拆分为「基础能力预训练+语义对齐微调」两阶段，比如电商导购/客服Agent可先用海量无标注交互日志预训练通用对话/操作逻辑，再用少量标注数据对齐业务规则，大幅降低标注成本

  - 自监督预训练范式复用：可借鉴Inverse Dynamics目标，用无标注离线轨迹（如用户浏览/加购行为序列、推荐系统历史交互日志）预训练通用用户/动作表征，降低下游排序、召回任务的微调数据需求

  - 鲁棒性优化思路：面向存在噪声的业务场景（如用户输入歧义、特征扰动），可通过先预训练通用基础能力再做业务微调的范式，提升模型抗干扰性能'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
当前Vision-Language-Action (VLA)模型训练高度依赖成本极高的大规模专家标注三元组（观测、指令、动作），核心痛点是传统训练范式混淆了「物理能力习得」与「语义对齐」两个独立目标，仅后者需要语言监督。
### 方法关键点
基于能力拆分假设提出两阶段Task-Agnostic Pretraining (TAP)框架：
1. 第一阶段用低成本无标注交互数据（含废弃非任务轨迹、机器人自主探索数据），通过自监督Inverse Dynamics目标学习可迁移的通用运动先验；
2. 第二阶段用极少量专家标注数据做轻量微调，将预训练得到的运动先验与语言指令对齐。
### 关键结果
- 在SIMPLER基准上，仅用远少于基线的标注数据，性能追平用1M+专家轨迹训练的模型，较标准行为克隆绝对提升10%；
- 在真实WidowX平台相机扰动场景下，互联网规模基线准确率降至0%时，TAP仍保留25%成功率
