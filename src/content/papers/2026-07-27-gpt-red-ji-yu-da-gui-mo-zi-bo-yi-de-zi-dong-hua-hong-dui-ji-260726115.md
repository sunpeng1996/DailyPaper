---
title: 'GPT-Red: Automated Red Teaming via Self-Play at Scale'
title_zh: GPT-Red：基于大规模自博弈的自动化红队攻击Agent
authors:
- Eric Wallace
- Christopher A. Choquette-Choo
- Nikhil Kandpal
- Sam Toyer
- Dylan Hunn
- Stephanie Lin
- Yuxin Wen
- Xiangyu Qi
- Christopher Wolff
- Zizhao Wang
affiliations:
- OpenAI
arxiv_id: '2607.26115'
url: https://arxiv.org/abs/2607.26115
pdf_url: https://arxiv.org/pdf/2607.26115
published: '2026-07-27'
collected: '2026-07-30'
category: Agent
direction: Agent 自博弈自动化红队LLM安全优化
tags:
- Agent
- Red-Teaming
- Self-Play
- RL
- Prompt Injection
- LLM Safety
one_liner: 通过大规模自博弈训练自动化红队Agent，攻击成功率超人类红队，用于LLM鲁棒性优化
practical_value: '- 做Agent安全对抗时可复用自博弈框架：同步训练攻击/防御Agent，生成的对抗样本比人工标注覆盖场景更广，适合电商客服、导购类Agent的安全对齐

  - 工具调用型Agent的测试框架可直接迁移：支持多轮交互迭代优化攻击的harness设计，可用于电商Agent的合规检测、恶意prompt注入防御的自动化测试环节

  - 对抗训练工程实践参考：将自动生成的对抗样本混入常规RL训练数据，能大幅提升模型OOD鲁棒性，可用于推荐系统query改写防御、内容生成合规性优化'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM红队依赖人工标注或小规模自动生成攻击样本，覆盖场景有限，模型易过拟合已知攻击模式，无法支撑Agent场景下快速扩大的攻击面的安全防御需求。

### 方法关键点
- 三维度规模化训练框架：推理侧给攻击Agent提供`defender_model`工具，支持多轮交互迭代优化攻击策略；环境侧将常规能力任务转化为对抗场景，覆盖直接/间接prompt注入、多模态攻击、jailbreak等场景；训练侧采用大规模RL自博弈，攻击Agent同时对抗多版本防御LLM，避免攻击模式坍塌。
- 非对称奖励设计：攻击Agent奖励为攻击有效性+合规性（符合真实威胁模型的约束），防御Agent奖励为抗攻击能力+原任务完成度。

### 关键实验
在2025Q4间接prompt注入挑战数据集上测试，对比基线为人类红队、GPT-5.5（带/不带防御模型访问权限）：GPT-Red攻击成功率远超人类红队；用其生成的对抗样本训练的GPT-5.6，间接prompt注入攻击成功率从GPT-5.3的7%降至3.5%，Fake CoT类攻击鲁棒性从5.2%提升至95.9%，对2025IPI挑战的人类攻击样本鲁棒性接近100%。

### 核心结论
自博弈红队训练能形成「更强红队→更鲁棒模型→更强红队」的安全飞轮，是大模型Agent落地安全保障的核心可行路径。
