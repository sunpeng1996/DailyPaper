---
title: 'MemPilot: Orchestrating On-Demand Multimodal Memory Curation for LLM Agents'
title_zh: MemPilot：面向LLM Agent的按需多模态记忆编排框架
authors:
- Haozhen Zhang
- Haodong Yue
- Quanyu Long
- Jianzhu Bao
- Qingyuan Liu
- Tao Feng
- Bohan Liu
- Weida Liang
- Wenya Wang
affiliations:
- Nanyang Technological University
- Tsinghua University
- University of Illinois Urbana-Champaign
arxiv_id: '2610.06830'
url: https://arxiv.org/abs/2610.06830
pdf_url: https://arxiv.org/pdf/2610.06830
published: '2026-10-05'
collected: '2026-10-06'
category: Agent
direction: Agent 多模态记忆编排优化
tags:
- LLM_Agent
- Memory_Orchestration
- Multi_Modal
- Reinforcement_Learning
- Resource_Scheduling
one_liner: 基于RL的多步编排策略，实现LLM Agent多模态记忆的性能、成本、延迟可控调度
practical_value: '- 记忆架构可复用双视图设计：预构建的查询无关记忆库（如用户历史行为预编码向量库）+ 原始多模态交互历史（如用户浏览的商品图文、会话记录），兼顾常规检索效率和长尾query的信息完整性，适合电商个性化推荐、智能客服Agent场景

  - 多目标RL优化思路可迁移到推荐算力调度场景：把回答质量、成本、延迟三个目标的优势分别归一化再加权聚合，避免单目标优化偏差，可用于大模型生成推荐文案、搜索query改写时的算力动态分配，如高价值用户请求路由到强模型，低价值请求用小模型

  - 前缀边际效用赋值方法可用于长序列推荐的credit分配：对多步决策的每一步单独计算其对最终效果的边际贡献，解决长会话推荐、多轮导购Agent的多步决策reward分配模糊问题，提升RL训练稳定性

  - 异构模型路由机制可直接落地：根据请求难度、资源约束动态选择不同规格的LLM/VLM处理记忆片段，可降低电商多模态内容理解、商品属性抽取的整体算力成本，平衡模式下可在效果损失<5%的情况下成本下降60%以上'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有LLM Agent的记忆系统大多采用查询无关的预构建模式，要么预处理阶段浪费算力、丢失关键细节，要么运行时适配逻辑固定，无法灵活平衡回答质量、算力成本、响应延迟三个核心冲突目标；尤其多模态场景下视觉处理成本高，缺乏动态调度能力，无法满足工业级Agent的落地需求。

### 方法关键点
- 双视图记忆存储：同时维护查询无关的预构建记忆库M（兼容现有所有Agent记忆系统）和原始多模态交互历史H，兼顾检索效率和信息完整性
- 多步编排策略：每步决策选择从M检索或调用异构LLM/VLM对H做查询专属编排，可细粒度控制检索证据量、编排指令、模型选择、是否调用视觉能力
- 多目标RL优化：采用目标级优势解耦，分别归一化质量、成本、延迟的优势后加权聚合，适配不同业务偏好；引入前缀边际效用估计，给多步决策的每一步分配精准credit，提升训练稳定性

### 关键实验
在5个多模态Agent记忆基准数据集（含2个OOD数据集）上对比12种基线方法：性能优先模式的LLM judge得分比最优基线高12~18个百分点；平衡模式在效果接近最优基线的前提下，推理成本降低62%，延迟降低57%；成本优先模式成本仅为性能优先模式的19%，可覆盖低优先级请求场景；性能-成本、性能-延迟的帕累托前沿完全覆盖所有基线方法，调度灵活性远超现有方案。

### 最值得记住的一句话
Agent记忆系统不应该只追求效果最优，而要根据业务偏好动态分配算力，在性能、成本、延迟三者间找到可控的平衡，才具备工业落地价值。
