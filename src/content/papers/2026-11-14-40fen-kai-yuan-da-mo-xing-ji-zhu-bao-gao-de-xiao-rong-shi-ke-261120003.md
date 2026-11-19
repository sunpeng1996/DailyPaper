---
title: 'The novelty exposed: ablation, reproducibility and transparency in 40 technical
  reports of open-weight large language models (LLMs)'
title_zh: 40份开源大模型技术报告的消融实验、可复现性与透明度调研
authors:
- Bahaeddin Türkoğlu
arxiv_id: '2611.20003'
url: https://arxiv.org/abs/2611.20003
pdf_url: https://arxiv.org/pdf/2611.20003
published: '2026-11-14'
collected: '2026-11-19'
category: Eval
direction: LLM技术报告评估与发布规范
tags:
- LLM
- reproducibility
- ablation study
- transparency
- open-weight
- technical report
one_liner: 调研40份开源LLM技术报告的创新有效性与透明度，输出7项发布报告规范
practical_value: '- 自研业务LLM（如推荐/广告文案生成模型）迭代时可参考7项报告准则，对齐可复现性要求，避免无效架构改动

  - 选型第三方开源LLM适配业务场景时，优先核查消融实验支撑、训练关键参数（数据/Token量/算力）披露情况，减少选型踩坑

  - 内部模型迭代过程中强制做核心模块的对照消融实验，准确定位性能提升来源，降低重复造轮子成本'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
近年Hugging Face平台开源LLM新增数量快速增长，大量宣称的架构创新未经过严谨验证，技术报告的透明度、可复现性缺乏统一标准，从业者难以判断模型的真实增量价值。
### 方法
1. 分析2025年Hugging Face新增48个LLM架构的参考代码，比对核心模块的复用情况；
2. 随机抽样40份配套技术报告，核查创新点的消融实验支撑、可复现性信息披露情况；
3. 排查已知模块换名重发的违规情况。
### 关键结果
- 39/48的新架构至少2个核心模块复用自Llama等已有模型；
- 73项架构/训练创新点中仅19项有对照消融验证，仅1份报告完整披露数据混合、Token量、算力3项关键训练信息；
- 配套输出7项LLM发布报告规范，明确创新验证、信息披露的强制要求
