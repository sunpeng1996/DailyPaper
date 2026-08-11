---
title: 'Decoding-Level Taboo: A Diagnostic Stress Test for LLM Robustness'
title_zh: 解码级禁忌：面向大语言模型鲁棒性的诊断压力测试
authors:
- Tadanobu Chuyo Kamijo
- Ori Rottenstreich
- Javier Conde
- Gonzalo Martínez
- Pedro Reviriego
affiliations:
- University of the Ryukyus
- Technion
- IPTC
- Universidad Polécnica de Madrid
arxiv_id: '2608.09900'
url: https://arxiv.org/abs/2608.09900
pdf_url: https://arxiv.org/pdf/2608.09900
published: '2026-08-10'
collected: '2026-08-11'
category: Eval
direction: LLM鲁棒性评估 · 解码层压力测试
tags:
- LLM Robustness
- Stress Test
- Logit Masking
- Model Evaluation
- Synthetic Data Generation
one_liner: 提出零提示解码层logit掩码压力测试方法，评估LLM脱离标称生成路径的鲁棒性
practical_value: '- 可复用解码层动态token掩码trick，在电商LLM文案生成、客服Agent回复场景强制规避敏感词/违禁词，替代prompt禁令减少幻觉

  - 可借鉴该压力测试方法，上线前对推荐场景LLM排序/语义理解模块做鲁棒性校验，降低线上badcase

  - 可利用该方法生成多样化合成训练数据，补充电商Query改写、个性化文案生成的训练语料，提升模型泛化性'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有LLM评估仅聚焦标称生成条件下的表现，无法覆盖实际部署中受系统prompt、安全护栏、结构化输出约束等被迫偏离标称生成路径的场景，导致基准得分与线上性能存在显著差距。
### 方法关键点
Decoding-Level Taboo是零提示诊断压力测试，运行时直接在logit空间的词边界处动态屏蔽排名靠前的候选token，强制模型迂回生成，脱离其熟悉的标称生成路径。
### 关键结果
对多个开源模型家族测试表明，离路径鲁棒性同时受参数量级、指令对齐程度双重影响，鲁棒性随模型规模、对齐程度提升而同步增强。该方法可作为基础组件，用于合成多样化数据集、运行时安全护栏压力测试、上线前模型可靠性审计。
