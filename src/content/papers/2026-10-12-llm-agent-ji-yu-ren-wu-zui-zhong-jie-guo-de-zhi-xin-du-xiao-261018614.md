---
title: Can an Agent Learn to Predict Its Own Failure? Outcome-Grounded Confidence
  Calibration in LLM Agents
title_zh: LLM Agent 基于任务最终结果的置信度校准方法
authors:
- Ashutosh Hathidara
affiliations:
- SAP
arxiv_id: '2610.18614'
url: https://arxiv.org/abs/2610.18614
pdf_url: https://arxiv.org/pdf/2610.18614
published: '2026-10-12'
collected: '2026-10-15'
category: Agent
direction: Agent 置信度校准与失败预判
tags:
- LLM Agent
- Confidence Calibration
- GRPO
- Reinforcement Learning
- Outcome Grounding
one_liner: 基于GRPO用多步任务最终结果校准LLM Agent每步置信度，实现可靠的早期失败预判
practical_value: '- 电商导购、客服、售后类Agent可直接复用这套方案：要求Agent每步输出带<conf>标签的置信度，基于最终成单/问题解决率作为校准标签，无额外标注成本，低置信度路径可提前转人工，大幅降本提效

  - 推荐系统的Agent化多轮交互场景（如复杂需求导购、套装组合推荐）可增加置信度校准逻辑：top10%高置信度路径直接执行，低置信度路径提前召回/切换策略，避免无效交互损失用户体验

  - 工程实现优先选RLOO作为优势估计器，效果优于GRPO、PPO；冷启动阶段不要用带learned value critic的PPO，大概率学不到有效格式；校准奖励选Brier即可，不用纠结其他proper
  scoring rule形式，效果差异极小

  - 校准后的置信度更适合做任务级分诊，不用追求极细粒度的排序，高置信度区间直接放行即可，最顶端的1%置信度样本反而存在过拟合，稳定性差'
score: 9
source: huggingface-daily
depth: full_pdf
---

### 动机
长horizon任务下LLM Agent的每步决策不确定性会持续累积，现有置信度校准方法仅针对单步或单答案的正确性，无法预判整个任务的最终成败，无法支撑运行时的继续执行/放弃/转人工决策；小模型自报告的口头置信度基本接近随机水平，没有实用价值。

### 方法关键点
- 要求Agent每步输出动作时附带<conf>0-100</conf>标签的口头置信度，校准目标是每步置信度匹配当前路径最终成功的概率P(Y=1|h_t)
- 基于GRPO框架，同一任务的多轮rollout的最终成功/失败标签直接复用为每步置信度的标注，无需额外标注成本
- 每步奖励由三部分组成：校准奖励（默认用Brier proper scoring rule）+ 格式合规奖励 + 置信度分布正则项，优势计算同时考虑任务最终结果和置信度校准质量
- 支持离线RL（基于历史轨迹训练）和在线RL（和环境交互实时训练）两种模式，用LoRA微调基座，训练成本低

### 关键结果
实验基于ALFWorld、TextWorld、WebShop三个Agent benchmark，基座用Qwen2.5-7B/14B，对比无训练模型、仅格式训练的baseline：
1. 离线训练后，三个环境的步级置信度预判最终结果的AUROC从近随机（0.462~0.578）提升到0.681~0.850，top10%高置信度步骤的成功率是平均水平的4.3倍
2. 在线训练后，ALFWorld环境的Expected Calibration Error（ECE）从0.42降至0.05~0.12，早期窗口AUROC提升0.048~0.101，任务成功率无下降

### 最值得记住的一句话
基于任务最终结果校准的Agent置信度是几乎无额外标注成本的可靠早期分诊信号，核心价值是提前识别Agent必然失败的任务，而非判断同任务下不同尝试的优劣。
