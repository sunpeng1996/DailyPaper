---
title: 'UEmbed: Unified Sparse and Dense Multimodal Embeddings'
title_zh: UEmbed：统一稀疏与稠密表征的多模态嵌入模型
authors:
- Tingyu Song
- Mingxin Li
- Yanzhao Zhang
- Dingkun Long
- Pengjun Xie
- Zhijie Nie
- Yilun Zhao
- Shu Wu
affiliations:
- CASIA
- Alibaba Group
- University of Chinese Academy of Sciences
- Yale University
arxiv_id: '2608.02583'
url: https://arxiv.org/abs/2608.02583
pdf_url: https://arxiv.org/pdf/2608.02583
published: '2026-08-02'
collected: '2026-08-04'
category: RAG
direction: 多模态检索 · 稀疏稠密统一表征
tags:
- Multimodal Embedding
- Sparse Retrieval
- Dense Retrieval
- Decoder-only
- Agentic Search
- RAG
one_liner: 基于Decoder-only架构的单模型多模态嵌入方案，同时输出稀疏稠密表征，性能领先公开训练基线
practical_value: '- 电商多模态搜索/商品召回场景可复用其单模型双输出架构：一次前向同时生成稀疏、稠密表征，混合打分可提升文本/富视觉商品召回精度，同时兼容现有倒排索引、向量检索引擎与vLLM等高吞吐serving栈，无需额外部署两套模型

  - Agent工具调用场景下，针对用户短关键词类查询优先调用稀疏检索分支，相比同规模稠密检索可降低10%~20%的搜索轮次，减少工具调用成本，同时召回率基本持平

  - 工程实现可直接复用其词汇压缩+语义分区方案：通过k-means划分词汇子集分配给追加的特殊token，解决Decoder-only架构下稀疏表征的单token表达瓶颈，几乎无性能损耗即可获得双检索能力'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有Learned Sparse Retrieval（LSR）依赖Encoder双向架构，多模态场景需额外引入跨模态模块，无法兼容Decoder-only LLM成熟的serving栈；同时业界需要部署稀疏、稠密两套独立检索模型，成本高，多模态场景下稀疏检索效果远低于稠密检索，缺乏统一的高效方案。
### 方法关键点
- 基于Qwen3.5 Decoder-only多模态底座，在输入末尾追加16个可学习特殊token，通过k-means将词汇表划分为16个不相交语义子集，每个特殊token负责预测对应子集的稀疏权重，拼接得到完整稀疏向量
- 稠密表征直接取EOS token隐藏态，仅需稠密检索时可省略特殊token，无额外计算开销
- 采用Dense InfoNCE + Sparse InfoNCE + FLOPS正则的混合损失联合训练，保证双模态性能无负迁移，使用公开多模态+文本数据集+大模型硬负样本挖掘完成训练
### 关键结果
- 多模态基准MMEB-v2上，UEmbed-9B稠密得分71.8、稀疏得分71.0，是公开训练数据模型中的SOTA，首次实现多模态稀疏检索效果追平稠密
- 文本检索基准BEIR上，UEmbed-9B稠密nDCG@10达56.3、稀疏达55.2，与专门的稀疏检索模型Echo-Mistral-SPLADE效果持平
- Agent检索基准BrowseComp-Plus上，稀疏分支相比同规模稠密分支平均搜索轮次降低约20%，召回率基本持平

> 值得记住的结论：Decoder-only架构可原生支持统一稀疏稠密多模态检索范式，在保证效果的同时大幅降低部署成本，适配多模态搜索、Agent检索等多场景需求
