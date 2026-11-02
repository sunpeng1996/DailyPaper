---
title: 'Latent Sparse Attention: Towards Subquadratic Ultra-Long Context Attention'
title_zh: 隐式稀疏注意力：实现亚二次复杂度的超长上下文注意力
authors:
- Ales Kubicek
- Andrea Caciolai
- Liangzu Peng
- Sukrit Sumant
- Benjamin Hoover
- Fraser Greenlee
- Ruairidh M. Battleday
- Radim Urban
- Torsten Hoefler
- James C. R. Whittington
affiliations:
- Prefrontal AI
- ETH Zurich
arxiv_id: '2610.42147'
url: https://arxiv.org/abs/2610.42147
pdf_url: https://arxiv.org/pdf/2610.42147
published: '2026-10-30'
collected: '2026-11-02'
category: LLM
direction: LLM超长上下文优化 · 稀疏注意力
tags:
- Sparse Attention
- Long Context
- LLM Inference
- Attention Optimization
- KV Cache
one_liner: 提出两种隐式稀疏注意力方案，10M token上下文下推理速度最高提升72.4倍且精度损失极小
practical_value: '- 电商/推荐场景处理用户超长全生命周期行为序列时，可复用D-LSA蒸馏方案，仅微调每层小投影矩阵即可将现有LLM上下文窗口扩展到10M级别，无需全量微调，落地成本极低

  - 生成式推荐、Agent长会话场景需要跨超长序列检索语义相关内容时，可借鉴LSA的语义聚类选key思路替换现有块稀疏注意力，精度更高，尤其适配跨周期行为匹配、历史订单关联等需求

  - 工程上可直接复用论文开源的SGLang集成代码与H200/B300优化Kernel，快速落地超长上下文LLM推理能力，无需从零实现稀疏注意力逻辑'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
Agent长周期任务、科研文献理解等场景对1M+ token超长上下文窗口的需求快速增长，但传统稀疏注意力的索引环节在10M级上下文下占prefill耗时的98%，成为核心性能瓶颈；现有稀疏注意力方案要么仍保持二次复杂度，要么在超长上下文下精度下降严重。
### 方法关键点
- 核心逻辑：将key在学习到的隐空间按语义分层聚类，query仅对聚类中心打分选top桶后展开桶内key做注意力，支持Flat/Tree两种搜索模式，Tree模式下prefill复杂度为亚二次O(TlogT)
- D-LSA：适配预训练模型，仅训练每层的小索引投影矩阵，通过蒸馏对齐原模型注意力分布，支持无训练版本（用key主成分做投影）
- N-LSA：原生训练版本，无需蒸馏、无额外参数，仅用next-token loss训练，直接复用注意力自身的key做聚类
### 关键结果
- 测试模型为QWEN-3.8-27B、GLM-5.3-FLASH，对比基线为全注意力、传统块稀疏注意力
- D-LSA在10M token下，GLM上比原稀疏注意力prefill快22.7×、decode快4.6×，QWEN上比全注意力prefill快72.4×、decode快42.5×，精度保持在基线95%置信区间内
- N-LSA在128k上下文下训练速度比全注意力快1.6×/层，精度完全持平

> 最值得记住的一句话：超长上下文下稀疏注意力的核心瓶颈是索引而非注意力计算本身，用语义聚类替代全key扫描是突破性能瓶颈的核心方向
