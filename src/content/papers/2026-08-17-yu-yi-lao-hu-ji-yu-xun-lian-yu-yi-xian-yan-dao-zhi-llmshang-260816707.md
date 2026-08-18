---
title: 'Semantic Bandits: In-Context Exploration-Exploitation is Biased by Semantic
  Priors'
title_zh: 语义老虎机：预训练语义先验导致LLM上下文探索利用存在偏差
authors:
- David Eric Austin
- Kaheer Suleman
- Jackie Chi Kit Cheung
affiliations:
- McGill University
- Mila – Quebec AI Institute
- Skyfall AI
- Canada CIFAR AI Chair
arxiv_id: '2608.16707'
url: https://arxiv.org/abs/2608.16707
pdf_url: https://arxiv.org/pdf/2608.16707
published: '2026-08-17'
collected: '2026-08-18'
category: Agent
direction: LLM Agent决策 · 语义先验偏差分析
tags:
- Semantic Bandit
- LLM Agent
- Exploration-Exploitation
- In-Context RL
- Semantic Prior
one_liner: 提出语义多臂老虎机框架，量化语义先验、奖励极性对LLM Agent上下文探索行为的偏差影响
practical_value: '- 搭建电商/推荐类LLM Agent时，动作（商品、品类、运营策略）的语义描述必须对齐真实业务reward，否则会导致LLM过度偏向语义正向但实际低收益的选项，显著提升累积regret

  - 可利用奖励极性偏差做自动探索调度：业务出现负向反馈（点击率暴跌、退货率飙升）时，LLM会自动提升探索概率，无需额外逻辑；全正反馈场景需主动加探索指令避免局部最优

  - 若业务环境的动作标签可能存在误导，可在prompt中加入「标签可能与真实收益无关，请充分探索」的提示，实测可显著提升探索覆盖率，降低误导性语义先验带来的损失

  - 若需要LLM做纯统计层面的探索利用、避免语义干扰，可将动作标签替换为无意义随机字符串，此时LLM的探索表现接近经典UCB1算法'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有上下文强化学习（ICRL）评估框架沿用经典RL逻辑，忽略LLM通过自然语言交互的特性：预训练学到的语义先验会对探索利用决策产生无形式化对应规则的偏差，可能导致真实场景下LLM Agent决策稳定性不足，甚至出现系统性错误，亟需系统性量化这种偏差的影响。

### 方法关键点
- 语义多臂老虎机（Semantic Bandit）框架在经典MAB基础上新增动作文本标签、场景上下文两个语义变量，单独控制语义因素的影响
- 设计4类动作标签体系：无意义字母数字串（对照组）、情感极性标签、排序标签、领域知识标签，设置标签与reward对齐/错位两组对照
- 覆盖3类测试场景：抽象老虎机、农场种植、服装推荐，测试OLMo-3.1-32B、Qwen3-32B、Gemini 3.1 Flash Lite三类主流模型，对比经典UCB1基线
- 额外设置奖励极性对照（全正/全负奖励）、prompt去偏干预（仅警告/警告+强制探索指令）两组实验

### 关键结果
- 语义标签与reward对齐时，LLM的归一化累积regret比UCB1基线低最多90%（Qwen3用对齐排序标签时regret低至0.00）；标签错位时，regret最高比基线高5倍（OLMo在服装推荐错位标签下regret达1.00）
- 负向奖励触发的探索概率比同等幅度正向奖励高60%以上，0是明确探索阈值，reward<0时LLM基本会放弃语义先验主动探索
- 加入「警告+探索指令」的去偏prompt可将探索覆盖率提升100%以上，最多可将错位标签下的regret降低70%

LLM做决策时的语义先验影响强到足以覆盖简单任务的明确奖励信号，业务落地时不能假设LLM会完全忽略语义信息仅基于统计反馈做决策。
