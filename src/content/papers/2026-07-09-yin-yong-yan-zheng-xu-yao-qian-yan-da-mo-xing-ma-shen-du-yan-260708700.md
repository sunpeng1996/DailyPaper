---
title: Do You Need a Frontier Model as a Citation Verifier? Benchmarking Rubric LLMs
  for Deep-Research Source Attribution
title_zh: 引用验证需要前沿大模型吗？深度研究场景下打分LLM基准测评
authors:
- Ethan Leung
- Elias Lumer
- Corey Feld
- Austin Huber
- Vamse Kumar Subbiah
- Kevin Paul
affiliations:
- PricewaterhouseCoopers U.S.
arxiv_id: '2607.08700'
url: https://arxiv.org/abs/2607.08700
pdf_url: https://arxiv.org/pdf/2607.08700
published: '2026-07-09'
collected: '2026-07-10'
category: Eval
direction: LLM评测 · 引用校验裁判模型选型
tags:
- LLM-as-Judge
- RAG Evaluation
- Reward Model
- Benchmark
- Citation Validation
one_liner: 对比8款不同成本LLM的引用裁判效果，证实低成本模型可媲美前沿大模型
practical_value: '- 做电商商品种草文案/详情页生成的RAG事实校验时，无需盲目选用高成本前沿大模型，可优先测试GPT-5-mini、Gemini
  3.1 Flash Lite这类低成本模型，在保证90%左右准确率的前提下可降低数十倍推理成本

  - 将LLM裁判作为RL微调奖励信号时，不能仅看F1指标，需根据业务诉求优化偏差：电商虚假宣传零容忍场景选FPR低的模型，避免幻觉被奖励；鼓励多引用的场景选FNR低的模型，避免正确引用被惩罚

  - 结构化rubric打分任务可拆分维度独立选型：比如引用相关性校验选GPT-5-mini，事实支持度校验选Gemini 3.1 Flash Lite，相比单模型方案可同时提升效果与性价比'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前RL VR（带可验证奖励的强化学习）已成为LLM后训练主流方案，大量场景使用LLM作为rubric结构化打分裁判充当奖励模型，但行业缺乏明确的裁判模型选型标准：不确定结构化打分任务是否必须使用高成本前沿大模型，且单一F1指标掩盖的 directional bias 会直接导致下游RL训练出现reward hacking、信号稀疏等问题。尤其是RAG、深度研究Agent的引用质量校验场景，推理成本高、幻觉影响大，亟需明确最优选型方案。
### 方法关键点
1. 构建Deep-Research Citation Benchmark：覆盖25个领域，共624个<声明-引用>对，1248个LLM打分决策，其中378个为多模型意见不一致的难例，所有样本均经过人工标注校验
2. 将引用质量拆分为3个维度：URL可访问性（程序自动判断）、来源相关性、事实支持度，后两者为LLM打分的二元任务
3. 测评来自OpenAI、Anthropic、Google三个系列的8款商用LLM，除F1、Cohen's κ外，额外统计通过率漂移、FPR、FNR三类偏差指标，覆盖49倍成本区间的模型
### 关键结果
- 来源相关性维度：GPT-5-mini F1达0.908排名第一，成本仅为最高成本的Claude Opus 4.6的1/20
- 事实支持度维度：所有模型的95%置信区间重叠，无统计显著性能差异，最低成本模型F1 0.649，最高成本模型F1 0.75，差距可忽略
- 相同F1的模型偏差差异极大：部分模型事实支持度FNR高达0.47，接近一半的正确引用会被误判为不支持，这类偏差是F1无法反映的

最值得记住的一句话：结构化rubric打分任务无需盲目选用最贵的前沿大模型，按维度匹配最优低成本模型+校准偏差，性价比远高于单一大模型方案
