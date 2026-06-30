---
title: 'TUA-Bench: A Benchmark for General-Purpose Terminal-Use Agents'
title_zh: TUA-Bench：面向通用终端使用智能体的评测基准
authors:
- Shoufa Chen
- Luyuan Wang
- Xuan Yang
- Zhiheng Liu
- Yuren Cong
- Yuanfeng Ji
- Feiyan Zhou
- Xiaohui Zhang
- Fanny Yang
- Belinda Zeng
affiliations:
- Meta AI
- Duke University
- Stanford University
arxiv_id: '2606.28480'
url: https://arxiv.org/abs/2606.28480
pdf_url: https://arxiv.org/pdf/2606.28480
published: '2026-06-25'
collected: '2026-06-30'
category: Agent
direction: Agent评测 · 终端智能体
tags:
- Terminal Agent
- Benchmark
- LLM Agent
- Agent Evaluation
- General Agent
one_liner: 构建覆盖多场景120个真实任务的通用终端使用智能体公开评测基准
practical_value: '- 构建垂直领域工具类Agent（如电商运营Agent、搜索调试Agent）的评测基准时，可复用「真实环境+确定性配置脚本+执行式评分」方案，比纯LLM打分更可信

  - 针对多能力维度的Agent评测，可参考按任务族划分能力维度的设计，更清晰定位不同能力的缺口

  - 当前顶级LLM Agent在复杂真实任务仍有超过34%的性能缺口，业务落地需警惕高估现有通用Agent能力'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：现有通用计算机任务评测基准大多针对GUI，已有终端类基准仅聚焦编程类shell工作流，缺少覆盖通用真实任务的终端使用智能体（TUA）评测体系，无法准确评估通用TUA的实际能力。
**方法关键点**：提出TUA-Bench评测基准，包含5大任务族共120个真实任务，覆盖文档编辑、邮件管理、网页信息检索等日常数字活动，以及和PhD级领域专家合作设计的、需专用软件的科研工程流程；所有任务人工设计，可在真实终端通过确定性配置脚本一键搭建环境，采用基于执行结果的客观评分协议。
**关键结果**：当前最强前沿Agent Claude Code（Claude Opus，最大推理努力）仅取得65.8%的整体得分，在所有任务赛道均存在显著性能缺口，验证了通用TUA仍有较大提升空间。
