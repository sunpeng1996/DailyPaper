---
title: Generative Skill Composition for LLM Agents
title_zh: 面向LLM Agent的生成式技能组合框架SkillComposer
authors:
- Xinyu Zhao
- Zhen Tan
- Vaishnav Tadiparthi
- Nakul Agarwal
- Kwonjoon Lee
- Ehsan Moradi Pari
- Hossein Nourkhiz Mahjoub
- Tianlong Chen
affiliations:
- University of North Carolina at Chapel Hill
- Arizona State University
- Honda Research Institute USA
arxiv_id: '2606.32025'
url: https://arxiv.org/abs/2606.32025
pdf_url: https://arxiv.org/pdf/2606.32025
published: '2026-06-30'
collected: '2026-07-01'
category: Agent
direction: Agent 技能调度与组合优化
tags:
- LLM Agent
- Skill Composition
- Autoregressive Decoding
- Retrieval Augmented
- Task Planning
one_liner: 轻量生成式框架联合预测Agent技能的子集、数量与执行顺序，性能超越检索与大模型基线
practical_value: '- 电商/客服Agent的技能库调度可直接复用架构：采用冻结embedding+小参数AR解码器，无需全量SFT大模型，成本仅为通用大模型微调的1%，同时具备联合预测技能顺序、数量的能力，适配多步骤复杂任务（如退货流程、订单查询+优惠券推荐组合场景）

  - 解码阶段logit融合trick可直接落地：将AR解码器的上下文logit、TF-IDF稀疏检索分数、技能相关性头分数加权融合，无需修改训练逻辑即可提升10%以上的技能匹配准确率，尤其适合电商场景（技能名/描述有明确关键词，稀疏检索效果优于dense
  embedding）

  - 技能组合训练数据构造方法可迁移：基于业务技能依赖规则（如查询物流需先获取订单ID）合成训练样本，分层过滤去重，无需大量人工标注即可快速生成万级训练对，适配业务新增技能的快速迭代'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
随着LLM Agent的技能库规模持续扩大，现有技能选择方法存在明显缺陷：纯检索仅输出无顺序的候选集，全量推理让Agent自行决策则上下文开销高、稳定性差，二者均无法同时解决「选哪些技能、选多少、按什么顺序执行」三个耦合问题，成为Agent落地复杂任务的核心瓶颈。
### 方法关键点
- 将结构化技能组合建模为任务条件下的闭集技能序列预测问题，单次自回归解码同时输出技能子集、数量与执行顺序，所有输出均来自现有技能库，保证可直接执行
- 架构采用冻结预训练文本编码器+仅3.9M参数的轻量Transformer解码器，新增两个辅助监督头：基数头预测所需技能数量，集合头预测单技能相关性，补充独立监督信号降低学习难度
- 推理阶段采用logit融合策略：将解码器上下文logit、TF-IDF稀疏检索分数、集合头相关性分数加权融合，兼顾技能依赖的上下文信息与语义匹配精度
- 训练数据基于真实人工标注的技能库构建，结合技能依赖图合成单/多技能任务对，分层过滤去重，覆盖长尾技能与依赖关系
### 关键结果
在SkillsBench编码任务上，对比无技能基线，SkillComposer为GPT-5.2-Codex提升23.1pp通过率，为Gemini-3-Pro-Preview提升18.2pp，超过Top-3检索基线，匹配黄金技能检索上限且prompt token成本更低；真实任务泛化测试上，比全量SFT的0.6B模型Set F1高19.3pp，推理延迟比API调用的大模型低两个数量级。
### 核心结论
对于闭集技能库的Agent调度场景，小参数专用结构化预测模型的效果与成本表现，均远优于通用大模型微调或纯检索方案。
