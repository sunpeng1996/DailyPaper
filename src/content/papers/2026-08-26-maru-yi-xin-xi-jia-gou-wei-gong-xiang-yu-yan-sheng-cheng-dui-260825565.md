---
title: 'Maru: Information Architecture as a Shared Language for Generating Aligned
  and Persistent User Interfaces'
title_zh: Maru：以信息架构为共享语言生成对齐且持久的用户界面
authors:
- Eunhye Kim
- DaEun Choi
- Bryan Min
- Hyunjung Yi
- Yue Jiang
- Juho Kim
affiliations:
- KAIST
- University of California San Diego
- Korea University
- University of Utah
- SkillBench
arxiv_id: '2608.25565'
url: https://arxiv.org/abs/2608.25565
pdf_url: https://arxiv.org/pdf/2608.25565
published: '2026-08-26'
collected: '2026-08-27'
category: Agent
direction: 会话Agent UI生成 · 偏好持久对齐
tags:
- GenUI
- Information Architecture
- Preference Persistence
- Conversational Agent
- Alignment
one_liner: 将四类信息架构元素作为人机共享语言，实现生成式UI跨会话的用户偏好持久对齐
practical_value: '- 可将四元信息架构（分区/层级/排序/词汇）作为用户交互偏好的结构化存储范式，替代非结构化RAG存储，降低推荐/UI生成的对齐成本

  - 电商导购Agent可复用该思路，将用户交互行为（如排序、筛选、自定义分类）自动转化为持久化IA规则，跨会话无需用户重复提需求

  - 生成式商品列表/活动页场景可引入IA持久化逻辑，既保留个性化结构一致性，又支持动态内容迭代，降低用户认知负担'
score: 7
source: arxiv-cs.HC
depth: abstract
---

### 动机
当前生成式UI（GenUI）每次生成的结构决策完全由模型自行决定，忽略用户在交互过程中建立的信息组织逻辑（如分类规则、排序优先级、自定义术语），缺乏人机共享的持久化表示结构，导致跨生成环节的对齐度随会话推进持续下降，用户需要反复重复需求。
### 方法关键点
引入信息架构（IA）作为人机共享交互语言，定义分区、层级、排序、词汇4类核心IA元素，每类元素可直接映射为具体UI生成决策；开发Maru会话系统，自动将用户prompt和显式交互行为捕捉为IA偏好规则，作为持久化状态跨生成环节供人机共同调用。
### 关键结果
用户研究显示，引入IA持久化机制后，生成UI的用户对齐度随会话推进保持稳定；无IA持久化的对照组对齐度随交互次数增加显著下降，该机制可适配不同用户和场景的个性化需求。
