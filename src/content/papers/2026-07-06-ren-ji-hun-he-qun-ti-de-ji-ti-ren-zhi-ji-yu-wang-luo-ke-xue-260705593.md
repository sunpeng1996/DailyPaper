---
title: 'Collective Cognition in Hybrid Groups: A Network Science Synthesis'
title_zh: 人机混合群体的集体认知：基于网络科学的系统性综述
authors:
- Babak Hemmatian
- Razan Baltaji
- Lav R. Varshney
affiliations:
- Stony Brook University
- University of Illinois Urbana-Champaign
arxiv_id: '2607.05593'
url: https://arxiv.org/abs/2607.05593
pdf_url: https://arxiv.org/pdf/2607.05593
published: '2026-07-06'
collected: '2026-07-08'
category: Agent
direction: 人机混合群体 · 集体认知网络建模
tags:
- Hybrid Intelligence
- Collective Cognition
- Network Science
- Multi-Agent System
- Human-AI Teaming
one_liner: 整合网络科学与认知科学成果 提出人机混合群体集体认知的统一分析框架
practical_value: '- 搭建人机协同的推荐/运营Agent团队时，可参考拓扑设计原则：采用中等稀疏度的网络结构，AI负责信息过滤、批量处理，人类负责异常校验、高风险决策，平衡探索效率与准确率

  - 多LLM Agent协同系统设计要规避同质化问题：定期引入人类输入注入多样性，避免群体快速收敛到局部最优，适配选品、创意生成等复杂任务

  - 做AI辅助决策的业务系统时，可采用升级漏斗架构：AI处理常规case，仅将置信度低于阈值的高风险case路由给人类，降低人工成本的同时控制错误率

  - 混合Agent系统的交互规则可分层设计：AI节点之间的冗余通信可按需裁剪，而人机交互链路要保留足够的校验冗余，减少幻觉传播'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
AI Agent已广泛融入各类人类协作场景，但现有研究多聚焦个体、双人级别的人机交互规律，缺乏对群体级动态的统一理论支撑，纯人类、纯AI网络的研究结论无法直接迁移到混合场景，导致混合团队设计无章可循，容易出现过早收敛、共识偏差、信任崩塌等问题。
### 方法关键点
- 采用记忆-注意力-推理（MAR）认知框架统一刻画人类与AI节点的能力差异，明确二者能力互补而非冗余的核心特征
- 梳理5类核心集体任务（竞争/协调/合作/信息传染/集体决策）的网络结构适配规则，提炼出12种混合场景原生的特有拓扑结构（如人类AI枢纽、一人多AI编排器、升级漏斗等）
- 对比纯人、纯AI网络的参数效果，明确了18项可迁移规律、6项需修正规律和7项混合场景独有规律
### 关键结论
作为综述研究，整合了近5年100+相关实证研究结果：混合群体中AI占比的效果呈倒U型，10%-30%的低剂量AI可提升20%-40%的集体决策效率，人类占比低于30%时会出现信任崩塌、性能陡降；纯LLM Agent群体的多样性会在3-5轮迭代后下降60%以上，引入人类输入可将多样性维持周期延长3倍以上；人机交互链路是混合系统的核心性能瓶颈，其容量决定了整体集体计算的上限。

**最值得记住的一句话**：人机混合群体的表现不是两类个体能力的加权平均，而是由网络拓扑、节点角色、交互规则共同决定的涌现特性。
