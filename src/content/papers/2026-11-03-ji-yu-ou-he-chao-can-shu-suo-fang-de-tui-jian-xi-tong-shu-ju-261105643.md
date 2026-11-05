---
title: Data-Efficient Scaling-Law Discovery for Recommendation Systems via Coupled
  Hyperparameter Scaling
title_zh: 基于耦合超参数缩放的推荐系统数据高效缩放定律挖掘
authors:
- John Martabano Landy
- Louis C. Tiao
- Yao Xuan
- Luc Kien Hang
- Rupinder P. Khandpur
- Arvind M. Vepa
- Srinidhi Raghavendran
- Anirudh Agrawal
- Xiaoyi Leo Liu
- Jiang Liu
affiliations:
- Meta
arxiv_id: '2611.05643'
url: https://arxiv.org/abs/2611.05643
pdf_url: https://arxiv.org/pdf/2611.05643
published: '2026-11-03'
collected: '2026-11-05'
category: RecSys
direction: 推荐系统缩放 · 异构模型算力分配
tags:
- scaling-laws
- recommendation-system
- ads-ranking
- bayesian-optimization
- pareto-optimization
one_liner: 提出低开销自动缩放框架Axia，高效挖掘异构推荐模型的算力-性能权衡帕累托前沿
practical_value: '- 架构参数分组技巧：将推荐模型耦合的原生参数按语义分组为embedding维度、交互深度、交互宽度3个超超参数，大幅降低架构搜索空间维度，避免单独调参出现的性能瓶颈

  - 低开销调参流程：先做算力profiling筛选可行配置，再用带缩放先验的贝叶斯优化自适应选实验，仅需20次左右训练就能找到当前算力约束下的最优模型配置，大幅降低调优成本

  - 全fleet评估方法：用基于业务流量占比加权的舰队效用指标评估跨异构模型的优化收益，避免单场景实验结果无法泛化到全量生产集群的问题'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前大厂推荐/广告排序模型数量多、异构性强，手动逐个调参分配算力要消耗数天到数周的时间，现有LLM的单维度缩放定律无法直接适配推荐模型多架构维度耦合的特性，急需低开销的自动缩放方法最大化全集群的投入产出比。

### 方法关键点
- 设计Scaling Layer：将推荐模型原生架构参数按语义分组为3个独立可控的超超参数（交互深度、交互宽度、embedding维度），从低维空间映射到完整合法的模型配置，避免参数缩放失衡
- 开发Axia自适应搜索框架：先完成64组配置的算力profiling筛选可行范围，通过16组初始化训练+4组自适应实验，结合带缩放先验的高斯过程surrogate、约束期望提升（EI）/超体积提升（EHVI）采集函数，自动输出算力-性能帕累托前沿
- 配套集群级评估协议：基于各模型的业务流量占比加权计算舰队效用，统一度量跨异构模型的优化收益，保障实验结论可落地

### 关键结果
在Meta广告排序、检索集群的34个生产模型迭代上测试，对比手动调参基线，平均离线Normalized Entropy提升0.66%，累计在线业务指标提升0.36%；单模型实验下，仅用20次训练就比随机搜索、通用贝叶斯优化分别带来0.07%、0.059%的NE提升。

最值得记住的一句话：推荐模型的算力分配不需要手动逐个调参，通过参数语义分组+自适应搜索，仅需少量实验就能找到最优配置，可系统性提升全生产集群的投入产出比。
