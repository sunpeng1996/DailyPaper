---
title: 'Who Says What: Symbolic Trimodal Binding Mechanisms in Audio-Visual LLMs'
title_zh: 视听大语言模型符号三模态绑定机制：解决“谁在说什么”问题
authors:
- Jihoo Jung
- Youngjoon Jang
- Joon Son Chung
affiliations:
- KAIST
- VGG, University of Oxford
arxiv_id: '2609.31193'
url: https://arxiv.org/abs/2609.31193
pdf_url: https://arxiv.org/pdf/2609.31193
published: '2026-09-25'
collected: '2026-09-28'
category: Multimodal
direction: 多模态大模型 · 三模态绑定优化
tags:
- AVLLM
- Multimodal Alignment
- Symbolic Binding
- Active Speaker Detection
- Prompt Engineering
one_liner: 揭示AVLLM三模态绑定失效根因，提出基于ASD的免训练提示方法，提升多说话人视频推理性能
practical_value: '- 短视频/直播内容理解场景（比如主播话术归因、商品口播内容打标）可复用免训练ASD提示思路，无需全量微调即可快速提升音视频模态对齐准确率

  - 多模态Agent处理多说话人场景（比如直播带货用户-主播交互意图识别、多人访谈内容结构化）可引入符号化模态变量编码，降低跨模态关联误差

  - 多模态模型性能优化可先定位失效根因（比如音视频错位而非文本语义问题），再通过提示工程/300步以内轻量微调低成本优化，无需盲目扩充训练数据'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有Audio-Visual LLMs（AVLLM）对包含多说话人对话的视频推理能力不足，无法精准完成“谁在说什么”的文本-音频-视觉三模态绑定，是多模态内容理解的核心瓶颈。
### 方法关键点
1. 定位AVLLM内置的符号三模态绑定机制：将音频编码为对应时间话语序列的符号变量、视觉编码为对应空间实体坐标的符号变量，在抽象空间完成跨模态关联
2. 发现三模态绑定失效的核心诱因是音视频连接错位，而非语义理解误差
3. 提出基于现成Active Speaker Detection（ASD）模型的提示方案：给活跃说话人叠加视觉bounding box，支持免训练直接优化，也可结合少于300步的轻量微调拓展泛化性
### 关键结果
- 免训练方案在4个对话类基准上直接获得性能提升
- 300步以内轻量微调后，在3个通用AV基准上也获得稳定增益
