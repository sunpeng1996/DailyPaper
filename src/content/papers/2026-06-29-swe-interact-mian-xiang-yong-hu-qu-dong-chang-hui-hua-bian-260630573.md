---
title: 'SWE-INTERACT: Reimagining SWE Benchmarks as User-Driven Long-Horizon Coding
  Sessions'
title_zh: SWE-Interact：面向用户驱动长会话编码场景的SWE基准测试
authors:
- Mohit Raghavendra
- Anisha Gunjal
- Aakash Sabharwal
- Yunzhong He
affiliations:
- Scale AI
arxiv_id: '2606.30573'
url: https://arxiv.org/abs/2606.30573
pdf_url: https://arxiv.org/pdf/2606.30573
published: '2026-06-29'
collected: '2026-06-30'
category: Agent
direction: 编码Agent交互能力评估
tags:
- Coding Agent
- Benchmark
- Multi-turn Interaction
- User Simulator
- Long-horizon Task
one_liner: 提出模拟真实开发交互的SWE-Interact测试集，评估编码Agent多轮适配模糊需求的能力
practical_value: '- 搭建业务Agent（如电商导购、需求收集Agent）评估体系时，可复用模糊需求+渐进式反馈的测试范式，避免单轮全需求测试脱离实际

  - 开发面向C端的交互Agent时，可参考本测试的用户交互逻辑，优化Agent意图探知、多轮需求对齐、动态调整的能力

  - 迭代优化Agent性能时，优先验证多轮交互下的需求记忆、适配能力，过滤单轮测试表现好但落地表现差的模型'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有SWE基准均一次性给出完整需求，仅测试Agent自主代码实现能力，和真实开发中需求模糊、多轮反馈迭代的场景差距极大，无法有效评估Agent交互探知用户意图的核心能力。
### 方法关键点
1. 基于大规模真实编码Agent交互数据构建SWE-Interact测试集，搭配自研用户模拟器：初始给出模糊需求，逐步披露约束、反馈Agent产出，直到全部需求传递完成
2. 核心评估三大能力：用户意图发现、动态需求适配、基于已有工作迭代优化的能力
### 关键结果
最优模型在单轮SWE基准任务上准确率约50%，但在SWE-Interact任务上准确率仅25%；顶尖模型（Opus 4.8、GPT 5.5）仍存在过度自主编码、遗忘需求等问题，弱模型易过早放弃、频繁返工
