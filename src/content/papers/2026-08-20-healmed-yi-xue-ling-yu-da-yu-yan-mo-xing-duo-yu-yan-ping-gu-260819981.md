---
title: 'HealMed: Multilingual Evaluation of Large Language Models in Medicine'
title_zh: HealMed：医学领域大语言模型多语言评估基准
authors:
- Yingjian Chen
- Fan Gao
- Sherry T. Tong
- Haoyu Zhang
- Aosong Feng
- Kevin W. Jin
- Xing Wu
- Jinghui Lu
- Abdul Samad
- Akbar Faruqi
arxiv_id: '2608.19981'
url: https://arxiv.org/abs/2608.19981
pdf_url: https://arxiv.org/pdf/2608.19981
published: '2026-08-20'
collected: '2026-08-22'
category: Eval
direction: LLM多语言评测 · 医疗领域基准
tags:
- Benchmark
- LLM Evaluation
- Multilingual
- Medical LLM
- Cross-lingual
one_liner: 推出经医学专家审核的9语言医疗LLM评测基准HealMed，明确翻译质量与模型属性对跨语言性能的影响
practical_value: '- 做多语言电商/广告LLM应用评测时，可复用「双语专家审核翻译质量」的流程，避免翻译偏差导致评测结果失真

  - 多语言场景选型LLM时，优先选择头部闭源模型，其跨语言性能稳定性优于开源/垂直微调模型，可降低适配成本

  - 垂直领域微调无法直接保证LLM多语言鲁棒性，小语种垂直应用需额外补充小语种语料适配，不能仅依赖主语言微调'
score: 4
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有医疗LLM能力验证集中在英语场景，多数多语言评测基准由英语数据集直接翻译生成，翻译偏差易干扰模型性能评估结果，缺乏经专家审核的高质量多语言医疗LLM评测基准。
### 方法关键点
由9个国家地区的23名医学专家耗时2年构建HealMed基准，覆盖9种语言各1000条样本，包含MCQA、NLI、开放问答3类任务，每条样本的翻译均由2名精通英语和目标语言的专家审核修订。
### 关键结果
低资源语言下模型性能下降最明显，不同语言、不同模型的性能差距差异显著；头部闭源模型跨语言性能最稳定，开源/医疗专用模型的跨语言性能差距更大、一致性更差；仅靠医疗领域微调无法保证多语言鲁棒性，翻译质量对跨语言评测结果影响显著。
