---
title: 'Your Home Remembers: A Voice-Enabled Household Memory Assistant for Conversational
  Retrieval'
title_zh: 面向会话检索的语音赋能家庭记忆助手
authors:
- Aleix Sant
- Jordi Luque
- Fernando López
- Pablo Gómez
- Carlos Escolano
affiliations:
- Telefónica Innovación Digital, Scientific Research
- Universitat Politècnica de Catalunya
- Universidad Autónoma de Madrid
arxiv_id: '2610.30895'
url: https://arxiv.org/abs/2610.30895
pdf_url: https://arxiv.org/pdf/2610.30895
published: '2026-10-22'
collected: '2026-10-24'
category: Agent
direction: 语音Agent · 会话记忆RAG检索
tags:
- RAG
- Voice Agent
- Conversational Memory
- Speaker Diarisation
- On-device AI
one_liner: 提出模块化可配置的语音家庭助手方案，基于RAG实现家庭会话存储与自然语言问答检索
practical_value: '- 会话类Agent可复用「VAD+说话人分野+轮次感知分段+时间戳索引」的语音会话结构化处理流程，提升非结构化语音数据的检索准确率

  - 多组件依赖的Agent架构可参考可编排层设计，支持ASR、Embedding、LLM等模块的灵活替换/灰度切换，降低迭代成本

  - 面向家庭场景的语音交互Agent可落地端侧唤醒词检测+VAD query捕获方案，实现自然交互同时降低云端算力消耗'
score: 7
source: arxiv-cs.HC
depth: abstract
---

### 动机
家庭日常会话包含大量未被书面记录的私有信息（如用药说明、物品位置、约定安排），极易遗忘错记，传统智能助手依赖预训练参数知识，无法回答这类私有场景问题。
### 方法关键点
1 采用模块化可编排架构，ASR、说话人分野、Embedding、LLM等组件可独立替换配置，整体部署于安卓平板设备；
2 端侧实现唤醒词检测+VAD语音捕获，支持免手交互，音频分片处理后转写为带说话人标识、会话轮次、时间戳的结构化段落，存入向量库索引；
3 问答环节采用RAG pipeline召回高相关会话段落，基于召回内容生成答案，同时支持会话源时间戳溯源查看。
### 结果
已实现全链路可用的交互流程，覆盖会话录制、管理、问答、溯源全功能。
