---
title: 'AgSpec: Pushing the Limits of Retrieval-Based Speculative Decoding in Coding
  Agent Pipelines'
title_zh: AgSpec：面向编码Agent流水线的检索式投机解码优化框架
authors:
- Sumin Lee
- Sukmin Cho
- Suengjae Lim
- Youngjin Kwon
affiliations:
- KAIST
arxiv_id: '2610.01108'
url: https://arxiv.org/abs/2610.01108
pdf_url: https://arxiv.org/pdf/2610.01108
published: '2026-10-01'
collected: '2026-10-02'
category: Agent
direction: Agent流水线 · 投机解码加速
tags:
- Speculative Decoding
- Retrieval Augmented
- Coding Agent
- LLM Inference
- Multi Agent
one_liner: 基于感知Agent的语料设计与自适应长度控制，无侵入提升检索式投机解码吞吐量
practical_value: '- 可复用三级语料设计思路：针对电商/推荐Agent构建会话历史、用户/场景专属物料、全局知识库三级检索库，同时将物料按Agent输出格式预处理后索引，解决检索内容与输出格式不匹配的问题，比如给商品文案加统一prompt前缀再入库。

  - 自适应生成长度控制可直接迁移：对不同角色的业务Agent（选品Agent、文案生成Agent、审核Agent等）离线 profiling 最优生成长度上限，再结合实时校验反馈动态调整长度，大幅减少无效生成的算力浪费。

  - 无侵入优化思路适合业务快速落地：不需要修改底层检索/推理引擎代码，仅靠上层语料策略和长度控制即可实现提效，可快速对接现有vLLM等推理服务框架。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有检索式投机解码(SD)在编码Agent流水线中表现受限：一是可复用文本要么未纳入语料库，要么存储格式与Agent实际输出格式不匹配；二是固定草稿长度策略忽略了不同Agent的接受长度差异，以及长度随交互轮次的动态漂移，最终导致解码吞吐量低、多轮交互下用户等待时间过长。

### 方法关键点
- 编码Agent感知的检索：构建三级分层语料库，会话语料存储全会话轨迹跨调用复用，工作区语料按Agent输出格式索引仓库文件适配生成格式，全局语料存储静态参考文本；匹配优先级遵循会话>工作区>全局，全局匹配需超过本地匹配阈值δ才生效。
- Agent感知的草稿长度控制：离线 profiling 每个Agent的接受长度分布，设定单Agent专属的草稿长度上限；在线根据校验反馈动态调整长度缩放因子，平衡接受率和无效验证开销。
- 完全兼容SAM-Decoding、SuffixDecoding等现有检索引擎，无需修改底层逻辑即可接入。

### 关键实验
在SWE-bench、TeamBench两个仓库级多Agent编码基准测试，对比AR解码、5种检索式SD方法、EAGLE-3：batch=1时吞吐量最高达AR的4.37倍，batch=16时最高达4.76倍，相比最优 baseline 平均吞吐量提升18%；在无仓库、单Agent场景下同样有效，LiveCodeBench上吞吐量最高达AR的7.94倍。

### 最值得记住的一句话
针对Agent场景的检索式投机解码优化，核心是适配Agent流水线的结构特征，而非仅优化底层检索匹配逻辑。
