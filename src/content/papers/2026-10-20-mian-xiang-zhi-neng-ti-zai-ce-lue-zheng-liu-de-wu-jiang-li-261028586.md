---
title: 'Capable Teacher, Myopic Scorer: Reward-Free Teacher Repair for Agentic On-Policy
  Distillation'
title_zh: 面向智能体在策略蒸馏的无奖励教师模型修复方法R2S
authors:
- Shu Zhao
- Tan Yu
affiliations:
- NVIDIA
arxiv_id: '2610.28586'
url: https://arxiv.org/abs/2610.28586
pdf_url: https://arxiv.org/pdf/2610.28586
published: '2026-10-20'
collected: '2026-10-21'
category: Agent
direction: Agent在策略蒸馏 · 无奖励教师修复
tags:
- On-Policy Distillation
- R2S
- Agent Training
- Reward-Free Learning
- Teacher Repair
one_liner: 提出无奖励R2S框架修复教师滚动-打分差距，在12个测试场景中平均超SOTA OPD方法12.8个成功点
practical_value: '- 电商多轮交互Agent（导购、客服）做知识蒸馏时，可复用R2S的教师修复逻辑：针对学生和教师决策分歧大的会话节点，用教师接管的完整交互轨迹微调其单步打分，不需要业务侧额外标注奖励信号

  - 推荐/搜索场景的query改写、多轮检索Agent训练时，可通过该方法抑制模型的无意义延迟操作（反复检索、冗余查询），降低交互轮次消耗，提升用户体验

  - 弱监督模型蒸馏场景可复用论文的无奖励筛选机制：用多轮生成结果的共识或低成本LLM judge作为合格性判断信号，大幅降低标注成本

  - 小模型自迭代场景不需要依赖更大的教师模型，用模型自身的最优滚动轨迹修复其打分逻辑即可实现效果提升，适配端侧小模型的优化需求'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有智能体在策略蒸馏（OPD）依赖教师的逐token打分训练学生，过往将效果差归因于学生错误累积偏离教师可信区间，但实验发现即使学生偏离的状态，教师接管后仍能完成任务。核心问题是教师逐token打分存在短视缺陷：仅看当前上下文不感知后续全轨迹，会放过无意义的延迟操作（如反复查询、冗余思考），而普通OPD没有结局侧惩罚，导致学生训练后极易耗尽交互轮次失败，现有方法均未修复教师本身的打分问题。
### 方法关键点
- 提出R2S框架，蒸馏前先无奖励修复教师打分：先用未训练的学生跑全量交互轨迹，挖掘学生与教师打分分歧最高的状态节点
- 从分歧节点开始让教师多次接管生成完整滚动轨迹，通过无奖励规则（多轨迹共识、LLM judge）筛选出合格的完成轨迹
- 微调教师模型，使其在看不到后续接管轨迹的情况下，对分歧节点之后的所有学生token给出与有接管上下文时一致的打分，修复后的教师冻结后用于标准OPD训练，全程不需要任务奖励
### 关键结果
在ALFWorld、WebShop、ScienceWorld3个交互环境，2个教师（9B dense、30B MoE）、4个学生的12个测试组合中，R2S全部超过3个现有SOTA OPD方法，平均比每个组合的最优基线高12.8个成功点；其中9B教师带学生平均提升17.0点，30B MoE教师带学生平均提升8.5点；自蒸馏场景下（教师学生同模型）效果也远超基线，甚至超过更大的9B教师单独执行的效果。

**最值得记住的一句话**：逐token打分的短视问题比学生偏离教师可信区间对OPD效果的影响更大，不需要任务奖励，仅用教师自身的滚动轨迹修复打分逻辑就能实现大幅效果提升。
