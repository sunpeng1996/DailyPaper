---
title: Beam Search, Self-Consistency, and the Limits of Inference-Time Scaling for
  Grammar-Constrained Text-to-SQL in Small Language Models
title_zh: 小模型语法约束Text-to-SQL的推理缩放边界与解码策略对比
authors:
- Ty Chermsirivatana
- John MacCormick
affiliations:
- Dickinson College
- Deep Network Understanding Lab
arxiv_id: '2608.25761'
url: https://arxiv.org/abs/2608.25761
pdf_url: https://arxiv.org/pdf/2608.25761
published: '2026-08-26'
collected: '2026-08-27'
category: LLM
direction: 大模型推理 · 结构化输出解码优化
tags:
- text-to-SQL
- beam-search
- self-consistency
- grammar-constrained-decoding
- small-language-model
one_liner: 对比语法约束Text-to-SQL解码策略，证明推理算力难替代模型参数，beam搜索优于自洽投票
practical_value: '- 做Agent工具调用/结构化输出（生成SQL、JSON参数、规范文案）时，相同算力预算下优先选择beam search而非sample+vote（自洽性投票），准确率更高

  - 小模型（<3B）做结构化输出任务时，可将beam width提升到4~8，最多获得1.4倍准确率提升，成本远低于更换大模型；大模型（≥7B）加大beam收益低于5%，无需额外消耗算力

  - 语法约束对大模型会造成准确率损失（3B约3%、7B约4%），上线前需先完善语法规则覆盖度（比如覆盖IN值列表、IS NOT NULL等常用语法），避免破坏正确输出

  - 不要试图用增加推理算力的方式替代升档模型，除1.5B升3B可通过2倍beam算力替代外，其余档位提升模型参数的收益远高于增加推理算力'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
低资源/端侧部署场景常尝试用「小模型+推理时算力扩容」替代大模型，同时叠加语法约束保证结构化输出（SQL、工具调用参数等）合法，但此前没有系统验证过约束场景下「模型大小 vs 推理算力」的 tradeoff 有效性，以及不同解码策略的效果差异。

### 方法关键点
- 测试模型为Qwen2.5-Instruct全系列，参数覆盖0.5B~7B，统一采用4-bit量化控制显存占用
- 对比两种推理算力扩容策略：可变宽度beam search、sample+vote（多采样+执行结果投票），算力预算B取1/2/4/8，匹配相同算力做公平对比
- 采用上下文无关文法做语法约束，解码时实时屏蔽不符合语法的token，保证输出SQL符合目标库schema

### 关键结果
- 数据集采用Spider text-to-SQL基准的1034条开发集，评估指标为执行准确率
- 相同算力下beam search在11/16组对比中显著优于sample+vote，无一组sample+vote效果更优
- 小模型（0.5B/1.5B）将beam提升到8可获得1.2~2.2倍准确率提升，大模型（3B/7B）提升幅度不到1.3倍，收益随模型增大快速衰减
- 仅1.5B模型用B=2的beam可追平3B模型的greedy效果，其余场景8倍推理算力都无法弥补上一档参数的差距
- 语法约束对小模型有2.5%的准确率提升，对7B大模型反而带来4.3%的损失，主要来自语法覆盖不全

### 核心结论
语法约束的结构化输出场景下，beam搜索的性价比远高于自洽性投票，且推理时算力扩容几乎无法替代模型参数的升级。
