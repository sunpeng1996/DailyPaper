---
title: 'Mingbird: A Local-First Agent Harness Enabling Small Open Models to Complete
  Real Tasks'
title_zh: Mingbird：适配小参数量开源模型的本地优先Agent编排框架
authors:
- Hao Wang
- Ting Huang
affiliations:
- University of Science and Technology Beijing
- Honor Device Co., Ltd.
arxiv_id: '2610.02001'
url: https://arxiv.org/abs/2610.02001
pdf_url: https://arxiv.org/pdf/2610.02001
published: '2026-10-01'
collected: '2026-10-02'
category: Agent
direction: 本地Agent · 小模型适配优化
tags:
- Agent
- SmallLLM
- LocalFirst
- AgentHarness
- Ollama
one_liner: 针对2-9B小开源模型设计10项故障补偿机制，大幅提升本地Agent真实任务完成率
practical_value: '- 小模型Agent落地可复用3个核心trick：字节级严格控制静态prefill token数避免上下文溢出、任务结束前重注入原始需求做校验避免虚假完成、工具调用签名去重避免死循环，无需修改模型即可提升小模型Agent成功率

  - 电商场景Agent架构可复用域分类+按需加载工具的设计：处理用户query时先分类需求域，仅挂载商品查询、订单、优惠券等相关工具，既节省上下文空间又降低prefill耗时

  - 可复用其artifact-based确定性评分框架做内部Agent评估：放弃模糊人工打分，直接基于最终产出的结构化结果（如营销文案合规性、推荐商品匹配度）自动评分，大幅提升评估效率和一致性'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
2-9B小开源模型可在普通笔记本本地运行，但现有面向大模型设计的云原生Agent框架下，小模型普遍出现prefill上下文溢出、自校正发散、工具调用死循环、任务静默放弃等问题，行业普遍认为小模型无法承载Agent任务，而实际验证发现70%以上故障来自编排框架而非模型本身，优化空间极大。

### 方法关键点
- 设计10项针对性机制匹配小模型故障模式，核心3项：M1字节级零增长prefill预算，分类任务域仅加载相关工具静态prompt，出厂prefill固定797token；M3完成校验门，接受任务完成前重注入原始需求要求模型逐点核对交付物；M4签名级死循环检测，相同工具+参数调用≥6次触发矫正。
- 配套5层安全模型避免本地Agent操作风险，所有能力均适配Windows+Ollama runtime，无额外推理 overhead。

### 关键实验
- 自研LRAB受控基准，固定机器、模型、算力预算、评分规则，仅换编排框架，对比4个框架×4个模型（2B-35B）×18个真实任务，采用确定性artifact评分。
- 核心结果：Mingbird整体得分0.886，远超goose（0.631）、opencode（0.479）、agent-mini（0.405）；2B小模型场景下优势最显著，得分0.821 vs 基线最高0.271，无小模型性能悬崖。第三方τ2-bench 278个任务下得分0.856，领先原生Agent的0.791和opencode的0.737。

### 核心结论
小模型Agent落地的瓶颈往往不是模型本身的能力，而是编排框架是否适配小模型的特性，针对性的工程优化能带来远超模型迭代的收益。
