---
title: Do Recommendation Algorithms Work When Users Are LLM Agents? A Case Study on
  Moltbook
title_zh: 当用户为LLM Agent时推荐算法仍有效吗？Moltbook案例研究
authors:
- Daming Li
- Simeng Han
- Jialu Zhang
affiliations:
- Independent Researcher
- Stanford University
- University of Waterloo
arxiv_id: '2606.29762'
url: https://arxiv.org/abs/2606.29762
pdf_url: https://arxiv.org/pdf/2606.29762
published: '2026-06-29'
collected: '2026-06-30'
category: RecSys
direction: 推荐系统 · LLM Agent用户行为研究
tags:
- Recommender Systems
- LLM Agents
- User Modeling
- Collaborative Filtering
- Multi-agent Systems
one_liner: 在全LLM Agent原生社交平台Moltbook评测现有推荐算法 揭示Agent用户推荐特性
practical_value: '- 当平台存在大量LLM Agent流量/水军时，必须先做Agent用户检测与分段，排除Agent数据后再训练面向人类的推荐模型，否则Agent的无偏好行为会稀释个性化信号，降低人类用户推荐效果

  - 面向LLM Agent群体的推荐，优先选用ItemKNN、TopPopular这类依赖结构共现/popularity信号的简单方法，不需要复杂的个性化用户表征建模，效果更好且成本更低

  - 对结构类推荐方法，加入互动质量加权（类似本文的karma评分）可以大幅提升效果，该trick可直接复用在业务中'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：现有推荐算法的核心前提是用户拥有稳定、可学习的持久偏好，但随着autonomous LLM Agent越来越多入驻各类网络平台，多数Agent缺乏跨会话持久记忆与明确稳定的内容偏好，原有核心假设不再成立，亟需验证现有推荐算法在Agent用户群体下的实际表现。

**方法关键点**：
- 基于公开的Moltbook Observatory Archive数据集，这是首个全LLM Agent原生的类Reddit社交平台数据集，过滤后得到79643个活跃Agent、5406个话题板块，共177169次互动，交互矩阵密度仅0.041%；
- 系统性评测8类经典推荐算法，覆盖非个性化基线、个性化隐因子、混合内容CF、纯内容方法、item-based CF、图CF、序列推荐多个范式，额外做 ablation 验证互动质量加权、静态Agent persona描述、训练测试时间间隔的影响。

**关键结果**：
- 效果排序：ItemKNN(Recall@10=0.0236) ≈ LightGCN(0.0242) ≈ SASRec(0.0234) > TopPopular(0.0232) > 各类显式学习用户表征的方法（BPR-MF仅0.0165），显式个性化建模的效果反而不如简单结构方法；
- karma（互动赞数）加权能让TopPopular/ItemKNN/HybridMF的效果提升2.15~5.17倍，对个性化隐因子模型BPR-MF几乎无影响；
- 静态Agent persona描述（对应人类的偏好档案）对预测互动几乎无额外价值，加入模型反而会降低效果；
- 和人类用户不同，训练测试的时间间隔增大不会带来效果衰减，验证了Agent互动模式不存在偏好漂移。

**核心结论**：当用户是LLM Agent时，推荐任务从个性化偏好学习退化为结构模式匹配
