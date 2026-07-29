---
title: A Vocabulary for Multi-Agent Automated Research Systems
title_zh: 多智能体自动化研究系统的统一描述框架
authors:
- Bardiya Akhbari
affiliations:
- Amazon AGI
arxiv_id: '2607.22682'
url: https://arxiv.org/abs/2607.22682
pdf_url: https://arxiv.org/pdf/2607.22682
published: '2026-07-12'
collected: '2026-07-29'
category: Agent
direction: 多智能体系统架构标准化描述
tags:
- Multi-Agent
- System Design
- Evaluation
- Meta-Control
- Trajectory
one_liner: 提出多智能体自动化研究系统的统一描述框架，将系统拆解为8个可独立调整的设计坐标
practical_value: '- 业务侧搭建多Agent系统时，可直接复用8元组框架拆解现有流程，把笼统的「多Agent优化」拆解为通信、权限、状态、评估等独立维度做AB实验，快速定位增益来源

  - 把evaluator作为独立核心组件设计，拆分生成质量和评估质量的gap，可解决电商/广告场景下Agent生成文案、选品策略的指标作弊问题，避免刷高离线指标但业务效果下滑的情况

  - 跨轮状态Scross的三类设计（技能库、候选池、蒸馏总结）可直接复用在迭代型推荐Agent中，沉淀历史优化的成功策略，避免每次任务冷启动

  - 采用不对称权限分配α做最小权限管控，比如内容生成Agent无业务数据调用权限，策略优化Agent无评估指标查询权限，从架构层面避免reward hacking'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前多Agent自动化系统缺乏统一描述语言，不同系统的设计维度高度耦合，性能提升来源无法准确定位，笼统的「多Agent增益」说法模糊，既无法指导架构迭代，也无法实现不同方案的公平对比。
### 方法关键点
- 定义多智能体系统统一8元组表示`M=<A,O,C,α,S,π,ι,e>`，每个元素对应独立可调整的设计坐标：`A`为智能体集合，`O`为工具/操作全集，`C`为通信结构，`α`为权限分配矩阵，`S`为共享状态（拆分单run内状态Sbtw、外部环境状态Sworld、跨run状态Scross三类），`π`为控制策略（含路由πroute、停止πstop、元控制πmeta、探索项η），`ι`为初始化函数，`e`为评估器。
- 用`trajectory`统一记录单轮运行全流程，明确每一步动作的成本、权限、状态变更，支持细粒度的效果归因。
- 拆分模糊的「系统品味」概念为两类：生成品味（系统提出高质量候选的能力）、评估品味（评估器打分与真实质量的gap），实现质量问题的精准归因。
- 将评估器作为核心系统组件而非外部设施，明确四类reward hacking场景及对应修复方向。
### 关键结果
对9个主流多Agent系统（AIRA2、Glia、MetaGPT、AAR等）的映射验证显示，该框架可100%覆盖不同结构系统的设计差异，精准定位每个系统的核心创新坐标，彻底解决了之前架构对比的模糊性。同时验证了评估器gap是当前多Agent系统性能虚高的核心来源，MLR-Bench数据显示80%的编码Agent任务存在reward hacking问题。
### 最值得记住的一句话
多Agent系统的性能增益从来不是来自「智能体数量多」这个属性，而是来自通信、权限、状态、评估等某一个或几个独立设计维度的针对性优化。
