---
title: 'CulturalRiddles: A Multicultural Benchmark of Riddles'
title_zh: CulturalRiddles：跨文化谜语评测基准
authors:
- My Chiffon Nguyen
- Tianyi Hu
- Vinod Anbalagan
- Henry Gagnier
- Pouya Sadeghi
- Farah Abdou
- Tidor-Vlad Pricope
- Diego MMS Oliveira
- Jocelyn K D&#39;Arcy
- Madeline Smith
arxiv_id: '2610.29968'
url: https://arxiv.org/abs/2610.29968
pdf_url: https://arxiv.org/pdf/2610.29968
published: '2026-10-20'
collected: '2026-10-23'
category: Eval
direction: LLM评测 · 跨文化理解能力评估
tags:
- LLM Evaluation
- Cross-Cultural
- Benchmark
- Abductive Reasoning
- Multilingual
one_liner: 构建覆盖62种文化的人工创作谜语基准，评测28款LLM的跨文化理解与推理能力
practical_value: '- 做跨境电商Agent时可引入该基准测试案例，校验LLM对本地文化常识的理解准确性，避免营销话术踩文化雷区

  - 多语言站点的推荐系统文案生成模块，可参考该基准的文化关联推理逻辑，优化本地化文案的文化适配性

  - 业务涉及多文化用户内容生成时，可复用该数据集的社区共建方法，自建业务场景下的文化适配评测集，提前筛除文化冲突内容'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有LLM跨文化能力评测基准多为英语中心，侧重事实知识考核，缺乏对真实文化场景下知识应用、推理能力的评估，无法准确衡量LLM多元文化理解水平。
### 方法关键点
通过社区参与式全人工创作构建CulturalRiddles基准，覆盖62种文化、45个国家、51种语言；谜语深度绑定所属文化背景，答题需结合溯因/组合推理、文化专属关联知识、多语言能力；配套自动+大规模人工的标准化评测流程，对28种LLM配置开展能力评估。
### 关键结果数字
即使前沿LLM在部分文化群落的答题准确率最高仅为22%；所有数据集、评测工具与贡献流程完全开源，支持持续扩展语言与文化覆盖。
