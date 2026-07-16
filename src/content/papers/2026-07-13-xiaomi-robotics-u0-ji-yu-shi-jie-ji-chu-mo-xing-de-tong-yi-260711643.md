---
title: 'Xiaomi-Robotics-U0: Unified Embodied Synthesis with World Foundation Model'
title_zh: Xiaomi-Robotics-U0：基于世界基础模型的统一具身合成系统
authors:
- Xinghang Li
- Jun Guo
- Qiwei Li
- Long Qian
- Hang Lai
- Yueze Wang
- Hongyu Yan
- Jiahang Cao
- Xi Chen
- Jingen Qu
affiliations:
- Xiaomi Robotics
arxiv_id: '2607.11643'
url: https://arxiv.org/abs/2607.11643
pdf_url: https://arxiv.org/pdf/2607.11643
published: '2026-07-13'
collected: '2026-07-16'
category: Agent
direction: 具身Agent · 统一多模态生成框架
tags:
- Multimodal
- Embodied AI
- Autoregressive Model
- Foundation Model
- Generative AI
one_liner: 推出380亿参数多模态自回归模型，实现跨多机器人的统一高质量具身生成
practical_value: '- 预训练基础模型适配下游场景时可采用「通用原有任务+下游专有任务联合优化」范式，避免预训练知识遗忘，可直接复用在LLM4Rec的模型微调流程中，同时保留通用语义理解能力和推荐场景任务效果

  - 统一多任务生成框架的设计思路可复用在多模态生成式推荐中，同时支撑商品文案生成、商品图编辑、场景化导购内容生成等多类业务需求

  - 跨实体一致性保持的优化方法可迁移到电商多模态内容生成场景，解决同款商品多视图、多场景展示的风格/属性一致性问题'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有图像视频生成基础模型直接应用于具身场景时，受限于多视角一致性、几何连贯性、机器人具身约束要求；现有适配方法依赖少量机器人数据微调，易损失大规模预训练获得的通用视觉知识。
### 方法关键点
构造380亿参数多模态自回归模型Xiaomi-Robotics-U0，将具身生成作为图像视频基础生成能力的延伸，联合优化文生图、图像编辑、具身场景生成、具身迁移、具身视频生成5类任务，既保留预训练世界基础模型的泛化性，又适配具身场景约束；支持跨多机器人的高质量多视角场景生成，引入结构化可控具身迁移实现细粒度编辑，同时保持多视角一致性和交互动态。
### 关键结果
在单步和序列生成任务上达到SOTA，具身场景生成与迁移的人类评估优于GPT-Image-2.0，具身视频生成在World Arena排名第一，现实世界操纵任务的分布外成功率从36.9%提升至63.2%。
