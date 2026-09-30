---
title: 'MERGE: Multi-LLM Ensemble for Retrieval via Generative Enrichment'
title_zh: MERGE：基于生成式增强的多LLM检索集成框架
authors:
- Tzu-I Ho
- Yung-Yu Shih
- Shang-Yu Su
- Dongzhe Wang
- Yun-Nung Chen
affiliations:
- University of Waterloo
- National Taiwan University
- Rakuten Group, Inc.
- Rakuten Asia Pte. Ltd.
arxiv_id: '2609.37574'
url: https://arxiv.org/abs/2609.37574
pdf_url: https://arxiv.org/pdf/2609.37574
published: '2026-09-29'
collected: '2026-09-30'
category: QueryRec
direction: 多LLM查询扩展 · 自动提示优化
tags:
- Query Expansion
- LLM Ensemble
- Automatic Prompt Optimization
- BM25
- Information Retrieval
one_liner: 双阶段多LLM查询增强框架结合任务驱动APO，无需语料处理即可大幅提升BM25检索性能
practical_value: '- 电商搜索场景可直接复用双阶段多小模型查询增强架构：用3个7-8B异构开源LLM并行生成扩展query，再用14B模型融合，无需修改索引、无需重新训练检索器，即可提升搜索召回效果，推理成本远低于单一大模型全量推理

  - 任务驱动APO流程可直接落地替代手动prompt调优：用20%左右的业务标注开发集的实际检索指标（如nDCG@10、召回率）作为prompt打分信号，采用锦标赛式迭代优化，收敛仅需10轮以内，大幅降低多模型prompt调优的人力成本

  - 无需对文档侧做任何修改（如docT5query需要给全量文档加扩展query并重索引），特别适合电商、广告这类商品/素材更新频繁的场景，query侧增强的一次性优化成本可完全摊销到后续流量中

  - 可直接迁移到RAG系统的query改写模块：替换原有单LLM query改写逻辑，即可提升召回阶段的相关文档覆盖率，减少RAG回答幻觉'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有单LLM查询扩展方法受训练数据、架构偏见限制，生成的扩展query意图覆盖度有限，且不同LLM的prompt适配性差，手动调优成本随模型数量线性增长，多模型集成方案难以规模化落地；同时现有主流query扩展方案要么需要对全量文档做扩展并重索引（如docT5query），要么需要多次检索加排序融合（如Exp4Fuse），部署复杂度高，不适合电商、广告这类语料更新频繁的业务场景。
### 方法关键点
- 双阶段集成架构：Stage1调用3个异构7-8B开源LLM（Llama-3.1-8B、Qwen2.5-7B、Mistral-7B）并行生成独立的查询扩展候选，保证意图覆盖的多样性；Stage2用14B Qwen2.5模型将多个候选融合为单一扩展query，过滤幻觉并合并互补信息
- 任务驱动自动提示优化（APO）：覆盖两个阶段所有模型的prompt优化，用20%标注开发集的实际BM25 nDCG@10作为打分信号，采用锦标赛式迭代：每次由优化LLM基于当前最优prompt生成2个候选，三者对比取最优作为新的冠军prompt，连续2轮卫冕则终止收敛；历史增强版额外输入最近5轮优化轨迹，适配探索性查询场景
- 检索器无关设计：输出为纯文本扩展query，仅需一次检索，无需排序融合、无需文档侧修改、无需监督训练数据
### 关键实验
在5个BEIR基准数据集（NQ、SciFact、FiQA、Touché-2020、DBPedia）上测试，对比Vanilla BM25、docT5query、Exp4Fuse等基线：相比原生BM25，nDCG@10最高提升14.9个点（NQ场景），其余数据集提升2.1~7.4个点；优于所有无监督query扩展基线，在3/5数据集上超过监督+无监督融合的强基线docT5query+Exp4Fuse；Stage2融合相比最优单Stage1模型，nDCG@10额外提升0.6~4.4个点，APO可将手动prompt导致的最多5个点的效果回退转为正向收益。

> 最值得记住的一句话：用小比例业务标注数据做任务驱动的自动prompt优化，配合多小模型集成的query增强，仅需一次检索即可达到甚至超过需要文档侧改造、多轮检索的复杂方案效果，落地性价比极高
