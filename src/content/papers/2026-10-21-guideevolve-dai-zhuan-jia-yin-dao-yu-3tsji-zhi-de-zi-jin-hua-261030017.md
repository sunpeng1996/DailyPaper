---
title: 'GuideEvolve: Self-Evolving Agent Framework with Expert Guidance and 3Ts Mechanisms'
title_zh: GuideEvolve：带专家引导与3Ts机制的自进化Agent框架
authors:
- Meihong Jia
- Yasemin Timar
- Jonathan Taws
affiliations:
- Amazon
- Amazon Web Services
arxiv_id: '2610.30017'
url: https://arxiv.org/abs/2610.30017
pdf_url: https://arxiv.org/pdf/2610.30017
published: '2026-10-21'
collected: '2026-10-22'
category: Agent
direction: 自进化Agent · 性能与稳定性优化
tags:
- Self-Evolving Agent
- Expert Guidance
- 3Ts Mechanism
- Agent Stability
- LLM Agent
one_liner: 提出拆分专家评估与进化控制的自进化Agent架构，搭配3Ts机制大幅提升稳定性和迭代效率
practical_value: '- 可复用「专家评估与进化控制分离」的架构，在电商推荐策略自迭代、客服Agent优化、营销文案生成自调优场景中，拆分效果评估和策略迭代逻辑，避免上下文溢出和判断偏差

  - 3Ts机制可直接落地：Throwback回滚机制在推荐策略、搜索排序规则迭代出现效果下跌时快速回退到历史最优版本；Termination by choice在A/B测试达到效果平台期时自动终止迭代，节省算力

  - 将自进化从无引导zeroth-order优化改为带专家梯度的first-order优化的思路，可迁移到生成式推荐prompt迭代、搜索query改写自优化流程，预计迭代效率可提升近50%

  - 动态token预算分配+渐进式上下文缩减机制，可直接用于生产环境LLM Agent的资源管控，避免token溢出导致的任务失败，提升部署稳定性'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有自进化Agent框架（如Gödel Agent）存在稳定性差、迭代效率低、上下文易溢出等问题，生产部署时会出现4%的意外终止、14%的优化失败等情况，难以落地到企业级业务场景。
### 方法关键点
- 分层架构设计：将自进化流程拆分为独立的任务专家模块、自进化控制Agent、执行Solver三层，专家模块仅基于任务效果输出性能评估、优劣分析和可落地改进建议，避免评估逻辑与进化控制的上下文污染
- 3Ts自治机制：①Think Fast and Slow：双速认知，低风险操作用快速执行，高风险操作（如Solver修改、效果评估）走慢思考校验；②Throwback：保留历史最优Solver状态，支持性能劣化时回滚或参考历史最优策略优化；③Termination by Choice：自适应终止，达到性能平台期或最优效果时自动停止迭代，避免无效探索
- 资源管控机制：动态token分配+渐进式上下文缩减，适配Bedrock等LLM平台的限制，避免token溢出
### 关键实验
在MGSM（小学数学推理）、MMLU（多任务知识理解）数据集上对比SOTA自进化框架Gödel Agent（GPT-4版）：①MGSM准确率89.8% vs 90.6%，方差降低25%；MMLU准确率89.1% vs 87.9%，方差降低59%；②进化成功率100% vs 基线的82%；③迭代次数减少约50%（MGSM从30次降到15.1次，MMLU降到13.4次）
### 核心结论
将自进化Agent的无引导zeroth-order搜索，改为带独立专家梯度引导的first-order优化，是同时提升性能、稳定性和迭代效率的核心路径
