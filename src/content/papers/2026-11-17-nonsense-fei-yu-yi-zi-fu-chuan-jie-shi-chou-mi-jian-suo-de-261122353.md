---
title: 'NONSENSE: Non-Semantic Strings Expose Semanticity Gaps in Dense Retrieval'
title_zh: NONSENSE：非语义字符串揭示稠密检索的语义性缺口
authors:
- Ankit Gupta
affiliations:
- Michigan State University
arxiv_id: '2611.22353'
url: https://arxiv.org/abs/2611.22353
pdf_url: https://arxiv.org/pdf/2611.22353
published: '2026-11-17'
collected: '2026-11-18'
category: Eval
direction: 稠密检索评估 · 黑盒对抗探针
tags:
- DenseRetrieval
- BlackBoxProbe
- AdversarialAttack
- EmbeddingRobustness
- RAGSecurity
one_liner: 提出黑盒探针NONSENSE，证明主流单向量稠密检索高相似度可脱离语义相关性
practical_value: '- 上线稠密检索/RAG系统前，可复用NONSENSE探针做压力测试，筛查高相似度非语义样本风险，避免召回垃圾内容

  - 电商搜索、推荐的召回层不要完全依赖单向量稠密检索，需叠加BM25等稀疏检索、词汇校验、语义合法性校验等多层过滤，规避对抗样本攻击

  - 针对Agent的检索工具模块，可在返回结果后加轻量级语义验证（如判断是否为可理解的自然语言），避免非语义内容进入后续LLM推理环节'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
稠密检索是当前搜索、RAG、开放域问答的核心基建，工业界普遍默认高相似度得分对应语义相关，但这一假设从未被严格验证。若存在无意义非语义字符串也能获得高相似度，会直接导致RAG幻觉、搜索召回垃圾内容、推荐结果无效等业务问题，亟需针对性的探测方法。
### 方法关键点
- 黑盒探针NONSENSE无需访问模型梯度、权重，仅通过单字符替换迭代优化字符串与query的稠密相似度，全程禁止包含长度≥3的query术语，最终生成完全无意义、无query词汇重叠的可见非语义字符串
- 采用QRP（同检索器下打分最高的标注相关文档）作为对比基准，核心指标为非语义字符串得分超过QRP的成功率、插入全语料后的排名
### 关键实验结果
在5个BEIR风格数据集（语料规模3.6k~57.6k）、3款主流单向量稠密检索器（E5、BGE、Contriever）上测试：
- 多数数据集-检索器组合的成功率超过90%，部分组合达99%，非语义字符串全语料中位数排名为1
- 仅需1k~5k次迭代即可超过QRP得分，效果与初始化方式、字符串长度无关，仅含符号的无字母串仍有最高56.6%的成功率
- 随机字符串、空白串的成功率接近0，排除随机概率的影响
### 核心结论
不要默认稠密检索的高相似度等于语义相关，工业级检索系统必须叠加多层校验机制规避语义性缺口导致的业务风险
