---
title: 'WASP-Mem: Let Agent Organize Procedural Memory. Human Spend Effort on Diagnosis'
title_zh: WASP-Mem：让Agent自主组织过程记忆，人力专注故障诊断
authors:
- Peizhi Niu
- Ge Shi
- Vaibhav Gorde
- Sarthak Ghosh
- Christos Faloutsos
- Min Cheng
- Kevin Chen
affiliations:
- University of Illinois Urbana-Champaign
- Amazon
arxiv_id: '2611.04003'
url: https://arxiv.org/abs/2611.04003
pdf_url: https://arxiv.org/pdf/2611.04003
published: '2026-11-02'
collected: '2026-11-04'
category: Agent
direction: Agent 过程记忆优化与人力投入分工
tags:
- Procedural Memory
- LLM Agent
- Continual Learning
- Memory Consolidation
- Enterprise Agent
one_liner: 提出无预设schema的Agent维基式过程记忆方案，性能更高存储开销更低
practical_value: '- 搭建业务Agent过程记忆系统时优先选择无预设schema的自主组织方案，比硬编码固定结构+显式去重的方案性能高2.1-6.1pp，存储量低2/3以上，可适配电商流程中未预设的异常场景、自定义规则。

  - 人力标注投入优先倾斜到失败案例的诊断，1轮带人类诊断的反馈比4轮Agent自评估的效果高7.0-10.9pp，比仅标注成功案例的收益高9.6-10.5pp，适合电商客服、运营自动化等Agent场景低成本迭代。

  - 记忆系统核心是高信号密度过滤而非大容量存储，WASP-Mem存储仅为原始Trace存储的3-6%，同时性能提升10.9-14.5pp，可大幅降低检索时的上下文Token消耗和KV
  cache开销。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
企业场景下LLM Agent执行复杂流程时，静态预设的规则无法覆盖未文档化的内部政策、异常服务状态、执行时才暴露的恢复路径，重新微调模型成本极高，过程记忆是无需训练即可补全知识缺口的核心方案，但现有过程记忆整理方法要么冗余度高泛化性差，要么预设结构限制了关键信息保留，同时人力投入的ROI分配不清晰。

### 方法关键点
- 提出WASP-Mem，将Agent执行轨迹和反馈整理为可互链的Markdown维基页面，支持增量更新、语义检索+目录导航查询、自动质量校验三个核心操作，完全由Agent自主决定页面结构、内容和去重逻辑，无需提前预设知识schema。
- 开展四维度控制变量实验：系统性对比不同记忆整合方式、反馈类型、Trace摄入范围、迭代轮次的效果差异。

### 关键实验
在TheAgentCompany、τ²-Bench零售两个企业级基准上，对比Claude Opus 4.6、GPT-5.4、GLM-3三个模型：
- 无预设schema的Free Form版本WASP-Mem比最强基线提升checkpoint通过率4.6-6.1%，存储量降低57-61%，相比无记忆基线通过率提升10.9-14.5pp，任务全通过率提升11.8-25pp。
- 预设schema+显式去重的变体性能比Free Form低2.1-6.1pp，存储高2.3-7.2倍；1轮带人类诊断的反馈比4轮Agent自评估效果高7.0-10.9pp，仅摄入成功案例几乎无额外收益。

### 最值得记住的一句话
给Agent提供通用记忆框架即可，让它自主组织过程知识，人力仅需投入到失败案例的诊断上，远好于提前预设复杂的记忆结构和规则。
