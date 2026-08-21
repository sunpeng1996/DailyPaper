---
title: 'Repo0: Design-Driven Zero-to-All Code Generation'
title_zh: Repo0：设计驱动的从零到全代码生成框架
authors:
- Silin Chen
- Haoyi Teng
- Xiaodong Gu
- Yuling Shi
- Jiale Huang
- Yongpan Wang
- Hongyu Zhang
- Haibing Guan
affiliations:
- Shanghai Jiao Tong University
- Chongqing University
arxiv_id: '2608.19854'
url: https://arxiv.org/abs/2608.19854
pdf_url: https://arxiv.org/pdf/2608.19854
published: '2026-08-19'
collected: '2026-08-21'
category: Agent
direction: Agent 零代码仓库生成架构优化
tags:
- LLM Agent
- Code Generation
- Repository Generation
- Modularity Optimization
- Dual-DAG
one_liner: 提出基于双DAG结构与模块化指标迭代演进的从零构建完整代码仓库的Agent框架
practical_value: '- 开发复杂业务系统Agent（如推荐链路自动化工具、电商运营代码生成）时，可复用双DAG设计拆分需求依赖与实现依赖，避免需求和实现混叠导致的架构混乱

  - 架构迭代阶段可复用内聚度、耦合度等模块化指标作为收敛判断依据，替代纯LLM自由决策，减少过度拆分或模块冗余，同时降低迭代成本

  - 做需求到落地的长周期Agent任务时，可复用「需求分解→架构迭代收敛→测试驱动代码生成」的三段式流程，提升任务成功率'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有代码生成Agent大多默认已有预定义仓库架构，无法支撑从零到完整仓库的生成场景；静态一次性架构规划容易出现低内聚高耦合、模块边界混乱、跨文件协同差等问题，导致生成代码的功能覆盖率低、运行通过率差。
### 方法关键点
- 设计双DAG（Dual-DAG）架构状态，拆分需求层DAG（记录功能依赖）和组件层DAG（记录实现依赖），并维护两者的对齐关系，全程保留需求到代码的可追溯性
- 基于内聚度、耦合度等模块化指标触发结构动作（拆分、合并、修改、保存），迭代演进组件边界直到结构收敛，避免纯LLM决策导致的过度拆分问题
- 架构收敛后采用测试驱动开发（TDD）流程生成代码，基于验证反馈做局部修复，保障代码正确性
### 关键结果
在RepoCraft数据集的6个真实Python仓库上测试，对比RPG、Paper2Code等基线，以GPT-5 mini和DeepSeek V3.2为基座时，Repo0在所有场景下的功能覆盖率和通过率均为最优；相比最强基线RPG，功能覆盖率最高提升20.08个百分点，通过率最高提升29.74个百分点。
**最值得记住的结论**：从零构建复杂系统的Agent不能依赖一次性静态规划，基于可量化指标的持续结构演进是提升效果的核心。
