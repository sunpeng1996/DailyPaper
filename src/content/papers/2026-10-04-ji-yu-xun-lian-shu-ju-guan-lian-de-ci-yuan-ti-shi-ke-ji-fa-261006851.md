---
title: Base Models Can Reason By Taking a Cue From Training Data
title_zh: 基于训练数据关联的词元提示可激发基座模型推理能力
authors:
- Sophie L. Wang
- Amil Dravid
- Rulin Shao
- Kevin Farhat
- Sewon Min
- Alexei A. Efros
affiliations:
- MIT
- UC Berkeley
- University of Washington
- Allen Institute for AI
arxiv_id: '2610.06851'
url: https://arxiv.org/abs/2610.06851
pdf_url: https://arxiv.org/pdf/2610.06851
published: '2026-10-04'
collected: '2026-10-06'
category: Reasoning
direction: 基座模型推理 · 词元提示触发
tags:
- Base Model
- Reasoning
- Token Cue
- RL Fine-tuning
- Training Data Association
one_liner: 发现仅固定基座模型输出前1-2个词元提示，即可使其推理性能追平RL微调版本
practical_value: '- 电商导购Agent、智能客服场景可快速复用：无需微调，仅固定输出开头的1-2个预设词元，即可提升优惠计算、规则解释等复杂问题的回答准确率

  - 训练垂直领域（如电商规则、广告文案生成）专属LLM时，可刻意将高频有效行为（如 step-by-step 算优惠）与特定简单词元绑定，后续推理时prefill该词元即可快速触发对应行为，成本远低于全量SFT/RL

  - 推荐/广告Agent的安全对齐场景：可通过预设输出开头词元的方式降低有害内容、违规营销话术的输出概率，无需额外微调即可快速提升合规性，适合快速上线的个性化场景'
score: 9
source: huggingface-daily
depth: full_pdf
---

### 动机
当前RL微调被广泛用于提升大模型推理能力，但学界长期存在争议：RL到底是教会了模型全新的推理技能，还是仅仅激活了基座模型已经具备的能力？此前的推理触发方法多依赖显式指令或复杂解码策略，尚未有研究探索极短的输出开头词元对推理行为的调控作用。
### 方法关键点
- 无监督挖掘有效词元提示：先用beam search生成模型对推理问题的高概率前2位输出词元作为候选，再基于多轮采样的答案熵最小化准则选择最优提示，全程无需标注答案
- 训练数据干预验证因果关联：通过替换训练数据中词元与推理内容的绑定关系，可将任意无意义词转化为推理提示，也可消除原有提示的推理触发效果
- 隐态分析解释机制：有效提示会使模型后续输出的隐藏状态向训练集中的推理轨迹样本偏移，且仅插入在输出开头的提示能维持该偏移以保证推理效果
### 关键实验
在MATH-500、GSM8K、HumanEval等基准上测试，对比原生基座模型、RL微调后模型：Olmo-3-7B加`.

 Okay`提示后MATH-500 pass@1从42%提升至78%，超过其RL微调版本的75%；Qwen3-14B加`Alright ,`提示后准确率从72%提升至87%，追平RL版本；修改训练数据后，“Think duck duck goose”可达到与“Think step by step”相当的推理触发效果。
### 核心结论
LLM的推理能力很大程度上早已存在于基座模型中，RL微调的核心收益大多来自提升有效推理触发词元的生成概率，而非教会模型新的推理能力
