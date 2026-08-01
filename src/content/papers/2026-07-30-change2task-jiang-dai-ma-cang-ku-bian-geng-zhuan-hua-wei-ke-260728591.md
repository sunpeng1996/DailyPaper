---
title: 'Change2Task: From Repository Changes to Executable Coding Agent Tasks and
  Environments'
title_zh: Change2Task：将代码仓库变更转化为可执行编码Agent任务与环境
authors:
- Haomin Qi
- Xingliang Wang
- Xuanqi Gao
- Baihui Sang
- Xin Zhang
- Minghua Ma
- Pengfei Gao
- Yu Kang
- Qingwei Lin
- Saravan Rajmohan
affiliations:
- Microsoft
- University of California San Diego
- Zhejiang University
- Xi’an Jiaotong University
- Nanjing University
arxiv_id: '2607.28591'
url: https://arxiv.org/abs/2607.28591
pdf_url: https://arxiv.org/pdf/2607.28591
published: '2026-07-30'
collected: '2026-08-01'
category: Agent
direction: 编码Agent · 任务数据集自动构建
tags:
- Coding Agent
- Task Generation
- Benchmark Construction
- Repository Mining
- Agent Evaluation
one_liner: 提出从仓库历史PR自动生成可验证编码Agent训练与评测任务的系统
practical_value: '- 业务Agent训练/评测数据集构造可复用该思路：从历史工单/运营操作/代码变更反向生成带校验逻辑的可执行任务，无需从零人工构造

  - 三重任务重建（Patch Reversal/Code Mapping/Agent Reconstruction）+ 全链路校验逻辑，可直接迁移到业务Agent测试用例自动生成流程，降本提效

  - 复用健康基准环境而非存储全量历史环境的工程方案，可大幅降低Agent训练/评测的存储、环境部署开销，适配资源受限的业务场景'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
编码Agent规模化落地缺乏持续、可执行的训练/评测数据，现有任务构造成本高、环境复用性差，缺少能耦合真实运行状态、工具链、验证逻辑的高质量任务供给方案。

### 方法关键点
1. 基于仓库历史合并PR，对齐历史变更与当前演进代码，在健康的最新仓库版本上构造任务；
2. 支持三种任务状态重建方案：Patch Reversal、Code Mapping、Agent Reconstruction；
3. 全生命周期校验：验证从健康基准→任务状态→恢复状态的完整链路有效性。

### 关键结果数字
覆盖Bug修复、功能新增、测试生成、API迁移、安全修复5类编码任务，从1130个符合要求的源变更出发，验证过的任务构造成功率达79.6%；比PR基线多生成29.2%的验证任务；Agent评测下历史与重建案例结果一致性最高达98.0%；复用最新基准环境使全链路开销降低10.8%
