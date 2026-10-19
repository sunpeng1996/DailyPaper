---
title: 'From Trajectories to Differentiated Skills: Cognitive Differentiation for
  Self-Improving Agents'
title_zh: 面向自进化Agent的认知分化技能进化框架CDSE
authors:
- Yewei Zhao
- Derong Xu
- Wei Chen
- Yin Xu
- Peilun Zhou
- Xiaohan Wang
- Guojun Yin
- Wei Lin
- Mingjun Xiao
affiliations:
- 中国科学技术大学
- 美团
- 香港城市大学
arxiv_id: '2610.23599'
url: https://arxiv.org/abs/2610.23599
pdf_url: https://arxiv.org/pdf/2610.23599
published: '2026-10-16'
collected: '2026-10-19'
category: Agent
direction: Agent 自进化 · 技能分层迭代
tags:
- LLM Agent
- Self-Improvement
- Skill Evolution
- Cognitive Differentiation
- Trajectory Distillation
one_liner: 将Agent技能拆分为四大功能组件，从执行轨迹分层提取并迭代可复用的差异化能力
practical_value: '- 搭建电商场景Agent（客服、运营自动化、选品决策Agent等）的技能库时，可直接复用CDSE的四组件拆分逻辑：Meta存全局流程规则、Experience存场景化经验、Tool存工具调用指南、Script存可执行脚本，避免技能杂乱堆砌，提升调用准确率和迭代效率

  - 可复用结果对比语义梯度提取逻辑：从推荐生效/失效、用户交互成功/失败的业务轨迹中，对比提取有原始证据支撑的可复用优化点，再分类入库，减少无效规则污染技能库

  - 跨类目/跨业务迁移Agent能力时，优先迁移Meta层的全局控制规则，比直接迁移完整技能包兼容性更高，可大幅降低新场景部署成本'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有Agent技能进化方法普遍围绕技能文档、记忆条目等人工定义的载体组织知识，忽略单条技能内部的功能异质性：不同用途的知识在更新规则、验证标准、调用时机上存在本质差异，混用会导致技能迭代效率低、生效准确率差，难以适配复杂业务场景需求。
### 方法关键点
- 借鉴认知科学理论，将统一技能拆分为四大功能独立的组件：Meta（全局任务控制、规划、校验规则）、Experience（场景化启发式规则、故障恢复策略）、Tool（工具选型、操作指南）、Script（可复用可独立验证的执行脚本）
- 首先通过结果对比语义梯度发现，从成功/失败的执行轨迹中提取有原始证据支撑的可复用行为优化点，过滤运行时无关信息
- 再通过认知引导的梯度聚合，过滤无效、单场景独有、冗余的梯度，按功能归属分配到对应组件
- 最后做自适应自更新：各组件走独立的更新、验证流程，再做跨组件冲突消解，生成各组件的调用描述引导Agent按需加载
### 关键实验
覆盖6个通用Agent基准、3个大模型、2个执行环境共36个测试场景，对比Base、Trace2Skill、SkillOpt-lite等主流基线：CDSE在所有场景下均取得最优准确率，相对Base平均提升7.6pp，相对各场景最优基线平均提升2.6pp；Meta组件跨场景迁移平均提升3.6pp，通用性远高于其他组件；每1pp性能提升的token消耗仅为最优基线的1/3左右，迭代效率更高。
### 核心结论
Agent技能迭代的核心不是存储知识的量级，而是按功能角色分类组织、更新、调用知识，才能最大化复用效率和落地效果。
