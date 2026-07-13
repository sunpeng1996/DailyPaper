---
title: Native Video-Action Pretraining for Generalizable Robot Control
title_zh: 面向可泛化机器人控制的原生视频-动作预训练框架
authors:
- Qihang Zhang
- Lin Li
- Luyao Zhang
- Shuai Yang
- Yiming Luo
- Shuaiting Li
- Ruilin Wang
- Junke Wang
- Jiahao Shao
- Gangwei Xu
arxiv_id: '2607.08639'
url: https://arxiv.org/abs/2607.08639
pdf_url: https://arxiv.org/pdf/2607.08639
published: '2026-07-09'
collected: '2026-07-13'
category: Agent
direction: 具身Agent · 视频动作基础模型预训练
tags:
- Embodied AI
- MoE
- Video-Action Model
- Causal Pretraining
- Foundation Model
one_liner: 提出原生为具身场景设计的LingBot-VA 2.0，实现复杂操作任务的少样本泛化
practical_value: '- 针对垂直场景定制基础模型而非复用通用生成模型的思路，可迁移到电商多模态推荐、广告生成等垂直场景，避免通用模型适配时的性能损失

  - 稀疏MoE backbone兼顾模型容量与推理效率的设计，可复用在高吞吐的推荐/广告排序大模型落地场景，降本提效

  - 异步预计算+实时动态重对齐的推理框架，可参考优化实时推荐系统低延迟响应链路，同步处理用户实时行为与下一轮候选预计算

  - 语义对齐的多模态tokenizer设计，可借鉴到多模态召回中视觉-文本-用户行为表征的联合对齐，提升query/用户指令理解准确率'
score: 4
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有视频动作模型多复用面向数字内容生成的预训练架构，天然不适应具身物理环境的控制需求，存在指令跟随差、动作精度低、推理延迟高、泛化性弱等问题。
### 方法关键点
1. 自研语义视觉-动作tokenizer替代传统重构优先的VAE，实现视觉表征与语义、动作的双向对齐，提升策略学习的指令遵循度与动作精度
2. 采用因果预训练范式从头训练，适配时序动态的严格因果特性，规避双向架构适配时常见的灾难性遗忘问题
3. 主干采用稀疏MoE架构，在不损失推理效率的前提下扩展模型容量，满足高频推理需求
4. 优化异步推理方案，动作执行阶段并行预测未来隐变量，同时基于最新观测通过前向动力学重对齐，实现实时闭环控制
### 关键结果
真实场景部署验证，LingBot-VA 2.0在各类复杂操作任务上具备优异的少样本泛化能力
