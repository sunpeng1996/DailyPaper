---
title: 'Profiling a Frontier Agent with EBench: From Direct Control to Harness with
  Policy'
title_zh: 基于EBench的前沿Agent能力画像：从直接控制到策略调度
authors:
- Yifei Yao
- Yude Zou
- Guanbo Jiao
- Xing Gao
- Ning Gao
- Yukai Wang
- Jiantong Chen
- Zihou Zhu
- Xinyu Li
- Ningyu Yan
affiliations:
- Shanghai Artificial Intelligence Laboratory
- Shanghai Jiao Tong University
- Fudan University
- Zhejiang University
arxiv_id: '2610.35832'
url: https://arxiv.org/abs/2610.35832
pdf_url: https://arxiv.org/pdf/2610.35832
published: '2026-10-26'
collected: '2026-10-27'
category: Agent
direction: Agent 能力评测与策略调度优化
tags:
- Agent
- MLLM
- VLA
- WAM
- Policy Orchestration
- Embodied AI
one_liner: 对比GPT-6-Astra直接控制与调用VLA/WAM的机器人操控表现，定位能力边界并给出Agent调度优化方向
practical_value: '- 分层Agent架构可直接复用至推荐/广告系统：LLM负责用户需求理解、任务规划、异常修复，将高频、标准化的召回/排序/内容生成逻辑下沉为可调用的领域策略，相比LLM直接生成结果，成本降低、可控性提升

  - 能力边界量化方法可迁移到业务优化：先分别评测LLM直接执行、独立领域策略的效果边界，再组合评测调度模式的表现，针对性优化调度逻辑，避免无效调用浪费资源

  - 单样本ICL+工具调用的范式适配业务冷启动场景：新类目推荐、新营销活动落地等缺标注数据的场景，仅需少量示例即可快速上线Agent能力，无需大量域内微调

  - 降本技巧可复用：将高token消耗的连续执行逻辑下沉到小模型，LLM仅在关键决策点介入，可大幅降低调用成本，适合大流量业务上线'
score: 9
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
前沿MLLM无需机器人领域微调就能控制机器人，但直接控制和调用后训练VLA/WAM策略两种模式的能力边界、互补性尚未被系统量化，现有Agent调度框架的优化方向不明确。

### 方法关键点
- 采用EBench机器人操控基准，覆盖26类任务、510个测试episode，包含长短时序、不同精度、桌面/移动场景、多维度泛化测试，统一观测协议，所有配置仅接收RGB图和机器人本体状态，无额外深度/标定信息
- 测试两类Agent配置：1）直接控制：GPT-6-Astra直接生成末端执行器指令；2）策略调度模式：GPT-6-Astra可调用后训练VLA（π0.5）或WAM（InternW0-Δ）执行动作，仅保留规划、进度监控、错误恢复能力
- 所有配置单任务仅输入1个标注好的演示样例做ICL，无参数更新

### 关键结果
- 直接控制模式下，GPT-6-Astra整体成功率46.7%，超过6个在6600条域内数据上微调的VLA/WAM，短时序任务成功率73.2%排名第一，泛化维度性能波动最小，但长时序/桌面/高精度任务成功率仅27.3%/20.0%/11.3%
- 策略调度模式下，调用InternW0-Δ时整体成功率达56.0%，超过所有对比的单模型策略，token成本降低50%以上；但高精度任务表现仍低于独立策略，存在策略调用不合理、无段子目标传递、控制权切换时抓握失效等问题

> 最值得记住的结论：大模型做上层规划调度、领域小模型做底层执行的分层Agent架构，是平衡效果、成本、可控性的最优落地路径之一
