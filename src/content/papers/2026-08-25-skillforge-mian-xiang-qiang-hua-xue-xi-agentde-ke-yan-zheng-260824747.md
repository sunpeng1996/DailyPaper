---
title: 'SkillForge: Evolving Verifiable Skills for Reinforcement Learning Agents'
title_zh: SkillForge：面向强化学习Agent的可验证技能演化框架
authors:
- Shidong Yang
- Ziyu Ma
- Tongwen Huang
- Xucong Wang
- Renda Li
- Yiming Hu
- Yong Wang
- Xiangxiang Chu
affiliations:
- Alibaba Group AMAP
arxiv_id: '2608.24747'
url: https://arxiv.org/abs/2608.24747
pdf_url: https://arxiv.org/pdf/2608.24747
published: '2026-08-25'
collected: '2026-08-26'
category: Agent
direction: Agent 强化学习技能库演化
tags:
- LLM-Agent
- RL
- Skill-Evolution
- GRPO
- Knowledge-Reuse
one_liner: 通过显式技能调用与证据驱动验证机制，实现RL Agent可复用技能库的持续演化与质量管控
practical_value: '- 电商导购/客服Agent可复用显式技能调用设计：将常用操作（搜品、退改规则查询等）封装为带调用标签的结构化技能，既压缩prompt长度，又可统计每个技能的调用成功率，自动淘汰无效策略

  - 技能库迭代机制可迁移到推荐系统规则库/话术库维护：采用「多路径归纳（从成功/失败/对比案例生成新规则）+ EMA成功率追踪 + LLM复盘」的流程，自动淘汰过时、错误的运营规则/话术，降低人工审核成本

  - 小模型训大模型用技巧：训练业务Agent时，可先用小模型结合SkillForge框架演化技能库，再直接迁移给大模型使用，实验显示4B模型演化的技能效果不亚于30B模型自生成的技能，能大幅降低大模型训练成本'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有基于RL的LLM Agent多为 episodic 训练，无法跨episode复用经验；此前的技能类方法（如SKILLRL）仅向技能库追加内容，无有效性验证机制，存在技能调用不可观测、效果难归因、无效技能污染知识库的问题，导致Agent学习效率低、长期性能不稳定。

### 方法关键点
- 显式技能调用设计：技能封装为带唯一ID、意图、适用条件、核心策略的结构化单元，Agent决策时仅看到精简技能目录，需通过`<skill_call>`标签显式调用才能获取完整技能内容，调用行为被记录到轨迹中，实现RL对动作和技能调用的联合优化
- 多路径技能归纳：每间隔固定训练步，从成功轨迹提取通用策略、从失败轨迹总结修正方案、从成败对比中提炼关键决策差异，生成新技能后经词汇+语义去重加入技能库
- 证据驱动技能验证：追踪每个技能的EMA成功率、调用次数，计算欠性能得分，得分高的低质技能触发LLM复盘，决定保留或修订，持续管控技能库质量

### 关键实验
在ALFWorld、WebShop（电商购物仿真环境）、AppWorld三个基准测试，对比SKILLRL、GRPO等基线：相同Qwen2.5-7B backbone下，比SKILLRL平均提升6.3%，WebShop成功率提升10.3个百分点，AppWorld SGC指标从5.36提升到14.3（接近翻3倍）；技能库可跨模型迁移，4B模型演化的技能效果不弱于30B模型自生成的技能，额外训练开销低于10%。

> 最值得记住的一句话：技能不应是静态的记忆条目，而应是可被环境反馈持续验证、迭代的可复用决策单元。
