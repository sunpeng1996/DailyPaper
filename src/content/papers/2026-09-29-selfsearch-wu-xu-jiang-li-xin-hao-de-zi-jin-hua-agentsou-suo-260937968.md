---
title: 'SelfSearch: Reward-Free Search for Self-Improving Agents'
title_zh: SelfSearch：无需奖励信号的自进化Agent搜索框架
authors:
- Jungwoo Yang
- In Jin Kong
- Yohan Jo
affiliations:
- Graduate School of Data Science, Seoul National University
arxiv_id: '2609.37968'
url: https://arxiv.org/abs/2609.37968
pdf_url: https://arxiv.org/pdf/2609.37968
published: '2026-09-29'
collected: '2026-09-30'
category: Agent
direction: Agent 无奖励自进化优化
tags:
- Self-Improving Agent
- Reward-Free Learning
- Agent Evolution
- Code Agent
- LLM Agent
one_liner: 无需下游奖励信号，基于历史自改进记录引导Agent迭代，成本更低效果比肩评估引导搜索
practical_value: '- 做Agent自优化时可复用无奖励迭代思路：不需要每次迭代都跑下游业务A/B测试，仅基于历史优化过程的错误、执行轨迹就能优化Agent工具链、执行逻辑，大幅降低迭代成本

  - 多lineage并行探索+经验共享的架构可直接迁移：分能力提升、自适应优化两个方向并行迭代，各lineage共享历史改进记录，既能覆盖不同优化方向，又能互相复用优化成果

  - Agent工具链优化经验可复用：自改进过程中沉淀的行范围文件查看、带输出限制的文本搜索等工具，可直接复用到电商场景下的商品内容爬取、规则校验、用户评论分析等工具型Agent中'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有Agent自进化方案依赖下游任务重复评估引导搜索，迭代成本极高，优化效果绑定特定评测任务，同时自改进过程中的轨迹、错误、工具交互等经验未被有效利用。
### 方法关键点
- 统一Agent架构：同一套代码同时负责下游任务执行与自我修改，仅修改指令、工具、执行逻辑，不改动底层LLM权重
- 双lineage并行迭代：分为能力提升、自适应优化两个分支，前者聚焦开发可复用工具补全能力短板，后者优化失败重试、策略调整逻辑
- 历史记录驱动：每轮迭代的自改进记录（推理过程、工具轨迹、代码改动、结果）共享给后续迭代，无需下游奖励信号引导修改
- 运行时隔离：LLM调用、资源限制、轨迹记录等逻辑放在不可编辑的运行时中，避免Agent改崩执行环境
### 关键结果
在SWE-bench Verified、SWE-bench Multilingual、Terminal-Bench 2.1三个基准，GPT-5.6、DeepSeek V4两个模型配置上测试：
1. 6组模型+基准场景下群体平均成功率全部超过初始Agent，Terminal-Bench 2.1单个Agent最高提升11.2pct，SWE-bench Multilingual上成功率提升5pct的同时执行成本降低38.5%
2. 搜索成本比评估引导基线低13.4%~53.2%，仅花$4.03搜索成本得到的Agent在Terminal-Bench 2.1上达到82.0%成功率，与当时最高的Codex harness持平
3. 进化得到的Agent实现可跨模型迁移，无需额外优化就能在不同LLM上超过初始Agent效果

> 最值得记住的一句话：Agent自改进过程本身的经验就是最好的优化信号，不需要依赖下游任务的奖励反馈也能实现能力和效率的双重提升
