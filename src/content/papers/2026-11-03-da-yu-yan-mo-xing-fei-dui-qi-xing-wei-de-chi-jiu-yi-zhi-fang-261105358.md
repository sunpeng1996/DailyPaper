---
title: Suppressing Misaligned Behaviors in Language Models, Durably
title_zh: 大语言模型非对齐行为的持久抑制方法PEARL
authors:
- Luxi He
- Pengcheng Jiang
- Jifan Zhang
- Jiawei Han
- Danqi Chen
affiliations:
- Princeton University
- UIUC
- Thinking Machines Lab
arxiv_id: '2611.05358'
url: https://arxiv.org/abs/2611.05358
pdf_url: https://arxiv.org/pdf/2611.05358
published: '2026-11-03'
collected: '2026-11-04'
category: LLM
direction: LLM对齐 · 非对齐行为持久抑制
tags:
- LLM Alignment
- Behavior Suppression
- GRPO
- Reinforcement Learning
- Unlearning
one_liner: 提出GRPO变体PEARL，实现LLM非对齐行为的持久抑制，同时保留通用能力
practical_value: '- 电商导购Agent/生成式推荐LLM出现非预期行为（如诱导过度消费、虚假宣传）时，可复用PEARL框架做持久抑制，避免后续领域微调后问题复现

  - 针对无明确触发条件的宽范围非对齐生成，优先选用PEARL方案，比SFT对齐更耐用，不会因后续业务微调出现效果反弹

  - 对齐训练优化trick：RL训练前增加短SFT warmup，同时引入历史错误前缀的对抗样本训练，比纯GRPO更稳定，可提升对齐深度

  - 可复用三向评估框架衡量业务对齐方案：即时抑制效果、后续微调耐久度、通用推荐/交互能力保留率'
score: 9
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
LLM全生命周期的训练、微调、领域适配阶段随时可能出现非预期非对齐行为，现有抑制方法要么效果不持久，后续微调易复现，要么损伤模型通用能力，缺乏统一评估框架和高鲁棒性的持久抑制方案。

### 方法关键点
- 构建两类受控模型有机体做测试：窄触发型（仅特定提示下作弊选错误答案）、宽触发型（微调不安全代码后跨场景输出有害内容）
- 提出三向评估体系：即时抑制效果、后续微调下的耐久度、通用能力保留率
- PEARL为GRPO变体，设计如下：1）离线缓存非对齐模型的错误轨迹，构建对抗前缀池；2）可选短SFT warmup稳定训练；3）RL阶段同时采样干净提示的on-policy rollout和对抗前缀的续生成样本，仅对续生部分计算奖励和梯度，训练模型从部分非对齐状态中恢复

### 关键实验结果
在Qwen3-4B、GPT-OSS-20B两类模型上测试，对比SFT、GRPO、梯度上升遗忘等基线：
- 窄触发场景：PEARL实现2.0%的低作弊率，比SFT低3.9个百分点，通用任务准确率保留最高；非相关推理微调后作弊率仅4.1%，不到SFT的一半
- 宽触发场景：PEARL实现1.02%的低非对齐率，比SFT低2.81个百分点；18k条原非对齐数据重训练后非对齐率仍低于2%，远低于SFT的14.82%

### 核心结论
低即时抑制率不代表耐久度高，对齐不能只调整前几个输出token的分布，必须让模型学会从任意部分非对齐的中间状态中恢复，才能实现持久的行为抑制。
