---
title: Real-Time Detection and Repair of LLM Agent Failures
title_zh: LLM Agent故障实时检测与修复：微秒级无额外LLM开销的监控方案
authors:
- Sunny Dubey
arxiv_id: '2608.02464'
url: https://arxiv.org/abs/2608.02464
pdf_url: https://arxiv.org/pdf/2608.02464
published: '2026-08-03'
collected: '2026-08-04'
category: Agent
direction: LLM Agent 运行时故障检测与修复
tags:
- LLM Agent
- Anomaly Detection
- Runtime Monitoring
- Failure Recovery
- Telemetry
one_liner: 仅依赖运行时可观测遥测实现微秒级LLM Agent故障检测，结合确定性校验修复提升任务成功率
practical_value: '- 业务侧部署Agent（如电商导购Agent、推荐理由生成Agent）时，可复用分层检测架构：先上微秒级遥测统计监控覆盖循环、工具调用错误、目标漂移类故障，再叠加确定性校验（工具返回格式校验、数值溯源校验）覆盖内容篡改、幻觉类故障，成本比全链路LLM-as-judge低90%以上

  - 故障修复阶段可直接复用「仅告知故障检查类型、不提供具体修正值」的策略，比给出具体修正值的修复成功率更高，无额外Prompt工程成本，可直接落地于电商Agent回复纠错、广告文案生成纠错场景

  - 该监控方案需基于当前部署环境的健康运行数据校准，不要跨模型、跨任务直接迁移；校准仅需健康运行轨迹，不需要故障标注，适配电商业务快速迭代的Agent部署需求'
score: 9
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有LLM Agent运行时故障检测普遍依赖第二个LLM作为judge逐步骤校验，成本甚至超过Agent本身的运行开销，且无法做到实时告警；同时多数方案需要故障标注训练，落地门槛高，难以适配大规模业务Agent部署的低延时、低成本需求。

### 方法关键点
- 仅用运行时可观测遥测数据（步骤输出语义哈希嵌入、token不确定性聚合、动作元数据、9维内容接地特征）作为输入，不需要模型内部权重、不需要故障标注，仅在健康运行轨迹上训练
- 分层检测架构：第一层是基于回声状态网络（ESN）集成+CUSUM告警的时序异常检测器，单步耗时~200μs；第二层是确定性校验模块，包含工具返回格式校验、数值溯源校验、任务覆盖度校验三类规则，零假阳
- 故障修复策略：检测到故障后回滚到上一个事实采集步骤重跑，仅告知故障检查类型即可实现最优修复效果

### 关键结果
在2823条真实Agent运行轨迹（覆盖Qwen2.5、Llama3.1、Gemini-2.5-flash三类模型，LangGraph、AutoGen等三类框架）上验证：
1. 时序检测器对循环、工具调用错误、目标漂移类故障检测率分别达0.48~1.0、0.17~1.0、0.66~0.86，结合内容接地特征后内容篡改类故障检测率从0.28提升到0.59
2. 确定性校验模块故障召回率60%（加覆盖度校验达96%），假阳率为0；整体修复后任务成功率从52%提升到73%，单步额外开销不到1ms，仅为LLM-as-judge方案开销的千分之一

最值得记住的一句话：监控和LLM judge的故障覆盖盲区互补，分层检测架构可以用极低的成本覆盖绝大多数Agent故障，只有边界场景才需要调用LLM judge
