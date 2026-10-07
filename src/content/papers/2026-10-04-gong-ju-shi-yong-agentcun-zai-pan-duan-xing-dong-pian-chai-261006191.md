---
title: 'Judged Useless, Queried Anyway: Tool-Using Agents Rarely Turn Their Own Evidence
  Judgments into Stopping Decisions'
title_zh: 工具使用Agent存在判断-行动偏差：明知结果无用仍持续检索
authors:
- Chubin Zhang
- Zhenglin Wan
- Xingrui Yu
- Jingxuan Wu
- Yaxin Zhou
- Ivor Tsang
- Bo An
affiliations:
- Nanyang Technological University
- National University of Singapore
- Agency for Science, Technology and Research (Singapore)
- UNC-Chapel Hill
- Carnegie Mellon University
arxiv_id: '2610.06191'
url: https://arxiv.org/abs/2610.06191
pdf_url: https://arxiv.org/pdf/2610.06191
published: '2026-10-04'
collected: '2026-10-07'
category: Agent
direction: Agent 工具调用停止决策优化
tags:
- Tool-Use Agent
- Retrieval Policy
- Stopping Rule
- LLM Agent
- Agent Evaluation
one_liner: 发现工具使用Agent可准确识别无用检索结果但不会据此停止，提出外挂强制停止规则提升性能
practical_value: '- 做电商导购Agent、搜索推荐Agent时不要指望靠prompt让Agent自己停止无用检索，直接在系统层加强制停止规则：连续k次检索结果被Agent判断为无用就强制终止，成本低收益高，k可根据业务场景调优

  - 评估Agent工具调用效率时不能只看最终成功率，要测时间匹配的停止对比Δ，避免把到期停止误判为证据驱动停止，尤其适合预算敏感的广告检索、商品搜索场景

  - 可以直接从Agent的推理链中读取结果有用性判断，不需要额外调用LLM做标注，能大幅降低规则落地的额外开销

  - 不要给7-8B小参数Agent加复杂的停止规则prompt，基本不会生效，直接外挂规则性价比更高'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有工具增强Agent普遍存在过度检索问题，此前无法明确问题根源是识别无用结果的能力不足，还是无法将判断转化为停止动作，也无法验证prompt层面的规则提示是否有效，这类过度检索在电商导购、广告搜索等大规模落地场景会产生大量不必要的算力开销。
### 方法关键点
- 构建可控检索失败环境，覆盖无故障、持续故障、故障后恢复等6种模式，基于HotpotQA、FEVER两个公开数据集测试
- 设计时间匹配对比指标Δ：在相同步数下对比连续无用结果、曾出现有用结果两种场景的停止概率，精准区分证据驱动停止、到期/时钟驱动停止
- 测试7类主流模型（含4款开源模型、2款闭源模型、1款RL训练的搜索Agent），对比7种条件的效果：无提示、允许记忆回答、预算提示、规则prompt、调用成本提示、计数提示、系统层强制停止规则
- 强制停止规则由外挂harness实现：连续5次检索被Agent判断为无用时，直接强制Agent输出答案
### 关键结果
- 所有测试模型对无用检索结果的识别准确率达97~100%，但无强制规则时，7~8B小模型连续5次判断无用后主动停止的概率仅0.3%~2.5%
- 仅通过prompt提示停止规则、调用成本、无用计数都无法让小模型实现证据驱动停止，预算提示只会让模型卡截止时间停止，预算翻倍时调用量直接翻倍且无成功率提升
- 外挂强制停止规则可让所有模型的Δ转为正值（0.33~0.4），故障源场景成功率提升2.6~9.7个百分点，且停止点不受预算变化影响
- 直接从Agent推理链读取有用性判断的轻量化规则，性能与额外调用LLM做判断的规则差距小于1%，额外开销极低
> 最值得记住的一句话：Agent的判断不等于行动，不要指望prompt教会Agent做复杂决策，系统层外挂简单规则的性价比远高于prompt调优。
