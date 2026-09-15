---
title: 'Realtime-Venus: A full-duplex interaction system with asynchronous delegation'
title_zh: Realtime-Venus：支持异步代理的全双工实时交互系统
authors:
- Ruixiang Zhao
- Hualei Wang
- Renhe Sun
- Enzhi Zhou
- Jincenzi Wu
- Xujie Song
- Kexin Shi
- Zihang Liu
- Pengcheng Zhu
- Jiayi Zhou
affiliations:
- Ant Group
- Tsinghua University
arxiv_id: '2609.13814'
url: https://arxiv.org/abs/2609.13814
pdf_url: https://arxiv.org/pdf/2609.13814
published: '2026-09-11'
collected: '2026-09-15'
category: Agent
direction: 全双工交互Agent · 异步任务代理
tags:
- Full-Duplex
- Asynchronous Delegation
- Multimodal Agent
- Speech Interaction
- Tool Augmented LLM
one_liner: 推出两款9B参数全双工交互模型，搭配异步执行框架，性能超越GPT-4o、Gemini 3.1 Live等SOTA
practical_value: '- 双循环 runtime 架构可直接复用在电商直播数字人、语音客服等实时交互Agent场景，前台保障低延迟响应，后台异步执行工具调用/商品查询，避免响应阻塞

  - 全双工交互控制逻辑（区分用户插话/反馈音/背景音）可迁移到语音客服、直播带货场景，提升用户打断时的交互自然度，降低误停/漏响应率

  - 无训练长视频记忆模块的relevance+novelty检索逻辑可复用在长会话用户行为理解、直播内容实时理解场景，无需额外训练即可扩展上下文窗口

  - 统一流序列化的多模态时间对齐方法可用于多模态推荐的用户实时行为建模，对齐用户语音/手势/浏览行为的时间戳，提升意图理解准确率'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有实时交互模型无法同时兼顾低延迟全双工对话与复杂任务执行，要么无法处理用户插话、背景音等复杂交互场景，要么调用工具时阻塞前台响应，无法满足直播、客服、智能助手等场景的自然交互需求。

### 方法关键点
- 双9B参数前端模型：Realtime-Venus-Omni支持音视频交互，Realtime-Venus-Audio支持纯语音交互，共享Omni-Flow架构，原生集成感知、对话控制、语音生成能力
- 双循环 runtime：前台交互循环负责低延迟实时响应，后台Harness框架异步执行工具调用、复杂推理任务，通过共享因果时间线对齐用户输入、模型输出、代理事件
- 无训练长视频记忆模块：通过运动预测门控过滤冗余帧，结合 relevance+novelty 检索召回历史内容，支持小时级视频理解，无需额外训练
- 训练数据管道：覆盖离线理解、全双工交互、异步代理三类场景共280万样本，联合监督交互控制、响应生成、代理请求三类输出

### 关键实验
对比GPT-4o、Gemini 3.1 Live、MiniCPM-o 4.5等SOTA模型：
- Omni模型在8个视频基准中6个登顶，StreamingBench达70.2%，Daily-Omni达81.3%
- Audio模型在MMAU（78.0%）、MMAU-Pro（63.2%）等4个音频基准登顶，VoiceBench AlpacaEval得分4.81持平最优
- 全双工测试中，Audio模型对用户插话响应率75%，在反馈音、他人对话、背景音场景下的对话续接率分别达97%、88%、86%，全面超过GPT-4o和Gemini 3.1 Live

### 核心结论
全双工交互的核心是把对话控制、响应生成、异步代理放在统一的因果时间线中建模，而非依赖独立的VAD、工具调用模块实现
