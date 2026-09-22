---
title: 'DolphinBench: Mapping the Pareto Frontier of Agent Memory'
title_zh: DolphinBench：Agent记忆能力的帕累托前沿评估基准
authors:
- Soumil Rathi
- Deshraj Yadav
- Taranjeet Singh
affiliations:
- Mem0
arxiv_id: '2609.24971'
url: https://arxiv.org/abs/2609.24971
pdf_url: https://arxiv.org/pdf/2609.24971
published: '2026-09-21'
collected: '2026-09-22'
category: Eval
direction: Agent记忆 · 多维度评测基准
tags:
- AgentMemory
- Benchmark
- LLMAgent
- MemoryEvaluation
- ParetoOptimization
one_liner: 首个结合动作评测、多指标上报、用例有效性校验的Agent记忆评测基准
practical_value: '- 业务Agent记忆系统选型时不要仅看准确率，需同步评估成本、latency的帕累托表现，匹配业务容忍度，比如电商实时导购Agent对latency要求高，可优先选择低延迟记忆方案

  - 内部自研Agent记忆能力评测可复用论文的用例校验逻辑：每个测试用例必须满足有对应记忆时通过、无对应记忆时失败，避免无效用例干扰评估结论

  - 电商个性化导购、售后等场景的Agent记忆效果评估，可抛弃传统QA式评测，改用任务动作完成率作为核心指标，更贴近真实用户交互场景'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有Agent记忆基准多采用问答格式，问题本身会给出明确的检索提示，跳过了Agent主动识别需要召回记忆的核心难点，无法反映真实场景下的记忆能力；且绝大多数基准仅评估准确率，忽略生产部署必须考虑的成本、延迟 tradeoff，易出现实验室指标好但无法落地的问题；同时多数合成基准存在测试用例无效、答案标注错误等缺陷，评测结果可信度低。
### 方法关键点
- 覆盖3类典型知识工作者persona：创业公司CEO、基建工程师、产品经理，为每个persona生成跨度数年、约500k tokens的对话历史，模拟真实长周期交互场景
- 共设计600个无检索提示的任务（单persona200个），需Agent主动调用历史记忆完成工具调用类动作，避免问答格式的提示bias
- 所有测试用例经过双重有效性校验：给Agent提供对应历史时连续2次测试均通过，不提供时连续2次均失败，剔除无效用例
- 要求上报准确率、总运行成本、单任务中位数延迟三个核心指标，可绘制不同记忆系统的帕累托最优前沿
### 关键结果
在600个任务上对比不同Agent框架、基座LLM、记忆系统的组合：最优配置（Hermes框架 + GPT-5.6-Luna + Mem0）准确率达70.67%；对比发现成本最高的配置既不是准确率最高也不是延迟最低的，Mem0相比内置记忆可提升5个点准确率的同时降低15%的中位数延迟。
### 核心结论
Agent记忆系统的评估不能只看准确率，需结合业务对成本、延迟的要求选择帕累托最优配置，单一指标无法反映记忆系统的落地价值
