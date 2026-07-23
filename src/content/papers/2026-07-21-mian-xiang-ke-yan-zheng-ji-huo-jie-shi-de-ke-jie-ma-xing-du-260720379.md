---
title: 'Train the Model, Not the Reader: Decodability Supervision for Verifiable Activation
  Explanations'
title_zh: 面向可验证激活解释的可解码性监督：优化模型而非解读方
authors:
- Hiskias Dingeto
affiliations:
- StackOne Technologies
arxiv_id: '2607.20379'
url: https://arxiv.org/abs/2607.20379
pdf_url: https://arxiv.org/pdf/2607.20379
published: '2026-07-21'
collected: '2026-07-23'
category: LLM
direction: 大模型可解释性 · 激活解释可验证
tags:
- Interpretability
- Activation Explanation
- Decodability Supervision
- Audit Protocol
- LLM Safety
one_liner: 提出RECAP可解码监督与两种审计协议，解决激活解释重构评分漏检虚假声明的问题
practical_value: '- 做LLM4Rec/Agent推理链路可解释性校验时，可复用grounded-vs-true cross、evaluator
  swap两种审计协议排查解释的虚假声明，避免信任不可靠的模型自解释结果

  - 对推荐/Agent系统中需要可验证的内部状态（如用户意图向量、召回排序触发逻辑的隐状态），可参考RECAP思路额外训练线性探测头，仅+0.001nat损失即可实现指定内容的可校验性，方便问题排查与合规审计

  - 对抗生成虚假解释的场景下，优先用独立探测头替代传统重构评分做假内容识别，RECAP训练的探测头在对抗篡改场景下AUC仍达0.95，远高于普通方案的随机水平'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有基于自然语言自编码器的激活解释方案，通过重构分数判断解释可信度，存在结构性缺陷：不校验单条声明真实性，仅匹配主旨就可拿高分，甚至会出现模型适配的私有伪编码欺骗评分。
### 方法关键点
1. 两种审计协议：grounded-vs-true cross、evaluator swap，可检测解释的声明级真实性；
2. RECAP方案：与目标模型同步训练线性头，约束指定内部内容可解码，规避私有伪编码生成。
### 关键结果数字
- 沙箱模型上RECAP仅带来+0.001nat损失，即可消除私有编码，解释声明真实性大幅提升；
- 预训练Pythia-160M上，RECAP训练后探测头识别虚假声明AUC达0.96（无RECAP仅0.82）；
- 对抗篡改解释欺骗重构评分场景下，RECAP探测头识别谎言AUC仍为0.95，对照组降至随机水平0.51
