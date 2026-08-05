---
title: 'MonitrLLM: A Community-Centered Evaluation Infrastructure for Large Language
  Models'
title_zh: MonitrLLM：面向大语言模型的社区中心化评估基础设施
authors:
- Victor Ojewale
- Ro Encarnación
- Suresh Venkatasubramanian
- Danaé Metaxa
affiliations:
- Brown University
- University of Pennsylvania
arxiv_id: '2608.02409'
url: https://arxiv.org/abs/2608.02409
pdf_url: https://arxiv.org/pdf/2608.02409
published: '2026-08-03'
collected: '2026-08-05'
category: Eval
direction: LLM评估 · 交互轨迹与用户反馈关联
tags:
- LLM Evaluation
- User Feedback
- Conversation Trajectory
- Open-source
- User Intent
one_liner: 开源社区导向LLM评估框架，关联对话轨迹、用户任务意图与结果反馈
practical_value: '- 做Agent/LLM导购效果评估时，不要仅依赖用户满意度评分，需额外关联实际任务完成率（如下单/找品成功率），规避高满意下的隐性任务失败

  - 多轮交互不要直接判定为用户高engagement，可作为任务难度高/当前推荐未命中需求的信号，触发降级或人工介入逻辑

  - 搭建内部LLM应用评估体系时，可复用「全对话轨迹+用户意图+任务结果」三元组作为核心评估信号，替代单一满意度指标'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有LLM评估体系存在明显断层：benchmark仅测量受控场景下的任务能力，大规模会话语料缺乏用户反馈，界面内反馈机制仅记录满意度却不关联任务目标，没有基础设施可常规打通交互轨迹与用户定义的任务结果。
### 方法关键点
开源MonitrLLM社区中心化评估基础设施，将完整会话转录文本、用户上报的任务意图、结果评估三者作为核心评估信号而非可选元数据，直接打通三者的关联链路。
### 关键结果
26名大学生参与的2周试点共收集206份带完整会话的评估报告：用户平均交互满意度达4.19/5，但任务实际失败率高达23.1%；多轮会话的失败率是单轮会话的2.5倍，说明长交互更可能对应任务难度高，而非用户参与度高。
