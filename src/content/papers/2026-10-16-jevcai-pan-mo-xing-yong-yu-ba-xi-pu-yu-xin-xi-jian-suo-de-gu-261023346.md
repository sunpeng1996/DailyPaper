---
title: 'Jev-as-a-Judge for Brazilian Portuguese Information Retrieval: Relevance Assessment
  and Reranking'
title_zh: Jev裁判模型用于巴西葡语信息检索的相关性评估与重排序
authors:
- Leandro Carísio Fernandes
- Jayr Pereira
affiliations:
- Câmara dos Deputados, Brazil
- Universidade Federal do Cariri (UFCA), Brazil
- Universidade Estadual de Campinas (Unicamp), Brazil
arxiv_id: '2610.23346'
url: https://arxiv.org/abs/2610.23346
pdf_url: https://arxiv.org/pdf/2610.23346
published: '2026-10-16'
collected: '2026-10-20'
category: RecSys
direction: 信息检索 · 相关性标注与重排优化
tags:
- Reranking
- Relevance Assessment
- Information Retrieval
- System One Model
- Judge LLM
one_liner: 验证轻量System One模型Jev可同时作为相关性标注工具与检索重排器，性能优于BM25
practical_value: '- 小语种/垂直领域搜索场景可复用轻量System One类模型替代人工做相关性标注，相邻级吻合度超94%，可满足模型迭代评测需求

  - 检索重排阶段可引入Jev类轻量裁判模型对BM25召回的Top1000候选重排，实测nDCG@10提升超90%，MRR提升超30%，性价比高于大模型重排

  - 缺乏官方评测集qrels时，可用Jev生成的伪标注替代，其对检索系统的排序结果与官方标注的Kendall tau可达0.9以上，可满足快速迭代的效果验证需求'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
现有LLM作为检索相关性裁判推理成本高、速度慢，小语种垂直领域缺乏低成本的相关性标注与重排方案。
### 方法关键点
采用专为快速结构化决策设计的System One模型Jev，在4个巴西葡语IR数据集上开展两类任务验证：①相关性标注任务与官方人工标注做一致性对比；②重排任务对BM25召回的Top1000候选重排，对比BM25基线效果。
### 关键结果
相关性标注精确吻合率52.9%~64.9%，加权Cohen's kappa 0.52~0.82，94.5%以上标注结果与人工完全一致或仅差1个相关等级，生成的伪标注对检索系统的排序Kendall tau达0.90~0.93；重排任务nDCG@10从0.3329提升至0.6331（+90.2%），MRR从0.6852提升至0.9033（+31.8%）
