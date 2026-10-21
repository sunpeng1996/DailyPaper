---
title: Harness Self-Evolution for Long-Horizon Terminal Agents
title_zh: 面向长程终端智能体的Harness交互框架自演化方法
authors:
- Ruhan Wang
- Yucheng Shi
- Zongxia Li
- Junyao Yang
- Zhongzhi Li
- Yue Yu
- Haitao Mi
- Dongruo Zhou
- Leoweiliang
affiliations:
- Tencent HY LLM Frontier
- Indiana University
- University of Maryland, College Park
- University of Georgia
- National University of Singapore
arxiv_id: '2610.27435'
url: https://arxiv.org/abs/2610.27435
pdf_url: https://arxiv.org/pdf/2610.27435
published: '2026-10-19'
collected: '2026-10-21'
category: Agent
direction: 长程Agent · Harness自演化与可靠性优化
tags:
- Agent
- Harness Evolution
- Long-Horizon Agent
- Agent Reliability
- Self-Improvement
one_liner: 固定模型权重下通过迭代优化交互Harness提升长程Agent任务成功率与执行一致性
practical_value: '- 不需要微调LLM权重，仅优化Agent交互层（如工具调用、上下文管理、终止判断逻辑）就能提升任务稳定性，适合业务场景下模型固定时的快速迭代

  - 可复用「成功-失败轨迹对比+ runtime trace埋点+问题聚合」的诊断范式，定位推荐/搜索Agent的工具调用错误、上下文丢失等问题

  - 跨框架复用成熟Harness机制的思路可迁移：如电商导购Agent可直接借鉴现有框架的用户意图确认、多轮会话状态管理实现，减少重复开发

  - 业务Agent上线前可复用pass@k、flip率等指标评估执行一致性，避免单次运行成功就上线的漏测问题'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
长程Agent单次运行可完成任务但重复执行一致性差，随机生成的局部误差会在后续交互中传播，导致任务成功率与可靠执行能力存在明显gap；现有基于微调的优化方案成本高、迭代慢，而负责工具调用、上下文管理、终止判断的交互层Harness的性能潜力未被充分挖掘，亟需不修改模型权重的可靠性提升方案。

### 方法关键点
- 核心框架RiseHarness：固定模型权重，聚焦「翻转任务」（同配置下既有成功也有失败运行的任务）开展迭代优化
- 双轨trace采集：同时记录Agent交互轨迹与Harness内部运行日志，结合Harness Handbook（行为-代码映射库）定位根因，明确是模型决策错误还是Harness机制缺陷
- 外部机制复用：检索其他开源Harness框架的相关实现，适配当前交互流程与模型行为生成修改方案
- 灰度验证机制：候选修改先做行为校验，再通过重复任务评测，只有指标达标才进入下一轮迭代

### 关键实验结果
在TBH（100个长程终端任务）、TB2.1（89个迁移任务）上测试，对比Terminus-2基线等方案：
- 针对DeepSeek-V4-Flash，TBH Pass@1提升7.25%，Pass4（4次全成功比例）提升14%，flip率下降12%；迁移到TB2.1 Pass@1提升7.3%
- 针对GPT-6-sol，TBH Pass@1提升5.25%，迁移到TB2.1 Pass@1提升3.09%
- 消融实验显示，去除Harness trace+Handbook会损失7%的Pass@1增益，去除外部机制复用损失5.5%的Pass@1增益

### 核心结论
LLM的能力上限不只是模型本身决定的，交互层Harness的优化可以在不修改权重的前提下大幅释放模型现有能力的可靠性
