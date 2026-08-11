---
title: 'Beyond Naturalness: Probing Automated Text-To-Speech Evaluators on Linguistically
  Grounded Dimensions'
title_zh: 超越自然度：基于语言学维度的TTS自动评估器能力探测
authors:
- Oluwanifemi Bamgbose
- Simon Rosen
- Jash Shah
- Lindsay Devon Brin
- Hoang H Nguyen
- Anke Koelzer
- Rachel Hansen
- Tara Bogavelli
- Fanny Riols
affiliations:
- ServiceNow
arxiv_id: '2608.09930'
url: https://arxiv.org/abs/2608.09930
pdf_url: https://arxiv.org/pdf/2608.09930
published: '2026-08-10'
collected: '2026-08-11'
category: Eval
direction: TTS系统自动评估基准构建
tags:
- TTS
- Audio-LLM
- MOS
- Evaluation Benchmark
- Linguistic Annotation
one_liner: 拆解TTS自然度为10个语言学维度，构建首个维度级TTS元评估基准，揭示现有两类自动评估器的能力盲区
practical_value: '- 电商智能客服/直播数字人/商品语音介绍的TTS效果评估，可直接复用本文10维语言学标注框架，替代单一MOS打分，精准定位影响用户体验的语音问题根因

  - 用Audio-LLM做TTS自动评估时，需针对重音、断句、语调等不同语言学维度设计专用Prompt，不要使用通用Prompt避免漏检结构化语音错误

  - 业务上线前TTS效果验收，不能完全依赖自动MOS预测器，需补充人工抽查语言学维度错误，避免出现用户可感知的低级语音问题'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有TTS自动评估方法（MOS预测器、Audio-LLM评审）是否匹配人类感知尚不明确，单一的「自然度」整体打分无法定位具体语音错误，难以支撑业务级TTS效果的精细化优化。
### 方法关键点
将模糊的「自然度」指标拆解为覆盖语音声学、语义表达的10个语言学维度的标注体系，构建首个维度级TTS元评估基准，包含860条经专业语言学家标注的语音样本，对4款主流MOS预测器、4款Audio-LLM评审开展系统性基准测试。
### 关键结果
MOS预测器仅能有效评估声学信号质量，完全无法覆盖语言学维度的语音错误；Audio-LLM评审的维度识别能力强依赖Prompt设计，跨维度泛化性差，两类评估器均无法可靠覆盖全部10个语言学维度的结构化语音问题。
