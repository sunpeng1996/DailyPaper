---
title: Coding Agents with an Obstacle-Aware Harness for Safe Robot Manipulation
title_zh: 配备障碍感知管控模块的安全机器人操作编码Agent
authors:
- Bingxin Xu
- Yuzhang Shang
- Zhen Dong
- Emilio Ferrara
affiliations:
- USC
- UCF
- UCSB
arxiv_id: '2609.20822'
url: https://arxiv.org/abs/2609.20822
pdf_url: https://arxiv.org/pdf/2609.20822
published: '2026-09-17'
collected: '2026-09-19'
category: Agent
direction: Agent安全约束优化 · 机器人操作场景
tags:
- CodingAgent
- SafetyConstraint
- ObstacleAvoidance
- RobotManipulation
- SafeHarness
one_liner: 提出SafeHarness障碍感知管控框架，解决编码Agent机器人操作中的安全约束优先级缺失问题
practical_value: '- 做带硬约束的Agent规划时，可参考将任务拆分为「路径阶段+关键执行阶段」双阶段分别注入约束，避免约束被核心目标的优先级覆盖

  - 可复用「预规划-校验-重规划」的执行流设计，在电商履约调度、合规审核类Agent中加入硬约束校验环节，降低违规风险

  - 将抽象约束（如避障、合规）落地为可量化的校验规则（如本文用bounding box判定路径合规），可降低LLM对约束的理解偏差'
score: 4
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有编码Agent机器人操作范式仅以任务完成为核心目标，忽略安全约束，在带避障要求的场景中碰撞率极高；根源是规划环节未将安全约束设为高优先级，同时缺乏路径校验、重规划机制，执行阶段也未将约束落地。
### 方法关键点
提出SafeHarness框架，拆分操作任务为路径规划、接触执行两个阶段分别嵌入障碍感知管控：
1. 路径阶段将物体映射为bounding box，生成候选路径点序列，执行前校验路径合规性，不可行则触发重规划
2. 接触执行阶段筛选接触点位置，确保接触操作本身也避开障碍
### 关键结果
SafeHarness任务成功率达71.9%，避障率达87.5%，较原有SOTA分别提升6.5pct、27.0pct，较无管控的同基线Agent分别提升2.3倍、1.5倍
