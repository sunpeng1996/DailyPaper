---
title: 'SWE-Duel: Towards a Self-Scaling Arena for Coding Agents'
title_zh: SWE-Duel：面向代码Agent的自扩展评测竞技场
authors:
- Wei Minn
- Zhensu Sun
- Lwin Khin Shar
- David Lo
affiliations:
- Singapore Management University
arxiv_id: '2610.12569'
url: https://arxiv.org/abs/2610.12569
pdf_url: https://arxiv.org/pdf/2610.12569
published: '2026-10-07'
collected: '2026-10-13'
category: Eval
direction: Agent评测 · 自扩展红蓝对抗框架
tags:
- Coding Agent
- Benchmark
- Adversarial Evaluation
- Self-scaling
- Red-Blue Duel
one_liner: 提出红蓝对抗式自扩展代码Agent评测竞技场，解决静态基准数据泄露、难度饱和问题
practical_value: '- 可复用红蓝对抗的自扩展评测思路，解决推荐/广告Agent静态基准数据泄露、难度固定无法适配策略迭代的问题，可落地到召回/排序策略的动态评测场景

  - 评测用例准入校验逻辑可直接复用：要求任务生成方自身可盲解任务，避免生成不可解/无意义用例，适配大模型时代推荐系统效果评测的用例自动生成环节

  - 同模型家族版本越高生成任务难度越高的结论可复用：做Agent对抗训练时，可同步迭代任务生成端的模型能力，自动匹配当前求解端的训练难度天花板'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有静态代码Agent评测基准发布后内容易泄露进训练集，能力迭代后的Agent很快会达到效果饱和，无法适配持续进化的Agent评测需求。
### 方法关键点
提出SWE-Duel自扩展竞技场，采用红蓝轮流对抗模式：红方Agent基于真实开源仓库实现新功能并嵌入隐蔽bug，生成的PR需通过原有测试、新功能测试，且红方自身盲测可修复bug才准入；蓝方Agent在未知存在bug的前提下评审PR，修复所有bug则获胜，随后双方互换角色。任务与难度随参与Agent能力动态调整，无预先生成内容避免泄露。
### 关键结果
11组模型-框架参与者在5种语言的15个仓库完成1500轮对战，GPT-5.5搭配Codex CLI缺陷修复率达98.3%排名第一；Claude Opus 4.8搭配mini-swe-agent红方胜率27.3%为最强任务生成方；同模型家族最新版本生成的任务击败固定求解器的比例达42.9%，远高于旧版本的4.0%，验证了难度随任务生成方能力自动扩展的有效性
