---
title: 'MEUSLI: a Multilingual Projector for LLM-based ASR and Beyond'
title_zh: MEUSLI：面向LLM驱动ASR及下游任务的多语言投影器
authors:
- Lorenzo Concina
- Seraphina Fong
- Marco Matassoni
- Alessio Brutti
affiliations:
- Fondazione Bruno Kessler
- University of Trento
arxiv_id: '2607.22100'
url: https://arxiv.org/abs/2607.22100
pdf_url: https://arxiv.org/pdf/2607.22100
published: '2026-07-24'
collected: '2026-07-27'
category: Multimodal
direction: 多模态SpeechLLM · 跨语言投影器
tags:
- Multilingual-LLM
- SpeechLLM
- ASR
- Whisper
- Projector
- Low-Resource-Language
one_liner: 推出开源多语言投影器MEUSLI，连接Whisper与多语言LLM，支持28种欧洲语言ASR及下游语音任务
practical_value: '- 搭建跨语言语音交互Agent时，可复用MEUSLI轻量投影器架构，基于Whisper+开源多语言LLM快速实现端到端语音理解pipeline，规避级联ASR的误差传播问题

  - 适配小语种语音类业务（如跨境电商小语种语音搜索）时，可借鉴其持续学习扩展新语言的方案，仅需少量标注即可快速完成新语种适配

  - 落地语音下游任务（如语音内容主题识别、多语言语音转营销文案）时，可直接复用预训练MEUSLI投影器，仅需少量任务微调即可上线，大幅降低训练成本'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有连接语音编码器与LLM的轻量投影器大多仅支持少数语言甚至仅限英语，无法满足多语言语音理解需求，传统级联ASR-LLM架构存在误差传播、延迟高、丢失副语言信息等问题。
### 方法关键点
开源多语言投影器家族MEUSLI对接Whisper语音编码器与开源多语言LLM，将声学特征映射为LLM可接收的token级嵌入；配套持续学习策略支持快速扩展训练集外的新语言，可复用至ASR之外的多类语音任务。
### 关键结果
支持28种欧洲语言的端到端开源ASR，在高、低资源语言上均达到优异效果；扩展至多语言语音翻译、主题识别任务时，单语言仅需数小时任务级标注即可落地，为开源SpeechLLM提供可扩展的多语言基座。
