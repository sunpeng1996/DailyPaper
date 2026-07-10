---
title: Multi-Modal, Multi-Environment Machine Teaching for Robust Reward Learning
title_zh: 多模态多环境机器教学实现鲁棒奖励学习
authors:
- Ali Larian
- Qian Lin
- Chang Zong Wu
- Daniel S. Brown
affiliations:
- University of Utah
arxiv_id: '2607.08647'
url: https://arxiv.org/abs/2607.08647
pdf_url: https://arxiv.org/pdf/2607.08647
published: '2026-07-09'
collected: '2026-07-10'
category: Agent
direction: Agent 鲁棒奖励学习 · 多模态多环境教学
tags:
- Reinforcement Learning
- Reward Learning
- Machine Teaching
- Inverse RL
- Multi-Modal Learning
one_liner: 提出分层集覆盖最优教学框架HSCOT，跨多环境多模态高效学习泛化性强的奖励函数
practical_value: '- 做RL-based推荐/广告Agent奖励设计时，预算有限优先选择专家演示反馈，单条约束效率最高；预算充足可补充比较类反馈强化全局约束，进一步降低奖励歧义

  - 做跨场景（不同类目、不同流量层、不同用户群）的推荐Agent奖励泛化时，可复用HSCOT分层逻辑：先筛选能覆盖互补约束的核心场景，再在场景内选高信息度反馈样本，同步降低标注成本与跨场景泛化误差

  - 评估奖励函数鲁棒性时，可借鉴广义行为等价类（gBEC）指标，通过全局约束覆盖度而非单场景准确率判断奖励歧义度，提前识别跨场景失效风险'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有Inverse RL（IRL）的机器教学方案仅支持单环境、演示类单一反馈模态，单环境下学到的奖励会与环境特有结构深度耦合，跨新场景部署时极易失效；同时不同反馈模态的约束效率差异缺乏系统性分析，无法在有限标注预算下最大化奖励的鲁棒性。

### 方法关键点
- 理论量化不同反馈模态的约束特性：无限数据场景下，比较类反馈的全局约束能力最强；有限预算场景下，演示类反馈单query的约束效率最高
- 证明单环境奖励可识别性存在天然缺陷：即便在单环境下获取无限反馈，依然存在无法消解的奖励歧义，必须引入多环境的互补约束才能解决
- 分层集覆盖最优教学（HSCOT）框架采用双层贪心策略：外层贪心选择能覆盖最多未覆盖约束的环境，内层选择对应环境下信息度最高的反馈样本，本质是嵌套的集合覆盖优化，优先最小化使用的环境数再最小化反馈总量

### 关键实验结果
在GridWorld、LavaMiniGrid两个测试域各生成50个共享奖励、仅布局不同的MDP，20%作为未见过的测试集，对比均匀采样教学基线：
- 相同反馈预算下，HSCOT的held-out regret比基线低60%~100%，GridWorld场景下基本实现0 regret
- HSCOT可实现100%的全局约束覆盖，基线仅能覆盖20%~60%的约束
- HSCOT平均使用的环境数比基线少15%~20%

### 核心结论
单环境下的奖励歧义无法通过增加同环境反馈消解，必须通过多场景+多模态反馈的组合教学实现奖励的跨环境泛化。
