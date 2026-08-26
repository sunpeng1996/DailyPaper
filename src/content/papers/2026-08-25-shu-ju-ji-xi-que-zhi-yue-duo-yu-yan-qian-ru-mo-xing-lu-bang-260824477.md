---
title: 'Dataset Scarcity Limits Robust Evaluation of Multilingual Embedding Models:
  A Case Study of Slavic Languages'
title_zh: 数据集稀缺制约多语言嵌入模型鲁棒评估：斯拉夫语系案例研究
authors:
- Ana Gjorgjevikj
- Barbara Koroušić Seljak
- Tome Eftimov
affiliations:
- Jožef Stefan Institute
arxiv_id: '2608.24477'
url: https://arxiv.org/abs/2608.24477
pdf_url: https://arxiv.org/pdf/2608.24477
published: '2026-08-25'
collected: '2026-08-26'
category: Eval
direction: 多语言Embedding模型鲁棒评估
tags:
- Multilingual Embedding
- Evaluation Framework
- MTEB
- Evidence Strength
- Low-resource NLP
one_liner: 提出融合证据强度的多语言嵌入评估框架，揭示斯拉夫语基准稀疏性并筛选跨任务稳定模型
practical_value: '- 跨境电商多语言召回/搜索场景评估Embedding效果时，可复用Evidence Strength Score（ESS）量化评估置信度，避免单数据集/高相关数据集带来的选型偏差

  - 面向斯拉夫语系的跨境业务可直接选用验证过的稳定模型：聚类/重排选llama-embed-nemotron-8b，分类选Qwen3系列，双语对齐选bge-m3，大幅降低选型成本

  - 构建业务端Embedding benchmark时，可参考论文的数据集相关性聚类方法剔除冗余测试集，搭配多维度排名方案（多准则决策方法+多种权重策略）提升评估鲁棒性

  - 低资源语言的RAG系统选型时，优先参考高ESS得分任务的top模型，避免被低证据强度的虚高稳定性结论误导'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
多语言Embedding是跨语言NLP任务的基础，但现有基准（如MTEB）的评估在高低资源语言间严重失衡，直接平均多数据集指标的方式忽略了数据集相关性、任务覆盖不均问题，低资源场景下看似稳定的模型排名可能仅来自稀缺或冗余数据，无法反映真实鲁棒性。斯拉夫语系覆盖超3亿人口，但多数语言属于中低资源语言，是验证低资源下评估可靠性的理想场景。

### 方法关键点
- 构建二维评估框架，覆盖「任务内评估」「跨任务泛化」两个维度，联合分析排名鲁棒性、模型top-k一致性、证据强度三个核心属性
- 提出Evidence Strength Score（ESS），结合数据集数量、去冗余后的有效多样性、稳定性可评估性三个因子量化评估结论的置信度，同时划分5个证据等级明确不同场景可支持的评估类型
- 排名稳定性用Kendall's W衡量不同聚合方法、去相关数据集组成下的排名一致性，top-k迁移一致性采用加权计分，头部排名权重更高，贴合业务对头部模型的选型需求

### 关键结果
实验基于MTEB斯拉夫语子集，覆盖12种斯拉夫语、8类任务，采用15种排名方案验证：
- 87%的语言-任务对仅依赖单数据集或高相关数据集，仅bitext mining任务的平均ESS可达0.8，其余多数任务ESS低于0.3，基准稀疏性问题极严重
- 跨任务最稳定的3个模型为llama-embed-nemotron-8b、multilingual-e5-large-instruct、Qwen3-Embedding系列，在高ESS场景下仍保持稳定表现

**核心结论**：多语言模型的评估结论不能仅看排名，必须结合证据强度判断置信度，低资源场景下的高稳定性很可能是基准数据不足导致的假象。
