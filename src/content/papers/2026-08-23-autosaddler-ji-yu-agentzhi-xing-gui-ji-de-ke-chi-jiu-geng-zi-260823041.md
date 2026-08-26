---
title: 'AutoSaddler: Automatic Harness Optimization with Durable Updates from Agent
  Execution Traces'
title_zh: AutoSaddler：基于Agent执行轨迹的可持久更新自动Harness优化框架
authors:
- Sungho Park
- Wonjoong Kim
- Rongyuan Tan
- Jue Zhang
- Wook-Shin Han
- Pengfei Gao
- Chanyoung Park
- Yongqiang Yao
- Rao Fu
- Elsie Nallipogu
affiliations:
- POSTECH
- KAIST
- Southern University of Science and Technology
- Microsoft
arxiv_id: '2608.23041'
url: https://arxiv.org/abs/2608.23041
pdf_url: https://arxiv.org/pdf/2608.23041
published: '2026-08-23'
collected: '2026-08-26'
category: Agent
direction: Agent 长周期任务 Harness 自动优化
tags:
- LLM Agent
- Harness Optimization
- Offline Learning
- Failure Diagnosis
- Long-horizon Task
one_liner: 将Agent Harness优化转化为离线学习问题，结合深度诊断等模块在三个长周期任务基准上取得显著提升
practical_value: '- 可复用「深度诊断+结构化补丁+泛化校验」三段式Agent迭代框架，同时覆盖prompt、工具、执行逻辑三层优化，替代现有纯prompt调优方案，解决单维度优化的局限性

  - 迭代Agent系统时可引入EvoDAG结构存储跨批次优化经验，结合验证集过滤过拟合的局部修复补丁，大幅降低新版本的回归概率

  - 优化Agent时可参考分阶段补丁调度策略：优先做工具、执行逻辑等能力层补丁，再做prompt、规则等引导层补丁，能力层补丁接受率更高、回归概率更低

  - 电商导购Agent、售后Agent等长周期交互场景，可直接套用该框架基于历史失败会话自动优化系统逻辑，降低人工调试成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
长周期多步任务中LLM Agent可靠性极低，微小局部错误会级联导致整体任务失败；当前靠人工设计Harness（包含prompt、工具配置、控制逻辑）提升鲁棒性的方案成本极高，需要遍历的设计空间极大，且评估、调试长轨迹的效率极低，无法快速适配新场景、新基座模型。

### 方法关键点
- 将Harness优化定义为离线学习问题，采用mini-batch迭代范式，每次迭代先在小批量训练任务上测试当前Harness表现
- 诊断-补丁阶段：基于失败轨迹做深度根因诊断，按prompt补丁、工具补丁、中间件补丁三类结构化生成补丁，采用分阶段调度策略，优先做工具、逻辑等能力层补丁，再做prompt等引导层补丁
- 泛化校验阶段：补丁先在当前mini-batch验证是否提升表现，通过后再在验证集评估泛化性，避免过拟合单条轨迹
- 引入EvoDAG有向无环图存储所有迭代历史的Harness版本、补丁、效果和经验教训，进化阶段基于历史经验合成下一代候选Harness，避免陷入局部最优

### 关键实验
在GAIA2、SWE-Bench Pro、Terminal-Bench 2.0三个长周期Agent基准上测试：相比手工base Harness，分别提升9.0pp、9.6pp、10.0pp；对比最优自动基线GEPA、Meta-Harness，分别领先7.4pp、4.4pp、6.7pp；优化效率是基线的10倍，仅需147条执行轨迹就能达到最优dev集表现，消耗1000次任务执行就能达到72.3%的dev准确率，远超基线2800次执行的饱和表现。

### 核心结论
有效的Harness优化需要三个核心要素：深度调试而非浅层反思、定向修改而非无约束编辑、泛化感知的选择而非单轨迹修复
