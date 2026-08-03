---
title: 'GALA: Generative Aligned Learning for Adaptive Multimodal Representation in
  the Taobao Shangou Recommender System'
title_zh: GALA：淘宝闪购推荐系统自适应多模态表征的生成式对齐学习
authors:
- Jiping Liu
- Zhongmin Zhang
- Zisen Sang
- Zhijia Fang
- Tao Ouyang
- Ma Jiang
- Shaopeng Liang
- Zeyang Hou
- Guodong Cao
- Jia Jia
affiliations:
- Rajax Network Technology (Alibaba Taobao Shangou)
- Central South University
arxiv_id: '2607.29213'
url: https://arxiv.org/abs/2607.29213
pdf_url: https://arxiv.org/pdf/2607.29213
published: '2026-07-31'
collected: '2026-08-03'
category: RecSys
direction: 多模态推荐 · 表征对齐与自适应融合
tags:
- Multimodal-RecSys
- Representation-Alignment
- GRPO
- Adaptive-Fusion
- Industrial-Deployment
one_liner: 提出三阶段生成式对齐多模态推荐框架，已落地淘宝闪购，实现订单量提升0.55%
practical_value: '- 多模态预训练阶段可挖掘搜索转下单的query-图文三元组做对比学习，引入用户行为信号替代纯通用图文预训练，既适配领域术语又降低语义gap

  - 新增GRPO驱动的RL对齐中间层，用下单转化为奖励优化多模态emb，无需端到端训大编码器，即可对齐下游业务目标，且不增加线上推理开销

  - ID占优的工业排序场景可加ID驱动的自适应门控+多模态分支辅助损失，避免门控塌陷，能根据商品热度动态分配ID/多模态权重，对长尾/冷启商品增益更明显

  - 离线训好的多模态emb存在KV缓存线上直接查，完全兼容现有工业推荐「离线emb计算+线上KV lookup」范式，改造成本极低'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
外卖场景用户决策高度依赖商铺图文等多模态信号，但现有方案存在三大痛点：通用图文预训练不理解领域专属术语（如菜品俚语），预训练静态表征与下游动态行为目标对齐差，ID主导的排序模型易压制多模态信号，长尾/冷启商铺效果差；端到端多模态训练延迟高，不符合工业毫秒级服务要求。
### 方法关键点
- 领域自适应跨模态对齐：挖掘搜索转下单的query-图文三元组，用MoCo负采样做三重对比学习（query-图、query-文、query-融合表征），生成128维低维领域适配多模态emb
- 生成式行为对齐：新增中间RL层，基于用户行为序列做下一商铺预测任务，先SFT暖启动，再用GRPO以转化为奖励微调多模态emb，对齐业务目标后emb冻结
- 自适应融合：设计ID驱动的动态门控，根据ID表征置信度动态分配ID/多模态权重，加多模态分支辅助损失避免ID主导导致的门控塌陷
### 关键结果
基于淘宝闪购全量业务数据验证：阶段1用8M图文对+14M三元组，阶段2用900M行为序列，阶段3用42B排序样本。对比SOTA多模态基准与排序基准，离线CTR AUC+0.12%、CVR AUC+0.20%，PCOC更接近理想值1；线上A/B测订单量提升0.55%，已服务2亿+日活用户。
> 最值得记住：工业多模态推荐无需盲目上端到端训练，在现有离线emb+线上KV lookup范式下新增中间RL对齐层+自适应融合，即可用极低线上改造成本拿到明确业务增益
