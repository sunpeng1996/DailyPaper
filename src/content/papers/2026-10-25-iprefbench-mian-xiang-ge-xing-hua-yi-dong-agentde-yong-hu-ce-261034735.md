---
title: 'iPrefBench: A User-Centric Benchmark for Personalized Mobile Use Agents'
title_zh: iPrefBench：面向个性化移动Agent的用户中心评测基准
authors:
- Yuting Ning
- Ruijia Cheng
- Sushobhan Ghosh
- Peitong Duan
- HungShi Lin
- Abhishek Sundararajan
- Shreyash Pandey
- Huan Sun
- Jeffrey Nichols
- Eldon Schoop
affiliations:
- The Ohio State University
- Apple
arxiv_id: '2610.34735'
url: https://arxiv.org/abs/2610.34735
pdf_url: https://arxiv.org/pdf/2610.34735
published: '2026-10-25'
collected: '2026-10-28'
category: Agent
direction: 个性化Agent · 偏好推断与交互评测
tags:
- Personalized Agent
- Benchmark
- Preference Inference
- Human-Agent Interaction
- Mobile Agent
one_liner: 提出首个区分可推断/需询问信息的个性化移动Agent评测基准
practical_value: '- 个性化Agent架构可借鉴「缺失信息二分法」框架：将用户需求的缺失信息拆分为「可从历史推断」「仅能询问用户」两类，平衡自主推断和交互成本，避免无依据猜测或过度提问降低用户体验。

  - 电商导购/服务类Agent可复用这套判断逻辑：历史可明确推断的偏好（如常买尺码、口味、收货地址）不要重复询问，当前场景特有信息（如送礼对象、时效要求）主动澄清，大幅降低交互摩擦。

  - Agent评测可参考三维度评估体系：分别评估动作完成率、个性化准确率、交互召回/精度，比单纯看任务成功率更能反映真实用户体验。

  - 工程实现上，用户历史召回无需喂全量数据，Top50相关行为事件即可达到和全量历史相当的偏好推断效果，可显著降低token消耗和推理延迟。'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
真实用户的指令普遍存在信息缺失，现有计算机使用Agent（CUA）基准大多基于全指定任务，要么仅提供用户历史不支持交互，要么支持交互但无历史上下文，无法评估Agent「哪些信息该从历史推断、哪些该主动询问用户」的核心能力，而这一能力直接决定个性化Agent的用户接受度。

### 方法关键点
- 基于iOS模拟环境，构造包含3051条跨26个App的用户行为历史的连贯人设，配套严格遵循「仅回答被提问内容、不主动提供额外信息」规则的LLM驱动模拟用户。
- 设计130个真实模糊用户任务，每个缺失信息都标注为「可从历史推断」或「仅能询问用户」两类，同时覆盖指令冲突、偏好迁移、偏好选项不可用三类扰动场景，贴近真实业务情况。
- 评测维度分为两部分：个性化任务完成度（动作完成率、偏好匹配准确率），用户交互效率（需询问信息的召回率、提问准确率，同时惩罚漏问和不必要提问）。

### 关键实验结果
评测7个前沿大模型Agent，表现最好的Claude Opus 5动作完成率达91.6%，但全任务成功率仅47.7%；需询问信息的召回率最高仅44.3%，提问准确率在60%-77%之间；增加执行前主动澄清阶段可提升任务成功率14.6个百分点，但会降低提问精度23.3个百分点，存在明显的猜测和过度询问的权衡。

当前个性化Agent的核心瓶颈不是任务执行能力，而是区分可推断信息和需询问信息的决策能力，单纯鼓励Agent多提问不能解决问题，反而会增加用户负担。
