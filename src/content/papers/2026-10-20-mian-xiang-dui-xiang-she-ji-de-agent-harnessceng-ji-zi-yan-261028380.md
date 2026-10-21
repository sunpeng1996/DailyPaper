---
title: 'Object-Oriented Harness: Evolving Agent Harnesses through Object-Oriented
  Design'
title_zh: 面向对象设计的Agent Harness层级自演化框架
authors:
- Gaotang Li
- Bhavana Dalvi Mishra
- Yifei Ming
- Yanfei Chen
- Zhongying CuiZhu
- Lesly Miculicich
- Long T. Le
- Rui Meng
- Chun-Liang Li
- Hanghang Tong
affiliations:
- University of Illinois Urbana-Champaign
- Google Cloud AI Research
arxiv_id: '2610.28380'
url: https://arxiv.org/abs/2610.28380
pdf_url: https://arxiv.org/pdf/2610.28380
published: '2026-10-20'
collected: '2026-10-21'
category: Agent
direction: Agent Harness 自演化优化
tags:
- Agent Harness
- Object-Oriented Design
- Self-Evolving Agent
- Task Routing
- Long-Horizon Task
one_liner: 基于面向对象继承构建层级化专用Agent Harness，结合任务路由提升异质长周期任务性能
practical_value: '- 业务Agent（电商客服、运营流程自动化、智能导购Agent）可复用OO继承架构设计Harness：公共逻辑（工具调用、上下文管理）放在Base类，场景专用逻辑（如订单查询、售后处理）做子类重写，降低多场景Harness的维护与迭代成本

  - 可借鉴「Base轨迹+任务元数据」的双输入路由策略：先轻量跑Base Harness，效果达标的直接复用结果，仅Base效果差的任务调用专用Harness，兼顾效果与推理成本

  - Harness迭代优化可按任务聚类做验证：每次优化仅在目标任务聚类跑测试，不需要全量任务验证，大幅减少LLM调用成本，加速迭代效率

  - OOD场景必须保留Base Harness作为回退选项，避免专用Harness在陌生任务域出现效果劣化，提升业务系统鲁棒性'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
全局统一的Agent Harness难以适配异质长周期任务的差异化执行策略需求，针对部分任务的优化容易导致其他任务效果下降，全局Harness优化效率低、分布 shift 下泛化性差。
### 方法关键点
- 采用面向对象设计构建Harness层级体系：专用Harness以子类形式继承Base或已有Harness的所有方法，可重写现有方法或新增方法实现差异化逻辑，公共代码无需重复开发
- 训练阶段先执行Base Harness得到全量任务执行记录，按任务的共性执行需求聚类，演化Agent针对每个聚类迭代生成子类Harness，仅在目标聚类验证效果，无需全量任务跑测，同步积累设计经验与路由经验
- 测试阶段Harness路由器结合任务元数据+Base Harness执行轨迹，匹配路由经验选择最合适的Harness，Base执行效果达标的直接复用结果，无需二次执行
### 关键结果
在3个长周期任务基准（AutomationBench、Workspace-Bench、Toolathlon-GYM）上，OO-Harness主指标全面领先所有基线：较Base Harness最高绝对提升15.79%；较全局优化的Meta-Harness训练时间缩短73%（从109.1h降至29h），OOD场景下较Meta-Harness的PASS率高14.28pct。
### 核心结论
Agent Harness优化不需要追求完美的全局版本，分层复用+按需路由的模式，可同时兼顾异质场景适配、迭代效率与OOD鲁棒性
