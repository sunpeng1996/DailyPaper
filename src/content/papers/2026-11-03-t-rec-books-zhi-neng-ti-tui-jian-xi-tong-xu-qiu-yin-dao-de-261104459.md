---
title: '$τ$-Rec-Books: A Disclosure-Controlled Benchmark for Requirement Elicitation
  in Agentic Recommender Systems'
title_zh: τ-Rec-Books：智能体推荐系统需求引导的披露可控评测基准
authors:
- Bharath Sivaram Narasimhan
- Karthik R. Narasimhan
affiliations:
- Independent Researcher, Mountain View, CA
- Princeton University, Princeton, NJ
arxiv_id: '2611.04459'
url: https://arxiv.org/abs/2611.04459
pdf_url: https://arxiv.org/pdf/2611.04459
published: '2026-11-03'
collected: '2026-11-04'
category: Eval
direction: 智能体推荐 · 需求引导评测
tags:
- Conversational Recommendation
- LLM Agent
- Evaluation Benchmark
- Preference Elicitation
- User Simulation
one_liner: 推出用户需求披露时机可控的智能体推荐评测基准，量化多场景下的推荐效果差异
practical_value: '- 搭建自有领域的智能体推荐评测集时，可复用「固定需求集合、仅调整披露时机」的分组设计，精准量化需求引导模块的效果，消除任务本身差异的干扰

  - 智能体推荐的prompt工程可直接复用两个优化点：一是显式要求Agent主动询问未披露需求，二是要求推荐前先向用户提案、获取反馈后再调用推荐工具，可将混合披露场景的成功率提升至0.93以上

  - 工具选型上优先给Agent提供结构化过滤搜索接口，比纯关键词搜索平均提升7.1%的成功率，且受商品/内容库规模扩大的影响极小，2万条库相比5千条库成功率仅降0.8个百分点'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有智能体/对话推荐系统的评测未将用户需求披露时机作为控制变量，无法精准区分推荐失败源于需求挖掘不足还是检索排序能力缺陷；真实场景下用户仅主动披露36%的需求，52%需被询问才透露，12%仅能通过推荐后的反馈推断，现有基准既无法覆盖这类场景，还存在依赖LLM judge打分不稳定、结果难复现的问题。
### 方法关键点
- 构建基于Wikidata的2万本图书元数据集，嵌套5k、10k子集，生成150组共450个任务，每组任务的需求、答案集、用户画像完全一致，仅分三种披露模式：volunteer（所有需求主动告知）、mixed（1个需求主动说，其余询问后告知）、hidden（至少1个需求全程不披露，仅能通过推荐后的接受/拒绝反馈推断）
- 采用规则化模拟用户应答，完全基于图书元数据打分，无需LLM judge，所有结果可复现
- 对比4类LLM Agent（DeepSeek V4.1、GLM 5.3、Qwen 3.8 27B、GPT-6.1 Sol）、2种搜索接口（关键词、结构化过滤）的表现，设置popularity基线（先问所有字段再推热门品）、eliminating基线（通过拒绝反馈排除无效需求）
### 关键结果
- 所有Agent和接口的平均成功率从volunteer场景的0.975，降至mixed场景的0.756，再降至hidden场景的0.283；加入主动询问的prompt后，所有Agent的mixed场景成功率至少提升至0.931
- 结构化过滤接口比纯关键词搜索平均成功率高7.1个百分点，库从5k扩容到20k时，结构化接口成功率仅降0.8个点，远低于关键词接口的4.2个点
- hidden场景下要求Agent先提案再推荐，成功率可提升至0.48-0.62，叠加拒绝反馈消去无效需求的逻辑，成功率最高可达0.956

> 最值得记住的结论：智能体推荐的效果瓶颈，绝大多数场景下都不是检索能力或内容库规模，而是是否能主动挖掘用户未披露的需求、且在推荐前通过提案验证匹配度。
