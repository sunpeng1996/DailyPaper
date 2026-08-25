---
title: Better Retrieval, Worse Robustness:How Multi-hop RAG Amplifies Upstream ASR
  Errors
title_zh: 更好的检索，更差的鲁棒性：多跳RAG如何放大上游ASR错误
authors:
- Zhenghua Bao
affiliations:
- Continuum AI
arxiv_id: '2608.22872'
url: https://arxiv.org/abs/2608.22872
pdf_url: https://arxiv.org/pdf/2608.22872
published: '2026-08-23'
collected: '2026-08-25'
category: RAG
direction: 多跳RAG · 语音场景鲁棒性优化
tags:
- RAG
- Multi-hop RAG
- ASR
- Robustness
- Speech QA
one_liner: 实证发现多跳RAG的实体图链接、迭代改写扩展会放大上游ASR转录错误 降低语音场景鲁棒性
practical_value: '- 语音交互类电商Agent/导购场景下，选用多跳RAG时需额外增加ASR实体纠错模块，避免上游错误被放大导致推荐/答复发错

  - 多跳RAG上线前需加入带口音、发音模糊等低质量ASR输入的鲁棒性测试，不能仅用干净文本评估效果

  - 若业务中ASR WER高于10%，优先选用简单朴素的RAG结构，避免复杂多跳扩展带来的性能跌幅超过绝对精度收益'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
语音交互场景下ASR转录错误是上游固定约束，此前未知多跳RAG的常见扩展（实体图链接、迭代改写）是吸收还是放大这类错误。
### 方法关键点
用神经TTS合成4种英语口音的语音输入，在3个多跳QA基准（HotpotQA、2WikiMultiHopQA、MuSiQue）上对比4种RAG配置与干净文本oracle的性能差异。
### 关键结果数字
1. 结构更复杂的RAG配置在ASR输入下绝对F1更高，但会放大错误：两者结合时，干净文本与最高WER口音的F1 gap比朴素密集检索高36-67%；
2. 核心失败原因是查询实体被破坏，占2WikiMultiHopQA退化案例的87-96%；
3. 轻量级表层修正仅能弥补小部分gap，实体错误仍会被下游检索结构放大。
