---
title: 'OneStreamer: Unifying Perception, Memory, and Proactive Response in Streaming
  Video Interaction'
title_zh: OneStreamer：流媒体视频交互中感知、记忆与主动响应的统一框架
authors:
- Xiangyu Zeng
- Yuandong Yang
- Zhiqiu Zhang
- Yuhan Zhu
- Xinhao Li
- Qingyi Si
- Dingyu Yao
- Changlian Ma
- Haoran Chen
- Xinyu Chen
affiliations:
- NJU
- PJLAB
- JD
- SJTU
- USTC
arxiv_id: '2610.01762'
url: https://arxiv.org/abs/2610.01762
pdf_url: https://arxiv.org/pdf/2610.01762
published: '2026-09-30'
collected: '2026-10-03'
category: LLM
direction: 流式视频LLM · 主动记忆与响应
tags:
- Streaming-LLM
- Multimodal-LLM
- Memory-Mechanism
- Proactive-Response
- Video-Dataset
one_liner: 提出统一主动生成框架与百万级数据集，实现流式视频LLM感知记忆响应协同
practical_value: '- PHCM分层字幕记忆机制可迁移到长会话推荐Agent，将用户历史交互生成结构化语义记忆替代原始行为特征回放，降低KV cache占用同时提升历史召回准确率

  - PSTL状态迁移学习方法可复用在实时流推荐场景，仅对状态变化节点做监督，降低标注成本的同时提升等待/响应状态判断准确率

  - 流式数据合成pipeline可用来构造电商直播场景的QA数据集，对齐直播流内容与观众咨询的时机、内容，优化直播导购Agent的响应及时性'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
流式视频LLM需提前留存潜在关联证据，在证据充足时主动响应，核心痛点是构建可复用事实记忆的同时不损害实时感知性能。
### 方法关键点
1. 提出Proactive Hierarchical Caption Memory (PHCM)，生成带时间戳的局部细节字幕与已完成事件摘要，推理时用生成的记忆替代历史视觉特征回放，无需重算历史特征；
2. 提出Proactive State Transition Learning (PSTL)，仅选取代表性的状态变化/持续token做监督，缓解等待状态样本占比过高的问题；
3. 构建流式数据合成pipeline，生成包含100w+样本的OneStreamer-1M数据集，覆盖多类流式交互任务。
### 关键结果
4B参数模型在8个流式视频理解基准上全部取得SOTA；保留生成字幕可提升历史QA效果且不降低实时感知性能；PSTL仅监督27.5%的标注状态token，性能优于稠密状态监督。
