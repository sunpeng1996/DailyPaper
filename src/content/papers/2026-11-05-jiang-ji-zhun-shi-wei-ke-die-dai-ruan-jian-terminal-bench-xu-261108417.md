---
title: 'Benchmarks as Software: Terminal-Bench and the Case for Continuous Benchmarks'
title_zh: 将基准视为可迭代软件：Terminal-Bench 持续校验方法与实践
authors:
- E. Kelly Buchanan
- Crystal Zhou
- Scott W. Linderman
- Christopher Ré
affiliations:
- Stanford University
- Cornell University
arxiv_id: '2611.08417'
url: https://arxiv.org/abs/2611.08417
pdf_url: https://arxiv.org/pdf/2611.08417
published: '2026-11-05'
collected: '2026-11-06'
category: Eval
direction: Agent基准 持续评估与维护优化
tags:
- Agent_Evaluation
- Benchmark_Maintenance
- Continuous_Validation
- Terminal_Bench
- LLM_Agent
one_liner: 提出Agent基准持续校验工作流，修复Terminal-Bench 2.0 30%缺陷，推出更稳定的2.1版本
practical_value: '- 自研电商导购Agent、运营自动化Agent的内部评测基准时，可直接复用这套持续校验工作流，定期审计三类常见缺陷，避免评测结果失真误导模型选型或迭代方向

  - Agent评测的资源预算（wall-clock时间、output token上限）要设置1.5倍以上的可行性余量，同时测试多档预算下的性能表现，避免将速度差异误判为能力差异：实测同一模型不同harness的性能gap
  80%以上可通过延长超时消除

  - 基于公开Agent基准做模型选型时，不要只看单一版本的绝对分数，要同步确认基准版本、评测用harness和资源配置，同一模型在不同配置下分数差可达20pp以上

  - 低阶LLM可用于基准缺陷的初筛（二分类是否存在问题），再用高阶模型+人工做归因和修复，兼顾审计效率和成本，初筛准确率可达70%以上'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有Agent基准发布后易产生维护债务：LLM可发现校验逻辑未覆盖的合法解、外部依赖（API、包版本）漂移、资源预算不合理等问题都会导致基准分数与模型实际能力脱钩，而当前主流校验多为一次性静态操作，无法适配快速迭代的Agent生态。

### 方法关键点
- 四阶段持续校验工作流：证据收集（静态任务文件、历史执行traces、社区反馈）→ Agent审计（按「指令-校验不匹配、任务漂移、环境问题」三类打标签）→ 修复验证（运行oracle参考解校验修复效果，确保无新缺陷）→ 人工终审后发布更新
- 修复规则明确：指令与校验冲突时以指令为准接受所有合法解；任务漂移优先固定依赖版本或移除不可靠依赖；资源预算设置1.5倍oracle运行所需余量，避免合法解因资源不足被误判

### 关键实验
- 覆盖Terminal-Bench 2.0全量89个任务，审计发现30%（28个）任务存在缺陷，修复后发布Terminal-Bench 2.1
- 19个Agent评测结果：版本迭代后整体排名相关性仍达Spearman ρ=0.958，但单个模型分数最高提升10pp以上，榜单排名最多变动3位
- 资源预算对结果影响极大：默认配置下超50%的失败任务是超时导致，将超时扩展到32倍后，同一模型不同harness的20pp性能gap缩小到5pp以内
- 跨基准泛化验证：在Harbor-Index v0.1的34个任务上缺陷识别精度达86%

### 核心结论
Agent基准不是静态数据集，而是需要持续迭代的软件系统，资源预算、执行harness和任务本身一样是评测规范的核心组成部分
