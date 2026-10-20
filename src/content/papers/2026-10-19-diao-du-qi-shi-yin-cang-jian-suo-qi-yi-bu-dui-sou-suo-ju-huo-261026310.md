---
title: 'The Scheduler Is a Hidden Retriever: How Asynchrony Shapes Evidence Acquisition
  in Search Agents'
title_zh: 调度器是隐藏检索器：异步对搜索Agent证据获取的影响
authors:
- Ruiyang Ren
- Yuhao Wang
- Yinan Zhang
- Chunyan Miao
affiliations:
- Nanyang Technological University
arxiv_id: '2610.26310'
url: https://arxiv.org/abs/2610.26310
pdf_url: https://arxiv.org/pdf/2610.26310
published: '2026-10-19'
collected: '2026-10-20'
category: Agent
direction: Agent 异步搜索调度稳定性优化
tags:
- Search Agent
- Asynchronous Execution
- Schedule Invariance
- Evidence Acquisition
- CEA
one_liner: 提出调度无关的CEA方法，解决异步搜索Agent证据获取不稳定的问题
practical_value: '- 电商导购/商品搜索Agent做异步工具调用时，可复用CEA「子任务证据域完整后再启动推理」的逻辑，避免过早提交检索请求导致因资源返回顺序产生检索偏差

  - 多子任务共享检索预算时，不要使用先就绪先分配的规则，可按用户query核心维度预定义优先级，避免调度顺序导致核心需求的证据缺失

  - Agent子任务可维护私有推理上下文，无需全量携带所有子任务历史，可降低约40%的输入token成本，同时不损失准确率

  - 做Agent性能优化时，无需等待所有初始证据到齐再启动推理，子任务证据集齐即可并行处理，可缩短首包响应时间，提升用户体验'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前LLM搜索Agent普遍采用并行异步推理+信息采集模式提升效率，但证据到达顺序会直接影响检索决策，相同初始输入下证据获取差异最高可达24pp，且这种差异会在所有证据到齐后、二次检索时仍然存在，导致结果不可复现、准确率波动。现有方案要么牺牲效率等待全量证据，要么存在调度依赖的稳定性问题。

### 方法关键点
- 提出Confluent Evidence Acquisition (CEA) 框架，将任务拆分为多个子任务依赖域，每个子任务仅在所属域的所有证据全部到达后才启动推理，不受其他无关证据到达顺序影响
- 共享检索预算采用预定义优先级的调度规则，完全不依赖子任务完成顺序分配检索资源，避免资源竞争导致的证据漂移
- 各子任务维护私有推理上下文，仅在最终合成阶段合并结果，降低上下文传递的token开销

### 关键实验
基于DeepSeek-V4-Flash和GPT-5.6在2Wiki、HotpotQA、MuSiQue基准测试，对比早提交、全量等待等baseline：
1. CEA将证据获取的超额差异降到同顺序重复波动的1.0pp以内，准确率比早提交策略最高提升12.6pp，和全量等待策略准确率持平
2. 子任务私有上下文比共享全量上下文减少40.2%的输入token，准确率无显著下降
3. 最终响应速度比全量等待策略快3.1%~3.9%，首个子任务决策时间提前8s左右

### 核心结论
异步搜索Agent的调度器本质是隐藏的检索器，仅靠提升平均准确率无法保障结果可复现，需要从证据依赖和资源分配两个层面设计调度无关的执行逻辑
