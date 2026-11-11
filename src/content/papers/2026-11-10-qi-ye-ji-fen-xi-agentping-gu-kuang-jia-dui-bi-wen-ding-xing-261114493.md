---
title: 'Comparative Analysis of Agent Evaluation Frameworks: Stability, Detection,
  and Discovery in Enterprise Analytics Agents'
title_zh: 企业级分析Agent评估框架对比：稳定性、故障检测与风险发现
authors:
- Howard Zhang
- Chuck Arvin
- Logan Brown
- Mihir Bhatia
- Neelu Choudhary
- Lily Miao
affiliations:
- Amazon
arxiv_id: '2611.14493'
url: https://arxiv.org/abs/2611.14493
pdf_url: https://arxiv.org/pdf/2611.14493
published: '2026-11-10'
collected: '2026-11-11'
category: Eval
direction: Agent 评估框架对比与落地优化
tags:
- Agent Evaluation
- LLM-as-a-Judge
- Red Teaming
- Evaluation Stability
- Enterprise Agent
one_liner: 对比三类Agent评估范式优劣势，提出分层结合的企业级Agent落地评估方案
practical_value: '- 落地Agent评估优先采用分层策略：用trace-based LLM judge做功能评估（F1达0.90，误报率仅10%），搭配text-only红队框架做安全评估，覆盖两类无重叠的故障场景

  - LLM-as-a-Judge选型优先选Claude Haiku/Sonnet 4.6，Qwen3 32B在trace评估场景下稳定性不足，不建议用于高一致性要求的评估任务

  - 内部Agent评估不要完全依赖人工抽检，研究显示人工会漏掉12.5%的语法正确但语义错误的故障，搭配带领域规则的LLM评估器可补全这类漏检

  - 纯确定性规则（如字符串匹配、正则）仅适合做已知结构类错误的前置校验，不要用于复杂Agent的全链路评估，其对语义类故障召回率为0'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
企业场景下LLM驱动的分析Agent需执行SQL生成、多工具调用等复杂工作流，语法正确但语义错误的故障易逃过人工抽检，现有三类评估范式（trace-based LLM judge、text-only LLM judge、确定性规则）缺乏系统性的性能对比，无法可靠覆盖功能故障与安全风险，亟需可落地的评估选型方案。
### 方法关键点
- 选取三类代表性评估框架：Strands Evals（可访问全OpenTelemetry执行链路的trace-based LLM judge）、PromptFoo（仅访问输入输出的text-only LLM judge+红队测试能力）、Agenta（纯字符串匹配的确定性规则评估，零LLM成本）
- 三阶段实验设计：阶段1量化评估稳定性，阶段2测试已知故障检测能力，阶段3测试未知风险发现能力，全程采用冻结执行trace消除Agent本身随机性的干扰
- 评估对象为亚马逊内部两个供应链分析Agent，覆盖SQL结构错误、语义错误两类典型故障模式
### 关键实验
- 基于72个专家标注的测试用例，累计完成11700次评估；97%的(框架+模型)配置达到稳定性阈值（组内标准差≤0.15）
- trace-based框架检测已知故障的F1达0.90，误报率仅10.3%，比text-only框架误报低5倍；纯确定性规则对语义类SQL故障召回率为0
- 两类LLM评估框架共发现24个未知故障，功能测试和安全测试发现的故障零重叠；LLM评估器补全了人工漏检的12.5%语义类故障
### 核心结论
评估框架的信息访问权限是决定评估质量的核心因素，没有单一框架能覆盖所有需求，功能+安全的分层评估是企业Agent落地的最优策略。
