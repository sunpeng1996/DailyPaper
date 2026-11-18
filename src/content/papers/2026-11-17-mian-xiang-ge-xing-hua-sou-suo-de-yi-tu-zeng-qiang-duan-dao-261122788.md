---
title: 'IntentGR: Enhancing Intent for End-to-End Personalized Generative Retrieval
  in Search'
title_zh: 面向个性化搜索的意图增强端到端生成式检索框架IntentGR
authors:
- Gefan Ye
- Yanjing Wu
- Yinfu Feng
- Zhiqiang Wang
- Liang Li
- Jun Xiao
- Rong Xiao
- Xiaoyi Zeng
affiliations:
- Zhejiang University
- Alibaba International Digital Commercial Group
arxiv_id: '2611.22788'
url: https://arxiv.org/abs/2611.22788
pdf_url: https://arxiv.org/pdf/2611.22788
published: '2026-11-17'
collected: '2026-11-18'
category: GenRec
direction: 生成式检索 · 意图增强
tags:
- Generative Retrieval
- Semantic ID
- Personalized Search
- Intent Enhancement
- E-commerce Search
one_liner: 在端到端生成式检索全链路注入意图增强机制，公开/工业数据集Recall@10最高提升11.96%
practical_value: '- 输入层可直接复用QBR设计：新增同query下全局历史点击序列作为输入信号，无需修改模型结构即可快速提升召回效果，尤其适配电商搜索场景

  - 长尾query优化可复用LQE策略：对长尾query按频率倒数重采样+语义改写增强，无需改动模型即可缓解头部query偏置，实测长尾Recall@10最高提升15%+

  - 解码层可复用QAM trick：解码时在所有非query上下文位置注入全局query语义（融合系数α取0.8效果最优），强化意图对SID生成过程的引导

  - 端到端生成式检索训练可新增QSA对比损失：对齐query表征与RQ-VAE tokenizer输出的物品重构表征，能让Semantic ID更贴合搜索意图，无额外推理开销'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有端到端生成式检索方案多适配推荐场景，仅将query作为普通输入特征，未在Semantic ID学习、序列生成全流程做意图引导，导致生成结果偏向高频token模式，偏离当前搜索意图，尤其在长尾query、低活用户场景下效果衰减明显。

### 方法关键点
- Query-Aware Semantic Behavior Representation（QBR）：输入层新增同query下全局历史点击序列，与原query、用户历史行为拼接输入，引入query级协作信号
- Query-Semantic Alignment（QSA）：优化层新增双向对比损失，对齐query编码表征与RQ-VAE tokenizer输出的目标物品重构表征，让SID空间与query语义对齐
- Long-Tail Query Enrichment（LQE）：数据层对长尾query按频率倒数重采样+语义改写增强，平衡训练分布，缓解头部query主导的偏置问题
- Query-conditioned Attention Modulation（QAM）：解码层将全局query向量注入所有非query上下文位置，α=0.8融合原始上下文与query语义，强化意图对生成过程的引导

### 关键结果
在公开AOL4PS基准、阿里Express（AE）工业电商数据集上，相比最优基线ETEGRec-Q，Recall@10分别提升8.11%、11.96%；长尾query场景Recall@10最高提升15.85%，低活用户场景也获得稳定增益，且无头部query效果损失。

最值得记住的结论：端到端生成式检索不能仅将query作为被动输入特征，在输入、优化、数据、解码全链路注入意图引导，可同时兼顾搜索相关性、个性化偏好与长尾场景效果。
