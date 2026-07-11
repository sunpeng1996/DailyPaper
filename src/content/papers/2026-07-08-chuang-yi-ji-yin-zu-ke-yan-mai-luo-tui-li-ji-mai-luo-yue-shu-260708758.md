---
title: 'Ideas Have Genomes: Benchmarking Scientific Lineage Reasoning and Lineage-Grounded
  Idea Generation'
title_zh: 创意基因组：科研脉络推理及脉络约束创意生成基准
authors:
- Yifan Zhou
- Qihao Yang
- Yan Li
- Donggang Li
- Xiru Hu
- Hokin Deng
- Ziyang Gong
- Xuanyi Zhou
- Huacan Wang
- Xiangchao Yan
affiliations:
- Shanghai Jiao Tong University
- Carnegie Mellon University
- University of Chinese Academy of Sciences
- Shanghai Artificial Intelligence Laboratory
- University of Science and Technology of China
arxiv_id: '2607.08758'
url: https://arxiv.org/abs/2607.08758
pdf_url: https://arxiv.org/pdf/2607.08758
published: '2026-07-08'
collected: '2026-07-11'
category: Eval
direction: 大模型评测 · 科研创意生成与脉络推理
tags:
- Benchmark
- Lineage Reasoning
- Idea Generation
- LLM Evaluation
- Scientific LLM
one_liner: 构建面向科研脉络推理与脉络约束创意生成的基准IG-Bench，配套结构化评估框架与指标
practical_value: '- 可复用GenomeDiff差分标注思路，对推荐场景的用户兴趣演化、爆款商品迭代脉络做结构化建模，提升序列推荐的可解释性

  - 可借鉴PES（Population-Evolution Score）评估逻辑，用于生成式推荐的候选item/文案评估，同时兼顾历史继承性、差异化、未来价值三个维度

  - 结构化脉络上下文的排序波动结论可复用：做RAG时不能盲目加所有历史脉络数据，需针对性筛选适配不同大模型的上下文输入'
score: 5
source: huggingface-daily
depth: abstract
---

### 动机
现有大模型评估体系缺乏对创意继承、演化逻辑的验证能力，无法衡量AI系统复现科研思路脉络、基于历史脉络生成合理新创意的水平。
### 方法关键点
基于IdeaGene框架，将每篇论文/方案抽象为结构化Idea Genome对象，用GenomeDiff记录创意的继承、突变、丢失、外部引入、新增等6类演化动作；构建IG-Bench基准覆盖10个科研领域，配套两类评估任务：IG-Exam共42类任务1029个实例，测试脉络推理能力；IG-Arena采用脉络约束的PES指标评估生成创意的合理性。
### 关键结果
基准包含1961条金标脉络轨迹、1085个标注Idea Genome对象、920条成对GenomeDiff记录。对14款LLM科研助手的测试显示存在显著组合瓶颈，最强系统的脉络推理精确准确率仅27.3%，结构化脉络上下文会改变系统排名而非普适提升所有系统性能。
