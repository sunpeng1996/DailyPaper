---
title: 'Mosaic: A Fleet of User Embedding Specialists for Recommendation at Meta'
title_zh: Mosaic：Meta面向推荐场景的专业化用户嵌入集群框架
authors:
- John Zhiyuan Zheng
- Xian Sun
- Xiangyang Mou
- Yujunrong Ma
- Christina You
- Michael Jiayuan He
- Hrishikesh Paranjape
- Aakarsha Agarwal
- Hong Li
affiliations:
- Meta
arxiv_id: '2607.24015'
url: https://arxiv.org/abs/2607.24015
pdf_url: https://arxiv.org/pdf/2607.24015
published: '2026-07-27'
collected: '2026-07-28'
category: RecSys
direction: 工业级推荐 · 大规模用户表征学习
tags:
- User Embedding
- Multi-Specialist
- Large-scale Recommendation
- Hybrid Serving
- Evaluation Efficiency
one_liner: 基于四类异构用户嵌入专家集群，搭配降冗余、快评估、混合部署方案提升全链路推荐效果
practical_value: '- 架构层面可复用多专家设计：按信号类型拆分记忆型、稠密特征型、序列型、下游对齐型4类独立用户塔，避免单模型容量竞争，开发迭代更灵活，故障隔离性更强

  - 降冗余trick可直接复用：新增用户嵌入时引入Cosine Redundancy Loss约束与已有嵌入正交，配合Multi-task Relation Mining构造复合标签，缓解边际收益递减问题

  - 工程优化可落地：混合CPU/GPU、在线/离线部署策略适配不同专家的延迟、新鲜度需求，AOT编译+模型拆分+缓存的组合可降低79%GPU服务占用

  - 评估效率提升：采用CoEval免日志评估框架，直接用冻结用户塔接入下游排名模型评估，迭代速度提升3-5倍，避免长周期线上埋点验证'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
工业推荐系统中用户表征优化是高杠杆点，单模型/共享骨干的传统方案无法同时覆盖稀疏ID、稠密统计、行为序列等异构用户信号的建模需求；新增嵌入时信息冗余导致边际收益递减，且嵌入评估依赖长周期线上埋点，大规模部署时难以平衡新鲜度、延迟和算力成本。
### 方法关键点
- 多专家异构架构：拆分4类独立用户塔，记忆型用超大哈希表捕获细粒度偏好，稠密型建模统计特征非线性交叉，序列型基于HSTU+MoE建模时序动态，CoTrain专家引入下游梯度对齐任务目标
- 降冗余机制：MRM挖掘任务关联构造复合监督标签，CRL余弦冗余损失约束新嵌入与已有嵌入正交，最大化增量信息
- 混合部署栈：支持CPU在线、GPU在线、GPU离线三类路径，搭配AOT编译、模型拆分、缓存优化降低算力成本
- 免日志评估：CoEval直接将冻结用户塔接入下游模型评估，User Tower Zero-Out量化边际贡献，迭代效率提升3-5倍
### 关键结果
在Meta 6个下游推荐场景测试，离线NE最高下降0.33%，在线A/B测试核心指标最高提升0.28%；四类专家中稠密型贡献最大，EvalΔNE达-0.22%，所有Mosaic嵌入在下游20k+输入特征中排名稳定进入前2%。
> 核心结论：异构专业化用户嵌入集群在相同算力下的表现优于单一通用大模型，是工业级用户表征规模化落地的可行路径
