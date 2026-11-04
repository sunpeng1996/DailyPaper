---
title: 'SLATE: A Large-Scale Benchmark for Long-Horizon API Selection in E-commerce
  Tool Use'
title_zh: SLATE：面向电商工具调用场景的大规模长时序API选择基准
authors:
- Rongzhe Wei
- Ge Shi
- Min Cheng
- Sarthak Ghosh
- Vaibhav Gorde
- Leman Akoglu
- Pan Li
- Na Zhang
affiliations:
- Amazon
- Georgia Institute of Technology
arxiv_id: '2611.03982'
url: https://arxiv.org/abs/2611.03982
pdf_url: https://arxiv.org/pdf/2611.03982
published: '2026-11-02'
collected: '2026-11-04'
category: Agent
direction: Agent工具调用 · 电商API选择评估
tags:
- Agent
- Tool Use
- Benchmark
- E-commerce
- API Selection
one_liner: 发布含1000个API、长时序任务的电商工具调用基准与确定性模拟评估框架
practical_value: '- 企业电商Agent评估可复用SLATE的确定性仿真框架，无需对接数千线上API即可完成长时序工具调用链路的正确性验证，大幅降低测试成本

  - 内部工具调用Agent的候选API构造可参考其「语义检索Top N相似工具+混入正确答案」的策略，平衡任务难度与评估公平性

  - 工具调用SOP落地可复用其分层任务拆解、工具输入输出链路依赖校验的设计方案，减少多步调用的级联错误

  - 效果验收可复用其端到端任务成功率的判定逻辑，替代主观LLM-as-judge打分，实现可复现、无偏差的效果评估'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有工具调用基准普遍存在工具库规模小（仅数十个API）、仅支持单步调用评估、依赖主观LLM-as-judge打分的问题，无法匹配企业电商场景下长时序任务、千级内部API池、要求确定性可复现评估的真实需求，亟需适配企业级工具调用场景的标准化基准。
### 方法关键点
- 数据集构造：覆盖买家、卖家共11类电商核心任务，包含100个长时序复杂任务，平均单任务10.8个步骤，配套1000个覆盖商品、订单、营销、库存等全链路的API库，其中583个为干扰API
- 确定性仿真：设计上下文感知模拟器，预存（工具+参数）→结果的真实调用映射，支持参数格式归一化匹配，无需对接线上API即可完成链路验证
- 评估逻辑：采用端到端任务成功率作为核心指标，只要调用轨迹触达全部参考结果即判定成功，兼容多种正确执行路径，避免LLM打分的主观性
### 关键结果
评测6组3B-12B参数的开源决策模型及对应基座LLM，最优的Gemma-4-12B-it基座仅达到**5.0%的任务成功率**、74.4%的单步准确率；4/6的决策模型比基座提升6.6-15.7个百分点的单步准确率，但部分决策模型效果弱于基座，说明现有训练策略尚未对齐长时序API选择需求。
> 最值得记住的结论：千级API池下长时序工具调用的成功率受级联错误影响被指数级压低，是当前企业级Agent落地的核心瓶颈。
