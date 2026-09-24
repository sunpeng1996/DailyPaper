---
title: Reference-Based Analysis of Coherence and Diversity in Open-Ended Text Generation
title_zh: 基于参考的开放式文本生成连贯性与多样性分析
authors:
- Esteban Garcés Arias
affiliations:
- Department of Statistics, LMU Munich
- Munich Center for Machine Learning (MCML)
arxiv_id: '2609.28080'
url: https://arxiv.org/abs/2609.28080
pdf_url: https://arxiv.org/pdf/2609.28080
published: '2026-09-23'
collected: '2026-09-24'
category: Eval
direction: 开放式文本生成质量评估
tags:
- Text Generation
- Evaluation
- Coherence
- Diversity
- Human Preference
one_liner: 提出基于人类参考的三维框架，度量开放式生成文本的连贯性、多样性与人类感知质量的关联
practical_value: '- 生成式推荐/广告文案生成的质量评估场景，可复用三维参考评估框架，从轨迹对齐、单样对比、分布似然三个维度打分，替代单一的BLEU类重合度指标

  - 生成场景的多样性&连贯性调优时，可参考人类参考分布似然指标，平衡生成质量和人类偏好匹配度，避免过度追求多样性导致内容脱离需求

  - 生成文案A/B测试效果归因场景，可复用该框架拆解连贯性、多样性两个维度对用户满意度的贡献，快速定位迭代方向'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
开放式文本生成质量难评估，单一参考重合度指标无法覆盖多维度质量要求，连贯性、多样性与人类感知质量的关联缺乏结构化度量方法。

### 方法关键点
提出三维参考评估框架：1. 时序维度对齐生成文本与人类续写的连贯性/多样性演化轨迹；2. 单样本维度对比生成与人类续写的连贯性/多样性统计特征；3. 分布维度计算生成文本在人类参考分布下的似然。对比temperature/top-p/beam search等不同生成策略的评估表现，结合人工评分验证框架有效性。

### 关键结果
多样性时序对齐、均值特征对比可捕捉质量相关差异；参考似然与人工评分正相关，关联度随参考配置、打分范围变化；时序对齐未体现出比简单基线更强的预测优势。
