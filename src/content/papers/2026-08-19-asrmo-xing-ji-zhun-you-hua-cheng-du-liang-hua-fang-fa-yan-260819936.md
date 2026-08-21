---
title: Towards Quantifying Benchmark Optimization in ASR Models
title_zh: ASR模型基准优化程度量化方法研究
authors:
- Theo Lebryk
- David Ayllon
- Alice Baird
- Jakub Piotr Cłapa
- Jens Madsen
- Panagiotis Tzirakis
affiliations:
- Hume AI Research
arxiv_id: '2608.19936'
url: https://arxiv.org/abs/2608.19936
pdf_url: https://arxiv.org/pdf/2608.19936
published: '2026-08-19'
collected: '2026-08-21'
category: Eval
direction: ASR模型 基准过拟合量化评估
tags:
- ASR
- Benchmark Evaluation
- Model Probing
- Generalization
- Overfitting
one_liner: 提出三类行为探针量化ASR模型基准过拟合，揭示高分模型基准性能虚高机制
practical_value: '- 电商语音搜索、智能客服场景的ASR模型评估可复用三类探针，快速检测模型是否过拟合训练/测试集，避免线下benchmark高分但线上转录错误率高的问题

  - 模型迭代时可参考低秩线性steering方法，定向消除模型的基准过拟合行为，无需全量重训即可提升真实场景泛化性

  - 搭建业务模型专属benchmark时，需加入模糊输入、矛盾输入等对抗case，避免benchmark分数与线上效果脱节'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
公开ASR基准普遍存在过拟合风险，高分模型的基准WER常与真实场景泛化能力脱节，缺乏量化基准优化（即benchmaxxing）程度的通用方法。
### 方法关键点
设计三类行为探针：参考不一致探针（音频与参考转录矛盾）、掩码数字恢复探针（音频对应数字被掩码）、拼写切换探针（同发音不同拼写的歧义场景），检测模型是否优先输出基准参考片段而非忠实还原音频；结合机制探针定位过拟合的触发线索，引入低秩线性调控等方法验证过拟合行为的可干预性。
### 关键结果
开源高分ASR模型即使在音频矛盾、掩码、歧义场景下，仍会逐字输出基准参考片段；可通过低秩线性steering或片段末尾追加音频的方式，因果性调控模型的基准过拟合行为，证明基准性能虚高并非来自真实转录能力提升。
