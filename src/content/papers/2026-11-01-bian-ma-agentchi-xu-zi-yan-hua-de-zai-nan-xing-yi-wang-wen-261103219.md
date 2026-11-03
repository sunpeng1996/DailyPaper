---
title: Can Coding Agents Sustain Continual Evolution without Forgetting?
title_zh: 编码Agent持续自演化的灾难性遗忘问题研究
authors:
- Shangziqi Zhao
- Yitong Zhang
- Jia Li
affiliations:
- Tsinghua University
arxiv_id: '2611.03219'
url: https://arxiv.org/abs/2611.03219
pdf_url: https://arxiv.org/pdf/2611.03219
published: '2026-11-01'
collected: '2026-11-03'
category: Agent
direction: Agent持续自演化 · 灾难性遗忘分析
tags:
- CodingAgent
- HarnessEvolution
- ContinualLearning
- CatastrophicForgetting
- SelfEvolution
one_liner: 实证现有编码Agent harness自演化方法跨任务存在严重灾难性遗忘，定位三类核心冲突原因
practical_value: '- 业务Agent（电商导购/客服/推荐决策Agent）迭代时，不同任务的harness配置做分支路由，不要直接在通用harness上叠加新任务逻辑，避免规则冲突

  - 拆解Agent harness为验证规则、工作流、资源预算三类模块，不同任务的对应配置隔离存储、版本化管理，避免跨任务修改覆盖

  - 跨任务迭代Agent时优先按任务相关性排序演化顺序，相关性越高的任务连续迭代，灾难性遗忘幅度越低

  - 验证规则是导致harness遗忘的核心因素，不同任务的输出校验逻辑不要硬编码到通用框架，单独做任务维度的规则匹配'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有Agent harness自演化方法大多针对单任务优化，实际场景中编码Agent需要处理代码修复、测试生成、功能开发等多类任务，跨任务持续演化时是否会出现灾难性遗忘尚未被验证，直接影响自演化Agent的长期落地可用性。
### 方法关键点
- 构建3类软件工程任务的6种跨任务演化顺序，覆盖SWE-Bench（代码修复）、SWT-Bench（测试用例生成）、FeatureBench（功能开发）三个基准数据集
- 选取AHE、Meta-Harness两种代表性harness自演化方法作为评估对象，固定基础模型DeepSeek-V4-Flash参数，仅迭代harness逻辑
- 收集520+条Agent执行轨迹，人工归因harness修改导致的冲突类型
### 关键结果
单任务演化时两类方法均有明显性能提升：AHE在SWE-Bench上性能从82%提升至96%，Meta-Harness在SWT-Bench上性能提升至100%；跨任务演化时存在严重灾难性遗忘：Meta-Harness在SWE-Bench演化到94%后，再在FeatureBench演化5轮，SWE-Bench性能跌至32%，相对下降66%；冲突归因显示验证冲突占87.1%，工作流冲突占8.2%，预算策略仅影响执行效率不影响性能。
### 核心结论
Agent harness自演化的灾难性遗忘本质是不同任务的规则、流程、资源配置的模块冲突，而非模型参数的权重覆盖，可通过模块隔离大幅降低遗忘风险。
