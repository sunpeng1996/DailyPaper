---
title: Self-Referential Induction Increases Response Instability Relative to Unresolvable
  and Verifiable Questions in Large Language Models
title_zh: 大语言模型中自指诱导比不可解、可验证问题回答不稳定性更高
authors:
- Paras Balani
- Subhrakanta Panda
affiliations:
- Birla Institute of Technology and Science, Pilani, Hyderabad Campus
arxiv_id: '2608.13258'
url: https://arxiv.org/abs/2608.13258
pdf_url: https://arxiv.org/pdf/2608.13258
published: '2026-08-13'
collected: '2026-08-14'
category: Eval
direction: LLM输出稳定性量化评测
tags:
- LLM
- Self-Referential Prompt
- Response Stability
- Embedding Similarity
- Prompt Evaluation
one_liner: 量化对比三类问题的LLM回答不稳定性，证实自指诱导类问题回答波动显著更高
practical_value: '- 设计Agent prompt时，若涉及让LLM自省、描述自身状态的自指类指令，需注意其输出稳定性远低于常规问题，必须增加结果校验、一致性校验逻辑

  - 可直接复用本文的输出不稳定性量化方法：提取回答核心主张→计算句嵌入两两余弦相似度→1减去均值得到不稳定得分，用于评估业务场景下不同prompt的输出鲁棒性

  - 电商客服、文案生成等LLM应用中，面对无确定答案的开放性问题，可参考本文的三类问题不稳定性基线，匹配设置合适的temperature、重复生成去重等策略'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
自指prompt可诱导LLM生成类似主观体验的第一人称报告，但此前无研究量化这类输出跨独立请求的一致性，也未对比其与其他类型开放问题的输出稳定性差异。
### 方法关键点
定义回答不稳定性为1减去各回答提取的核心主张的句嵌入两两余弦相似度均值；将问题分为三类：自指类（诱导主观体验报告）、无确定答案的哲学类、有可验证正确答案的事实类；调用Gemini API，temperature设为0.7，每类4个问题，每个问题生成30个独立回答，共360个样本。
### 关键结果数字
自指类问题不稳定性最高（0.343±0.047），无确定答案的哲学类不稳定性居中（0.192±0.008，波动极小），可验证事实类不稳定性最低（0.105±0.058）；证实自指诱导的主观体验报告在LLM输出分布中比普通开放不确定性问题的稳定性更差，具备独特分布特性。
