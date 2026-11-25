---
title: Efficient Video Retrieval Augmented Generation via Token Allocation
title_zh: 通过令牌分配实现高效视频检索增强生成
authors:
- Ayush Barik
- Fan Lai
- Francis Y. Yan
affiliations:
- University of Illinois Urbana-Champaign
arxiv_id: '2611.32938'
url: https://arxiv.org/abs/2611.32938
pdf_url: https://arxiv.org/pdf/2611.32938
published: '2026-11-24'
collected: '2026-11-25'
category: RAG
direction: 视频RAG · 令牌分配效率优化
tags:
- RAG
- Token Allocation
- Video Understanding
- VLM
- KV Cache
one_liner: 提出即插即用的Lembas框架，将视频RAG转化为共享预算下的令牌分配优化问题
practical_value: '- 电商短视频/直播理解、商品视频问答场景可直接复用Lembas的令牌分配逻辑，在固定VLM推理成本下提升多模态RAG准确率，平衡内容覆盖度与细节粒度

  - 多轮对话场景的KV cache增量复用方法可直接迁移，按离线预计算的查询无关令牌排名补充缺失令牌，无需全量重算prefill，可降低1.7~17.3倍多轮推理计算量，适配电商智能客服、直播导购多轮交互场景

  - 迭代注水算法的边际收益优化思路可迁移至多模态生成式推荐场景，给图文/视频等不同模态候选分配LLM上下文token时，兼顾相关性、边际收益递减与内容冗余，提升生成效率与效果'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
长视频理解场景下全量处理所有帧会超出VLM上下文窗口，带来极高推理成本；现有视频RAG方案仅做帧选择或统一令牌压缩，忽略单证据内部令牌边际收益递减、多证据间内容冗余的问题，无法在固定令牌预算下最大化推理准确率。
### 方法关键点
- 提出即插即用框架Lembas，将视频RAG转化为帧与字幕的共享令牌预算分配问题，用凹有理函数拟合令牌价值递减规律，同时引入冗余惩罚项降低相似内容的令牌分配权重
- 采用迭代注水算法求解最优分配，可证明收敛到连续松弛问题的全局最优，单请求仅需数十毫秒，overhead远低于VLM推理耗时
- 多轮对话场景支持两大优化：离线预计算查询无关的帧令牌注意力排名，仅预填充KV cache缺失的令牌；复用前序轮次VLM的注意力权重优化证据相关性，无额外计算开销
### 关键实验
在MLVU、LongVideoBench、Video-MME三个单轮视频QA数据集、MT-Video-Bench多轮数据集上测试，对比Top-K、Q-Frame、QuoTA等SOTA基线：同计算量下单轮准确率最高提升7.2个百分点，长视频子集准确率提升8.1个百分点；多轮场景下准确率提升0.3~1.5个百分点，同时TFLOPs降低1.7~17.3倍。
### 核心结论
令牌分配的核心是让每个令牌的边际收益相等，而非按相关性比例分配，才能在固定预算下实现效率最大化。
