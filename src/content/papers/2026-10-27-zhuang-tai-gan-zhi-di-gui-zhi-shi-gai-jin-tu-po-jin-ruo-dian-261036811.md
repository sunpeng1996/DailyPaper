---
title: 'Weakness Localization Is Not Enough: State-Aware Recursive Knowledge Improvement
  for Large Language Models'
title_zh: 状态感知递归知识改进：突破仅弱点定位的LLM优化瓶颈
authors:
- Runze Jiang
- Yan Wang
- Boran Jin
- Bingyu Zhu
- Longtao Huang
affiliations:
- Peking University
- Alibaba Group
- Delft University of Technology
arxiv_id: '2610.36811'
url: https://arxiv.org/abs/2610.36811
pdf_url: https://arxiv.org/pdf/2610.36811
published: '2026-10-27'
collected: '2026-10-28'
category: Training
direction: LLM知识注入 · 状态感知闭环优化
tags:
- Knowledge_Improvement
- State_Aware
- Recursive_Training
- Knowledge_Graph
- LLM_Alignment
one_liner: 针对LLM知识状态混淆问题，提出状态感知递归知识改进框架，大幅提升知识注入效果
practical_value: '- 电商垂类LLM迭代可复用状态分层逻辑，把知识缺陷拆分为「缺失/难召回/不会用」三类，对应选择预训练注入/召回SFT/场景化微调，避免统一调参浪费资源

  - 可借鉴图结构化知识单元设计，把商品/合规/运营知识拆分为关系、对比、链、树等单元，对齐诊断探针和训练数据，让弱点定位和修复精准对应

  - Agent知识库迭代可套用该闭环逻辑：每次修复后重新评估知识状态，相同错误持续出现时不要重复相同干预，根据最新状态调整优化策略'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM知识优化仅做弱点定位，但相同弱点可能对应完全不同的知识状态（知识缺失/已注入但难召回/可召回但不会用），即「知识状态混淆」问题，单一修复策略适配性极差；且模型更新后知识状态会动态变化，固定迭代策略效率极低。

### 方法关键点
- 提出Recursive Knowledge Improvement（RKI）框架，把知识优化建模为序列状态感知的闭环干预过程
- 将领域知识拆解为6类图结构化单元（关系、对比、自我网络、环、链、树），作为诊断、干预、重评估的统一载体
- 定义3类知识状态维度：可用性（是否注入）、可及性（能否召回）、易用性（能否应用），从6个诊断维度（获取、识别、召回、理解、推理、应用）估计当前状态
- 每轮迭代流程：定位弱点→结合历史干预记录估计当前知识状态→匹配对应干预策略（知识注入/召回强化/应用训练）→更新模型后重评估进入下一轮

### 关键实验
在公开多跳问答基准HOTPOTEVAL、阿里内部安全合规基准SAFEINTERNALEVAL上测试，对比Self-QA、GraphGen等7个基线，平均得分领先最强基线18.41分；仅增加状态感知决策就比仅用弱点定位的策略高5.17分；相同弱点持续存在时，57.1%的知识单元状态已发生变化，验证重评估的必要性。

### 最值得记住的一句话
相同的知识弱点背后可能对应完全不同的底层状态，仅靠弱点定位的修复策略天然存在瓶颈，闭环状态感知的递归迭代才能最大化知识优化效率。
