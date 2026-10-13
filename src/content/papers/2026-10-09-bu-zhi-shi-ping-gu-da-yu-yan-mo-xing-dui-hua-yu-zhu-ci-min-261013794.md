---
title: 'Not Just an Evaluation: A Case Study of Discourse Particle Sensitivity in
  Language Models'
title_zh: 不只是评估：大语言模型对话语助词敏感性的案例研究
authors:
- William Sheffield
- Jiahui Chen
- Amy Zhang
- Alex Warstadt
- Junyi Jessy Li
- Kanishka Misra
affiliations:
- The University of Texas at Austin
- University of California, San Diego
arxiv_id: '2610.13794'
url: https://arxiv.org/abs/2610.13794
pdf_url: https://arxiv.org/pdf/2610.13794
published: '2026-10-09'
collected: '2026-10-13'
category: LLM
direction: 大语言模型 · 话语助词敏感性分析
tags:
- LLM
- Discourse Particle
- Instruction Tuning
- Lexical Representation
- Model Interpretability
one_liner: 通过行为与机制分析揭示LLM对just、only等话语助词的敏感性及表征规律
practical_value: '- 优化对话式导购/客服Agent话术时，可通过增删just、only类语气助词匹配用户情绪感知，提升对话自然度

  - 做LLM生成话术的偏好评估时，需纳入话语助词维度校验，避免因忽略助词导致用户好感度误判

  - 指令微调对话类LLM时，可针对性加入话语助词标注样本，提升模型对语境语气的感知精度'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
不改变语句真值的话语助词可调节对话语境与说话人态度，在自然语言中出现频率极高，但现有研究极少关注LLM对这类助词的感知规律，相关机制完全不明确。
### 方法关键点
以英语常用多义助词just、only为研究对象，开展三类分析：1. 人类与LLM的助词偏好对比实验；2. 有无助词场景下LLM生成概率差异验证；3. 模型内部助词敏感单元的定位与迁移分析。
### 关键结果
1. LLM与人类偏好完全一致，均更倾向语境中存在这类助词，且对just的敏感度显著高于only；2. 指令微调可使模型对助词的敏感度平均提升17%；3. 二者语义表征不对称：only的敏感单元仅可迁移到排他义的just，而just的所有敏感单元均可无差别迁移到任意语义的only
