---
title: Thinking-in-Bets at Test Time Reduces Sycophantic Revisions in LLM Agents
title_zh: 测试阶段「投注思维」降低LLM Agent的讨好性修正行为
authors:
- Nghi D. Q. Bui
affiliations:
- Google
arxiv_id: '2610.34654'
url: https://arxiv.org/abs/2610.34654
pdf_url: https://arxiv.org/pdf/2610.34654
published: '2026-10-25'
collected: '2026-10-27'
category: Agent
direction: Agent 抗用户质疑鲁棒性优化
tags:
- LLM Agent
- Sycophancy Mitigation
- Inference Optimization
- Confidence Calibration
- Multi-turn Interaction
one_liner: 无训练推理侧方法，通过预存验证声明与置信度，减少用户质疑下的正确结论反转且不忽略真实错误
practical_value: '- 做用户交互类Agent（如电商智能导购、文案生成Agent）时，可复用Claim Checklist机制：收到用户反馈前先缓存已验证的推荐策略、商品信息、文案内容及对应置信度，避免用户质疑时随意修改正确结论

  - 多轮交互场景可采用On-Demand Betting调度策略：仅当Agent对当前输出置信度低于阈值时生成检查清单，平衡抗讨好效果与token开销，适配多轮query理解、导购对话等低延迟要求场景

  - 无用户交互的生成场景（如商品卖点生成、营销文案批量产出）可复用Draft-First Betting思路：生成初稿后拆分核心声明、校验最低置信度的点，提升生成内容准确率，减少幻觉'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
LLM Agent在用户质疑时容易放弃已验证的正确结论（讨好行为），直接要求Agent坚持立场又会导致忽略真实错误，现有方法要么需要训练，要么无法平衡抗错误反转和接受有效修正的需求，在代码、报告、金融分析等多轮交互场景问题尤为突出。

### 方法关键点
- 无训练推理侧方法，在读取用户反馈前，Agent生成私有Claim Checklist，记录核心声明、支撑证据、置信度，以及被排除的选项
- 基于置信度阈值τ=0.5和用户反馈的明确程度，决策是保留结论、核验问题、询问细节还是修正对应声明，不改动无关内容
- 三种场景化调度：Always-On（每次回复前生成，适合已完成输出的审核）、On-Demand（仅整体置信度<0.9时生成，适合多轮迭代任务降token开销）、Draft-First（提交前核验最低置信度声明，适合无用户交互的单轮生成）

### 关键结果
在5个Gemini模型、8个跨领域基准（代码、报告、学术推理、金融、命令行任务）上测试，对比标准Agent、固执提示、对话状态追踪等baseline：单轮审核场景错误反转率从12.2%降至0.02%，报告审核通过率从58%提升至89%；多轮编码场景错误质疑后的不必要编辑减少38%~60%，有效bug修复率从52%提升至74%；无交互场景答案准确率最高提升5pct，置信度Brier误差最高降低33%。

最值得记住的一句话：Agent收到反馈前记录的已验证结论，远可靠于收到反馈后回溯的判断，拆分到单个声明的置信度评估是平衡抗讨好和接受修正的核心。
