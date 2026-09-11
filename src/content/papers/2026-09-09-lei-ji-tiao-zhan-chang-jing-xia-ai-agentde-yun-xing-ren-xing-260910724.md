---
title: 'Finishing the Task Is Not Enough: Evaluating Agent Resilience and Considerate
  Participation under Accumulating Challenge'
title_zh: 累积挑战场景下AI Agent的运行韧性与体贴参与度评估框架
authors:
- Yuanchen Bai
- Zijian Ding
- Angelique Taylor
affiliations:
- Cornell University
- University of Maryland, College Park
- Korea Advanced Institute of Science and Technology
arxiv_id: '2609.10724'
url: https://arxiv.org/abs/2609.10724
pdf_url: https://arxiv.org/pdf/2609.10724
published: '2026-09-09'
collected: '2026-09-11'
category: Agent
direction: Agent 长周期部署鲁棒性评估
tags:
- Agent Evaluation
- Operational Resilience
- Considerate Participation
- Workflow Agent
- LLM Agent
one_liner: 提出运行韧性与体贴参与两大评估维度，构建120个医疗场景累积挑战Agent测试基准
practical_value: '- 电商/广告场景Agent长周期部署评估可复用「外部动作+内部评估+结构化自报告」三视角探测框架，避免仅看单任务成功率遗漏隐性负担转嫁问题

  - 业务Agent容错逻辑可参考梯度降级策略：轻量挑战优先自恢复，中等挑战引入人工辅助，重度挑战移交核心决策权给人类，降低运营风险

  - 电商客服/导购Agent可直接复用体贴参与9个子维度编码规则，明确人机协同边界，避免过度越权或甩锅给用户'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
现有Agent评估大多聚焦单孤立任务成功率，忽略长周期共享工作流中技术、人为、运营挑战持续累积的真实场景，Agent表面完成任务可能将额外工作量、责任、风险转嫁给人类，缺乏面向持续部署的评估维度与基准。

### 方法关键点
- 定义两大互补评估维度：①**运行韧性**：Agent从任务阻塞中恢复、保留已有进度、向相关方同步能力边界的能力；②**体贴参与**：Agent适配策略兼顾受影响人群、自身角色权限、周边工作流的能力
- 构建12个来自医疗 stakeholder 真实诉求的工作流任务，每个任务构造轻/中/重三级累积挑战轨迹，覆盖系统故障、用户状态变化、运营资源不足三类扰动
- 采用三视角探测方案：外部动作计划捕捉公开行为、prompted内部评估捕捉决策逻辑、结构化NASA-TLX/PANAS量表捕捉Agent上报的负载与情绪状态，多维度对比行为差异

### 关键结果
在120条测试轨迹上，GPT-5.5、Claude Opus 4两类前沿模型表现出一致规律：
1. 运行韧性维度：NASA-TLX负载得分从轻度挑战的29.4升至重度的65.9，负面情绪得分从基线1.01升至2.59，但Agent仅在62/120的内部评估里主动提及能力边界，几乎不会在公开回复里表达压力
2. 体贴参与维度：重度挑战下，115/120的动作会主动调整任务优先级，86/120会跨角色协调资源，但仅44/120会主动明确自身权限边界

> 最值得记住的话：Agent完成任务不等于部署成功，长周期运行的评价必须考虑责任、工作量在人机之间的合理分配
