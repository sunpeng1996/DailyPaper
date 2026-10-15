---
title: 'Retrieval Disagreement as a Signal: Diagnosing and Steering Multilingual Dense
  Embedders'
title_zh: 利用检索分歧信号诊断与调控多语言密集嵌入模型
authors:
- Faeze Ghorbanpour
- Shaghayegh Kolli
- Jana Diesner
- Alexander Fraser
affiliations:
- Technical University of Munich
- Munich Center for Machine Learning
arxiv_id: '2610.18526'
url: https://arxiv.org/abs/2610.18526
pdf_url: https://arxiv.org/pdf/2610.18526
published: '2026-10-13'
collected: '2026-10-15'
category: RAG
direction: 多语言密集检索 · 无标注偏差校正
tags:
- Multilingual Retrieval
- Dense Embedding
- Retrieval Bias
- Inference-time Intervention
- RAG
one_liner: 提出无标注跨语言检索分歧诊断方法与免训练推理调控策略，提升跨语言召回效果
practical_value: '- 跨境电商多语言搜索场景可直接复用跨语言分歧诊断方法，无需昂贵的跨语言相关性标注，即可定位模型是存在同语言拥挤还是英语引力偏差，针对性优化

  - 多语言RAG/跨境搜索业务可直接落地分歧引导调控方案，仅需在推理时给query embedding添加预计算的语言专属偏移向量，无需重训模型、重建索引，上线成本极低

  - 多场景/跨域召回任务可借鉴核心思路：用不同场景下的检索结果分歧作为无标注校正信号，解决小众场景/小语种标注不足的问题，无需逐场景标注'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有多语言密集检索模型将所有语言映射到共享向量空间，实际应用中相同语义的多语言query召回结果差异极大，query同语言或英语的无关文档会挤占跨语言相关结果的排名。传统基于标注的评估只能量化效果差距，无法区分是模型对低资源语言的表示能力不足，还是共享索引下的语言干扰导致的偏差，也缺乏低成本的校正方案。
### 方法关键点
- 提出三层跨语言检索分歧诊断框架：分别在单语言隔离检索、单语言vs共享索引检索、共享索引下多语言对撞三个场景，计算召回结果的集合重叠度与排序相似度，精准定位偏差来源。
- 提出分歧引导的推理时调控策略：基于外部平行语料，对比其他语言共识召回而当前语言漏召的文档、当前语言独召的无关文档的表示差异，加权得到每个语言的专属偏移向量，推理时直接叠加到query embedding上，无需训练、无需重建文档索引。
### 关键结果
在Belebele（10语平行）、XQuAD（6语平行）、Multi-EuP（24语非平行真实数据）三个数据集上测试7个主流多语言嵌入模型，对比均值移除、子空间移除、正交对齐三个baseline：分歧引导调控平均将跨语言Recall@20从86.4提升至93.1，召回结果中同语言文档占比从44.8降至14.8，去拥挤效果优于所有baseline，且在非平行数据集上的稳定性优于均值移除方案。

最值得记住的结论：多语言检索的失败绝大多数不是因为模型表示能力不足，而是共享索引下的语言干扰导致相关跨语言结果被降权而非丢失，用无标注的检索分歧信号即可低成本校正。
