---
title: 'AxDafny: Agentic Verified Code Generation in Dafny'
title_zh: AxDafny：面向Dafny的智能体形式化验证代码生成框架
authors:
- Benjamin Breen
- Austin Letson
- Borja Requena Pozo
- Leopoldo Sarra
affiliations:
- Axiomatic AI, Boston, MA, USA
arxiv_id: '2606.32007'
url: https://arxiv.org/abs/2606.32007
pdf_url: https://arxiv.org/pdf/2606.32007
published: '2026-06-30'
collected: '2026-07-01'
category: Agent
direction: 智能体代码生成 · 形式化验证优化
tags:
- Code Generation
- Agentic LLM
- Formal Verification
- Benchmark
- Iterative Repair
one_liner: 提出验证器引导的迭代修复智能体框架与Dafny编程基准，大幅提升形式化验证代码生成准确率
practical_value: '- 智能体迭代修复架构可迁移到推荐系统规则校验场景：生成的营销文案、活动规则先用规则引擎做确定性校验，再返回LLM迭代修改，降低违规风险

  - 两阶段审核机制可复用：先做确定性规则拦截（违禁词、格式错误等），再用LLM做语义校验，平衡审核效率与准确率

  - 滚动记忆模块设计可借鉴：每次迭代保留前序尝试的错误反馈和经验总结，减少智能体重复犯错，提升任务收敛速度'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有代码生成智能体多依赖有限测试用例校验，无法覆盖所有边界case，形式化验证可提供更严谨的逻辑正确性反馈信号，但面向验证语言的智能体架构和公开基准非常匮乏，且Dafny这类小众验证语言训练数据极少，直接生成的代码验证通过率极低，亟需适配的智能体架构提升效果。

### 方法关键点
- 迭代式智能体架构：由proposer生成可执行代码+证明注解，reviewer分两阶段校验：先做确定性规则检查（禁止弱化规约、使用绕过验证的作弊语法），再调用Dafny验证器返回错误诊断信息，反馈给proposer迭代修复
- 滚动上下文管理：每次迭代保留前序尝试的代码、反馈、经验总结，避免智能体重复犯同类错误
- 配套构建LCB-Pro-Dafny基准：翻译250道竞赛级编程题到Dafny，包含自然语言描述、形式化规约，配套自动化评估套件

### 关键实验
- DafnyBench（证明补全任务）：AxDafny搭配Gemini-3.1-Pro达到92.7%的验证通过率，比此前最优基线高6.5个百分点，且无需依赖人工构建的证明提示库
- LCB-Pro-Dafny（端到端代码生成任务）：AxDafny整体通过率56.4%，远高于GPT-5.5直接生成的11.6%；其中简单题通过率75%、中等题52%、难题28%
- 额外测试：验证通过的Dafny代码编译为Python后，运行失败基本都是超时/内存不足，几乎无逻辑错误，验证了形式化验证对逻辑正确性的强保障能力

### 核心结论
形式化验证的通过和运行时性能是两个完全独立的目标，仅靠验证无法保证代码满足资源约束。
