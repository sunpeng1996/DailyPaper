---
title: 'Kairos: Numerically Robust News Recommendation under Item Cold-Start via Cholesky-based
  LinUCB'
title_zh: Kairos：基于Cholesky改进LinUCB的冷启动鲁棒新闻推荐系统
authors:
- Finn Hertsch
affiliations:
- DHBW Ravensburg
arxiv_id: '2607.26832'
url: https://arxiv.org/abs/2607.26832
pdf_url: https://arxiv.org/pdf/2607.26832
published: '2026-07-29'
collected: '2026-07-30'
category: RecSys
direction: 冷启动推荐 · 数值鲁棒在线学习
tags:
- LinUCB
- Matryoshka Representation Learning
- Cold-Start Recommendation
- Numerical Stability
- Contextual Bandits
one_liner: 用Cholesky因子更新结合MRL实现冷启动场景下高效鲁棒的LinUCB新闻推荐
practical_value: '- 做LinUCB类在线学习场景时，用Cholesky因子rank-1更新替代传统Sherman-Morrison矩阵逆，避免数值不稳定导致的模型崩溃，尤其适合交互稀疏、数据噪点多的冷启动业务场景，比如新品推荐、新内容push

  - 召回和排序分阶用不同维度的Matryoshka嵌入：召回阶段用低维子空间（比如128d）做MIPS大幅降本提速，排序阶段用全维嵌入保证精度，实测几乎无效果损失的前提下能拿到接近5倍的推理效率提升，适合算力紧张的实时推荐场景

  - 冷启动内容/物品推荐场景下，可复用上下文老虎机的探索机制，对新鲜内容基于特征空间的置信度加权探索，既能缓解热门bias，也能在短TTL内容的生命周期内快速完成价值验证'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
新闻、电商新品等短生命周期内容/物品的推荐天然面临严重的物品冷启动问题，传统协同过滤类方法需要积累足够交互数据才能建模，往往耗时超过内容本身的有效生命周期（新闻TTL通常<48h），还会催生热门偏差；而传统LinUCB类在线学习方案依赖的Sherman-Morrison矩阵逆更新存在数值不稳定问题，长期运行易因浮点误差累积导致矩阵失去正定性，模型崩溃，同时高维特征下推理延迟高，难以适配实时业务需求。

### 方法关键点
- 改进LinUCB数值稳定性：放弃Sherman-Morrison逆更新，直接对协方差矩阵的Cholesky下三角因子做rank-1更新，天然保证矩阵的对称正定性，避免浮点误差累积，无需人工重启模型
- 嵌入层集成Matryoshka Representation Learning(MRL)，训练可嵌套截断的多粒度嵌入，支持不同业务阶段按需选择嵌入维度，平衡精度与效率
- 架构分阶设计：召回阶段用128d低维MRL嵌入做MIPS候选生成，重排序阶段用Cholesky更新的LinUCB做个性化排序，同时结合折扣因子实现历史交互的时序衰减，适配短生命周期内容的特性

### 关键实验
基于Tagesschau API的385篇48h窗口内的区域新闻小 corpus 验证，对比传统LinUCB方案：128d MRL嵌入召回保留95%以上语义方差，嵌入对相似度的MAE仅0.036，精度几乎无损失；推理速度提升4.85倍，单100篇文章的推理延迟从0.337ms降到0.069ms，算力节省79%；1000次蒙特卡洛模拟下，传统Sherman-Morrison更新的条件数发散方差持续扩大，而Cholesky更新的误差方差几乎为0，数值稳定性提升显著。

### 核心结论
短生命周期冷启动推荐的核心矛盾不是数据少，而是在线学习的数值鲁棒性和效率没有被足够重视，用结构化的数学优化而非暴力加数据加模型，往往能拿到更适配业务特性的收益
