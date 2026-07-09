---
title: 'VIBE: Voice-Induced open-ended Bias Evaluation for Large Audio-Language Models
  via Real-World Speech'
title_zh: VIBE：基于真实语音的大音频-语言模型开放式语音诱导偏差评估
authors:
- Yi-Cheng Lin
- Yusuke Hirota
- Sung-Feng Huang
- Hung-yi Lee
affiliations:
- National Taiwan University
- NVIDIA Research
arxiv_id: '2604.17248'
url: https://arxiv.org/abs/2604.17248
pdf_url: https://arxiv.org/pdf/2604.17248
published: '2026-07-02'
collected: '2026-07-09'
category: Eval
direction: 多模态大模型 · 公平性偏差评估
tags:
- LALM
- Bias Evaluation
- Fairness
- Speech Processing
- Open-ended Task
one_liner: 提出基于真实人类语音的开放式评估框架VIBE，检测12款SOTA大音文模型的系统性生成偏差
practical_value: '- 语音交互类电商推荐/Agent（如语音购物助手）业务可直接复用VIBE的开放式评估范式，用真实用户语音输入检测模型生成内容的性别、口音维度偏差，避免固化刻板印象引发用户反感

  - 做多模态大模型公平性评估时，不要仅依赖MCQ式的封闭测试，开放式任务评估更贴合真实业务场景，可捕捉预设选项外的隐性偏差

  - 语音场景下的个性化推荐业务可参考该研究结论，针对不同口音、性别用户做推荐结果校准，降低偏差带来的用户体验不均问题'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
大音频-语言模型（LALMs）已广泛落地语音交互类业务，但现有公平性评估基准依赖合成语音和选择题（MCQ）范式，无法全面覆盖真实场景下的生成式偏差，评估结果碎片化。
### 方法关键点
提出VIBE评估框架，采用真实人类录制的语音作为输入，基于个性化推荐等开放式任务开展偏差检测：无需预设候选选项，可让模型的刻板关联自然呈现，且框架易扩展到新的评估任务。
### 关键结果
对12款SOTA LALMs的测试显示，模型在真实场景下普遍存在系统性偏差；性别、口音两类语音线索均会触发统计显著的输出分布偏移，偏差幅度与任务类型强相关。
