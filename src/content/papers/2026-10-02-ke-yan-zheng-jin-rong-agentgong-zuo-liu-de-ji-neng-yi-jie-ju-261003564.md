---
title: Knowledge or Calculator? Decomposing the Skill Premium in Verifiable Financial
  Agent Workflows
title_zh: 可验证金融Agent工作流的技能溢价拆解：知识还是工具？
authors:
- Jermyn Zhen Yong Bek
- Zhuang Qiang Bok
- Zhongtian Sun
affiliations:
- Independent Researcher
- Deep Insight Labs
- University of Kent
- University of Cambridge
arxiv_id: '2610.03564'
url: https://arxiv.org/abs/2610.03564
pdf_url: https://arxiv.org/pdf/2610.03564
published: '2026-10-02'
collected: '2026-10-05'
category: Agent
direction: Agent评测 · 金融领域技能溢价拆解
tags:
- LLM Agent
- Benchmark
- Financial AI
- Tool Use
- Skill Evaluation
one_liner: 推出含2603个金融任务的FinSkillBench评测集，拆解Agent技能溢价的构成来源
practical_value: '- 做领域Agent优先落地预验证的可执行工具包，比让Agent临时生成技能效率高得多：数值类任务工具单独提分19.5pp，比文档（5.6pp）效果好，还省token和latency，电商场景的优惠券核算、库存预估等计算类任务可直接套用现成工具，避免让LLM自行推导计算。

  - 多步骤Agent工作流必须加跨阶段的全局校验，不能只看单步准确率：论文中9步金融工作流单步全满分但最终合规率0，对应电商全链路营销、履约等多环节Agent，要从原始业务规则校验最终结果，不能信任中间步骤的自校验结果。

  - 做Agent效果评测时要明确披露工具、数据访问规则、轮次限制，不同测试框架下的效果增益不具备直接可比性，避免实验室环境测出的效果上线后大幅缩水。'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有金融Agent评测大多聚焦知识问答，忽略了真实投资工作流要求的数值计算准确性、流程合规性、可验证结构化输出，也无法量化技能包中不同组件（文档、工具）的实际贡献，同时单步任务的高准确率无法保证多步工作流的最终正确性，亟需更贴近真实业务的可控评测框架。

### 方法关键点
- 构建FinSkillBench评测集，覆盖投资组合构建、风险管理、基本面分析3大领域12个子任务，共2603个带时间戳的任务样本，配套可复现的隐藏真值和确定性验证器。
- 设计5组对照实验：无技能、仅人工梳理文档、仅领域可执行工具、全套人工梳理技能包、Agent自行生成技能，控制变量拆解技能溢价的来源。
- 新增9阶段串联工作流测试，对比单步验证和全局合规校验的差异，验证多步任务的误差传递问题。

### 关键实验结果
测试9款主流大模型，共执行17820次任务：人工梳理技能包相对无技能基线提分16.2pp（0.366→0.528），Agent单轮内自行生成技能仅提分0.5pp，且token消耗翻倍、latency提升28%；拆分组件后仅文档提分5.6pp，仅工具提分19.5pp，二者结合增益低于单独加和（因轮次限制导致资源竞争），其中数值密集型任务工具贡献占比超80%，流程/输出schema类任务文档贡献更高；9阶段工作流测试中，单步准确率全部接近满分的情况下，自主串联的工作流最终合规率为0，出现「静默胜任」的失效模式。

最值得记住的结论：Agent的技能溢价不是大模型本身的固有属性，而是模型、可用资源、交互规则、评测框架共同作用的结果，多步工作流的全局合规校验远比单步准确率重要。
