---
title: 'Eureka: Task-Conditioned Meta-Agent Orchestration for Scientific Discovery'
title_zh: Eureka：面向科学发现的任务条件化元智能体编排框架
authors:
- Alizer Wong
- Heng Cui
- Yi Tan
- Xiongchao Zhan
- Liang Lin
- Yuxiang Guo
- Zhaorong Dai
- Zixin Zeng
- Wenyuan Li
affiliations:
- ManXis
- 广东工业大学
- 华南师范大学
- 上海交通大学
- 杜克大学
arxiv_id: '2608.19047'
url: https://arxiv.org/abs/2608.19047
pdf_url: https://arxiv.org/pdf/2608.19047
published: '2026-08-19'
collected: '2026-08-20'
category: Agent
direction: Agent动态架构生成与编排优化
tags:
- Meta-Agent
- Agent Orchestration
- Long-Horizon Task
- Dynamic Agent Architecture
- Task-Conditioned
one_liner: 提出任务条件化元Agent编排框架，可动态生成适配的专用子Agent，降低长周期复杂任务执行开销
practical_value: '- 长周期电商大促运营、新品孵化类复杂Agent任务可复用滚动时域规划逻辑，仅扩展当前信息可确定的子任务链路，避免无效预规划的计算浪费

  - 可借鉴架构热点识别逻辑，对重复调用的子任务（如同品类商品内容生成、用户分层运营）自动封装为专用Macro-Agent，绑定专属状态、工具、校验逻辑，降低重复上下文构建成本

  - 可复用成本收益门控的架构演化机制，仅当预期收益超过架构调整成本时才更新子Agent逻辑，避免过度迭代带来的架构复杂度上升和稳定性问题'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有固定架构Agent处理长周期、异构认知结构的复杂任务时，存在架构适配性差、编排开销高的问题：预构建全量任务计划容易因中间结果变化失效，单步迭代又会带来重复上下文传输、串行执行的高额成本，固定架构无法同时适配不同认知逻辑的任务需求。

### 方法关键点
- 采用滚动时域规划，仅扩展当前信息可确定的动态Obligation Graph部分，未确定的未来任务作为延迟责任保留，通过就绪任务背压控制规划节奏，避免无效预计算
- 识别执行中的架构热点（状态共享、依赖密集、算子/校验器重复调用），将对应子树提升为Macro-Agent，绑定专属状态、内存、算子、工具、校验器和局部拓扑，内部复杂度对父编排器透明
- 采用成本收益门控的受控演化机制，仅当瓶颈持续存在且剩余任务周期足够覆盖架构调整成本时，才修改局部认知架构，优先选择最低层级的有效修改方案

### 关键结果数字
170/170递归长周期任务全部完成，生成3948份验收证书，无未认证通过或错误终止状态；编译后的活跃上下文将中位数模型输入token从9490降至4005；12000个依赖更新任务中避免65.38%的重复计算；16000次并发执行全部与合法串行执行结果一致，无不安全提交；受控演化策略在4种评估策略中实现最低中位数总成本2525.4、最高成功率60.55%。

### 核心结论
智能体的能力不仅取决于底层模型，更取决于能否根据任务本身的认知结构形成并维护合适的智能体架构。
