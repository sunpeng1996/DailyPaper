---
title: 'The Fusion Tax: A Diagnostic Analysis of When Hybrid Retrieval Hurts'
title_zh: 融合税：混合检索性能损耗的诊断分析与选型指导
authors:
- Aaditya Chauhan
- Arun Agarwal
affiliations:
- Independent Researcher
arxiv_id: '2610.30612'
url: https://arxiv.org/abs/2610.30612
pdf_url: https://arxiv.org/pdf/2610.30612
published: '2026-10-22'
collected: '2026-10-23'
category: RAG
direction: RAG混合检索 · 性能损耗诊断
tags:
- Hybrid Retrieval
- RRF
- BM25
- Dense Retrieval
- RAG
one_liner: 量化稀疏-稠密混合检索的单查询损耗，给出RAG/搜索场景的融合策略选型依据
practical_value: '- 不要盲目使用框架默认的RRF融合：先测试业务语料的稀疏/稠密检索性能差，若稠密明显更强优先选dense-weighted score
  interpolation（α=0.6~0.7），可降低20%左右的融合税；仅当两者性能接近时再用RRF

  - 无需通过升级稠密编码器规模规避融合税：从22M到596M参数的嵌入模型融合税比例无明显下降，核心影响因素是稀疏、稠密检索的性能平衡

  - 放弃跨语料训练的低成本路由方案：用通用query特征预测融合失败的跨语料AUC仅0.59接近随机，优先在业务语料上小流量AB测选择静态融合权重，投入产出比更高

  - 若下游有强cross-encoder reranking阶段，无需过度纠结第一阶段融合策略：71%~90%的融合税可被修复，最终rerank后融合与纯稠密的nDCG@10差距不超过0.011'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前主流RAG框架、开源搜索栈均默认推荐稀疏+稠密混合检索+RRF融合，仅基于聚合指标的提升给出建议，未量化单查询维度的性能损耗，从业者无法判断什么时候融合反而劣于单路检索，也没有可落地的选型依据。

### 方法关键点
- 覆盖7个BEIR基准数据集，包含科学、金融、医疗、问答等多场景
- 对比3种主流融合方法：RRF、归一化分数插值、CombMNZ
- 测试5款跨代稠密编码器（参数规模22M~596M）、2种稀疏检索器（BM25、SPLADE），同时验证cross-encoder reranking对融合税的修复效果
- 定义「融合税」为单查询下融合结果的nDCG@10低于两路检索中最优结果的比例

### 关键结果
- 最优的稠密加权插值（α=0.7）在13%~48%的查询上劣于最优单路检索，8%~21%的查询劣于纯稠密检索；RRF的融合税更高，在15%~33%的查询上劣于纯稠密，仅在稀疏、稠密性能接近的场景占优
- 融合税不会随编码器规模升级消失，596M参数的Qwen3嵌入模型仍存在14%~43%的融合税
- 单语料内预测融合失败的AUC仅0.63，跨语料仅0.59，无法用低成本query特征实现可迁移的per-query路由
- 强cross-encoder可修复71%~90%的原始受损查询，rerank后融合与纯稠密的nDCG@10差距不超过0.011

混合检索没有通用最优策略，选型的核心依据是目标业务语料上稀疏和稠密检索的性能平衡。
