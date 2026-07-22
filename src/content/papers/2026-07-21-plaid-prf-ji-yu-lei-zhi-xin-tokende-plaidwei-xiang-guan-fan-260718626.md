---
title: 'PLAID-PRF: Pseudo-Relevance Feedback with Centroid-like Tokens in PLAID'
title_zh: PLAID-PRF：基于类质心Token的PLAID伪相关反馈方法
authors:
- Xiao Wang
- Sean MacAvaney
- Craig Macdonald
affiliations:
- University of International Business and Economics
- University of Glasgow
arxiv_id: '2607.18626'
url: https://arxiv.org/abs/2607.18626
pdf_url: https://arxiv.org/pdf/2607.18626
published: '2026-07-21'
collected: '2026-07-22'
category: RecSys
direction: 稠密检索 · 伪相关反馈优化
tags:
- Dense Retrieval
- Pseudo-Relevance Feedback
- ColBERT
- PLAID
- Query Reformulation
one_liner: 复用PLAID预训练质心实现轻量伪相关反馈，效果显著优于基线且仅增加少量查询延迟
practical_value: '- 电商搜索PRF场景可直接复用向量量化索引的全局codebook质心作为语义单元，替代实时KMeans聚类，能把PRF阶段延迟从几百ms降到几ms，满足线上SLA要求

  - 扩展向量选择环节可复用MMR策略平衡相关性与多样性，在用户模糊query、长尾query等难查询场景下，能有效提升头部结果的相关性

  - 跨类目/跨域检索场景可通过调整扩展向量的缩放系数β控制反馈贡献，避免query漂移，冷启动场景可适当调低β提升稳定性'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
多向量稠密检索模型（如ColBERT）凭借细粒度token匹配实现了优异的检索效果，但现有面向多向量模型的伪相关反馈（PRF）方法依赖实时聚类或额外模型推理，延迟过高无法落地到线上业务；而PLAID作为ColBERT的量化加速版本，索引构建时预训练了全局质心codebook，具备实现轻量PRF的基础条件。
### 方法关键点
- 先用原始query执行PLAID初始检索，取top-fp文档作为反馈集
- 将预训练质心ID作为语义term，预计算每个质心的全局文档频率df，在反馈集上统计每个质心的词频tf，用TF-IDF、RM3等经典权重公式计算质心的重要性，映射到对应反馈token的权重
- 采用MMR算法选择fe个高权重、低冗余的重建token向量（质心+残差），乘以缩放系数β后拼接到原始query向量序列
- 用扩展后的query二次执行PLAID检索得到最终结果
### 关键结果
在TREC DL 2019/2020、DL-HARD等基准数据集上，相比原始PLAID，PLAID-PRF在TREC DL 2019上nDCG@10提升4.3%、MRR@10提升4%，在难查询集DL-HARD上MRR@10提升7.3%，端到端延迟仅102ms，比ColBERT-PRF快16倍以上，在4个BEIR跨域数据集上也能稳定提升召回率。
### 核心洞察
向量量化索引的预计算质心可以直接复用为PRF的语义单元，无需额外训练即可实现效果与延迟的帕累托最优。
