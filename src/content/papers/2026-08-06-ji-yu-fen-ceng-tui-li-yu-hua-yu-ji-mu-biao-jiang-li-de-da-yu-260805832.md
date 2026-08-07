---
title: Enhancing Social Intelligence in LLMs with Hierarchical Reasoning and Utterance-Level
  Goal Rewarding
title_zh: 基于分层推理与话语级目标奖励的大语言模型社交智能增强
authors:
- Xiaofeng Wang
- Kakam Chong
- Shuai Xiao
- DeXin Kong
- Qingyuan Tian
- Chen Ju
- Xu Yan
- Shuai Zhao
- Fei Huang
- Rui Wang
affiliations:
- Independent Researcher
- Alibaba Group
- Shanghai Jiao Tong University
arxiv_id: '2608.05832'
url: https://arxiv.org/abs/2608.05832
pdf_url: https://arxiv.org/pdf/2608.05832
published: '2026-08-06'
collected: '2026-08-07'
category: Agent
direction: LLM Agent 社交智能优化
tags:
- LLM Agent
- Reinforcement Learning
- Hierarchical Reasoning
- Reward Modeling
- Social Intelligence
one_liner: 提出TSR分层推理框架与LHRL-VGR强化学习算法，7B模型社交谈判目标完成率超GPT-4o 7.32%
practical_value: '- 电商客服、议价、用户运营类Agent可直接复用TSR分层框架：先做用户意图推断→生成对话策略→输出回复，比端到端生成可控性更高，还可解释回复逻辑

  - 多阶段Agent RL优化可复用方差门控动态奖励路由：目标评估分数方差大时用目标完成度奖励，方差小时用策略对齐奖励，平衡短期效果与长期策略一致性，避免模型学捷径

  - 多阶段Agent联合训练时，采用策略层+执行层加权优势估计的方式联合优化，比单独训练某一层效果提升更明显，可迁移到导购、谈判等Agent场景训练'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM在动态社交交互（如谈判、多轮议价）中表现较差，现有方法给每轮对话统一施加目标奖励，忽略了每轮的目标特异性，也无法区分模型是真的学会了社交推理还是仅掌握了刷分的捷径回复，需要更符合人类决策逻辑的社交Agent优化方案。

### 方法关键点
- 提出Think-Strategy-Response（TSR）分层生成框架，参考计划行为理论将每轮对话生成拆为2阶段：上层先做用户状态推断、生成本轮对话策略，下层基于策略生成具体回复，推理过程不输入下层以减少计算开销
- 设计线性化分层强化学习算法LHRL-VGR：策略层采用「策略内容完整性+实际执行的目标完成度转移奖励」的复合奖励优化；回复层采用方差门控奖励路由，当多采样的目标完成度评分方差超过阈值时用目标完成度奖励，否则用策略对齐奖励，同时叠加重复惩罚
- 两阶段采用联合相对策略优化，策略层优势为内容奖励优势和转移奖励优势的加权和，两阶段同步训练

### 关键实验
在SOTOPIA、SOTOPIA-Hard社交谈判基准测试，以Qwen2.5-7B为基座，对比GPT-4o、Claude3.5-Sonnet、EPO、AMPO等10+基线，最终平均目标完成成功率比GPT-4o高7.32%，SOTOPIA-Hard上目标完成率比GPT-4o高9.76%，人类评估中策略和回复的最优占比均超过单阶段训练方案。

最值得记住的一句话：多阶段目标导向Agent的优化，不要用统一奖励覆盖所有层级，分层设计奖励、动态适配每轮的目标确定性，能让小参数模型实现超过大模型的任务表现。
