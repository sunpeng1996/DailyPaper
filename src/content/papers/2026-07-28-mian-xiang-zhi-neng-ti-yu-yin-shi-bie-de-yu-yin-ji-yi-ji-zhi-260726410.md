---
title: Voice Memory for Agentic Speech Recognition
title_zh: 面向智能体语音识别的语音记忆机制
authors:
- Chao-Han Huck Yang
- Zih-Ching Chen
- Piotr Zelasko
- Zhehuai Chen
- Jagadeesh Balam
- Boris Ginsburg
affiliations:
- NVIDIA
arxiv_id: '2607.26410'
url: https://arxiv.org/abs/2607.26410
pdf_url: https://arxiv.org/pdf/2607.26410
published: '2026-07-28'
collected: '2026-07-31'
category: Agent
direction: Agent 语音识别记忆机制优化
tags:
- VoiceAgent
- ASR
- MemoryMechanism
- Test-timeAdaptation
- InferenceOnly
- DomainAdaptation
one_liner: 提出仅推理的listener-thinker语音记忆架构，无需微调权重即可降低语音识别领域特定错误
practical_value: '- 可复用「score-gated异步更新只读记忆+推理时冻结模型决策」架构，落地电商语音导购、智能客服ASR纠错场景，无需微调大模型即可适配领域术语、品牌名等专属语料，避免过校正

  - 记忆文件跨模型可迁移的特性可直接复用，业务端可统一维护各垂类（美妆/3C/生鲜）纠错记忆库，适配不同大小的端侧/云侧ASR模型，降低多模型适配成本

  - 推理路径零新增参数的设计适合端侧语音交互场景，可迁移到IoT设备端语音搜索Query纠错、语音指令识别优化，无额外推理latency负担'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
当前ASR在干净语音下错误率已低至2%以下，但存在大量领域特定系统性错误，常规生成式纠错（GER）易过度校正破坏正确token，微调适配成本高、优化效果不可审计。
### 方法关键点
1. 提出listener-thinker拆分的仅推理Voice Memory机制，推理阶段冻结corrector读取单域记忆文件，逐句判断纠错或保留ASR 1-best结果
2. 异步侧用score-gated优化器仅接受严格提升验证集指标的有限编辑更新记忆，全程不修改模型权重，优化技能可审计、可跨模型迁移
### 关键结果
- 金融新闻场景过校正率从64%降至35%
- 10个HyPoradise域加权WER从8.36%降至7.52%，加3个ICL示例后可达7.47%，无数据集性能低于基线；航空指令场景WER从8.40%降至3.40%，CHiME-4远场噪声语音WER从12.69%降至10.46%
- 推理路径零新增参数，记忆可跨corrector家族迁移
