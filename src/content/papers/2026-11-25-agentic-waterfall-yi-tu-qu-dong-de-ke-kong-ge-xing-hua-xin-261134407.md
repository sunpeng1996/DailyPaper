---
title: 'Agentic Waterfall: An Intent-Driven Information Discovery Framework for Reclaiming
  User Control in the Attention Economy'
title_zh: Agentic Waterfall：意图驱动的可控个性化信息发现框架
authors:
- Yige Luo
- Shining Zhang
- Jikun Liu
- Hongjiao Qiang
- Ran Guan
affiliations:
- 2012 Laboratories, Huawei
arxiv_id: '2611.34407'
url: https://arxiv.org/abs/2611.34407
pdf_url: https://arxiv.org/pdf/2611.34407
published: '2026-11-25'
collected: '2026-11-26'
category: Agent
direction: Agent 可控个性化信息推荐框架
tags:
- LLM-Agent
- Recommendation-System
- User-Intent-Tracking
- Interactive-Recommendation
- User-Control
one_liner: 以LLM控制器协调检索、排序、状态更新的可控Agent推荐框架，较基线最高提升16.1%
practical_value: '- 可直接复用LLM控制器的三动作设计（Acquire/Recommend/UpdateState），适配电商/内容feed场景下用户主动变更需求（如下单后要教程、搜索后换品类）的动态推荐诉求

  - 共享历史回放的评估协议可落地，解决动态需求场景下传统点击/转化指标无法衡量推荐匹配度的问题，尤其适合直播电商、个性化内容feed的离线评测

  - 持久化用户记忆的设计可迁移：基于显式请求+隐式浏览行为更新用户事实、偏好、活跃目标的记忆模块，可解决相似行为下的用户意图歧义问题

  - 数据集的行为歧义、交互修订子集构造方法可参考，用来打磨自家推荐系统应对意图漂移、主动需求变更的能力'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前注意力经济下的推荐feed目标由平台定义，常与用户实时变化的需求脱节：传统序列推荐仅基于历史行为预测，既无法响应自由文本形式的显式需求，也难以跟踪用户意图的动态漂移（如用户买完相机后需求从选品切换为拍摄技巧学习）。
### 方法关键点
- 核心为LLM控制器，整合当前请求、浏览历史、持久化用户记忆、内容/工具描述，自主决策三类动作：Acquire（检索补充候选池）、Recommend（排序生成feed）、UpdateState（更新用户的事实、偏好、活跃目标记忆）
- 构造Agentic Waterfall Dataset，结合真实内容元数据与模拟交互轨迹，覆盖「行为歧义（相似初始行为对应不同后续意图）」「交互修订（用户显式修改需求）」两类核心难例场景
- 提出共享历史回放评估协议，为所有被测系统提供相同交互上下文，采用LLM盲判+相关性打分机制，量化推荐对当前用户目标的匹配度
### 关键结果
在5个公开基准数据集（KuaiRand、KuaiRec、MIND等）上与现有SOTA表现相当；在自有数据集上，整体DCG@5达7.86，较ClawRec高4.4%、较BM25+BGE高22.4%；盲选投票占总票数30.9%，较最强基线ClawRec提升16.1%；在用户显式修订需求的场景下，盲选投票较ClawRec高21.1%。
> 最值得记住：把控制权还给用户的推荐系统核心，是用统一LLM控制器串联记忆更新、检索、排序能力，动态响应用户显隐式意图变化，而非仅基于历史做静态预测。
