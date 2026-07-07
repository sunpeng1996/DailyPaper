---
title: 'The New Shape of Search: How Conversational AI Recomposes Information Seeking'
title_zh: 搜索的新形态：对话式AI如何重构用户信息获取行为
authors:
- Michael Iannelli
- Alan Ai
affiliations:
- Scrunch AI
arxiv_id: '2607.04282'
url: https://arxiv.org/abs/2607.04282
pdf_url: https://arxiv.org/pdf/2607.04282
published: '2026-07-05'
collected: '2026-07-07'
category: LLM
direction: 对话式AI · 搜索行为重构
tags:
- Conversational AI
- Information Seeking
- User Behavior Analysis
- Search Recomposition
- Cross-Surface Tracking
one_liner: 基于跨设备用户行为面板，揭示对话式AI分化而非替代搜索，重构信息获取全链路结构
practical_value: '- 可基于用户prompt长度分层设计交互：短query（3词内）直接给出精准结果/答案闭环，长query（20词以上）配套引导跳转搜索/相关商品入口，匹配用户行为分化特征

  - 电商/内容类Agent可新增workbench场景支持：针对文案生成、尺码换算、穿搭方案输出等非信息检索类需求，优化端内闭环能力，减少用户跳转流失

  - 验证功能无需全量强制透出：仅约1%用户会主动验证AI答案，仅需在高风险决策场景（如医疗、高客单价商品推荐）加验证入口，降低普通场景交互冗余

  - 核心搜索入口无需弱化：74.8%的跨场景行为仍包含搜索动作，可保留搜索作为会话中途的核心跳转选项，提升全链路流转效率'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
过往行业对对话式AI的认知普遍是替代传统搜索、导致公域流量下滑，但这类结论多基于宏观流量统计，存在用户活动burst带来的混淆偏差，缺乏单用户全链路行为的结构化分析，无法准确判断对话AI对信息获取链路的实际影响。
### 方法关键点
- 采用opt-in跨设备用户面板，关联2026年5月美英地区用户在ChatGPT、Claude等4款独立对话助手的会话内容，以及同期搜索、浏览全链路行为数据
- 以30分钟无操作作为会话分割阈值，重构包含对话、搜索、浏览动作的完整信息获取episode，按对话后后续动作分为collapsed（无后续动作）、scaffolded（≥3步后续动作）、redirected（1-2步内容跳转）、handoff（1-2步搜索跳转）四类
- 用经过三类模型基准标注的LLM对初始prompt做任务分类，排除prompt长度对分类的干扰，分析episode形态的核心影响因素
### 关键结果
- 59.5%的对话AI会话无后续动作直接终止，31.6%会触发≥3步的长链路行为；短prompt（1-3词）的终止率达72%，长prompt（≥20词）终止率仅48%
- 41%的对话AI会话属于非信息检索类的workbench场景（文案生成、编码等），这类场景终止率最高达63%
- 对话AI并未替代搜索，74.8%的会话内跳转仍涉及搜索动作，用户浏览页面后回到搜索的概率是回到对话助手的2.3倍，仅约1%的会话会触发显式验证行为
### 核心结论
对话式AI是在传统搜索链路之上新增了一层交互入口，而非替代搜索，它将信息获取行为分化为短需求直接闭环、长需求锚定更长链路两类形态。
