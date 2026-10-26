---
title: 'HarnessMM: Recursive Self-Improvement for Harness Token Efficiency'
title_zh: HarnessMM：通过递归自优化提升Agent工具调用Token效率的方法
authors:
- Yuhua Jiang
- Chang Xu
- Feifei Gao
- Li Zhao
affiliations:
- Tsinghua University
- Microsoft Research Asia
arxiv_id: '2610.32813'
url: https://arxiv.org/abs/2610.32813
pdf_url: https://arxiv.org/pdf/2610.32813
published: '2026-10-23'
collected: '2026-10-26'
category: Agent
direction: Agent 多轮推理Token效率优化
tags:
- TokenEfficiency
- AgentOptimization
- RecursiveSelfImprovement
- ToolCalling
- ReasoningEfficiency
one_liner: 通过缓存已决议动作与递归自优化，在保效前提下大幅降低Agent工具调用的Token消耗
practical_value: '- 电商导购/工具类推荐Agent可借鉴EDG设计：将用户触发的多步固定动作（如查库存→算优惠→推商品）提前缓存，每步仅校验前置条件（如库存是否充足），无需每步调用大模型推理，可大幅节省Token

  - 借鉴Guarded Decision Reuse思路，会话中复用已生成的确定性决策结果，仅遇到新语义决策需求时调用大模型：如用户多次查询同品类优惠时，直接复用已有计算规则仅校验参数即可

  - 递归自优化（RSI）框架可复用在Agent性能迭代上：用线上真实会话反馈持续优化决策缓存规则，无需修改大模型权重即可逐步降低Token消耗且保障效果

  - 成本核算可参考其完整任务Token统计方法：将决策生成、校验、fallback的所有Token计入成本，避免仅统计推理调用导致的成本低估'
score: 9
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
当前Agent调用工具时每轮反馈都要重新触发推理，哪怕前置步骤已经确定了后续动作，导致大量冗余Token消耗；现有效率优化方法多集中在上下文压缩、模型路由，没有解决重复推理的核心问题，还容易出现新增优化逻辑的消耗超过节省Token的「替换悖论」。

### 方法关键点
- 完全保留原大模型权重、工具接口与任务逻辑，仅在模型-工具边界插入控制器修改推理调用时机
- 设计**Executable Decision Graphs (EDG)**：存储大模型已经推理确定的动作、字面参数、依赖关系和公开执行守卫条件
- **Guarded Decision Reuse (GDR)**：工具返回结果后优先校验EDG中已存决策的守卫条件，符合要求则直接复用，不触发新推理
- **Certified Callback Substitution (CCS)**：用原生工具接口执行复用的决策，跳过原推理回调，记录替换凭证确保执行依赖完整
- **Recursive Self-Improvement (RSI)**：用任务执行的效果和成本反馈迭代优化EDG配置，验证通过后上线，持续提升决策复用率

### 关键实验
在HumanEval基准上：Codex接入后成功率保持90.82%不变，单任务Token消耗从66.72k降至47.02k，节省29.54%；DeepSeek Harness接入后成功率从71.43%升至85.71%，单任务Token从96.28k降至11.62k，节省87.93%。在MBPP基准上，比单次使用EDG的方案成本低26.91%，比保留回调的方案低19.52%，在ALFWorld、SearchQA等6个跨领域基准上均实现效果提升或保效下的Token成本下降。

### 核心结论
Agent多轮推理中已经确定语义的决策，仅需通过守卫校验执行条件即可复用，不需要重复调用大模型，是大幅降低Token成本且保障任务效果的可行路径。
