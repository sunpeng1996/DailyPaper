---
title: 'Mitigating Hallucinations in Medical Question Answering on ESC Cardiology
  Guidelines: Evaluation and Retrieval Optimization'
title_zh: ESC心脏病指南医疗问答幻觉缓解：评估与检索优化
authors:
- Ilkin Masimov
- Rufana Baghirli
- Muhammad Rashid
affiliations:
- 哈尔滨工业大学（深圳）计算机科学与技术学院
- Harzklinikum Dorothea Christiane Erxleben, Quedlinburg, Germany
arxiv_id: '2611.34427'
url: https://arxiv.org/abs/2611.34427
pdf_url: https://arxiv.org/pdf/2611.34427
published: '2026-11-25'
collected: '2026-11-26'
category: RAG
direction: RAG 幻觉缓解与流程可靠性评估
tags:
- Hallucination
- RAG
- Medical QA
- Verification
- Evaluation
one_liner: 通过人工标注量化医疗QA场景下RAG校验修正流程的误差，明确校验器可靠性是核心瓶颈
practical_value: '- 做RAG+校验的合规类场景（比如商品描述审核、广告文案校验）时，不可默认校验器输出为真值，必须抽样审计校验器准确率，避免高估问题检出率

  - 多轮独立运行校验流程取结果并集，可大幅提升幻觉/违规内容召回率，该技巧可直接复用在文案审核、智能客服应答校验等场景

  - 校验后的修正环节本身可能引入新错误，需增加修正后二次校验逻辑，避免最终输出错误率反弹'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
垂直领域LLM QA存在严重幻觉，现有基于检索的「校验-修正」幻觉缓解流程普遍默认校验器输出为真值，误差从未被系统量化。
### 方法关键点
构建覆盖4份ESC心脏病指南的160个专家标注QA数据集，含627条双粒度人工校验的检索语料；对比4种检索配置、3次独立运行的5阶段校验修正pipeline，全量审计606条被驳回的声明，人工标注误差来源。
### 关键结果数字
- 校验器标记的问题声明中仅44.7%~50.6%为真幻觉，检出高估近1倍
- 修正循环收敛率85.2%~95.1%，但35%的最终错误来自修正环节本身
- 单轮运行真幻觉召回率35.6%~41.2%，3轮结果并集召回提升至71%~80%
- 校验器间一致性Cohen's κ仅0.505，最终输出错误率1.7%，校验器可靠性是核心瓶颈
