---
title: 'LLMs Don''t Know What They Know: Benchmarking Temporal Self-Knowledge for
  Financial Backtesting'
title_zh: 面向金融回测的大语言模型时间自认知能力基准测试
authors:
- Lingfei Qian
- Yan Wang
- Xueqing Peng
- Yupeng Cao
- Yuechen Jiang
- Zhuohan Xie
- Anke Xu
- Wenbo Cao
- Jiarui Chen
- Zehan Li
affiliations:
- The Fin AI
- University of Manchester
- Mohamed bin Zayed University of Artificial Intelligence
- Deepkin AI
- University of Florida
arxiv_id: '2611.06808'
url: https://arxiv.org/abs/2611.06808
pdf_url: https://arxiv.org/pdf/2611.06808
published: '2026-11-03'
collected: '2026-11-09'
category: Eval
direction: LLM知识边界评估 · 金融回测
tags:
- LLM
- Knowledge Boundary
- Benchmark
- Financial Backtesting
- Temporal Knowledge
one_liner: 构建FinDendro基准验证LLM金融回测现有知识边界防护手段可靠性不足
practical_value: '- 做电商/广告领域LLM时效性预测任务（如大促销量预估、活动效果预测）时，不可完全依赖官方给出的knowledge cutoff，需自行实测时序知识边界，避免数据泄露

  - 需要LLM基于历史时间点信息推理时，在prompt中明确声明历史日期，可有效降低LLM滥用后续知识的概率，同时不影响推理准确性

  - 可复用本文基准构建思路，针对电商/广告领域时序事实（如商品上新时间、促销节点、历史大盘数据）构建自定义评测集，验证LLM时序自认知准确率'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
LLM用于金融时序预测回测的有效性前提是模型未预知待预测结果，现有依赖官方knowledge cutoff、模型自报告知识、prompt指定历史日期的三类防护手段可靠性未被验证。

### 方法关键点
构建FinDendro基准，包含1999-2026年共2226条标注日期的美国金融事实，覆盖宏观经济、股票价格、美联储决议三类，设计4类prompt测试不同场景下的知识自认知能力，控制随机准确率约为0.27。

### 关键结果数字
GPT-5事实回答准确率达76%，但仅声称知道38%，对声称不知道的事实仍有61%回答正确；知识声明可超出实际知识边界最多7个季度；prompt声明历史日期可消除大部分前置知识声明但不改变准确率；现有三类防护手段均无法保证回测无数据泄露。
