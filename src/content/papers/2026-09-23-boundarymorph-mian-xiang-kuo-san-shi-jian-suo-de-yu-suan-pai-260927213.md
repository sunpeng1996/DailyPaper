---
title: 'BoundaryMORPH: Budgeted Reranking via Active Set Selection for Diffuse Retrieval'
title_zh: BoundaryMORPH：面向扩散式检索的预算受限重排主动集选择算法
authors:
- Eylon Caplan
- Shamik Roy
- Shib Sankar Dasgupta
- Yingfan Wang
- Rashmi Gangadharaiah
affiliations:
- Purdue University
- AWS AI Labs
arxiv_id: '2609.27213'
url: https://arxiv.org/abs/2609.27213
pdf_url: https://arxiv.org/pdf/2609.27213
published: '2026-09-23'
collected: '2026-09-24'
category: RAG
direction: RAG 预算受限重排优化
tags:
- Reranking
- Cross-Encoder
- Gaussian Process
- Diffuse Retrieval
- Top-k Selection
- RAG
one_liner: 基于高斯过程的预算受限重排方法，聚焦top-k决策边界分配Cross-Encoder算力，提升扩散式检索质量
practical_value: '- 重排算力分配优化：当Cross-Encoder重排预算远小于top-k返回规模时，放弃对头部高置信度候选的冗余打分，优先决策边界候选，可大幅提升算力ROI，适配电商搜索/推荐的多阶段重排场景

  - 先验信息复用trick：将一阶双塔/MIPS召回的候选百分位排名作为高斯过程的先验均值，无额外训练成本即可提升未打分校验的估计准确性，可直接迁移到多阶段推荐的候选排序链路

  - 多主题召回适配：方法天然覆盖多个语义相关峰，适合电商泛搜、Agent深搜等需要召回多维度相关结果的场景，避免过度聚焦单一主题导致的漏召回问题

  - 低侵入改造：若业务核心目标是提升top-k集合的整体相关性而非精确排序，可直接替换现有重排的top-B打分逻辑，无需改动上下游链路'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前RAG系统处理开放型扩散式查询（如“光污染的影响”）时，需要召回大量相关文档填充LLM上下文，但昂贵的Cross-Encoder（CE）重排预算B通常远小于上下文窗口容量k。传统重排仅对头部B个候选打分，既浪费算力验证已确定的高相关文档，还会漏掉排名靠后的相关文档，无法充分利用有限的CE预算。
### 方法关键点
- 以双塔MIPS召回的候选百分位排名作为高斯过程（GP）的先验均值，建模CE打分与MIPS排名的残差，无标注区域自动 fallback 到MIPS排序，无需额外训练
- 放弃传统全局最优搜索的采集函数，改为聚焦top-k决策边界：每次优先选择当前最可能跨边界的候选对，仅对不确定性更高的候选调用CE打分，单次CE的打分信息通过GP核函数传播到所有语义相似的未打分校验，最大化单CE调用的信息增益
- 加入零成本查询锚点：将query向量作为最大相关的观测值输入GP，无需额外CE调用即可降低query附近的估计方差
### 关键实验
在NeuCLIRBench、Robust04、TravelDest三个扩散式查询数据集上测试，对比BM25、单阶段重排、RGS、BAGEL等基线，B=25、k=100时平均nCG@100比最强基线BAGEL高3.8pp，最高提升5.4pp，CE-nCG@200平均提升7.3pp；两个核心组件（MIPS先验、边界采集函数）分别贡献2-3pp的效果提升，多子主题查询下收益更高。
### 核心结论
当业务目标是选准top-k集合而非给所有候选精确排序时，算力应该优先花在决策边界的模糊候选上，而不是重复验证已经确定的高相关候选
