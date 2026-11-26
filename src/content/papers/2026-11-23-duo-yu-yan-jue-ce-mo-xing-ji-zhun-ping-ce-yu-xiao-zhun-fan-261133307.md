---
title: 'Lost in Translation, Not in Confidence: Benchmarking and Calibrating Multilingual
  Decision Models'
title_zh: 《多语言决策模型基准评测与校准：翻译场景下的置信度偏差问题》
authors:
- Mingzhe Du
- Thong Thanh Nguyen
- Nguyen Tran Cong Duy
- See-Kiong Ng
- Luu Anh Tuan
affiliations:
- Nanyang Technological University
- National University of Singapore
- VinUniversity
arxiv_id: '2611.33307'
url: https://arxiv.org/abs/2611.33307
pdf_url: https://arxiv.org/pdf/2611.33307
published: '2026-11-23'
collected: '2026-11-26'
category: Eval
direction: 多语言大模型 决策模型跨语言评测
tags:
- Multilingual-LLM
- Decision-Model
- Cross-lingual-Evaluation
- Confidence-Calibration
- Benchmark
one_liner: 评测25个开源多语言决策模型在14种语言下的表现，揭示跨语言准确率损失与置信度错配问题
practical_value: '- 跨境多语言Agent路由、意图识别、内容审核场景，不可直接复用英文场景的置信度阈值，需针对不同语种单独校准，小语种需额外预留容错空间

  - 多语言决策模型跨语言冷启动时，仅需几千条目标语种标注数据即可大幅缩小准确率损失，无需全量参数微调或海量标注，可大幅降低标注成本

  - 评测多语言决策模型业务性能时，需采用人译测试集，若使用LLM翻译测试集会低估实际落地时的准确率缺口，导致上线后效果不达预期'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
当前多语言决策模型（用于Agent路由、意图识别、内容审核等场景）的评测几乎全基于英文，跨语言场景下准确率与置信度的匹配度未得到验证，直接复用英文场景阈值易引发决策错误。
### 方法关键点
选取25个SOTA开源决策模型，在14种语言的17项并行任务上开展对照评测，完成81组受控微调实验验证跨语言迁移效果，对比人译与LLM翻译测试集的评测差异。
### 关键结果
所有模型在非英语语种上均出现准确率下跌：高资源语种跌2个点，泰米尔语等小语种跌8个点，置信度仅下跌约一半；英文下95%准确率对应的阈值，在泰米尔语下仅达90%准确率；英文习得的任务技能可跨语言迁移，几千条目标语种标注可大幅缩小损失但无法完全消除；LLM翻译的测试集会低估实际跨语言准确率缺口。
