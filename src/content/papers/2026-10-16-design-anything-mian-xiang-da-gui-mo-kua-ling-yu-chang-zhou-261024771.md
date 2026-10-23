---
title: Design Anything, Design at Scale
title_zh: Design Anything：面向大规模跨领域长周期设计的意图对齐Agent框架
authors:
- Xuchao Ren
- Siyuan Feng
- Jing Huang
- Yanhua Yao
- Jing Wang
- Lingyu Alina Wang
- Anan Chen
- Hangjie Yuan
- Tao Feng
- Qiong Wu
affiliations:
- Academy of Arts & Design, Tsinghua University
- Beijing Institute of Fashion Technology
- Senseable City Lab, Massachusetts Institute of Technology
- DAMO Academy, Alibaba Group
arxiv_id: '2610.24771'
url: https://arxiv.org/abs/2610.24771
pdf_url: https://arxiv.org/pdf/2610.24771
published: '2026-10-16'
collected: '2026-10-23'
category: Agent
direction: Agent · 长周期任务意图对齐调度
tags:
- LLM Agent
- Intent Alignment
- Long-Horizon Task
- Agent Harness
- Multimodal Generation
one_liner: 提出基于意图-执行图的Agent调度框架，实现跨领域长周期设计任务的高约束满足率
practical_value: '- 长周期多输出Agent任务可借鉴意图-执行图设计，将约束、决策、交付物绑定到工作流节点，不依赖LLM上下文记忆，大幅提升约束满足率，适配电商大促物料、系列商品详情页等多产出物生成场景

  - 确定性交付检查器思路可复用：不依赖LLM自行判断任务完成，通过绑定关系、执行记录校验输出类型/数量/依赖满足情况，减少任务提前终止问题，文中方案比通用prompt方案降低2/3
  LLM调用成本

  - 多交付物一致性验证可参考其评测逻辑：约束满足要求所有关联产出物均符合要求，而非单个符合，适配电商同系列商品素材、广告素材套装的一致性校验'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
长周期多产出的设计任务中，现有Agent容易丢失初始约束、遗忘前期决策，随着交付物数量上升，约束满足率和一致性大幅下降；现有方案要么依赖LLM自行判断完成状态，要么单artifact校验，无法保证整体项目对齐初始意图。

### 方法关键点
- 外置**意图-执行图**存储核心状态：任务合约持久化存储交付物清单、约束、已确定设计决策；工作流图显式记录各产出物依赖关系，前期产出直接作为后续生成输入；执行记录绑定交付物与对应工作流节点
- 双循环调度机制：Agent循环负责规划、构建工作流、执行生成、校验状态，所有操作经过确定性合法性检查才生效；交付循环通过绑定关系和执行记录自动识别未完成交付物，主动发起下一轮任务，不依赖LLM主动声明完成
- 配套DesignAnything-Bench基准，覆盖19个设计领域228个任务，包含38组分别设置6/14/24个交付物的同项目对照任务，专门测试长周期任务的意图对齐能力

### 关键结果
固定LLM不变时，搭配DeepSeek V4.1 Flash High约束满足率达85.0%，比最强基线高15.4%；搭配GPT-5.6 Sol High达92.5%，比最强基线高14.4%；24个交付物的大规模任务上提升幅度达25.1%/23.0%，18/19个领域表现领先，专业设计师盲测偏好度最高。

### 核心结论
长周期Agent任务的意图对齐，核心要把关键状态从LLM的隐式上下文转移到系统的显式可校验存储中，而非单纯依赖LLM的记忆能力
