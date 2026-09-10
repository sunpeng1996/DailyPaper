---
title: 'A-JIT: Agentic Just-In-Time Software Construction'
title_zh: A-JIT：智能体驱动的即时软件构建范式
authors:
- Mark Marron
- Earl T. Barr
affiliations:
- University of Kentucky
- University College London
arxiv_id: '2609.10248'
url: https://arxiv.org/abs/2609.10248
pdf_url: https://arxiv.org/pdf/2609.10248
published: '2026-09-09'
collected: '2026-09-10'
category: Agent
direction: Agent 运行时动态软件构建
tags:
- Agent
- JIT
- Program Synthesis
- Runtime System
- LLM4Code
one_liner: 提出嵌入AI代理的A-JIT范式，实现软件运行时动态生成、适配与持续演化
practical_value: '- 业务逻辑开发可借鉴hole语法设计，核心流程先上线，非关键/个性化分支留坑，后续基于真实用户行为数据用LLM动态补全，大幅缩短业务迭代周期

  - 复用IO对驱动代码合成的思路，推荐/广告冷启动场景先收集足够的用户行为输入输出样例，积累到阈值后自动生成适配的排序/召回分支逻辑，减少人工开发成本

  - 借鉴tactile values的强约束校验机制，Agent生成的业务规则（如促销逻辑、用户分层规则）上线前自动做类型、语义合法性校验，降低故障风险'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
传统软件采用静态预开发范式，上线后迭代周期长，无法快速响应用户个性化需求与业务变化；现有LLM辅助开发仅在开发阶段介入，无法在运行时基于真实用户交互动态调整功能，适配成本高。

### 方法关键点
- 语言层：基于Bosque语言提供hole原生语法，可显式标记待实现逻辑，配套预/后置条件、IO样例等元数据作为合成约束
- 运行时层：集成TECTON值生成框架，遇到hole时优先匹配已有IO样例返回结果，无匹配时调用LLM生成符合类型/约束的输出值，积累足够IO对后自动合成完整代码
- 校验层：支持tactile values（BAPI格式），可直接嵌入表达式引用输入值，自带强类型校验，避免生成逻辑违反语义约束
- 自适应层：运行时监控用户行为轨迹，聚类共性工作流，自动生成RPA工具简化操作，全程无需人工开发介入

### 关键结果
本文为范式提出型论文，暂无大规模量化对比实验，相关工具链已在BosqueCore仓库开源，验证了天气单位转换、办公流程自动化等场景的可行性。

### 核心结论
将软件开发能力嵌入运行时，让软件从静态交付产物变成可随用户行为持续进化的动态系统
