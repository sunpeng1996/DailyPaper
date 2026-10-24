---
title: 'CRANE: Post-Hoc Counterfactual Retrieval for Multimodal Classifiers'
title_zh: CRANE：面向多模态分类器的事后反事实检索框架
authors:
- Franco Rugolon
- Ioanna Miliou
- Panagiotis Papapetrou
affiliations:
- Stockholm University
- Department of Computer and Systems Sciences, Stockholm University
arxiv_id: '2610.31594'
url: https://arxiv.org/abs/2610.31594
pdf_url: https://arxiv.org/pdf/2610.31594
published: '2026-10-22'
collected: '2026-10-24'
category: Multimodal
direction: 多模态可解释 · 反事实检索
tags:
- Multimodal Explainability
- Counterfactual Explanation
- Post-hoc Explanation
- Nearest Neighbor Retrieval
- Model Agnostic
one_liner: 首个模型无关的多模态事后反事实解释框架，检索真实训练样本生成高可信解释
practical_value: '- 多模态商品推荐/广告审核模型的可解释性需求可复用MC-R策略：取各模态近邻交集找jointly接近的样本，生成的解释是真实训练样本，可信度高，无生成幻觉问题

  - 当单个模态（如商品主图>商品标题）主导推荐决策时，可直接切换为单模态检索策略降本，效果损失可控

  - 不需要修改原多模态模型结构，事后部署成本极低，适合已上线的多模态召回/排序模块的可解释性迭代'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有反事实解释方法仅适配单模态场景，多模态分类器的现有可解释方案仅独立对单模态做归因，存在解释一致性差、无法兼容任意预训练多模态架构的问题。
### 方法关键点
CRANE是首个模型无关的多模态事后反事实解释框架，直接从训练集中检索目标类的真实样本作为候选解释，天然保证解释的合理性；核心策略MC-R（Multimodal Consensus Retrieval）通过取各模态近邻集合的交集，筛选在所有模态下都与查询样本距离接近的实例。
### 关键结果
在4个异质数据集、3种多模态融合策略下验证，MC-R在3个数据集上取得最优或并列最优效果；当单一模态主导模型决策边界时，单模态检索策略效果仍具备竞争力。
