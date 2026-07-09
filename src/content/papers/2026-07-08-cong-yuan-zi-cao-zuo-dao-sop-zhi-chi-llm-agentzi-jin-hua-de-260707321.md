---
title: 'From Atomic Actions to Standard Operating Procedures: Iterative Tool Optimization
  for Self-Evolving LLM Agents'
title_zh: 从原子操作到SOP：支持LLM Agent自进化的迭代工具优化框架
authors:
- Haipeng Ding
- Yuexiang Xie
- Zhewei Wei
- Yaliang Li
- Bolin Ding
affiliations:
- Renmin University of China
- Alibaba Group
arxiv_id: '2607.07321'
url: https://arxiv.org/abs/2607.07321
pdf_url: https://arxiv.org/pdf/2607.07321
published: '2026-07-08'
collected: '2026-07-09'
category: Agent
direction: Agent自进化 · 工具集动态优化
tags:
- LLM Agent
- Self-Evolution
- Tool Optimization
- SOP
- Non-Parametric Learning
one_liner: 提出EVOSOP框架，将原子工具序列合成为可复用SOP，通过迭代优化提升Agent任务效率与成功率
practical_value: '- 电商/客服/订单处理等重复流程场景，可直接复用SOP生成逻辑，将高频调用的原子工具（查订单、改地址、发通知等）封装为高阶工具，减少推理轮次，降低API成本与级联错误率

  - 四模块工具全生命周期管理流程可直接落地：构造→合并→评估→剪枝，无需修改LLM参数即可快速优化现有Agent工具调用效率，避免工具集膨胀导致的决策噪声

  - SOP评估打标规则可复用：按最优执行、部分效用、中性、负向干扰、实现缺陷五类分类，自动剪枝低质/冗余SOP，适配大促等业务流程快速迭代场景，快速淘汰失效工具'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM Agent大多依赖静态原子工具集，每次处理重复流程都需要重新编排低阶逻辑，推理开销大、级联错误率高；现有动态生成工具的方法均为单次生成，缺乏生命周期管理机制，容易导致工具集膨胀、冗余噪声多，大幅提升Agent决策复杂度。

### 方法关键点
- 提出非参数化EVOSOP框架，无需修改底层LLM参数，通过四模块完成工具集迭代优化：
  1. Constructor：从执行轨迹中提取高频共现的原子操作序列，合成带条件判断、错误处理逻辑的可调用SOP
  2. Merger：合并功能冗余的SOP，生成泛化性更强的高阶工具，控制工具集规模，降低上下文冗余
  3. Evaluator：用更新后的工具集重新执行训练任务，收集SOP实际执行表现数据
  4. Reviewer：基于执行数据对SOP打标分类，剪枝高错误率、低效用的冗余工具
- 加入checkpoint机制，保留每轮迭代的工具集与日志，选择训练成功率最高的版本作为最终输出，避免误删有效SOP

### 关键结果数字
在ACEBench、Tau2Bench两个Agent基准测试中，对比ReAct、DFSDT、ASI、DRAFT等基线，以GPT-4o为backbone时：ACEBench多步任务成功率最高提升13.4%，多轮任务成功率最高提升12.2%，推理轮次较ReAct降低约30%；Tau2Bench电信场景成功率最高提升6.2%。

最值得记住的一句话：Agent自进化的核心不是无限新增工具，而是通过迭代的工具生命周期管理，得到小而精的高可靠高阶工具集。
