---
title: 'Hierarchical Self-Improvement: A Framework for Task-Specific Evolvable Agent
  Harnesses'
title_zh: 分层自改进：面向任务定制的可进化Agent Harness框架
authors:
- Tailin Zhou
affiliations:
- HKUST
arxiv_id: '2608.08466'
url: https://arxiv.org/abs/2608.08466
pdf_url: https://arxiv.org/pdf/2608.08466
published: '2026-08-08'
collected: '2026-08-21'
category: Agent
direction: Agent 自改进 · Harness进化
tags:
- Agent Self-Improvement
- Harness Evolution
- Frozen LLM
- Hierarchical Optimization
- Generalization
one_liner: 基于单冻结LLM的三层分层自改进框架，通过进化Agent Harness实现性能提升无需参数更新
practical_value: '- 电商导购/客服Agent可复用分层进化范式：任务执行阶段关闭LLM额外推理降低推理成本，进化阶段开启推理优化prompt、工具编排、记忆逻辑，无需微调即可持续提升业务效果

  - 推荐/搜索系统的Agent编排层可借鉴任务专属harness设计：按搜索、猜你喜欢、营销弹窗等不同任务域维护独立可热插拔的harness，通过业务反馈（转化率、用户满意度）迭代，避免通用方案的适配损耗

  - 可直接复用HSI的边界结论：仅在LLM具备基础能力的任务域开展harness进化才能拿到收益，超过模型能力边界或反馈信号稀疏的场景进化无增益，避免无效研发投入'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM Agent的执行脚手架harness（包含prompt、工具编排、记忆、校验逻辑等）大多部署后固定，手动迭代成本极高；已有的自改进方案要么仅优化单步决策逻辑，要么依赖外部更强模型做优化，且难以区分性能提升来自harness优化还是推理算力增加，同时普遍存在过拟合、泛化性差的问题。
### 方法关键点
- 三层分层架构：单冻结LLM同时覆盖三个层级的工作，任务harness层负责与环境交互执行任务、进化层负责修改迭代任务harness、元进化层负责优化进化策略本身，仅最外层元进化的执行逻辑固定作为锚点，避免无限制自引用问题
- 推理开关设计：任务执行阶段关闭LLM额外推理能力，进化阶段开启推理，彻底隔离harness进化的贡献，排除推理算力提升对效果的干扰
- 五阶段进化流程：种子选择→主进化→提交选择→元进化→最终版本选择，固定任务注入接口保证harness可热插拔，所有优化决策均基于环境反馈信号
### 关键实验
在BALROG长序列交互基准上采用DeepSeek-V4-Flash作为冻结 backbone，对比初始手工harness：中等难度任务上raw % Progress提升显著，BabyAI+39.3、Crafter+33.0、TextWorld+25.0、MiniHack+15.0；BabaIsAI子任务held-out泛化性优异，BreakStop达0.98、GoTo达1.0；超过模型能力边界的NLE任务无明显提升。
### 核心结论
Harness进化只能放大冻结LLM已有的能力边界，无法突破模型本身的能力上限，也无法在反馈信号不足的场景生效。
