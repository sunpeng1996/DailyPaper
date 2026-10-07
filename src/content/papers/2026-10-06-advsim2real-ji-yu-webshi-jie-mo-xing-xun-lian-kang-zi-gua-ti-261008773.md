---
title: 'AdvSim2Real : Training Web Agents Against Adaptive Prompt Injection in a Web
  World Model'
title_zh: AdvSim2Real：基于Web世界模型训练抗自适应提示注入的Web Agent
authors:
- Sarim Hashmi
- Mukul Ranjan
- Kshitij Mishra
- Mikhail Kuznetsov
- Praneeth Vepakomma
- Nils Lukas
affiliations:
- Mohamed bin Zayed University of Artificial Intelligence
- Amazon
- Massachusetts Institute of Technology
arxiv_id: '2610.08773'
url: https://arxiv.org/abs/2610.08773
pdf_url: https://arxiv.org/pdf/2610.08773
published: '2026-10-06'
collected: '2026-10-07'
category: Agent
direction: Web Agent 鲁棒训练 · 提示注入防御
tags:
- WebAgent
- PromptInjection
- AdversarialTraining
- WorldModel
- CurriculumLearning
one_liner: 提出两阶段协同演化框架，在冻结Web世界模型中训练兼具高能力与抗注入鲁棒性的Web Agent
practical_value: '- 电商导购/运营类Web Agent场景可复用success-flip奖励机制，训练Agent对抗第三方商家页面植入的恶意提示注入，避免偏离用户真实目标

  - 可复用两阶段训练范式：第一阶段用难度适配的任务课程快速提升Agent基础能力，第二阶段用自适应攻击迭代增强鲁棒性，无需大量人工标注数据

  - 交互类Agent任务可先基于冻结世界模型做低成本预训练，再迁移到真实环境，降低真实环境训练的风险和落地成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
Web Agent执行用户多步任务时，容易被第三方页面植入的间接提示注入攻击误导偏离用户目标；现有防御要么基于固定注入样本微调，无法对抗自适应攻击者，要么对抗训练时任务固定，Agent掌握后就失去训练价值，且依赖真实可执行站点的训练成本极高。

### 方法关键点
- 全流程在冻结的WebWorld-14B世界模型中运行，避免环境变动影响训练一致性，所有角色均用LoRA微调降低成本
- Stage1：协同优化任务课程和Agent，课程仅在Agent任务成功率接近50%时获得奖励，保证任务难度始终匹配Agent当前能力，快速提升基础任务完成率
- Stage2：冻结课程，协同优化自适应攻击者和Agent；攻击者仅在「成功翻转」（无攻击时任务成功，注入后任务失败）时获得奖励，避免将Agent自身失误算作攻击有效；Agent训练数据混合新攻击、历史攻击、干净任务三类样本

### 关键实验
在150个表单填写类Web任务上测试，对比base Qwen3.5-4B：干净场景任务完成率从74.89%提升到81.33%，迁移到真实浏览器时严格成功率从25.56%提升到44.44%；对抗训练过的攻击者时完成率从48.07%提升到57.48%，达到Qwen3.5-9B的水平；对抗从未见过的Kimi-K3 frontier攻击者时完成率从23.00%提升到30.72%，相对提升33.6%。

最值得记住的一句话：冻结世界模型+难度自适应课程+成功翻转奖励的对抗训练范式，可在不牺牲基础任务能力的前提下，大幅提升Web Agent对未知提示注入攻击的鲁棒性。
