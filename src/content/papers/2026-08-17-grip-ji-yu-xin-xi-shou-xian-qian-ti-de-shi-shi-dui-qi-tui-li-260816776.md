---
title: 'GRIP: Grounded Reasoning via Information-Restricted Premises'
title_zh: GRIP：基于信息受限前提的事实对齐推理框架
authors:
- Lirui Teng
affiliations:
- University of Waterloo
arxiv_id: '2608.16776'
url: https://arxiv.org/abs/2608.16776
pdf_url: https://arxiv.org/pdf/2608.16776
published: '2026-08-17'
collected: '2026-08-18'
category: RAG
direction: 检索增强生成 · 幻觉抑制
tags:
- RAG
- Information Bottleneck
- Hallucination Reduction
- Query Dominance
- Grounded Reasoning
one_liner: 为RAG设计容量不对称的低维随机证据瓶颈，解决查询主导问题，大幅降幻觉提推理准确率
practical_value: '- 电商导购Agent的RAG模块可直接复用容量不对称设计：query走全维路径，商品/评论等检索证据过4-8维随机瓶颈，强制仅传输query未覆盖的增量信息，减少乱报商品参数等参数知识导致的幻觉

  - 可借鉴Query-Latent Dependence (QLD) 互信息指标，作为RAG系统检索证据利用率的离线诊断指标，比注意力权重更可靠地预判幻觉风险

  - 检索后预处理阶段可复用「熵重排序 + 预测span提取 + NLI验证」pipeline，过滤冗余检索内容，仅保留对生成有预测性的有效证据，降低推理成本同时提升事实一致性'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有RAG系统普遍存在查询主导问题：高容量编码器让查询特征占据隐空间主导方向，检索证据沦为无关扰动，模型倾向于依赖参数知识生成内容，即使与证据冲突也会产生幻觉。现有方法仅干预解码或监督阶段，未从隐空间融合的几何结构层面解决核心矛盾。

### 方法关键点
- 核心采用容量不对称架构：查询和推理上下文走全维旁路输入解码器，检索证据经过严格的低维随机瓶颈（dz=4，加高斯噪声），强制证据通道仅传输查询未覆盖的信息残差
- 四阶段pipeline：熵引导重排序检索候选→预测性span提取（匹配全段落预测分布+长度稀疏惩罚）→NLI验证过滤不蕴含的span→低维随机压缩后作为特殊token注入解码器
- 训练采用两阶段课程：先冻结熵重排序，用普通top检索结果训练瓶颈和解码器，稳定后再开启熵引导重排序

### 关键结果
在HotpotQA、StrategyQA、2Wiki、ProofWriter、SQuAD 2.0五个推理基准测试，对比Standard RAG、Self-Ask、架构匹配的Llama-3 Iterative基线：平均准确率较Standard RAG提升8个点，查询-隐空间互信息降低约30×（14.8→0.47 bits），幻觉率平均降低73%。

**最值得记住的一句话**：RAG的证据利用率问题本质是隐空间的容量分配问题，而非单纯的内容选择问题，用极端的容量不对称强制证据传递增量信息，比复杂的融合策略更有效。
