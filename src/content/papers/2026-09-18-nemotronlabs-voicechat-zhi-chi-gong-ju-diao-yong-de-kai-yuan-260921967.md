---
title: 'NemotronLabs VoiceChat: An Open Full-duplex Speech-to-Speech Model with Tool
  Calling Capabilities'
title_zh: NemotronLabs VoiceChat：支持工具调用的开源全双工语音转语音模型
authors:
- Jagadeesh Balam
- Travis Bartley
- Edresson Casanova
- Sanjay Chauhan
- Chen Chen
- Zhehuai Chen
- Zijia Chen
- Francesco Ciannella
- Slyne Deng
- Mikyas Desta
affiliations:
- NVIDIA
arxiv_id: '2609.21967'
url: https://arxiv.org/abs/2609.21967
pdf_url: https://arxiv.org/pdf/2609.21967
published: '2026-09-18'
collected: '2026-09-21'
category: Agent
direction: 语音交互Agent · 全双工流式架构
tags:
- Speech-to-Speech
- Full-Duplex
- Tool Calling
- Streaming Architecture
- Open Source
one_liner: 提出统一架构开源全双工语音转语音模型，原生支持工具调用，实时交互效果领先同类开源系统
practical_value: '- 开发电商语音客服Agent可复用其流式多输出分支架构，并行生成回复文本、结构化工具调用指令，同时做用户语音增量转写，降低端到端延迟

  - 全双工的中断处理、后向通道恢复逻辑可直接复用在直播语音互动、电话外呼营销场景，提升交互自然度

  - 原生工具调用能力可对接电商商品查询、订单查询、售后受理等内部工具，实现语音服务端到端闭环'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有级联ASR-LLM-TTS语音Agent多为半双工，依赖VAD检测用户停止说话才响应，延迟高、交互不自然，缺乏原生工具调用能力，无法满足实时对话需求。
### 方法关键点
采用统一流式架构，整合流式语音编码器、Decoder-only LLM，新增3类并行输出分支：① Agent回复文本+结构化工具调用流；② 辅助RNN-T分支做用户语音增量转写；③ 流式TTS解码器，实现边听、边转写、边推理、边调用工具、边输出语音的全双工能力。
### 关键结果数字
Full-Duplex-Bench 1.0上用户中断后接管率100%，中断后回复质量4.33/5，为开源系统最低停顿接管率；1.5版本bench上用户反馈后恢复响应率93%；3.0版本bench上工具选择F1达82.5%，VoiceBench归一化平均得分55.1。
