---
title: Group-Aware Adaptive Retrieval for Evidence Navigation
title_zh: 面向证据导航的组感知自适应检索框架GAREN
authors:
- June Park
- Jun Kwon
- Jonghyo Kim
- Jongwuk Lee
affiliations:
- Sungkyunkwan University, Republic of Korea
arxiv_id: '2609.02188'
url: https://arxiv.org/abs/2609.02188
pdf_url: https://arxiv.org/pdf/2609.02188
published: '2026-09-02'
collected: '2026-09-03'
category: RAG
direction: RAG 自适应推理密集检索优化
tags:
- Adaptive Retrieval
- Reasoning Intensive Retrieval
- Corpus Graph
- Community Detection
- Reranking
one_liner: 通过语料组级粗粒度导航+文档级细粒度重排提升推理密集检索召回效果
practical_value: '- 离线分组优化：可复用Leiden社区检测算法对商品/内容的语义近邻图做离线分组，生成组语义摘要，替代单粒度检索，降低长距离相关内容召回成本

  - 多轮召回策略：在电商导购Agent、搜索query扩展场景，采用「早期多方向广度探索+后期高置信方向深度利用」的扩展策略，减少早期决策误差传播

  - 轻量后处理优化：重排后可基于同组（如同品类、同语义簇）高秩结果的RBP权重，给同组低秩结果加权，几乎无额外成本即可提升排序准确率

  - 架构选型参考：粗粒度方向决策用小模型（如4B级reranker），细粒度相关性判断用大模型，兼顾效果与latency，适合线上部署'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
推理密集型检索的相关文档无法通过表面语义匹配召回，初始候选集的边界召回问题突出；现有自适应检索基于单文档扩展，在早期证据不足时容易选错方向，误差持续传播，无法触达距离初始结果较远的相关文档。
### 方法关键点
- 离线分组：基于语料语义相似度构建k-NN图，用Leiden社区检测算法划分为语义一致的独立组，用LLM生成每个组的语义摘要作为扩展方向的粗粒度预览
- 在线迭代检索：每轮先对当前候选集做文档级重排，再对可达的候选组用轻量navigator打分；采用探索-利用策略：前τ_switch轮从多个高分组轮询选文档（广度探索），后续轮次优先从最高分组选文档（深度利用）
- 后处理：将同组高排名文档的RBP权重按系数α传播给同组其他文档，优化最终排序
### 关键实验
在BRIGHT推理密集检索基准上，对比SlideGAR、RGS等SOTA自适应检索基线，非推理重排设置下平均nDCG@10达28.3，较最强基线RGS提升7.2%；推理重排设置下平均nDCG@10达31.2，较最强基线REPAIR提升9.8%；在R2MED医疗检索基准上R@100达67.6，较基线RGS提升3.9个百分点，尤其当相关文档距离初始候选集7跳以上时，召回优势显著。
最值得记住的结论：粗粒度组级方向决策+细粒度文档级重排的双粒度架构，能以极低的额外成本大幅提升长距离相关内容的召回效果，显著突破单粒度自适应检索的性能天花板。
