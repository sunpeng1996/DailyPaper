---
title: 'Heterogeneous Ranking in Industrial-Scale Recommender Systems: A Case Study'
title_zh: 工业级推荐系统异构排序落地：Google Discover实践案例
authors:
- Di Bai
- Jintao Liu
- Zhenwei Tang
- Peifan Wu
- Nada Al-Thawr
- Luoshu Wang
affiliations:
- Google LLC
arxiv_id: '2607.27577'
url: https://arxiv.org/abs/2607.27577
pdf_url: https://arxiv.org/pdf/2607.27577
published: '2026-07-30'
collected: '2026-07-31'
category: RecSys
direction: 推荐系统 · 多内容异构统一排序
tags:
- Ranking
- Multi-Task Learning
- MoE
- Heterogeneous Recommendation
- Industrial Deployment
one_liner: 提出异构自适应HA-MoE架构、LENS观测框架与DL-AUC指标，落地Google Discover获全链路业务收益
practical_value: '- 异构内容统一排序场景可直接复用HA-MoE设计：将内容类型、业务属性等异构信号注入MoE的门控网络与专家层最后一层做线性调制，仅增加<5%参数量、<0.5%延迟即可解决负迁移与少数内容坍缩问题

  - 多内容排序评估可落地DL-AUC指标：加权融合全局Micro-AUC与跨内容类型Macro-xAUC，避免全局指标掩盖多数内容压制少数内容的问题，可通过权重参数灵活平衡业务收益与生态健康

  - 工业级MoE模型可采用LENS框架做可观测：通过激活切片可视化专家分工、PIEM得分监控训练过程中专家功能稳定性，提前定位模型坍缩问题，无需等全量离线评估完成'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有统一排序模型在异构内容（图文、长/短视频、UGC、特殊功能卡片等）场景下存在三大痛点：全局优化偏向高流量内容导致少数优质内容被压制、多任务优化出现负迁移、共享表征无法适配不同内容的交互模式差异，Google Discover作为聚合开放Web异构内容的feed产品，亟需在不增加过多运维成本的前提下解决上述问题。

### 方法关键点
1. **HA-MoE架构**：将显式异构信号（内容类型、创作者属性、可购物属性等）同时注入MoE的门控网络与专家层，门控网络基于异构信号动态分配专家权重，专家层最后一层通过HDLM线性调制适配不同内容的表征需求
2. **LENS可观测框架**：通过激活切片可视化不同内容、不同任务的专家分工，提出PIEM无标签指标监控连续训练过程中专家功能的稳定性，提前识别表征坍缩
3. **DL-AUC评估指标**：加权融合全局Micro-AUC与跨内容类型Macro-xAUC，同时衡量全局排序效果与跨内容类型的排序公平性

### 关键实验
离线基于Google Discover 1000万条7天交互数据，对比共享MLP、标准MMoE基线，HA-MoE的pInterest DL-AUC从0.679提升至0.691，pDisinterest DL-AUC从0.939提升至0.949，图文与视频的跨类型排序gap从0.141缩小至0.060；线上A/B测试获DAU+0.22%、内容多样性+0.36%、互动多样性+0.54%的收益，仅增加<5%参数量、<0.5%推理延迟。

### 核心结论
工业级异构排序的核心是在不突破资源约束的前提下，通过显式建模异构信号实现专业分工与全局优化的平衡，而非无限制增加模型参数。
