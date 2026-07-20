---
title: When Do Multi-Agent Systems Help? An Information Bottleneck Perspective
title_zh: 从信息瓶颈视角解析多智能体系统的适用边界
authors:
- Wendi Yu
- Lianhao Zhou
- Xiangjue Dong
- Sai Sudarshan Barath
- Declan Staunton
- Byung-Jun Yoon
- Xiaoning Qian
- James Caverlee
- Shuiwang Ji
affiliations:
- Texas A&M University
- Brookhaven National Laboratory
arxiv_id: '2607.16133'
url: https://arxiv.org/abs/2607.16133
pdf_url: https://arxiv.org/pdf/2607.16133
published: '2026-07-17'
collected: '2026-07-20'
category: Agent
direction: 多智能体系统 · 适用边界分析
tags:
- Multi-Agent
- Information Bottleneck
- Single-Agent
- LLM Agent
- Communication Efficiency
one_liner: 基于信息瓶颈理论揭示多智能体相对单智能体的优劣势边界与适用条件
practical_value: '- 业务架构选型时先评估任务的中继复杂度δ：子任务独立、仅需传递少量关键信息的场景（如商品分域召回、多维度合规审核、用户意图分流）优先用MAS；需要全局上下文联动的场景（如全链路用户旅程规划、跨场景个性化推荐）尤其是用强LLM时，优先考虑单Agent避免信息损失

  - 设计MAS通信机制时，优先保障下游任务必要的核心信息：比如电商导购Agent中继仅保留用户预算、品类、核心偏好等关键信息，压缩冗余闲聊内容；弱基座模型可加大压缩力度，强基座模型尽量保留完整上下文

  - 用小模型部署Agent时优先选择MAS架构：实验显示7B规模模型在低δ任务上MAS相对单Agent最高可提升19.4%，可在不升级模型的前提下大幅提升任务效果'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前LLM驱动的多智能体系统（MAS）性能波动极大，在不同任务、不同基座模型下相对单智能体（SAS）的优劣势没有统一规律，过往研究多为经验性结论，缺乏底层机制解释，无法指导业务场景下的架构选型。

### 方法关键点
- 核心观察：SAS使用全局共享上下文累积所有推理痕迹，MAS使用隔离的本地上下文，通过有限带宽的中继消息连接；中继带宽无限时MAS可完全模拟SAS，因此MAS的优劣势完全来自中继的压缩效应
- 将中继建模为信息瓶颈，推导MAS增益公式：增益=上下文压缩减少的冗余收益 - 模型能力加权的中继信息损失；其中有效参数β随基座模型能力增大而升高，模型越强对信息损失越敏感，压缩收益越低
- 设计三类对照实验：纯SAS、带任务拆分但共享上下文的SAS-contextflow、带压缩中继的MAS，隔离任务拆分和中继压缩的影响

### 关键实验
覆盖5类基准任务、3档基座模型（Qwen2.5-7B、GPT-4o-mini、Qwen3.5-27B）共18组对照：低中继复杂度（δ≈0，如信息检索、简单物体操作）任务下，MAS相对SAS-contextflow的增益分别为19.4%、15.7%、2.3%，增益随模型能力提升持续下降；高中继复杂度（δ≫0，如需要全局一致性的办公操作、旅行硬约束校验）任务下，MAS增益为负，27B模型在TravelPlanner硬约束任务上效果甚至比SAS低23.3%。

**最值得记住的结论**：多智能体设计本质是信息瓶颈优化问题，只有当上下文压缩的收益大于中继信息损失时，MAS才会优于单智能体。
