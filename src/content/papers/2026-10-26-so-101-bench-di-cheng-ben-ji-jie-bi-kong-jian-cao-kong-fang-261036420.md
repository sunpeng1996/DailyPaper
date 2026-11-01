---
title: 'SO-101 Bench: Accessible Spatial Manipulation'
title_zh: SO-101 Bench：低成本机械臂空间操控仿真评测基准
authors:
- Truman Hickok
affiliations:
- Independent
arxiv_id: '2610.36420'
url: https://arxiv.org/abs/2610.36420
pdf_url: https://arxiv.org/pdf/2610.36420
published: '2026-10-26'
collected: '2026-11-01'
category: Agent
direction: 具身Agent · 机械臂操控仿真基准
tags:
- Embodied Agent
- Simulation Benchmark
- Sim2Real
- VLA
- LLM Agent
one_liner: 推出基于Isaac Lab数字孪生的SO-101语言条件空间操控仿真基准，评测排序与真机完全匹配
practical_value: '- 做Agent评测可借鉴数字孪生思路，先在仿真/模拟环境做多维度低成本预评测，再上线真实业务，大幅降低试错成本

  - 复杂Agent任务可采用「LLM做上层逻辑规划+专用小模型做底层执行」的拆分架构，本文该方案比纯端到端VLA效果提升超22个百分点

  - 跨场景Agent性能评估可采用Spearman秩相关系数验证离线/模拟评测与真实环境的一致性，确保评测结果可信'
score: 4
source: huggingface-daily
depth: abstract
---

## 动机
低成本SO-101机械臂是机器人学习主流入门载体，现有基准仅支持物理硬件、任务简单、留出对象少，无开箱即用的空间约束语言指令任务执行策略，真机评测成本极高。
## 方法关键点
基于Isaac Lab构建SO-101真机数字孪生仿真基准，覆盖4类任务、5个评测维度，包含138个对象（按可见/未见实例/未见类别划分）、916个评测episode、3629个仿真演示样本，所有策略在相同计算预算下微调。
## 关键结果数字
仿真环境下策略排序与未知环境未知对象下的真机排序完全一致（Spearman rho=1.00，MMRV=0.000）；纯VLA最优准确率约61%，采用LLM写代码+专用策略执行抓取的架构准确率达83.2%，性能提升源于框架选型和LLM选型。
