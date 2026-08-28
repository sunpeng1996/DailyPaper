---
title: 'Modality Maturity Index: A benchmark for assessing multimodal capabilities
  of omni models'
title_zh: 模态成熟度指数：评估通用大模型多模态能力的基准
authors:
- Rohit Patel
- Dieuwke Hupkes
- Sloan Strader
affiliations:
- Meta Superintelligence Labs
arxiv_id: '2608.26317'
url: https://arxiv.org/abs/2608.26317
pdf_url: https://arxiv.org/pdf/2608.26317
published: '2026-08-26'
collected: '2026-08-28'
category: Eval
direction: 多模态大模型能力评估基准
tags:
- Multimodal
- Benchmark
- LLM Evaluation
- Omni Model
- Modality Scoring
one_liner: 提出覆盖5种模态、支持输入输出最多3种模态组合的多模态通用大模型能力评估基准MMI与评分体系
practical_value: '- 做跨模态搜索推荐/多模态Agent的能力评估时，可复用「模态存在分+内容质量分」双维度评分框架，避免把漏生成模态的问题和内容错误混为一谈

  - 搭建多模态大模型自动评估流水线时，可参考人工编写打分规则+LLM judge的模式，实测与人工标注一致性达70.8%，性价比高于纯人工标注

  - 自研多模态生成式推荐系统时，可基于MMI的模态组合测试用例设计逻辑，构造业务场景的模态覆盖测试集，提前发现多模态输出漏发错误'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
当前前沿大模型多以全模态能力为卖点，但现有多模态评估框架几乎仅聚焦文本+单一其他模态的双模态理解，既不覆盖多非文本模态组合输入场景，也不评估模型输出模态选择的正确性，存在明显评估缺口。
### 方法关键点
1. 提出MMI基准，覆盖文本、图像、音频、视频、文档5种模态，支持输入输出最多3种模态组合，共包含893个自包含测试题，每题配套人工编写的各模态打分规则；
2. 设计双评分体系：MMI值为每题各模态得分的平均，衡量内容质量；补充模态存在分MPS，为每题预期输出模态的F1值，衡量模态漏生成问题。
### 关键结果
测试5款前沿多模态大模型，MPS仅为15.6（Claude Opus 4.6）~34.9（GPT-5.4），现有模型多模态输出能力普遍较弱；LLM judge打分与盲测人工标注一致性达70.8%，具备实用性。
