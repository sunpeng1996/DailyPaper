---
title: How Web Research Agents Interpret User Priorities
title_zh: 网页研究Agent对用户优先级的解读机制研究
authors:
- Robin Sharma
- Parisa Suchdev
affiliations:
- Independent Researcher
- University of Vermont
arxiv_id: '2611.22989'
url: https://arxiv.org/abs/2611.22989
pdf_url: https://arxiv.org/pdf/2611.22989
published: '2026-11-17'
collected: '2026-11-18'
category: Agent
direction: Web研究Agent · 用户优先级对齐
tags:
- Web_Research_Agent
- User_Intent_Alignment
- Agent_Evaluation
- Human_AI_Interaction
- Financial_Agent
one_liner: 对比两类网页研究Agent，发现相同用户优先级下评估标准差异显著，仅看报告聚焦度不足以评估效果
practical_value: '- 做电商/金融导购类Agent时，不要只接受用户的模糊优先级（如「性价比高」「抗风险」），要提前将优先级拆解为可量化的评估标准显式给用户确认，避免Agent自行解读导致结果不符合预期

  - 评估搜索/研究类Agent任务完成效果时，除了检查最终输出是否提到用户要求的优先级，还要额外校验输出背后的评估逻辑是否和用户预期一致，避免「表面遵循需求、实际判断逻辑偏差」的问题

  - 设计Agent交互界面时，可以增加评估标准预览/修改环节：用户提交任务后先展示Agent计划使用的判断维度，用户调整后再执行任务，大幅提升结果对齐率，同时降低用户prompt编写成本

  - 若业务用不同基座的Agent执行同一类任务，要提前通过系统prompt固定评估维度，消除基座差异：比如同样是「优先选高增长商品」，不同基座的判断逻辑可能完全相反'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
Web研究Agent在用户仅给出模糊优先级（如「关注长期增长」「抗风险能力强」）时，会自行选择评估标准，直接影响最终结论，但现有评估仅校验输出准确性和引用合规性，不关注背后的判断逻辑，可能导致结果与用户真实意图偏差，尤其在金融、导购等高stakes场景风险极高。

### 方法关键点
- 选取两类主流商用Web研究Agent：基于GPT-5.6-terra的OpenAI Agent、基于Claude-sonnet-5的Anthropic Agent，均开启官方搜索工具
- 设计3组对照prompt：基础任务（对比微软和Alphabet未来5年业务）、加「关注长期增长」优先级、加「关注长期抗风险能力」优先级，每组每个Agent跑6次，共36次实验
- 全链路记录4类数据：最终报告内容、搜索query、返回的搜索源、报告引用的源，人工标注报告的聚焦方向、评估标准、偏好结论

### 关键结果
24组带优先级的实验中，21组报告确实聚焦了要求的优先级，但不同Agent的评估标准差异极大：增长优先级下，OpenAI Agent按「风险调整后增长」判断，全部选微软；Anthropic Agent按「增速绝对值」判断，全部选Alphabet；抗风险优先级下，两类Agent均选微软，但OpenAI用「经济周期暴露度」、Anthropic用「信用评级」作为判断依据。仅Anthropic Agent的搜索query wording随优先级发生显著变化（同优先级query重合度41% vs 跨优先级33%，调整后p=0.009），OpenAI Agent的搜索行为、引用源几乎不受优先级影响，仅在打开的文档内部搜索不同关键词。

### 核心结论
知道报告聚焦什么优先级，远远不足以知道它是怎么比较选项的。
