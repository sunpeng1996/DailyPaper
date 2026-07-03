---
title: 'Reasoning effort, not tool access, buys first-try reliability in agentic code
  generation: an observational study'
title_zh: 观察研究：Agent代码生成中推理投入比工具访问更能提升首次成功率
authors:
- Achint Mehta
affiliations:
- TrendAI
arxiv_id: '2607.02436'
url: https://arxiv.org/abs/2607.02436
pdf_url: https://arxiv.org/pdf/2607.02436
published: '2026-07-02'
collected: '2026-07-03'
category: Agent
direction: Agent 代码生成效果优化
tags:
- Agent
- Code Generation
- Observational Study
- Prompt Engineering
- LLM Evaluation
one_liner: 通过90次受控代码生成Agent实验，证明提升推理投入比额外工具访问对首次尝试可靠性的收益更高
practical_value: '- 业务Agent优化优先提升推理努力而非盲目堆工具：开启更高阶推理模式仅增9%-29%成本，即可将首次完美运行率从28%提至89%、人工干预次数降5倍，ROI远高于加额外工具

  - 要特定输出效果（如电商推荐文案风格、商品页视觉要求）直接加1段短明确指令即可，无需长prompt：1段精简设计提示可实现和全量长提示完全一致的视觉效果提升，从3分涨至4.5-5分

  - Agent效果评估不要仅看最终修复后总分，需新增首次尝试成功率、人工干预次数两个指标：总分差不足1分的模型，核心功能首次通过率可差3-4倍，直接对应落地的人工成本

  - 加工具前先对齐核心故障类型：本研究中前端测试工具完全覆盖不到占55%故障的构建/环境问题，仅提升42%-68%成本无任何收益'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
业界给代码Agent加工具、长系统提示的做法默认收益大于成本，但缺乏受控对比实验验证；现有基准多测单次短任务、仅报最终修复后总分，掩盖了首次尝试可靠性、不同配置的真实效果差异，无法指导业务落地的资源投入优先级。

### 方法关键点
- 90次独立受控Agent运行，统一任务为实现带WebSocket实时同步的回顾看板应用，所有运行采用相同详细需求规格，控制单一变量迭代
- 变量覆盖5个模型家族、2种Agent框架、2档推理努力（High/xHigh）、是否开启Playwright前端测试工具、3种设计提示配置（无/全量/1段精简版），相同配置多次重复消除随机性
- 评估维度：14项功能指标总分（满分42）、首次尝试完美率、人工修正提示次数、视觉质量1-5分评分、token成本拆解

### 关键结果
- 加Playwright测试工具使成本提升42%-68%，功能得分、首次成功率无任何提升，额外成本全部花在上下文重读而非生成有效代码
- 推理努力从High升到xHigh，首次完美成功率从28%涨到89%，人工修正提示次数降5倍，仅增加9%-29%的成本
- 1段精简设计提示和全量长设计提示效果完全一致，视觉评分从3.0升到4.5-4.7，功能得分无提升，交互类功能故障率略有上升
- 模型总分差异不到1分的情况下，Docker部署首次通过率可从19%差到75%，最终总分完全掩盖首次可靠性差异

**最值得记住的一句话**：Agent资源投入要匹配故障类型，同样预算优先投推理努力而非盲目加工具，要什么效果直接在prompt里明确说明即可
