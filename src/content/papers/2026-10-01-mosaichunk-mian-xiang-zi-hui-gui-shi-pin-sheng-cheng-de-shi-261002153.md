---
title: 'MosaiChunk: Compositing Spatio-Temporal Memory for Autoregressive Video Generation'
title_zh: MosaiChunk：面向自回归视频生成的时空记忆组合机制
authors:
- Yiwen Zhang
- Haocheng Xi
- Michael Tian-Yue Liu
- Alexei A. Efros
- Hadar Averbuch-Elor
- Qianqian Wang
- Haiwen Feng
affiliations:
- Cornell University
- University of California, Berkeley
- Harvard University
- Impossible, Inc.
arxiv_id: '2610.02153'
url: https://arxiv.org/abs/2610.02153
pdf_url: https://arxiv.org/pdf/2610.02153
published: '2026-10-01'
collected: '2026-10-03'
category: Multimodal
direction: 多模态视频生成 · KV缓存优化
tags:
- KV Cache
- Long-Context
- Video Generation
- Spatio-Temporal Memory
- Autoregressive Generation
one_liner: 提出轻量时空KV选择机制MosaiChunk，提升长时序视频生成的物体复现一致性
practical_value: '- 长时序生成任务可复用「冻结基座+轻量路由选历史KV」架构，无需微调大模型即可提升上下文一致性，适配电商商品生成视频、长直播剪辑等场景

  - 非连续历史KV可直接被冻结自回归模型消费的结论，可迁移到长对话Agent、生成式推荐长序列用户行为建模，降低推理显存开销

  - 固定内存预算下的KV选择思路，可优化生成式推荐、搜索Query联想的KV cache策略，提升长会话下的生成一致性'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
长时序自回归生成受有限上下文窗口约束，物体/场景滑出窗口后细粒度视觉细节易丢失，复现时易产生幻觉，现有滑动窗口、整块KV检索方案的复现一致性表现不佳。

### 方法关键点
1. 基于「冻结的自回归视频生成器可直接消费非连续历史KV恢复对应视觉内容」的核心观察，仅训练轻量路由模块，基座完全冻结，落地成本极低；
2. 提出MosaiChunk时空记忆机制，在固定活跃内存预算下，跨时空筛选历史KV条目拼接为记忆mosaic输入生成器；
3. 开源RememBench长时序复现基准，覆盖文本驱动、相机驱动视频生成两类测试子集。

### 关键结果
相同内存预算下，MosaiChunk在文本到视频、图像到视频两类场景的物体复现一致性，均显著优于滑动窗口推理、整块KV检索基线。
