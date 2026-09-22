---
title: Per-Query Gating of LLM Rerankers for Multi-Hop Retrieval
title_zh: 面向多跳检索的LLM重排器逐查询门控机制
authors:
- Andre Bacellar
affiliations:
- Independent Researcher
arxiv_id: '2609.22880'
url: https://arxiv.org/abs/2609.22880
pdf_url: https://arxiv.org/pdf/2609.22880
published: '2026-09-19'
collected: '2026-09-22'
category: RAG
direction: RAG系统 · 重排成本动态优化
tags:
- Reranking
- Multi-hop Retrieval
- Cost Optimization
- LLM RAG
- Gating Mechanism
one_liner: 通过轻量逐查询分类器判断是否跳过LLM重排，平均省51%调用量仅损失1.2pp检索准确率
practical_value: '- 可复用逐请求门控思路：在电商/广告搜索的大模型重排链路中，用前置召回的分数统计、轻量query embedding做特征训练二分类器，判断是否跳过LLM重排，降低推理成本

  - 评估可参考嵌套交叉验证协议：所有特征、阈值、fallback均在训练折内选择，避免数据泄露导致的离线效果高估，提升上线后效果稳定性

  - 可复用损失预算调优方法：基于Platt校准的伤害概率，根据业务可接受的准确率损失（如1pp）设置门控阈值，1pp预算下可平均节省42%LLM调用量

  - fallback策略可借鉴蒸馏思路：用历史LLM重排分数离线训练轻量GBM排序模型作为跳过重排后的兜底，效果优于原生召回排序，降低效果损失'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
多跳RAG系统中LLM重排可显著提升检索准确率，但每千次查询需消耗0.2-0.3美元成本，还会增加约1秒尾延迟；且不同query的重排增益差异极大，大量query无需重排即可达到目标准确率，现有全量走重排的方案成本浪费严重。

### 方法关键点
- GATERR逐查询门控仅用LLM调用前可获得的特征：27维召回列表分数、词法统计特征，加可选的BGE-SMALL query embedding PCA特征，训练轻量二分类器判断是否跳过LLM重排
- 提供两种可执行fallback：原生HIPPORAG2的top-K结果，或用LLM重排历史分数蒸馏的轻量GBM排序模型的top-K结果
- 采用严格嵌套交叉验证协议，所有特征、分类器、阈值、fallback均在训练折内选择，避免数据泄露；支持基于Platt校准的损失预算规则，可根据业务可接受的准确率损失动态设置阈值

### 关键结果
在2WikiMultiHopQA、MuSiQue、HotpotQA三个多跳检索基准的9个（数据集，K）单元格上测试：
- 平均跳过51%的LLM重排调用，仅损失1.2pp的LastHop@K；4个单元格满足1pp非劣效要求，最高可跳过99.6%的调用
- 1pp准确率损失预算下，平均跳过42%的调用，仅损失0.8pp，6个单元格满足1pp非劣效要求
- 门控效果远优于同跳过率的随机门控，随机门控在高增益单元格会损失2-11pp的准确率

### 核心结论
大模型链路的成本优化无需一刀切降级，逐请求轻量门控可在极小效果损失下实现显著成本节省
