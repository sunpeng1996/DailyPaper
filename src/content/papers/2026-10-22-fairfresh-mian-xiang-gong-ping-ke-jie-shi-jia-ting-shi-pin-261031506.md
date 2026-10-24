---
title: 'FairFRESH: A Neuro-Symbolic Framework for Fair and Explainable Household Food
  Recommendation'
title_zh: FairFRESH：面向公平可解释家庭食品推荐的神经符号框架
authors:
- Kodur Sai Vinay Sathvik
- Kakoli Bora
- Tejaswini R. M
affiliations:
- Department of Artificial Intelligence and Machine Learning, BNM Institute of Technology
arxiv_id: '2610.31506'
url: https://arxiv.org/abs/2610.31506
pdf_url: https://arxiv.org/pdf/2610.31506
published: '2026-10-22'
collected: '2026-10-24'
category: RecSys
direction: 多用户公平推荐 · 神经符号推理
tags:
- FairRecommendation
- NeuroSymbolic
- MultiUserRec
- ExplainableAI
- ConstrainedAllocation
one_liner: 提出神经符号框架FairFRESH解决家庭多成员食品推荐的资源冲突、合规与公平性问题
practical_value: '- 家庭共享账号类电商/内容推荐场景，可直接复用「将推荐转化为带约束公平分配问题」的思路，引入Nash welfare等福利目标，可降低群体效用基尼系数42%同时不跌甚至略升召回

  - 强规则约束类推荐场景（如过敏禁忌、商品限购、合规要求），无需将规则融入模型微调，可后置确定性过滤层100%保证规则合规，避免惩罚式训练在阈值附近失效的问题

  - 多参与方的推荐结果可解释性，可复用Shapley/Banzhaf归因方案，实验验证其归因得分与组件移除后的效用损失相关性达0.76，解释可信度高

  - 共享资源分配的贪婪调度算法有理论近似保证，工程实现复杂度低，性能距最优上界差≤2%，可直接落地'
score: 7
source: arxiv-cs.AI
depth: abstract
---

### 动机
传统单用户推荐假设服务独立个体，无法适配家庭类多成员共享有限资源、存在差异化规则约束的场景，易出现资源冲突、规则违反、群体公平性不足问题。
### 方法关键点
将家庭食品推荐建模为带约束的公平分配问题，提出神经符号框架FairFRESH：1）学习单成员效用函数；2）基于功利主义/平滑Nash福利目标做贪心分配；3）后置确定性过滤层100%保证饮食规则合规；4）用Shapley、Banzhaf归因生成可解释性。
### 关键结果
- 效用模型Recall@20达0.293，优于5个基线学习推荐器（最高0.244）
- Nash分配相比冲突解决基线，基尼差异降42%，Recall@20从0.180升至0.197，距平滑Nash最优上界差≤2%
- 归因得分与组件移除后效用损失相关性r=0.76；周轮换共享餐策略让最差成员效用提升38%
