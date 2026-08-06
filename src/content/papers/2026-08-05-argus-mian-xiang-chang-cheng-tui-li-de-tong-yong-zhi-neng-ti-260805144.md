---
title: 'Argus: A General-Purpose Agentic Runtime for Long-Horizon Reasoning'
title_zh: Argus：面向长程推理的通用智能体运行时
authors:
- Boxiu Li
- Zimo Wen
- Yijia Fan
- Junxiang Lei
- Sufeng Guo
- Jiaao Wu
- Ruize Tang
- Mukai Li
- Yifei Shen
- Xiaoyu Chen
affiliations:
- Microsoft
- Shanghai Jiao Tong University
- Fudan University
- Nanjing University
- Tsinghua University
arxiv_id: '2608.05144'
url: https://arxiv.org/abs/2608.05144
pdf_url: https://arxiv.org/pdf/2608.05144
published: '2026-08-05'
collected: '2026-08-06'
category: Agent
direction: 长程推理Agent · 运行时自进化
tags:
- Agent Runtime
- Long-Horizon Reasoning
- Verification Gating
- Fixed-Model Self-Evolution
- Multi-Role Agent
one_liner: 提出验证门控的多角色固定模型自进化智能体运行时，适配长周期复杂推理任务
practical_value: '- 多角色分工框架可直接复用在推荐系统迭代、营销活动全链路自治、商家自动化运营等业务Agent项目中，避免单一Agent目标漂移，提升落地稳定性

  - 验证门控的固定模型自进化机制无需微调LLM，仅靠沉淀可复用的技能、失败路径、校验规则即可逐步降低长任务的token消耗和耗时，适配算力受限的业务场景

  - 长任务拆分bounded missions的方案可迁移到大促预案生成、新品全生命周期运营等长周期Agent任务，避免执行中断后全链路重跑，提升容错性'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有长程推理Agent默认目标固定，实际科研、软件开发、长周期业务运营等复杂场景下，目标、约束会随执行动态调整，无约束的策略切换易出现目标漂移；同时单会话架构易丢失上下文、重复执行无效步骤，无法沉淀经验降低后续任务成本。
### 方法关键点
- 四角色权责拆分：Manager锚定用户核心意图、管控阶段流转，Planner拆解为边界清晰的子任务，Engineer执行落地，Reviewer独立校验结果，低风险任务允许Engineer自审核
- 运行时状态与LLM参数解耦，记忆、技能、校验规则、失败路径、路由策略等可复用资产，必须经对应角色的证据校验后才存入持久化状态，实现固定模型下的自进化
- 长任务拆分为多个独立的bounded missions，执行中断后可从持久化状态直接恢复，无需全链路重跑
### 关键结果
跨7个基准测试集验证：SWE-Bench Pro上准确率达78%，较Direct Copilot高19pct，仅消耗1.41倍总token；成熟运行阶段较启动阶段，单任务求解token消耗降低21%，活跃工作流耗时降低15%；AARRI-Bench科研任务准确率76.8%，数学数据合成任务领先baseline 28个百分点。
最值得记住的一句话：固定LLM权重时，通过验证门控沉淀可复用经验也能持续提升长程任务效率，比反复微调模型更适配业务落地的迭代需求。
