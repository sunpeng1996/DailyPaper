---
title: 'BizBench: Unveiling Hidden Challenges in Deploying Long-Horizon Agents for
  Real-World Business'
title_zh: BizBench：面向真实业务的长周期Agent执行合规性评测基准
authors:
- Enhan Zhao
- Yongqi Tong
- Xuejun Yu
- Hang Wang
- Pan Wang
- Yichao Wang
- Di He
- Jianshe Li
- Wei Wu
affiliations:
- Peking University
- Ant International
arxiv_id: '2610.20424'
url: https://arxiv.org/abs/2610.20424
pdf_url: https://arxiv.org/pdf/2610.20424
published: '2026-10-13'
collected: '2026-10-19'
category: Agent
direction: Agent评测 · 业务流程合规性
tags:
- Long-horizon Agent
- Benchmark
- Business Workflow
- Compliance Evaluation
- Tool Use
one_liner: 推出基于真实支付业务的长周期Agent评测基准，同时校验任务完成度与全流程合规性
practical_value: '- 业务类Agent落地需新增中间执行合规校验逻辑，覆盖前置授权、资源阈值、规则时效性校验，避免最终结果正确但中间违规导致合规/资金风险，可直接复用至支付、优惠券发放、售后退款等高约束场景

  - 业务场景RAG系统需新增规则优先级判断逻辑，除语义匹配外额外校验规则的生效时段、适用范围、版本效力，解决多版本/冲突规则的选择问题，适配电商活动规则、平台政策动态更新的场景

  - 长周期Agent的工具调用优化可参考Golden trace基线设置调用量阈值，过滤重复查询、无效调用，降低执行成本，适配客服Agent、运营自动化Agent等多工具调用场景

  - 业务Agent评测可复用三层校验框架：目标达成+流程合规+副作用防控，替代单纯LLM judge，提升评测结果的准确性与可解释性'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有长周期Agent基准普遍仅关注最终任务成功率，忽略中间执行环节的合规性校验，但真实业务场景（如支付、电商交易）对流程约束要求极高，未授权操作、临时突破资源阈值等中间违规行为，即使后续通过退款、调整修复了最终结果，仍会产生合规处罚、资金损失等不可逆转的风险。同时真实业务规则分散在多源文档中，存在多版本并存、适用范围/生效时段差异、规则冲突等问题，现有评测体系无法覆盖上述落地挑战。

### 方法关键点
- 基于头部支付企业真实业务流程构建状态一致的可执行环境，包含789份标注了时效、适用范围的业务文档，601个可调用业务工具
- 设计50个长周期多轮任务，覆盖资源约束、时序依赖、前置承诺、规则冲突/过时等真实业务场景，配套用户模拟器提供动态客户信息、审批交互
- 采用三层确定性校验逻辑，不绑定固定执行路径：目标达成校验、执行流程合规校验、无违规副作用校验，三者同时满足才算任务成功
- 所有任务通过Golden trace验证可行性，同时构造违规用例验证校验逻辑的准确性

### 关键实验
覆盖9个主流闭源/开源模型，核心结果：① 前沿模型严格成功率极低，Claude Opus 5为64.0%，GPT-6 Sol仅61.3%，小模型Qwen3.5-9B成功率为0；② 仅看目标达成会显著高估性能，Qwen3.8-27B目标达成率42.0%，但严格成功率仅32.7%，约1/4达标的执行存在中间违规；③ 工具调用开销远高于人工基线，DeepSeek-V4.1-Flash平均每次执行调用191.3次工具，比Golden trace多70%，大量为重复查询、无效调用。

### 核心结论
业务场景Agent落地，执行过程合规性比最终任务成功率更重要，仅看结果的评估体系会隐藏大量致命风险。
