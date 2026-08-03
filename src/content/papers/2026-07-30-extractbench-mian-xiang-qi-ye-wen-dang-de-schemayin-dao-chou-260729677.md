---
title: 'ExtractBench: A Benchmark for Schema-Guided Enterprise Document Extraction'
title_zh: ExtractBench：面向企业文档的Schema引导抽取评测基准
authors:
- Boyang Zhang
- Adrian Lyjak
- Eli Stewart
- Zhaoqi Li
- Simon Suo
affiliations:
- RunLlama AI
arxiv_id: '2607.29677'
url: https://arxiv.org/abs/2607.29677
pdf_url: https://arxiv.org/pdf/2607.29677
published: '2026-07-30'
collected: '2026-08-03'
category: Eval
direction: 大模型评测 · 企业文档结构化抽取
tags:
- Document Extraction
- Benchmark
- Schema-guided
- Grounding
- Cost Evaluation
one_liner: 构建覆盖8个业务域的Schema引导抽取基准，首次联合评估准确率、溯源性、成本
practical_value: '- 电商场景发票、订单、资质、物流单等文档结构化抽取可直接参考选型：单页短文档用通用VLM成本≤1美分/页，长列表/高准确率要求选专用抽取API，性价比比coding
  agent高60%以上

  - 自研结构化抽取系统的评估体系可直接复用：采用「顺序不敏感value F1 + 词/页级grounding F1 + 单页成本」三维指标，全面覆盖业务落地的合规、成本、效果要求

  - 标注流程可迁移：采用多模型共识自动标注易例、人工仅校验争议样本的标注pipeline，可将结构化数据标注成本降低70%以上，适合电商大量非标文档的标注场景'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有Schema引导的企业文档抽取基准普遍存在能力短板：要么仅支持固定抽取模板，无法适配企业自定义schema需求；要么不覆盖扫描件、手写体、跨页长列表等真实生产场景，也未联合评估准确率、可溯源性、处理成本三类核心落地指标，评测结果无法反映系统的实际生产可用性。
### 方法关键点
- 数据集覆盖370份共4869页真实企业文档，跨8个业务域、67种文档类型，标注13类挑战标签（长列表完整性、低资源事实查找、密集表单、扫描/手写噪声、跨页/超大表格等），支持细粒度错误归因。
- 采用分场景标注pipeline：真实文档用多模型共识标注易例、人工仅校验争议字段；长列表文档先构造结构化数据再渲染为PDF，天生自带真值；扫描表单用人工全量校验抽取值与对应位置框，兼顾标注质量与成本。
- 评估指标覆盖三个生产核心维度：顺序不敏感的value F1衡量抽取准确率，词/页级grounding F1衡量抽取结果的可溯源性，实测单页处理成本衡量规模化落地的经济性。
### 关键实验结果
对比14个前沿系统（商业VLM、coding agent、专用抽取API、开源模型）：
- LlamaExtract Agentic Plus整体value F1达95.6%，比Codex GPT-5.5高2个百分点，成本仅为后者的29%（8.1美分/页vs 27.8美分/页），综合表现最优。
- 通用商业VLM在≤10页的短文档上F1可达87.9%，但在>50页的长文档上骤降至27.9%，且所有VLM、coding agent默认不返回抽取结果的溯源证据，无法满足审计合规要求。
### 最值得记住的结论
企业级文档抽取系统的核心竞争力是准确率、可溯源性、成本三者的平衡，高投入不一定能换来高准确率，专用抽取API的性价比远高于通用VLM和coding agent。
