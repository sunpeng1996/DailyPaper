---
title: 'SciRet: A Compute-Aware Empirical Study of Retrieval and Reranking for Scientific
  RAG'
title_zh: SciRet：面向科学领域RAG的检索与重排序计算感知实证研究
authors:
- Kaysarul Anas Apurba
- Md. Hasibul Hasan
- Rofiqul Alam Shehab
- Asab Azad
affiliations:
- Laurentian University
- North South University
arxiv_id: '2608.03860'
url: https://arxiv.org/abs/2608.03860
pdf_url: https://arxiv.org/pdf/2608.03860
published: '2026-08-04'
collected: '2026-08-05'
category: RAG
direction: 垂直领域RAG 检索与重排选型优化
tags:
- RAG
- Hybrid Retrieval
- Cross-encoder Reranking
- Empirical Evaluation
- Domain Adaptation
one_liner: 面向科学RAG做控制变量实验，验证混合检索优势与通用重排的领域不匹配问题
practical_value: '- 垂直领域RAG落地可直接复用BM25+BGE-M3+RRF的混合检索作为基线方案，比单路稀疏/稠密召回稳定性更高，算力成本可控

  - 通用域（如MS MARCO）训练的跨编码器重排不要直接上线垂直领域业务，先做小范围ab测试，避免域不匹配导致精度下降

  - 做检索组件选型验证时，要覆盖不同量级的语料规模，小数据集的实验结论不能直接套用到大规模生产环境

  - 多路召回融合前可先计算不同召回通路结果的Jaccard相似度，相似度低于0.3时融合收益通常更显著'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
科学领域RAG对术语精准性、证据可信度要求极高，通用web场景下的RAG组件直接迁移到垂直领域效果不稳定，现有研究缺少控制变量下不同语料规模的对比实验，无法给资源受限的垂直RAG落地提供明确的选型参考。
### 方法关键点
- 固定预处理、chunking、嵌入模型、生成prompt等所有变量，仅调整语料规模，对比1K/5K/15K三个量级的CORD-19语料下的RAG效果
- 检索侧对比三类方案：BM25稀疏检索、BGE-M3稠密检索、二者基于RRF的混合检索
- 重排侧消融验证MS MARCO预训练的跨编码器重排的领域适配效果
- 同时评估检索侧的Recall@K、Precision@K，生成侧RAGAS的忠实度、答案相关性等多维度指标
### 关键实验结果
评测基于CORD-19标题+摘要语料，15个科学领域查询作为测试集：
- 混合检索在1K/15K语料下Recall@10均达到1.000，大幅优于单路稠密/稀疏检索
- MS MARCO跨编码器重排使1K语料下P@5从0.600降至0.404，所有量级下精度均出现下降
- 语料规模从1K升到15K时，RAG生成忠实度从0.917提升到0.960，答案相关性从0.680升至0.870
### 核心结论
垂直领域RAG落地不要直接照搬通用域最优组件，优先用低成本的混合检索作为基线，重排模块必须做领域适配验证后再上线
