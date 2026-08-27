---
title: 'Robust CurveMoE: Multi-Norm Adversarial Defense for Mixture-of-Experts Models
  via Mode Connectivity'
title_zh: Robust CurveMoE：基于模态连通性的MoE多范数对抗防御框架
authors:
- Xu Zhang
- Ren Wang
affiliations:
- Illinois Institute of Technology
arxiv_id: '2608.26043'
url: https://arxiv.org/abs/2608.26043
pdf_url: https://arxiv.org/pdf/2608.26043
published: '2026-08-26'
collected: '2026-08-27'
category: Training
direction: MoE训练 · 多范数对抗防御优化
tags:
- MoE
- Adversarial Defense
- Mode Connectivity
- Sparse Routing
- Robust Training
one_liner: 基于模态连通性曲线生成互补专家，实现高效低开销的MoE多范数对抗防御
practical_value: '- 构建多场景适配MoE时，可复用模态连通性曲线生成互补专家的思路，无需从头训练每个场景专用专家，大幅降低多场景MoE的训练成本，适配推荐系统多流量/多用户群的专家拆分需求

  - 优化MoE部署架构时，可通过梯度敏感度评估层的重要性，仅在高影响层拆分专家、其余层共享参数，在几乎不掉点的前提下降低30%以上的参数量，适配大模型推荐的线上部署资源约束

  - 大模型/MoE微调时，可采用初始化梯度分数筛选高贡献参数的方法，仅更新Top30%的高贡献参数，训练速度提升36%几乎不掉点，该思路也可迁移至LoRA微调的参数选择场景

  - 设计鲁棒MoE系统时，可加入专家候选池的跨场景效果约束，避免选到单一任务表现好但跨场景脆弱的专家，防止路由攻击或bad case扩散，适配推荐系统流量波动下的效果稳定性需求'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有多范数对抗防御普遍在单参数配置下优化多个冲突的鲁棒目标，存在精度-鲁棒性tradeoff差、训练成本高的问题；直接独立训练多个范数专用的MoE专家又会带来存储开销大、易被对抗路由攻击（引导至脆弱专家）的缺陷，亟需高效的多范数鲁棒MoE构建方案。
### 方法关键点
- 基于模态连通性构建连接ℓ1、ℓ∞鲁棒端点的二次贝塞尔曲线，曲线不同位置天然具备差异化的鲁棒性特征，直接作为专家候选池，无需独立训练每个专家
- 梯度敏感度引导选择性专家化：仅在对抗目标敏感度最高的TopK层拆分专家，其余层参数全局共享，大幅降低参数存储开销
- 贡献引导部分参数更新：用初始化阶段的梯度平方作为参数贡献度代理，仅更新Top30%的高贡献参数训练曲线，训练速度提升36%几乎不掉点，且有理论误差界保证
- 鲁棒性约束专家筛选：仅保留跨三个范数鲁棒性最差值不低于最优模型2个百分点的曲线位置作为候选专家，避免选到跨范数脆弱的专家，降低对抗路由攻击风险
### 关键结果
在CIFAR-100、ImageNet-100数据集，基于WideResNet、ViT架构对比MSD、ERMC两个SOTA基线：CIFAR-100上Union精度（同时抗三类范数攻击的准确率）提升2.37个百分点，ImageNet-100上Union精度提升2.13个百分点，同时clean精度、各范数专项精度均全面超过基线。
### 核心启示
利用模态连通性曲线生成互补专家，是兼顾效果、训练成本、部署开销的MoE构建新思路，不止适用于对抗防御，也可直接迁移至多场景适配的推荐/大模型MoE训练场景
