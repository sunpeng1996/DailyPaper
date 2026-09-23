---
title: Spoken Language Models that Think Aloud
title_zh: 《支持有声思考的口语大语言模型》
authors:
- Junyi Ao
- Kainan Peng
- Mingbo Ma
- Shun Zhang
- Zhenyu Tang
- Xutai Ma
- Xiang Li
- Yinghao Li
- Yuancheng Wang
- Zhizheng Wu
affiliations:
- Meta Superintelligence Labs
- The Chinese University of Hong Kong, Shenzhen
arxiv_id: '2609.26488'
url: https://arxiv.org/abs/2609.26488
pdf_url: https://arxiv.org/pdf/2609.26488
published: '2026-09-22'
collected: '2026-09-23'
category: Reasoning
direction: LLM推理优化 · 实时口语交互场景
tags:
- Spoken LLM
- Chain-of-Thought
- Asynchronous Reasoning
- Human-Computer Interaction
- Thinker-Talker Architecture
one_liner: 提出异步有声思考Thinker-Talker架构，解决口语大模型CoT推理长静默问题且不损失答案精度
practical_value: '- 双异步流架构可直接复用在电商语音客服、直播数字人等实时交互Agent场景，用过渡话术填补推理等待间隙，消除用户静默焦虑

  - 动态流调度策略可迁移到生成式推荐、RAG问答的流式响应场景，优先输出进度类提示语，不降低最终输出质量的前提下提升感知速度

  - 轻量增量输出分支的设计思路可降低实时流式交互系统的算力开销，适配高并发的C端服务场景'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
直接将Chain-of-Thought（CoT）推理能力应用于Spoken Language Model（SLM）时，串行「先思考后输出」范式会产生长静默间隔，严重破坏实时口语交互的用户体验。

### 方法关键点
1. 基于Thinker-Talker架构搭建异步有声思考框架，拆分两路独立流：主推理流负责完整逻辑推导，轻量级有声思考流基于用户输入和动态演化的推理状态生成短的任务相关进度话术；
2. 设计动态平衡策略运行时协调双流，自动触发额外有声话术填补静默间隙，当最终响应就绪时直接取消待输出的过渡话术。

### 关键结果
在口语推理、问答基准数据集上，相比串行先想后说基线，用户可感知静默时长大幅降低，同时答案精度与基线完全持平。
