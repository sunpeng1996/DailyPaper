---
title: 'UniWAM: Unified World-Action Model'
title_zh: UniWAM：统一世界-动作多模态模型
authors:
- Jiayi Chen
- Wenxuan Song
- Jingbo Wang
- Shuai Zhou
- Xicheng Gong
- Zehua Fan
- Ziyang Zhou
- Junwu E
- Haodong Yan
- Fuhao Li
affiliations:
- UniWAM Team
arxiv_id: '2610.02054'
url: https://arxiv.org/abs/2610.02054
pdf_url: https://arxiv.org/pdf/2610.02054
published: '2026-09-30'
collected: '2026-10-08'
category: Agent
direction: 具身Agent · 世界动作统一建模
tags:
- Embodied Agent
- Vision-Language-Action Model
- World Model
- Action Prediction
- Scaling Law
one_liner: 集成物理推理/世界生成/动作预测的统一具身模型，多任务达SOTA并发现人机共训缩放定律
practical_value: '- 多源异构数据分模块分配监督信号的预训练配方可复用，可迁移到电商多任务推荐模型训练，用用户行为、商品内容、搜索query等不同数据源分别监督对应模块，避免能力遗忘

  - 低层信号转自然语言表征的思路，可用于LLM4Rec的用户行为建模，将点击、加购、停留等低层行为转成语义描述，提升推荐系统的语义理解能力

  - 噪声增强+历史依赖生成初始化的策略，可落地到生成式推荐的商品文案生成、个性化推荐理由生成场景，在减少生成步数的同时保障输出质量'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有视觉-语言-动作模型仅靠动作监督对世界动态的grounding不足，而世界动作模型从视频生成继承时空先验，却在分布偏移下语义理解、推理能力受限。
### 方法关键点
1. 统一架构集成物理推理器、世界生成器、动作预测器，联合学习物理世界语义理解、视觉生成、动作预测任务；
2. 搭建人机第一视角数据清洗标注pipeline，将低层动作转自然语言表征，预训练阶段为VQA、人类第一视角数据、机器人演示数据分配对应模块的互补监督，保留原有语言能力的同时适配具身任务；
3. 后训练阶段引入未来视觉噪声增强、历史条件流匹配策略，降低对精准未来预测的依赖，用动作历史编码初始化动作生成。
### 关键结果
在6类仿真+真实场景评测（分布内性能、鲁棒性、泛化性、指令遵循、长周期任务执行等）上达SOTA，发现人机共训的对数线性缩放定律，验证了混合人机数据大规模预训练的有效性。
