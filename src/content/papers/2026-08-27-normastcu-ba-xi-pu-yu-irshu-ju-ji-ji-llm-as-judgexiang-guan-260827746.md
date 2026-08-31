---
title: NormasTCU --- A Brazilian Portuguese IR Dataset and an Evaluation of LLM-as-a-Judge
  for Relevance Assessment
title_zh: NormasTCU：巴西葡语IR数据集及LLM-as-Judge相关性评估
authors:
- Leandro Carísio Fernandes
- Marcus Vinícius Borela de Castro
- Leandro dos Santos Ribeiro
- Leonardo Augusto da Silva Pacheco
- Edans Flávius de Oliveira Sandes
affiliations:
- Câmara dos Deputados, Brasília, Brazil
- Tribunal de Contas da União (TCU), Brasília, Brazil
arxiv_id: '2608.27746'
url: https://arxiv.org/abs/2608.27746
pdf_url: https://arxiv.org/pdf/2608.27746
published: '2026-08-27'
collected: '2026-08-31'
category: Eval
direction: LLM-as-Judge 相关性评估数据集构建
tags:
- LLM-as-a-Judge
- Information Retrieval
- Dataset
- Relevance Assessment
- Evaluation
one_liner: 发布巴西葡语法律IR数据集，实测LLM-as-Judge相关性评估的效果边界
practical_value: '- 垂类搜索/推荐做LLM-as-Judge相关性标注时，优先用nDCG/MRR这类秩敏感指标对齐人工结果，慎用P@k/R@k类指标

  - LLM标注存在普遍正向打分偏置，可在prompt中加入偏置校准约束，或对输出分数做后验偏移修正降低MAE

  - 中小语种/垂类IR系统快速迭代时，可复用LLM-as-Judge做可扩展标注，其排序一致性甚至超过单个人工标注'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
巴西葡萄牙语IR领域公开数据集稀缺，专业领域相关性标注成本高，非英语垂类场景下LLM-as-Judge的可靠性尚未验证。
### 方法关键点
1. 发布NormasTCU数据集，包含14469份法律文档、46个query、812个query-文档对的3048条人工标注；
2. 采用2种prompt策略测试3款LLM的打分效果，对比15个IR系统在LLM标注与人工标注下的排序一致性。
### 关键结果
- LLM存在稳定正向打分偏置，0-2分制下MAE为0.46~0.66，与人工标注的Cohen's kappa仅0.32~0.53，一致性中等偏下；
- 基于LLM标注得到的系统排序，nDCG@10、MRR的Kendall's tau≥0.90，与人工排序一致性极高，甚至超过单个人工标注的一致性；
- P@10、R@10的一致性较差，不建议采用此类指标做LLM标注的对齐基准。
