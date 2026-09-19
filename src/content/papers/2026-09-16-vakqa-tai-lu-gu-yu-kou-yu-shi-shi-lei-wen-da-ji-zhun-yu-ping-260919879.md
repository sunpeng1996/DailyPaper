---
title: 'VākQA: A Benchmark and Evaluation Study for Telugu Spoken Factoid Question
  Answering'
title_zh: VākQA：泰卢固语口语事实类问答基准与评估研究
authors:
- Bhavana Akkiraju
- Ravi Sastry Kolluru
- Sri Charan D
- Srihari Bandarupalli
- Santosh Kesiraju
- Anil Vuppala
affiliations:
- International Institute of Information Technology Hyderabad
- Brno University of Technology
arxiv_id: '2609.19879'
url: https://arxiv.org/abs/2609.19879
pdf_url: https://arxiv.org/pdf/2609.19879
published: '2026-09-16'
collected: '2026-09-19'
category: Eval
direction: 低资源语言口语问答基准与评估
tags:
- SpokenQA
- LLM-as-a-judge
- Low-resource-language
- Benchmark
- Evaluation
one_liner: 发布含2001个问答对的泰卢固语口语问答基准，验证该场景自动评估方法可靠性
practical_value: '- 做多语言/小语种语音搜索、口语客服类业务时，可复用其LLM-as-a-judge校验框架，优先选闭源大模型作为评估器，减少表面形式差异导致的误判

  - 语音问答链路若采用ASR+MT级联方案，需提前做错误累加效应的量化评估，高优场景可考虑端到端方案避免误差传导

  - 小语种本土化问答/推荐业务不要直接依赖翻译语料，需保留原生表达的文化特性，避免核心信息丢失'
score: 4
source: huggingface-daily
depth: abstract
---

### 动机
现有问答技术及基准多面向英语等高资源语言，泰卢固语口语问答（SQA）领域无公开可用基准，且该场景下自动评估方法的可靠性未被量化。
### 方法关键点
构建VākQA公开基准，覆盖6个领域共2001个事实类问答对，包含2.53小时语音音频、双语转录结果及人工校验参考答案；先对比不同自动评估方案与人工判断的一致性完成评估框架校验，再基于该框架测试闭源/开源模型在不同输入模态、语言、领域下的表现。
### 关键结果数字
Gemini-as-a-judge最贴近人工评分，但严格程度存在不一致；开源评估器会系统性惩罚与参考答案表面形式不同的正确泰卢固语答案；级联ASR-MT链路误差会逐步累加，语音输入的语音混淆会改变问题语义，泰卢固语原生表达的文化特性在翻译中会丢失。
