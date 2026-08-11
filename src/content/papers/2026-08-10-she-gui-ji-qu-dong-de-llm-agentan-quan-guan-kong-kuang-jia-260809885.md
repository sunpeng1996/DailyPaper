---
title: 'SHE: Trajectory-driven Safety Harness Evolution for LLM Agents'
title_zh: SHE：轨迹驱动的LLM Agent安全管控框架演化方法
authors:
- Wanying Qu
- Qinghua Mao
- Yu Li
- Jiyao Liu
- Xin Zhang
- Dadi Guo
- Yanxu Zhu
- Qingyu Liu
- Leitao Yuan
- Xi Lin
affiliations:
- Shanghai Artificial Intelligence Laboratory
- Fudan University
- Shanghai Jiao Tong University
- The Hong Kong University of Science and Technology
arxiv_id: '2608.09885'
url: https://arxiv.org/abs/2608.09885
pdf_url: https://arxiv.org/pdf/2608.09885
published: '2026-08-10'
collected: '2026-08-11'
category: Agent
direction: Agent 安全管控框架迭代优化
tags:
- LLM Agent
- Agent Safety
- Harness Evolution
- Trajectory Attribution
- Safety Guardrail
one_liner: 将LLM Agent安全管控框架解耦为4个可编辑组件，通过轨迹归因迭代优化安全边界
practical_value: '- 业务Agent（如电商导购、广告投放Agent）可参考将安全管控模块解耦为System Prompt、Rule Bank、Safety
  Memory、Tool Policy四个组件，避免单点修改影响全局功能，降低安全问题定位成本

  - 可复用SHE的归因演化流程，从线上错误运行轨迹自动归因到对应管控组件，生成局部优化的规则/权限，无需全量重训或人工枚举所有安全规则

  - 跨基座部署Agent时，优化完成的安全管控组件可直接迁移到不同LLM上，无需针对每个基座重复做安全对齐，减少重复开发

  - 上线安全策略时可复用SHE的安全-效用双维度筛选机制，避免安全优化大幅降低正常业务执行效率，平衡风险与用户体验'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有LLM Agent的安全管控机制多为静态部署，无法自动从实际运行轨迹中学习新兴风险的边界；且组件功能耦合，安全问题难以归因定位，局部修改容易干扰全局功能，无法适配快速变化的业务风险场景。

### 方法关键点
- 管控层功能解耦：将安全管控框架拆分为4个权责清晰的可编辑组件：`System Prompt`（全局行为约束）、`Rule Bank`（结构化安全规则）、`Safety Memory`（未解决的失败案例经验）、`Tool Policy`（工具调用权限与执行管控）
- 归因引导的演化闭环：对每条运行轨迹先做结构化风险诊断（按危害域、攻击面、失败模式三个维度标注），自动归因到对应负责的管控组件，生成局部修改方案
- 双维度校验筛选：所有候选修改先做有效性校验，再通过安全-效用双维度评估，仅同时提升安全且不降低正常业务效用的修改才会被采纳，避免过度防护。

### 关键实验
在Agent-SafetyBench（200个安全相关任务）和跨域未知风险测试集AgentHarm（440个任务）上对比静态SafeHarness、LlamaFirewall等基线：
- 对比静态SafeHarness，SHE将平均攻击成功率（ASR）从17.1%降至5.5%，降幅达3.1倍，同时效用指标UA从31.6%提升至47.6%
- 跨未知风险的AgentHarm测试集上，SHE将危害得分从19.8%降至9.8%，危害拒绝率从78.4%提升至86.4%，不降低正常请求通过率
- 优化后的管控框架可直接迁移到DeepSeek、GLM、Kimi等不同基座Agent上，无需额外演化即可获得安全提升。

**最值得记住的一句话**：Agent安全不需要仅依赖基座模型对齐，可将管控框架作为可迭代的独立系统，通过轨迹反馈持续演化，同时兼顾安全、效用和跨模型迁移性。
