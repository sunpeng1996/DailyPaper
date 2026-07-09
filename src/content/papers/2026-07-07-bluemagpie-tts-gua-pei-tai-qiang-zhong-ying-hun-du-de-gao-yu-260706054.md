---
title: 'BlueMagpie-TTS: A Token-Efficient Tokenizer, Language Model, and TTS for Taiwanese-Accent
  Code-Switching Speech'
title_zh: BlueMagpie-TTS：适配台腔中英混读的高效Token化语音合成系统
authors:
- Ho Lam Chung
- Bo-Xuan Zheng
- Cheng-Chieh Huang
- Cheng-Han Chang
- Jung-Ching Chen
- Lok-Lam Ieong
- Ting-Lin Hsiao
- Yu-Cheng Lee
- Yi-Hsin Chung
- Yu-Kai Guo
affiliations:
- National Taiwan University
arxiv_id: '2607.06054'
url: https://arxiv.org/abs/2607.06054
pdf_url: https://arxiv.org/pdf/2607.06054
published: '2026-07-07'
collected: '2026-07-09'
category: Other
direction: 语音合成 · 区域场景专项适配
tags:
- TTS
- BPE Tokenizer
- Code-Switching
- Traditional Chinese
- PEFT
one_liner: 自底向上优化文本端适配台湾场景，实现高准确率的台腔中英混读TTS
practical_value: '- 面向特定区域/细分场景的文本任务，可优先自底向上优化Tokenizer：用区域/领域专属语料训练byte-level BPE，既能降低token率压缩推理成本，还能提升下游任务准确率

  - 跨模态生成任务可复用成熟预训练模态基座，仅通过可学习桥接层适配新的前端语义模型，无需全量微调基座，大幅降低训练算力开销

  - 区域化语音交互场景（如台港澳地区电商智能客服、语音导购）可直接参考该文本端适配思路，快速优化现有TTS的口音、中英混读效果'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有开源TTS对台腔普通话适配性差，默认口音不符合本地习惯，Tokenizer对台湾常用文本切分过碎，中英混读边界发音准确率低，核心根因是文本侧未适配台湾本地场景。

### 方法关键点
1. 基于台湾本地语料训练byte-level BPE的PangolinTokenizer，在9个对比Tokenizer中token率最低（0.485 tokens/字符）且词表最小；
2. 基于该Tokenizer训练10亿参数繁体中文LLM Barbet作为文本语义前端，14项任务评测在同量级公开模型中排名第一；
3. 通过可学习桥接层将Barbet对接预训练VoxCPM2声学基座，固定声学基座参数仅微调桥接层。

### 关键结果
1000句台湾本地测试集上，CER从11.45%降至4.81%，WER从14.83%降至5.36%，相对降幅分别达58.0%、63.9%；500句盲测中65.6%的听众更偏好该系统。
