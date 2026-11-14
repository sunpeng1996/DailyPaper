---
title: 'Beyond Word Error Rate: A Failure Taxonomy of Streaming Dictation ASR'
title_zh: 《超越词错误率：流式听写语音识别系统的错误分类体系》
authors:
- Harras Mansoor
- Muhammad Wisal
- Hassan Bhatti
- Masood Shakir
affiliations:
- heylemon.ai
arxiv_id: '2611.16919'
url: https://arxiv.org/abs/2611.16919
pdf_url: https://arxiv.org/pdf/2611.16919
published: '2026-11-12'
collected: '2026-11-14'
category: Eval
direction: 流式ASR评测 · 错误分类体系构建
tags:
- ASR
- Streaming Dictation
- WER
- Error Taxonomy
- System Evaluation
one_liner: 构建流式听写ASR错误分层分类体系，对比11款系统揭示同WER下实际错误表现的显著差异
practical_value: '- 搭建语音交互类Agent（电商语音导购、语音搜索助手等）时，不能仅以WER为选型指标，需针对低语、背景噪音、多语言混合等实际用户场景做专项错误测试，避免指标好看但实际体验差

  - 部署流式ASR服务时，谨慎使用默认VAD（语音活动检测）模块，针对低语等弱语音场景可降低VAD阈值或替换适配VAD，可大幅降低漏识别率

  - 多语言混合场景的ASR部署，不要固定单一语言选项，开启多语言识别模式可将非预期语种内容的漏识别率从80%+降至40%以内'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有ASR系统通常用去格式后的离线WER作为核心对比指标，但流式听写场景下用户需直接修正生成文本，WER无法反映实际错误类型和用户体验差异。

### 方法关键点
构建4层级错误分类体系（识别错误、输出格式错误、语言处理错误、自部署模型音频前置丢弃错误），针对11款主流ASR系统，测试覆盖单语言安静/有风扇噪音/低语场景、11种其他语言/方言、400条双语言混合流式语音样本，逐样标注错误。

### 关键结果数字
① 安静英语下WER接近的Zoom Scribe（7.4%）和OpenAI GPT-Live-Transcribe（7.3%），低语场景WER分别达34.7%/8.8%；② 默认VAD下Qwen3-ASR低语漏识别率32%，放松VAD后降至6%；③ 单英语模式下Gemini/Deepgram/自部署Whisper双语言样本非英语内容漏识别率86-99%，开多语言后降至33-46%；④ 搭配Silero VAD会将Whisper低语WER从10.1%抬升至51.4%。
