---
title: 'HearInContext: A Benchmark for Implicit Context in Speech Recognition'
title_zh: HearInContext：面向语音识别隐式上下文的评测基准
authors:
- Yifan Gao
- Yao Tian
- Hongbin Suo
affiliations:
- OPPO AI Center, Beijing, China
arxiv_id: '2609.18680'
url: https://arxiv.org/abs/2609.18680
pdf_url: https://arxiv.org/pdf/2609.18680
published: '2026-09-16'
collected: '2026-09-17'
category: Other
direction: 语音识别 · 上下文消歧基准构建
tags:
- ASR
- Benchmark
- Implicit Context
- Fine-tuning
- Homophone Disambiguation
one_liner: 构建中英双语语音识别隐式上下文消歧基准，验证微调可大幅提升隐式上下文召回且不损通用性能
practical_value: '- 语音交互类电商Agent可复用隐式上下文消歧思路，利用对话历史语义解决同音词识别误差，提升用户Query理解准确率

  - 微调ASR模型时可参考该论文的控制变量方法，在提升场景特定任务准确率的同时，保证通用ASR性能几乎无衰减

  - 电商语音搜索场景可借鉴同音词测试用例构建方法，建立适配业务场景的语音识别效果评测集'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有语音识别上下文消歧研究多聚焦显式上下文提示，缺乏专门针对隐式语义上下文（未直接提及目标词）的标准化评测基准，难以量化模型利用对话历史语义解决同音歧义的能力。
### 方法关键点
构建包含3764个同音词语义测试用例的中英双语基准HearInContext，配对相同合成语音与不同语义导向的助手回复，设置无上下文、无关上下文对照组，区分隐式上下文（未提候选词）、显式上下文（直接给出目标词）两种评测场景。
### 关键结果数字
微调Qwen3-ASR-1.7B后，中英隐式上下文目标召回分别提升11.0、11.5个百分点，同时AISHELL-1、LibriSpeech上的CER/WER绝对变化低于0.1个百分点，增益还可迁移到微调未覆盖的显式场景与真实录音的普通话热词识别任务。
