---
title: In-Place Tokenizer Expansion for Pre-trained LLMs
title_zh: 预训练大语言模型的原位Tokenizer扩展方法
authors:
- Jimmy T. H. Smith
- Tarek Dakhran
- Alberto Cabrera
- Simon S. Lee
- Paul Pak
- Aditya Tadimeti
- Tim Seyde
- Maxime Labonne
- Alexander Amini
- Mathias Lechner
affiliations:
- Liquid AI
arxiv_id: '2607.15232'
url: https://arxiv.org/abs/2607.15232
pdf_url: https://arxiv.org/pdf/2607.15232
published: '2026-07-16'
collected: '2026-07-17'
category: LLM
direction: LLM 词表扩展 · 多语言端侧适配
tags:
- Tokenizer Expansion
- BPE
- Multilingual LLM
- On-device LLM
- Continued Pre-training
- MoE
one_liner: 提出预训练LLM原位Tokenizer扩展两阶段适配方案，不损失原有能力的同时大幅提升小语种解码效率
practical_value: '- 做垂直领域/小语种LLM部署时，可复用该原位BPE扩展方案，无需从头预训练，仅需补充少量领域/小语种语料即可提升token压缩率，降低推理延迟

  - 词表扩展后初始化直接用新token对应源子token embedding均值，无需复杂对齐方案；适配时先训新增embedding再全量微调，可最大程度保留原有模型能力

  - 端侧Agent/推荐场景小模型部署，可参考该方案权衡词表大小与解码效率，针对重点语言/业务术语扩展词表，用不到10%的通用语言性能损失换重点场景2~3倍解码速度提升

  - 评估词表扩展效果时不能仅依赖MCQ类指标，必须加入生成类任务测试，避免出现判别能力正常但生成内容退化的问题'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
预训练LLM的Tokenizer在预训练初期固定，词表分配与初始语料分布强相关，后续新增的小语种、垂直领域术语会被拆分为大量子token，显著抬升推理延迟、算力与能耗。云模型词表开销占总参数比例极低可忽略，但端侧小模型的embedding与LM head占解码带宽比例高，原有小词表方案对新增语言/领域适配效率极低，从头预训练或直接替换Tokenizer的方案要么成本过高，要么易出现效果退化。

### 方法关键点
- Tokenizer构造：保留原有BPE合并规则不变，在加权的小语种多语言语料上继续训练新增合并规则，确保原有token1:1映射到新词表，所有新token均可确定性分解为源子token序列
- Embedding初始化：原有token的embedding直接复制，新token初始化为其分解的源子token embedding均值，保证向量范数与原有分布一致
- 两阶段适配：第一阶段仅训练新增embedding行，冻结其余参数与模型主干，训练600B小语种加权语料；第二阶段解冻全参数，用平衡多语种语料做400B token的继续预训练

### 关键结果
词表从65K扩展到128K后，印地语、越南语、泰语的token数分别降低2.4×、2.6×、4.0×，端侧解码速度提升2.2~3.7×；原有英语、代码等场景性能损失不超过9%；两阶段适配后模型在8项基准测试的平均得分超过源模型3.6分，小语种Global-MMLU得分最高提升11.6分，无明显能力退化。

最值得记住的一句话：Tokenizer扩展的核心是最小化对原有模型能力的扰动，两阶段训练+平衡语料的方案能在极低的通用场景损失下，实现重点场景的效率大幅提升。
