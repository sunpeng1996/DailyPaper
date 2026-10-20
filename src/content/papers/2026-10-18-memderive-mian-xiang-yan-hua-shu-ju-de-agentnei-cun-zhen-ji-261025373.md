---
title: 'MemDerive: A Diagnostic Benchmark for Agent Memory over Evolving Data'
title_zh: MemDerive：面向演化数据的Agent内存诊断基准测试集
authors:
- Sen Gao
- Yongan Li
- Han Chen
- Bingsheng He
- Ming Wu
- Jason Zeng
- Michael Heinrich
- Shixuan Sun
affiliations:
- National University of Singapore
- Shanghai Jiao Tong University
- Zero Gravity Labs
arxiv_id: '2610.25373'
url: https://arxiv.org/abs/2610.25373
pdf_url: https://arxiv.org/pdf/2610.25373
published: '2026-10-18'
collected: '2026-10-20'
category: Agent
direction: Agent 记忆能力诊断与基准构建
tags:
- Agent_Memory
- Benchmark
- Derived_State
- Evolving_Data
- Diagnostic_Evaluation
one_liner: 首个面向Agent衍生状态记忆的诊断基准，可定位失效环节并追踪动态数据下的答案一致性
practical_value: '- 做电商导购、售后等长周期服务Agent时，不要仅评估最终回答准确率，需新增衍生状态探针测试（比如用户未核销优惠券金额、符合保价条件的订单列表），可定位80%左右「存了正确信息但未召回」的ungathered类失效

  - 电商订单、会员等级等存在联动依赖的场景，不要依赖记忆系统自动更新，需给记忆条目显式标注依赖关系，参考增量视图维护逻辑做隐式状态更新，现有记忆系统对隐式变化的更新率仅41.1%，远低于显式更新的82.4%

  - 记忆系统选型可先用BM25做基线，在衍生状态查询场景下，简单BM25准确率达58.28%，优于Mem0等主流商用记忆系统的30.41%~48.30%，基线达标后再针对性优化复杂记忆逻辑'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
长驻Agent的决策高度依赖从多轮交互历史中推导得到的衍生状态（如用户可推荐的非竞技类商品、用户可报销的差旅金额），现有记忆基准仅评测最终答案准确率，无法定位失效的具体环节，也无法检测隐式状态更新的滞后问题，导致记忆系统的优化方向与实际业务需求错配。
### 方法关键点
- 用Datalog定义所有场景的规则和衍生状态，自动生成带精确黄金标注的推导DAG，每个中间状态都有唯一标准答案，无需人工标注
- 设计三个独立可控的难度维度：Access（召回相关记录的难度）、Evolution（事实更新的频率）、Composition（推导的层数和宽度），可直接定位失效根因所属环节
- 黑盒评估框架，包含可靠性检测、失效诊断、动态维护能力检测三个模块，无需侵入记忆系统内部即可完成全流程评测
### 关键结果
基准覆盖差旅、购物、教育3个领域共10个场景，4692个事件，1503条查询，对比4个主流记忆系统（Mem0、Cognee等）+2个召回基线：
1. 记忆系统准确率仅30.41%~48.30%，低于BM25的58.28%，给定全上下文时LLM准确率可达79.84%，瓶颈在记忆召回而非LLM推理能力
2. 61%~85%的失效为ungathered类型：记忆系统已存储正确的中间状态，但处理用户查询时未成功召回
3. 记忆系统对显式状态更新的刷新达82.4%，但隐式联动更新的刷新仅41.1%，状态滞后问题严重

面向衍生状态的记忆系统优化，核心要解决「正确的状态未被召回」和「隐式依赖变化未被更新」两大问题，而非盲目提升记忆抽取的准确率。
