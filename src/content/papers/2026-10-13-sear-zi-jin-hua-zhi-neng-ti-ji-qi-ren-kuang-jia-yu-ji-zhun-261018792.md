---
title: 'SEAR: Self-Evolving Agentic Robotics'
title_zh: SEAR：自进化智能体机器人框架与基准测试集
authors:
- Xinyi Wang
- Bangzheng Li
- Hanyu Wang
- Lin Zhang
- Andrea Yaoyun Cui
- Zhenggang Tang
- Shyamal Buch
- Dejia Xu
affiliations:
- Luma AI
arxiv_id: '2610.18792'
url: https://arxiv.org/abs/2610.18792
pdf_url: https://arxiv.org/pdf/2610.18792
published: '2026-10-13'
collected: '2026-10-15'
category: Agent
direction: 具身智能 · LM驱动自进化Agent
tags:
- LLM Agent
- Embodied AI
- Self-Evolution
- Robotics
- Benchmark
one_liner: 提出自进化机器人智能体评估基准与框架，可区分真实学习与运气、重复尝试的增益
practical_value: '- 自进化Agent评估可复用该框架的对照组设计：用best-of-3（同预算拆分多次短尝试）、无历史经验基线、密封盲测方法，区分真实算法增益、重复采样增益和运气，适合广告投放策略自优化Agent、推荐召回规则自迭代Agent的效果评估

  - 技能库设计可复用其结论：仅沉淀通用routine（如通用调价逻辑、通用用户画像规则），丢弃任务特定解决方案，同时增加技能校验机制避免错误经验传递；技能库仅对半强模型（无库准确率30%~80%）增益最大，过强/过弱模型投入产出比极低

  - Agent运行模式可按业务场景选型：高吞吐低延迟场景（如广告竞价、实时推荐排序）选code-as-policy模式，低并发高容错场景（如电商客服、复杂售后处理）选agent-as-policy模式，不同LLM适配不同模式可最大化效果

  - 泛化性评测可复用T1-T5分层逻辑：从同任务新样本、同任务扰动、新任务同环境、新环境新任务到落地真实业务场景，逐级量化经验迁移的真实价值，避免过拟合训练场景'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LM驱动的自进化机器人Agent缺乏统一评测基准，无法区分性能提升是来自真实学习、重复尝试、运气还是特权信息，也无法验证学习到的经验能否跨任务、跨模拟器、跨真机迁移，不同系统的效果无法横向对比。
### 方法关键点
- 定义三种Agent运行模式：code-as-policy（生成可直接执行的控制代码，运行时无LM推理延迟）、agent-as-policy（LM实时在控制环内决策，效果好但延迟高）、auto-research（自动收集数据微调VLA模型）
- 设计多组对照实验：best-of-3（相同总预算下拆分3次短尝试取最优，排除重复采样增益）、无技能库运行（排除历史经验增益）、密封评测（用Agent未见过的测试态打分，排除特权信息）、多次重复运行（排除运气）
- 定义5级泛化评测梯度T1-T5：从同任务新初始态、同任务扰动、新任务同环境、新环境新任务到落地真机，逐级衡量经验迁移能力
### 关键结果
覆盖7个前沿LLM、330个模拟任务、5个真机任务，累计Agent运行时长超4年。核心数字：① 技能库对半强模型（无库准确率30%~80%）平均增益12个百分点，过强/过弱模型增益不足1个百分点；② 真机上agent-as-policy模式下GPT-6-astra准确率从41%提升至88%，但单轮运行时长是code模式的3.4倍；③ 同能力级text-only模型搭配工具链可超过多模态模型，感知不是瓶颈，推理和工具使用价值更高。
> 最值得记住的结论：自进化系统的性能提升不能只看学习曲线，必须通过严格的对照组排除重复采样、运气、特权信息的干扰，才能验证真实的学习和迁移能力
