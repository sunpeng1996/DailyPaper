---
title: 'Component Benchmark: Hierarchical Model Profiling for Large-scale Recommendation
  Systems'
title_zh: 组件基准：面向大规模推荐系统的分层模型性能分析工具
authors:
- Dharak Kharod
- Yuzhen Huang
- Zhou Wang
- Jackie Xu
- Fuzail Khan
- Jacky Zhou
- Hao Yan
- Lidong Zhao
- Xizhou Feng
- Yvonne Liu
affiliations:
- Meta Platforms Inc
arxiv_id: '2609.30656'
url: https://arxiv.org/abs/2609.30656
pdf_url: https://arxiv.org/pdf/2609.30656
published: '2026-09-25'
collected: '2026-09-28'
category: RecSys
direction: 大规模推荐系统 · 性能分析优化
tags:
- Profiling
- Recommendation System
- Performance Optimization
- Benchmark
- Model Analysis
one_liner: 提出分层子模块粒度的大规模推荐模型性能分析工具CB，实现性能瓶颈的精准归因
practical_value: '- 性能 profiling 可采用分层子模块粒度设计，替代传统端到端/算子级粒度，更匹配算法工程师的模块迭代逻辑，快速定位召回/排序各子模块的性能瓶颈

  - profiling 框架可设计插件化架构，支持不同模型结构、硬件平台的扩展适配，降低新模型上线前的性能评估成本

  - 配套树状交互式可视化界面，将性能数据与业务迭代的子模块对应，大幅降低算法和工程团队的沟通成本'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
大规模推荐模型结构高度异构，混合内存带宽受限操作、小计算密集型 dense 层、不规则类别特征带来的动态 shape、低算术强度操作，且模型迭代速度极快，开发者通常不感知硬件执行特性；现有 profiling 工具仅能输出端到端吞吐或算子级 trace，无法将性能归因到算法工程师可直接迭代的子模块层面，性能优化效率极低。
### 方法关键点
提出Component Benchmark (CB) 分层性能分析系统，核心为轻量可扩展的子模块级基准框架，采用插件化架构支持分层性能归因，同时配套树状交互式可视化界面，将性能数据与子模块直接对应。
### 关键结果
可支撑TB级、日均处理100B样本、部署于数千GPU的超大规模推荐模型的性能分析，已在Meta内部落地并大幅加速推荐模型性能优化流程，同时在主流开源推荐模型上验证了分析有效性。
