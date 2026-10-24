---
title: 'Measuring the Verifier''s Floor: How Much Apparent Rare-Word Text-to-Speech
  Error Is ASR Error?'
title_zh: 验证基线测量：TTS稀有词表观错误中ASR错误的占比评估
authors:
- Kirill Borodin
- Vasilii Kudryavtsev
- Nikita Vasiliev
- Grach Mkrtchian
affiliations:
- BitmanagerAI
- lab260
arxiv_id: '2610.31470'
url: https://arxiv.org/abs/2610.31470
pdf_url: https://arxiv.org/pdf/2610.31470
published: '2026-10-22'
collected: '2026-10-24'
category: Eval
direction: 语音系统评估 · 错误率校准
tags:
- ASR
- TTS
- WER
- Rare Word
- Evaluation
- Error Calibration
one_liner: 量化TTS ASR回测评估中ASR自身的稀有词识别误差基线，优化TTS错误评估方法
practical_value: '- 开发语音交互类Agent（如电商语音导购、语音搜索）时，评估效果需拆分ASR自身识别误差与上游生成模块误差，避免归因错误

  - 评估稀有实体（如长尾商品名、小众品牌名）的语音交互准确率时，可引入多ASR交叉验证，降低单模型基线误差对评估结果的干扰

  - 对低置信度的单模型评估结论，需补充人工校验兜底，避免误判业务迭代的真实效果'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有TTS系统普遍采用ASR回转录计算WER的评估方案，最终误差包含ASR自身的识别错误，尤其稀有词场景下ASR基线误差未知，无法准确衡量TTS的真实生成效果。

### 方法关键点
选取LibriSpeech、FLEURS两类公开数据集，对同一测试句分别输入人类原声录音与TTS生成音频至多组不同架构的ASR系统，以人类录音的ASR识别误差作为基线，校准TTS的表观错误率。

### 关键结果
单评估用ASR对人类语音中的极稀有词漏识别率达33-67%，3类ASR的共同漏识别率为22-42%；引入2种不同架构ASR做交叉校验后，LibriSpeech极稀有词的TTS表观错误率从10-13%降至3-5%；直接过滤ASR对人类语音漏识别的词会引入显著偏差，约一半保留误差会被其他ASR推翻，剩余判定误差中近半数为拼写变体，仍需人工听测校验。
