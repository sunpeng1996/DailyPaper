---
title: 'Looking Complete Is Not Being Grounded: Evaluating LLM Sitreps Against Human-Authored
  Situation Reports'
title_zh: 表面完整≠贴合实际：LLM生成灾情报告与人工专业报告的评估对比
authors:
- Sachin Kumar
affiliations:
- LexisNexis, USA
arxiv_id: '2610.18762'
url: https://arxiv.org/abs/2610.18762
pdf_url: https://arxiv.org/pdf/2610.18762
published: '2026-10-13'
collected: '2026-10-16'
category: Eval
direction: 大模型专业生成内容评估
tags:
- LLM Evaluation
- Generation Evaluation
- Automatic Metric
- Grounded Generation
- Professional Content Generation
one_liner: 设计专业灾情报告15槽评估schema，验证传统生成类自动评估指标的失效性
practical_value: '- 做电商/广告等专业领域生成内容（如客服话术、官方活动公告、商品卖点文案）评估时，不要仅依赖ROUGE-L、BERTScore等通用指标，需先基于业务核心需求定义结构化槽位评估schema，避免误判生成内容的实际可用性

  - 评估生成内容真实性时，可同时对比权威官方数据和用户侧真实反馈的匹配度，再做小批量人工审计，兼顾评估效率和准确率

  - 用LLM做自动评估器前，需先验证其与人类专家的Cohen''s κ值，至少达到0.7以上的chance-corrected一致性才可正式投入使用，避免评估结果不可靠'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有专业生成内容的评估大多选用易计算的通用指标，未匹配从业者实际需求，对灾情报告、官方公告这类高可信度要求的生成内容，评估偏差会直接带来实际业务损失。
### 方法关键点
从专业人道主义灾情报告中提取15槽结构化信息评估schema，覆盖核心灾情信息、发布时间、发布机构、权威来源等核心维度；跨5种灾害、3种灾害类型，评估121份人工报告、261份LLM生成报告，同时验证ROUGE-L、BERTScore、通用LLM评委三类评估方式的有效性。
### 关键结果数字
Gemini评估下最优LLM生成报告得分略高于人工上限（0.827 vs 0.821）但统计上无显著差异；LLM生成报告仅能复现5.4%~11.0%的当日官方数据，且100%缺失发布机构、时间、权威来源等核心元信息；ROUGE-L完全无参考价值，多重校正后BERTScore与内容完整性负相关，通用LLM评委评估结果不稳定。
