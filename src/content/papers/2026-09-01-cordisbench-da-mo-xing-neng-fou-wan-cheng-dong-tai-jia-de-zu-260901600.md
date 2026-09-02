---
title: 'CordisBench: Can Language Models Reason About Component Lifecycles in Dynamic
  Agent Harnesses?'
title_zh: CordisBench：大模型能否完成动态Agent框架的组件生命周期推理
authors:
- Damien Sileo
- Dimitri Kachler
affiliations:
- Univ. Lille
- Inria
- CNRS
- Centrale Lille
- CRIStAL
arxiv_id: '2609.01600'
url: https://arxiv.org/abs/2609.01600
pdf_url: https://arxiv.org/pdf/2609.01600
published: '2026-09-01'
collected: '2026-09-02'
category: Agent
direction: Agent 组件生命周期推理基准构建
tags:
- Agent
- LLM Reasoning
- Benchmark
- Dynamic Harness
- Lifecycle Reasoning
one_liner: 发布含1200道题的Agent组件生命周期推理基准，测评多模型推理能力与扩展性
practical_value: '- 做Agent动态插件/工具调度的业务，可直接复用本基准的依赖推理、销毁顺序预测逻辑，避免组件冲突导致的状态异常

  - 当Agent需要动态调整推荐/广告工具链时，优先用显式依赖+语义规则计算状态变更，比让LLM硬推理成本低、准确率高，减少不必要的推理token消耗

  - 可复用基准的分层任务设计：先做影响组件定位，再做状态预测，最后做重配置选型，拆分复杂推理任务降低出错率'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
动态Agent框架支持运行时增删改插件、工具、内存策略等组件，带来了新的推理负担：单个组件变更会通过依赖传递、清理逻辑影响其他组件，销毁顺序的差异还可能导致最终状态不符合预期，但当前缺乏专门的基准测评LLM对这类生命周期逻辑的推理能力。

### 方法关键点
- 构建CordisBench共1200道结构化问题，覆盖受控形式化、可执行Cordis原生两类场景，组件交互数从2到32级逐步提升，任务包括组件影响定位、销毁调度预测、全局条件判定、可达条件判定、重配置选型5类
- 设计有限参考语义，可枚举所有合法生命周期路径得到精确参考答案，Cordis原生场景的答案直接与运行时执行结果比对验证
- 设置shortcut对照组，排除模型靠词法特征、题目位置等作弊的可能

### 关键实验
测评Gemini 3.7 Flash、GPT-5.6 Luna、DeepSeek V4 Flash三款效率向模型：
1. 组件定位任务表现随交互数增长下降较慢，但状态预测、跨调度顺序推理任务表现下降明显，GPT-5.6 Luna在交互数从2升至32时，Cordis原生重配置成功率从62.5%降至25.0%
2. 提升推理努力可大幅提升准确率，但GPT-5.6 Luna在16交互数场景下平均单题消耗近3000推理token，成本极高
3. 有限参考语义与Cordis运行时结果100%匹配，说明这类结构化推理完全可以用符号方法零成本解决

### 核心结论
Agent动态框架的组件生命周期推理应优先用显式依赖的符号计算完成，仅把LLM的推理能力用在无法形式化的高层决策上，兼顾可靠性和成本
