---
title: 'When LLMs Forget What They Believe: Characterizing State Integrity Collapse
  in Long-Horizon Dialogues'
title_zh: 长对话场景下大语言模型状态完整性崩溃的特征分析
authors:
- Yancheng Zhu
- Yifan Yuan
affiliations:
- School of Artificial Intelligence, Shenzhen University
arxiv_id: '2610.31314'
url: https://arxiv.org/abs/2610.31314
pdf_url: https://arxiv.org/pdf/2610.31314
published: '2026-10-22'
collected: '2026-10-23'
category: LLM
direction: LLM长对话 · 约束合规性评估
tags:
- Long-Horizon Dialogue
- State Integrity Collapse
- Instruction Following
- LLM Evaluation
- Constraint Compliance
one_liner: 提出状态完整性崩溃概念与测试基准，揭示长对话中LLM约束记忆与行为合规的解离现象
practical_value: '- 多轮电商导购/客服Agent设计时不要仅依赖RAG解决约束遵从问题，88.6%的失败是记住约束但行为漂移，需额外增加生成后合规校验环节

  - 优先对数值、格式、逻辑类符号约束做加固，这类约束比事实、人设类约束合规率低8-12个百分点，可采用Structured State Anchoring(SSA)方案，每轮前置激活活跃约束，最高可提24.4个点合规率

  - 上线前可参考STATETRACK-BENCH范式对对话Agent做多轮压力测试，重点观测12轮以上的约束遵从衰减，避免短轮评估遗漏长对话漂移问题

  - 电商导购的用户偏好（如价格上限、品类排除规则）属于易漂移的数值/逻辑约束，可单独维护活跃状态注册表，每轮生成前注入，减少SIC带来的错误推荐'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有单/短轮指令遵循评估无法满足长对话部署需求，很多场景下LLM能复述约束却不执行，这类状态完整性崩溃（SIC）比普通遗忘更隐蔽，在电商客服、导购等场景可能造成用户投诉、资损等实质危害，普通记忆优化方案（如更长上下文、RAG）无法直接解决这类行为漂移问题。

### 方法关键点
- 定义SIC：区别于普通遗忘，指LLM可被探测到记住约束，但后续对话中不再遵守的记忆-行为解离现象
- 构建STATETRACK-BENCH基准，覆盖数值、格式、人设、事实记忆、逻辑规则5类约束，对话深度覆盖3/5/7/10/12轮，采用分叉评估：同一对话前缀下分别测约束回忆率和行为合规率，分离记忆失败和行为漂移
- 提出结构化状态锚定（SSA）干预方案：每轮前置注入活跃约束+生成后校验+最多2次重试，无需训练即可提升合规性

### 关键实验
在7个主流闭源LLM上测试，核心结果：整体严格联合留存率（同时满足当前请求+约束）范围62.4%~100%，88.6%的失败属于行为漂移而非记忆丢失，排除表现最差的Gemini-3.1-Pro后该比例仍达84.4%；符号类约束（数值、格式、逻辑）的合规率比语义类（事实、人设）低8-12个百分点，对话深度到50轮时数值约束的SIC率可达20.8%；SSA方案在Gemini-3.1-Pro上最多提升24.4个点的合规率，其他模型提升2.4~8个点。

### 核心结论
单轮指令遵循能力无法推断长对话可靠性，评估必须追踪被记住的约束是否仍能实际指导生成行为。
