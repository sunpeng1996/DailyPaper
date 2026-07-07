---
title: Submitted and Diagnostic Analysis of Full-Text Temporal Retrieval for LongEval-Sci
title_zh: LongEval-Sci 全文时序检索方案提交及诊断分析
authors:
- Yingdong Yang
- Haijian Wu
arxiv_id: '2607.04088'
url: https://arxiv.org/abs/2607.04088
pdf_url: https://arxiv.org/pdf/2607.04088
published: '2026-07-05'
collected: '2026-07-07'
category: Eval
direction: 时序检索 · 动态语料性能评估
tags:
- Temporal Retrieval
- BM25
- RRF
- Cross-Encoder
- LongEval
one_liner: 对比十余种检索重排方案，给出动态累积语料下时序检索的最优路径与性能诊断结果
practical_value: '- 动态更新的商品/UGC内容库等检索场景，可复用「全文BM25+时序特征融合」基线架构，比纯BM25大幅降低长期性能衰减

  - 多路召回融合可优先采用RRF方案，能显著提升深层召回率，适合广告召回、全域内容召回等对召回率要求高的场景

  - 新增检索侧特征（如商品销量、内容点赞量等类引用特征）必须做校准，否则会严重损伤头部排序效果'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
科学检索语料随时间持续累积，单次调优的检索系统会随语料更新出现性能衰减，现有方案缺乏动态语料下的纵向性能验证与诊断框架。
### 方法关键点
针对LongEval-Sci 2026评测任务，对比十余种检索与重排方案，覆盖官方BM25/Qwen3稠密基线、全文BM25、时序/引用增强检索、RM3查询扩展、Cross-Encoder重排、RRF多路融合等，同时开展多快照纵向评测与内部性能诊断。
### 关键结果数字
时序增强的全文检索方案性能最优，FT BM25+时序/时序+引用在三个快照上的nDCG@10分别达0.285、0.267、0.180，将快照3的相对性能衰减从纯BM25的0.481降至0.368；内部诊断显示全文BM25是最优单检索器，RRF可将Recall@1000提升至0.9667，未校准的新增特征会严重损伤头部排序质量，引用特征暂未带来统计显著增益。
