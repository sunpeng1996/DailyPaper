---
title: 'What, When, and How: Audio Description as Constrained Global Optimization'
title_zh: 面向视障群体的电影音频旁白全局约束优化生成方法
authors:
- Igor Sterner
- Mirella Lapata
- Alex Lascarides
- Frank Keller
affiliations:
- University of Edinburgh
- School of Informatics, University of Edinburgh
arxiv_id: '2609.30121'
url: https://arxiv.org/abs/2609.30121
pdf_url: https://arxiv.org/pdf/2609.30121
published: '2026-09-24'
collected: '2026-09-25'
category: Multimodal
direction: 多模态生成 · 全局约束优化
tags:
- Audio Description
- Constrained Optimization
- LLM
- Mixed Integer Linear Programming
- Multimodal Generation
one_liner: 将电影音频旁白生成建模为全局约束优化问题，结合LLM与混合整数线性规划实现内容与时序联合决策
practical_value: '- 多模态内容生成场景可复用「LLM做内容/显著性打分 + 运筹优化做全局约束调度」的混合架构，解决内容选择与时序冲突的联合决策问题

  - 电商直播/短视频旁白/无障碍内容生成场景，可直接借鉴内容显著性评估、时长压缩生成、时序间隙匹配的全链路设计

  - 涉及多约束的序列生成/任务调度类任务，可参考将问题拆解为LLM候选生成+整数规划全局选优的思路，约束满足度远高于端到端LLM生成'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有自动音频描述（AD）系统仅将任务视为局部视频转文本问题，默认描述内容、投放时隙已提前确定，未耦合决策叙事显著性、时序不干扰对话、内容时长匹配三大真实落地要求，效果达不到可用标准。
### 方法关键点
将AD生成形式化为三类决策的约束全局优化问题，采用混合架构：1）用LLM完成视觉元素提取对齐、叙事显著性打分、符合时隙长度的压缩文本生成；2）用混合整数线性规划跨场景全局选择描述内容、调度投放时序，严格满足不遮挡对话的时间约束。
### 关键结果
在电影AD基准REFRAMED上，叙事QA、时序对齐指标达SOTA，较prompt驱动LLM的内容与时序决策效果更优；消融实验显示显式时序约束带来72%的时序放置准确率提升，显著性评估模块保留了89%的叙事有效内容，指标提升集中在时序与叙事维度而非n-gram重叠度，当前效果仍与专业人工有明显差距。
