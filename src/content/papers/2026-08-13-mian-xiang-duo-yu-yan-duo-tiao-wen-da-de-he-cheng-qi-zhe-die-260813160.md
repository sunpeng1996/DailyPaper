---
title: 'Better Decomposition, Free Aggregation: A Synthesizer-Folding Framework for
  Multilingual Multi-Hop Question Answering'
title_zh: 面向多语言多跳问答的合成器折叠RAG框架Syfer
authors:
- Yilin Wang
- Yuchun Fan
- Weidong Bao
- Zili Wei
- Shi Feng
- Tong Xiao
- Zhengtao Yu
- Jingbo Zhu
affiliations:
- Northeastern University
- Kunming University of Science and Technology
arxiv_id: '2608.13160'
url: https://arxiv.org/abs/2608.13160
pdf_url: https://arxiv.org/pdf/2608.13160
published: '2026-08-13'
collected: '2026-08-14'
category: RAG
direction: 多语言RAG · 多跳问答优化
tags:
- RAG
- Multilingual QA
- Multi-hop Reasoning
- Question Decomposition
- LLM
one_liner: 提出带翻译门控、聚合折叠的多语言多跳RAG框架Syfer，平衡性能与推理成本
practical_value: '- 多语言RAG场景可复用翻译门控逻辑：默认用原语言推理，仅当分解质量不达标时触发双语路径，大幅降低翻译成本与噪声，适合跨境电商多语言客服、搜索场景

  - 多跳任务可复用聚合折叠设计：将最终聚合步骤转化为分解器输出的终端子问题，避免独立聚合步骤引入的误差累积，适合商品溯源、多条件商品查询等复杂Query场景

  - 多语言检索阶段可复用MMR去重逻辑：过滤不同语言的平行重复文档，减少上下文冗余，提升RAG生成质量，适合多语言商品库检索场景

  - 离线蒸馏轻量化分解器的方案可直接复用：用大模型生成分解标注蒸馏小模型，降低在线推理成本，适合高并发多语言Query处理场景'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有多语言RAG处理多跳问答时存在两个核心痛点：一是默认全量翻译引入大量噪声、推高计算成本，还会丢失原语言的文化与本地化信息；二是多跳Query分解后的独立聚合步骤会累积中间推理误差，中低资源语言场景效果退化严重，无法满足跨境复杂查询需求。

### 方法关键点
1. 离线蒸馏轻量化分解器：用大模型生成带终端聚合子问题的子问题DAG标注，蒸馏小模型作为在线分解器，保证分解格式可控、质量可验证
2. 合成器折叠设计：分解器输出的DAG包含唯一终端子问题，回答该子问题等价于聚合所有中间推理结果，省去独立聚合步骤，减少误差累积
3. 翻译门控机制：仅当终端子问题与原Query语义相似度低于阈值时，才触发双语fallback，对齐原语言与英文子问题DAG，其余场景默认用原语言推理
4. 多语言检索优化：用MMR过滤不同语言的平行重复文档，减少上下文冗余，降低生成阶段的噪声干扰

### 关键结果
扩展HotpotQA、2WikiMultiHopQA、MuSiQue三个基准到9种语言（覆盖高/中/低资源），对比5类主流基线，在最难的MuSiQue基准上平均F1较最强分解基线DaPT提升+8.91（相对+29.8%），推理 latency 与 token 成本均优于所有基线，处于帕累托最优。

**最值得记住的一句话**：多语言RAG中盲目引入全量翻译或双语分支反而会引入噪声，按需触发跨语言能力、减少不必要的推理步骤是平衡性能与成本的核心。
