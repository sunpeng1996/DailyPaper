---
title: Is Deep Research Reliable? Misleading Knowledge Induces False Conclusions
title_zh: 深度研究Agent可靠性评估：误导性知识诱导错误结论
authors:
- Pengyu Zhu
- Lijun Li
- Longju Yang
- Sen Su
affiliations:
- 北京邮电大学
- 上海人工智能实验室
- 重庆邮电大学
arxiv_id: '2607.20891'
url: https://arxiv.org/abs/2607.20891
pdf_url: https://arxiv.org/pdf/2607.20891
published: '2026-07-22'
collected: '2026-07-31'
category: Agent
direction: Agent 深度研究鲁棒性评估
tags:
- Deep Research Agent
- Misinformation Robustness
- Evaluation Framework
- LLM Reliability
- Agent Defense
one_liner: 提出MisKnow-Agent评估框架，量化深度研究Agent被误导性知识诱导采纳错误结论的比例
practical_value: '- 搭建业务Agent（如电商调研、选品、用户研究Agent）的鲁棒性测试集时，可复用MisKnow-Agent的「蓝图构建→可控样本生成→多模型交叉校验」流水线，低成本生成符合业务场景的误导性测试用例

  - 优化长流程Agent的校验逻辑时，优先在最终合成前加核验节点：实验显示预合成阶段注入误导信息的采纳率高达85.5%，远高于早中期注入的40%左右

  - 设计Agent防御策略时，不要盲目叠加前后置校验：实验显示预+后置防御的效果不总是优于单防御，且防御效果强依赖底座LLM选型，需结合业务底座做适配

  - 做检索模块优化时，不需要过度纠结误导内容的粗排序位置：实验显示搜索结果排名对错误结论采纳率影响不足2%，重点要放在证据本身的可信度校验上'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
Deep Research Agent已被广泛用于长周期信息调研、科学研究等知识密集型任务，依赖多轮检索、证据积累生成结构化报告，但现有评估未系统验证这类Agent遇到看似可信、实际虚假的误导性知识时，是否会在长流程中隐式复用错误信息，最终在报告中采纳错误结论，无法满足业务对输出事实准确性的要求。
### 方法关键点
- MisKnow-Agent可控评估框架：为每个任务先构建包含预设错误结论、分权威等级机构池、采纳判定规则的蓝图，再按不同权威等级（高/中/低）、内容风格（论文/新闻/博客/帖子）生成定制化误导性文档
- 多轮交叉校验过滤机制：5个搜索增强模型一致判定为虚假的样本才保留，最终得到5933条高质量误导性样本，覆盖DeepResearch Bench的100个任务
- 两种可复用防御策略：前置防御在用户query后拼接通用证据校验提示，引导Agent全程核验证据；后置防御新增独立搜索Agent对最终报告逐claim校验修正
- 评估指标采用FCAR（错误结论采纳率）：仅统计最终报告明确支持错误结论的占比，排除仅提及、引用、反驳的情况，避免误判
### 关键实验结果
测试覆盖2个开源框架DeerFlow、WebThinker，搭配3款不同能力的底座LLM，以及闭源的Gemini Deep Research。核心数字：无误导内容注入时FCAR为0%；仅注入1条误导文档时平均FCAR升至54.7%；预合成阶段注入误导内容的FCAR高达85.5%；搜索结果排名对FCAR影响不足2%；论文风格的误导内容FCAR比帖子风格高23.5%，影响高于权威等级差异带来的14.8%差距；前后置防御可降低FCAR但无法完全消除，组合防御不总是产生叠加增益。
### 核心结论
孤立识别误导性文档不足以保障Agent可靠性，必须把校验能力嵌入证据采集、中间状态更新、最终合成的全流程
