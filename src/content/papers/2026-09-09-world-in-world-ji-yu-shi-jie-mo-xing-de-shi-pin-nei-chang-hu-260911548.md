---
title: 'World in World: Explore the World with World Models'
title_zh: 《World in World：基于世界模型的视频内场景交互式探索框架》
authors:
- Chenxi Song
- Yanming Yang
- Chi Zhang
affiliations:
- AGI Lab, Westlake University
- Westlake AGI Lab
arxiv_id: '2609.11548'
url: https://arxiv.org/abs/2609.11548
pdf_url: https://arxiv.org/pdf/2609.11548
published: '2026-09-09'
collected: '2026-09-11'
category: Multimodal
direction: 视频世界模型 · 免训练可控推理
tags:
- World_Model
- Controllable_Video_Generation
- Training_Free
- Attention_Routing
- Inference_Optimization
one_liner: 免训练推理接口让冻结自回归视频世界模型支持可控多视角生成、长程回访等多类任务
practical_value: '- 免训练适配冻结大模型的思路可直接复用：无需微调预训练大模型，仅在推理层新增控制路由即可适配多场景需求，大幅降低生成式推荐、Agent落地的训练成本

  - 多源异构信号的注意力加权融合机制可迁移：采用对应关系路由+分通道CFG加权的方案融合多模态控制信号，可直接用于多模态推荐中融合用户行为、内容属性、上下文等异构图输入

  - 长序列生成的历史状态召回机制可借鉴：生成长序列时主动召回滚动缓存外的历史状态保证时序一致性，可用于长会话推荐Agent的状态管理、生成式推荐结果的前后一致性优化'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
自回归视频世界模型可支持交互式长程场景探索，但灵活视角控制难度高，现有方案均需新增任务专属模块或额外训练，落地成本高、泛化性差。
### 方法关键点
1. 提出训练无关的推理层接口，将源视频观测、目标视角投影、几何渲染结果、缓存外历史生成状态等异构控制信号，转换为带相机与时间标签的视觉状态，通过冻结因果视频模型的原生自注意力读取
2. 设计对应关系路由，结合持久点标识与几何信息建立token级对应关系，引导查询匹配源视频token
3. 提出证据感知注意力CFG（EWA），基于同一次去噪前向传播的注意力响应，独立调节各辅助控制通道的贡献权重
### 关键结果
单冻结骨干模型即可同时支持相机可控重渲染、长程场景回访、人体动作迁移三类任务，在多视角变化场景下的感知质量、时序一致性、相机跟随精度均优于传统任务专属方案
