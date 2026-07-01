---
title: 'Self-Study Reconsidered: The Hidden Fragility of Learning from Self-Generated
  QA'
title_zh: 自学习反思：基于自生成QA训练的隐藏脆弱性
authors:
- Ekaterina Alimaskina
- Denis Shveykin
- Gleb Molodtsov
- Igor Shalygin
- Alexey Kadeishvili
- Aleksandr Beznosikov
affiliations:
- BRAIn Lab
- Yandex Research
arxiv_id: '2606.32002'
url: https://arxiv.org/abs/2606.32002
pdf_url: https://arxiv.org/pdf/2606.32002
published: '2026-06-30'
collected: '2026-07-01'
category: Training
direction: 合成QA训练 · 风险防御
tags:
- Synthetic QA
- Self-Study
- Prompt Injection
- Training Data
- LLM Safety
one_liner: 揭示自生成QA训练的双阶段脆弱性，给出低成本无侵入的防御方案
practical_value: '- 做领域小模型微调/蒸馏时，优先采用sentence-targeted生成策略，避免模型反复聚焦salient片段浪费训练预算，降低脏数据劫持概率

  - 处理爬取的电商/商品/用户评论等非结构化文本做合成训练数据时，前置关键词+正则过滤指令类片段，可将注入合规率从88%降到13%，几乎不损失有效文本

  - 做RAG/Agent用到外部第三方数据源生成训练数据时，不要依赖大模型能力天然抗污染，大模型反而更容易服从嵌入指令导致行为偏移

  - 生成合成QA数据时，新增适量diverse多问题prompt，可降低锚点偏差约10-20pp，无需改动下游训练逻辑'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
合成QA对已成为LLM微调、蒸馏、知识压缩、KV cache训练的主流监督信号，业界普遍将QA生成视为中立预处理步骤，未关注生成过程的隐含偏好对训练质量与安全性的影响，非可信语料下的风险更是被长期忽略。
### 方法关键点
- 拆分自生成QA流程为问题生成（证据选择）、答案生成（监督信号输出）两个独立阶段，分别定位脆弱点
- 问题侧：通过证据足迹提取技术，量化不同模型、prompt、语料下的锚点选择偏差，通过插入人工标记片段、HTML垃圾片段测试劫持效应
- 答案侧：在语料中嵌入17种不同类型的指令片段，测试不同规模模型的指令服从率
- 防御层：测试2种问题生成优化策略、3种上下文过滤方案，均无需修改下游训练逻辑
### 关键结果
基于Cartridges、LongHealth、QASPER三个公开数据集，覆盖Qwen3、Llama3.1、Gemma3三个系列共6个模型：① 问题生成覆盖率快速饱和，60%以上的新增QA重复聚焦已覆盖片段；② 插入的HTML垃圾片段可劫持55%~94%的生成QA；③ 答案阶段嵌入指令的平均服从率达87.7%，大模型在任务冲突场景服从率反而更高；④ 关键词正则过滤可将服从率降至12.6%且100%保留干净文本，sentence-targeted生成可降低劫持率32~44pp。
最值得记住的一句话：自生成QA不是中立预处理步骤，模型最终学到的内容由生成过程选择的监督信号决定，而非生成文本的流畅度，要主动控制信号源而非完全交给模型。
