---
title: 'Unlocking Speech-Text Compositional Powers: Instruction-Following Speech Language
  Models without Instruction Tuning'
title_zh: 解锁语音-文本组合能力：无需指令微调的指令跟随语音大模型
authors:
- Congrui Du
- Yang Zhang
- Kaizhi Qian
- Shiyu Chang
affiliations:
- University of California, Santa Barbara, USA
- MIT-IBM Computing Research Lab, IBM Research, USA
arxiv_id: '2607.02214'
url: https://arxiv.org/abs/2607.02214
pdf_url: https://arxiv.org/pdf/2607.02214
published: '2026-07-02'
collected: '2026-07-03'
category: Training
direction: 语音LLM训练 · 跨模态能力免微调迁移
tags:
- Speech LLM
- Weight Fusion
- Instruction Following
- Cross Modality Transfer
- Efficient Training
one_liner: 通过权重融合策略仅用30k小时语音预训练得到无需指令微调的指令跟随语音大模型
practical_value: '- 多模态Agent开发可复用权重差融合技巧：无需额外做跨模态指令微调，仅对齐模态后融合文本指令微调模型与基座的权重差，即可快速继承指令跟随能力，大幅降低语音交互类Agent的训练成本

  - 电商语音场景落地可参考该训练范式：语音导购、语音搜索、语音客服等场景的SLM搭建可复用30k小时小规模语音预训练+权重融合的方案，降低标注与计算开销

  - 跨模态能力迁移可复用该思路：图文、音视频等其他跨模态LLM的能力迁移可参考该权重差迁移逻辑，大幅减少特定模态的指令标注需求'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有语音语言模型（SLM）照搬文本LLM的预训练+指令微调范式，但语音序列远长于文本，大规模语音指令数据集构建与训练成本极高，难以规模化落地。
### 方法关键点
提出SpeechCombine方案：1）以文本LLM基座为起点，仅用30k小时语音数据做单轮连续预训练得到语音适配模型；2）直接将语音适配模型权重与「文本指令微调LLM和基座LLM的权重差」相加融合，全程无语音指令微调步骤。
### 关键结果
该简单融合策略既保留了原文本LLM的全部知识与能力，又将指令跟随能力完全迁移到语音域，无需依赖海量语音标注数据。
