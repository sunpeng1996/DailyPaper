---
title: 'SkillAlchemy: Open-World Agent Skill Creation'
title_zh: SkillAlchemy：面向开放世界的Agent技能自动生成框架
authors:
- Hengjun Wang
- Shuyue Wei
- Boyi Liu
- Jun Yang
- Yongxin Tong
affiliations:
- Beihang University
- Shandong University
- Northwestern Polytechnical University
arxiv_id: '2608.23417'
url: https://arxiv.org/abs/2608.23417
pdf_url: https://arxiv.org/pdf/2608.23417
published: '2026-08-24'
collected: '2026-08-25'
category: Agent
direction: Agent 开放世界技能自动生成
tags:
- Agent Skill
- Open-World Agent
- Skill Synthesis
- Procedural Knowledge
- LLM Agent
one_liner: 提出准入式开放世界Agent技能生成框架，性能追平人工标注技能，超SOTA基线8.6pp
practical_value: '- 业务Agent技能库建设可复用「对比式隐式需求发现」方法，通过替换变量、边界探测、邻域对比三类探针自动挖掘任务未明确的约束，减少人工梳理需求的成本，降低技能泛化时的场景遗漏问题

  - RAG+Agent的流程生成场景可直接复用「证据驱动流程准入」机制，将检索到的内容区分为通用规则、限定样例、无效信息三类，避免把局部案例当成通用执行逻辑，大幅减少幻觉

  - 电商运营、客服Agent的流程/话术自动沉淀场景可直接采用整套框架，从公开文档、社区内容生成的技能抗噪声和冲突信息能力远优于直接生成方案，且技能可直接复用在同类任务上

  - 技能包分层编译思路可迁移到生成式推荐的规则输出，核心逻辑放在主prompt，参考样例和附属资源按需加载，既控制上下文长度，又保留足够的可解释性支撑'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
当前Agent技能依赖人工编写、模型先验或执行轨迹蒸馏，陌生任务下上述来源往往不可用，开放世界中的文档、代码库、社区内容等公开资源未被有效利用为技能来源；现有开放源技能生成方案易遗漏任务brief未明确的隐式约束，且常将局部案例直接作为通用规则，生成的技能泛化性差，较人工标注技能有14pp左右的性能差距。
### 方法关键点
- 隐式需求发现：将任务brief中的具体值抽象为可调整的操作因子，通过替换、边界、邻域三类对比探针生成定向检索问题，收集结构化证据，识别会影响流程执行效果的隐式约束
- 证据驱动流程准入：按决策点聚合所有证据，仅将跨多场景一致、无冲突、有充分证据支撑的候选流程判定为通用指令，仅单场景支持的作为限定样例，证据不足或冲突的直接排除
- 语法引导技能包编译：基于公开优质技能提炼的语法规范，将准入内容打包为标准技能包，核心执行逻辑放在`SKILL.md`，样例、脚本、参考资料放在附属目录，控制运行时加载的上下文长度
### 关键实验
在SkillsBench v1.1的87个跨领域任务上测试，覆盖4种Agent+模型组合，对比无技能、Anthropic/OpenAI官方技能生成器、OpenSkill、MUSE-Autoskill等基线：
- 整体avg@5 pass率较无技能提升19.9pp，较最强自动基线MUSE-Autoskill提升8.6pp，总体达55.8%，与人工标注技能性能相当
- 抗扰动测试中，不会将注入的无关、冲突、对抗性错误内容转化为执行指令，下游执行通过率波动<2%
### 核心结论
可靠的技能生成应该把开放世界知识当做需要按明确范围准入的证据，而不是可以直接复制的指令
