---
title: 'IndicTalk: A Large-Scale Persona-Based Multilingual Conversational Corpus
  for Indic Languages'
title_zh: IndicTalk：面向印度语族的大规模人设驱动多语言对话语料库
authors:
- Sahil Deepak Gawande
- Mayank Singh
affiliations:
- Lingo Research Group
- IIT Gandhinagar
arxiv_id: '2607.23242'
url: https://arxiv.org/abs/2607.23242
pdf_url: https://arxiv.org/pdf/2607.23242
published: '2026-07-24'
collected: '2026-07-30'
category: LLM
direction: 多语言LLM · 对话语料自动化构建
tags:
- Multilingual-LLM
- Conversational-Corpus
- Code-Mixing
- Low-Resource-NLP
- Data-Generation
one_liner: 构建覆盖9种印度语族的132万+条码混合多轮对话开源语料
practical_value: '- 低资源小语种对话Agent开发可复用「真实事件锚定+人设条件生成+自动质量校验」的自动化语料生产pipeline，降低标注成本

  - 面向印度市场的电商客服Agent、多语言推荐话术生成场景，可直接用该语料做LoRA微调，提升码混合交互适配性

  - 跨语言搜索推荐的Query理解模块可基于该语料学习码混合表达模式，优化印度用户混合输入的意图识别准确率'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
印度语族用户日常普遍混合使用英语与本地语言、原生/罗马化双拼写，现有高质量多语言码混合对话语料稀缺，无法支撑相关对话系统开发。
### 方法关键点
采用全自动化pipeline生成语料：1）锚定真实新闻事件保证内容合理性；2）基于多语言LLM生成人设约束的多轮对话；3）配套自动质量校验流程过滤低质量数据。
### 关键结果
覆盖9种印度语族的18种语言变体，累计132.86万+条事件grounded多轮对话，经语言学、自动+人工多维度评估验证，对话流畅、码混合模式贴合真实用户习惯，已开源至Hugging Face。
