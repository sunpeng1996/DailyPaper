---
title: How Much of a Harness Does a Strong Agent Need for Autonomous ML Engineering?
title_zh: 强Agent实现自主机器学习工程所需最小外部辅助框架评估
authors:
- Kirill Brilliantov
- Alejandro Hernández-Cano
- Emmanuel Abbé
affiliations:
- EPFL
- Apple
arxiv_id: '2609.40303'
url: https://arxiv.org/abs/2609.40303
pdf_url: https://arxiv.org/pdf/2609.40303
published: '2026-09-30'
collected: '2026-10-01'
category: Agent
direction: Agent架构优化 · 最小工具Agent基线
tags:
- LLM-Agent
- Coding-Agent
- Multi-Agent-Orchestration
- Harness-Ablation
- MLE-Agent
one_liner: 控制变量下证明前沿LLM单会话最小工具Agent优于复杂多Agent编排的MLE辅助框架
practical_value: '- 做业务Agent优先给强LLM配直接读写、执行环境的原生工具权限，而非先做复杂多Agent编排/树搜索脚手架，ROI更高

  - 当LLM已具备工具调用、长上下文能力时，可先测单会话长运行Agent的基线效果，再评估是否需要额外加多Agent协调、任务拆分模块，避免过度工程

  - 资源有限时，优先投入提升Agent backbone的工具调用能力、长上下文支持，而非在弱backbone上堆复杂harness逻辑，符合Sutton bitter
  lesson规律

  - 多Agent并行方案要解决好结果自选择的一致性问题，否则并行带来的天花板提升无法转化为实际落地效果'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
当前自主MLE Agent普遍叠加复杂harness（多Agent编排、树搜索、记忆分层等），但LLM本身工具调用、长上下文能力快速提升后，harness的价值未被严格验证；之前的性能对比未控制backbone、硬件、时间预算变量，增益归属不清晰。
### 方法关键点
- 设计最小基线Agent Malena：单会话长运行，仅配备文件读写、代码执行、提交管理、资源查询4个基础工具，无额外编排逻辑
- 分层消融harness四类核心模块：编码Agent环境、搜索原语、自主控制权、多Agent编排，所有实验控制相同算力、时间、backbone
- 对比4个开源SOTA MLE harness，跨GLM 5.2、Kimi K3、DeepSeek V4、Gemma 4等多个主流前沿backbone测试
### 关键实验结果
- 仅给LLM配编码Agent执行环境，性能提升幅度远高于其他所有harness模块叠加的效果；额外加搜索策略、多Agent编排均无统计显著的性能提升
- 相同24h时间、1×A100 80GB算力下，Malena在所有前沿backbone上匹配或优于4个SOTA harness：GLM 5.2 backbone下Malena的奖牌率达62.5%，比最优外部harness高15.4个百分点
- 仅在较弱的Gemma 4 31B backbone上，复杂harness才有小幅性能优势，置信区间仍与Malena重叠
### 核心结论
对于已具备强自主工作能力的LLM，投入优化harness脚手架的回报极低，核心杠杆在backbone能力和原生运行环境支持，而非外层人工设计的编排逻辑
