---
title: 'Agentic Share-of-Search: A Multi-Agent AI System for Competitive Decision-Making
  in LLM-Mediated E-Commerce'
title_zh: 智能搜索份额：面向LLM导购电商的多Agent竞争决策系统
authors:
- Spandan Ghose Chowdhury
affiliations:
- Georgia Institute of Technology
arxiv_id: '2609.11190'
url: https://arxiv.org/abs/2609.11190
pdf_url: https://arxiv.org/pdf/2609.11190
published: '2026-09-10'
collected: '2026-09-11'
category: MultiAgent
direction: 多智体协作 · 电商商家决策支持
tags:
- MultiAgent
- E-commerce
- ReAct
- RootCauseAnalysis
- GenerativeRecommendation
one_liner: 提出ASoS指标与多Agent系统，支持LLM导购场景下卖家竞争力诊断与干预推荐
practical_value: '- 可复用ASoS指标计算逻辑，统计自家商品在GPT、Gemini等大模型导购场景下的搜索份额，替代传统SEO指标适配生成式搜索新场景

  - ReAct诊断Agent的设计可直接复用，结合商品价格、评论、标题关键词等属性关联排名表现，自动输出可落地的商品优化优先级，降低人工分析成本

  - 实体解析层的插件化设计可参考：默认用embedding匹配降低成本，需要SKU级精度时切换QLoRA微调的小模型，兼顾成本与效果

  - 多平台统一客户端架构可复用，封装不同大模型API的差异，支持批量探测大模型推荐结果，快速迭代优化运营策略'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
AI导购助手已成为用户商品发现核心入口，传统SEO工具无法感知大模型推荐结果，现有品牌曝光工具仅覆盖品牌级、无法定位SKU级优化点，卖家缺乏适配生成式推荐场景的竞争决策工具。

### 方法关键点
- 定义Agentic Share-of-Search (ASoS) 指标：按大模型响应中商品的出现排名做log折扣加权，统计零售商在可解析推荐结果中的曝光占比，支持多零售商归因、去重等规则，鲁棒性优于纯商品库匹配
- 多Agent架构：由协调器调度查询Agent批量向多个大平台发送搜索请求，抽取推荐结果后通过可插拔的实体解析层（默认embedding匹配，可选QLoRA微调小模型）映射到标准SKU库
- ReAct诊断Agent：关联SKU的价格、评论、标题关键词、结构化数据完善度等可运营属性，通过相关性计算定位曝光缺口根因，输出按业务影响优先级排序的可落地干预建议

### 关键实验
在跑鞋品类（23个SKU、7个零售商、34个查询、3个大模型平台）开展100次信号消融测试，对比随机选择、全局Top信号两个baseline：整体Precision@1达39%，是随机baseline的5.5倍；当消融信号为Top3相关性信号时，Precision@1升至63.9%；对相关性最高的商品问答属性，识别准确率100%。实体解析层embedding方案分辨率99.7%、延迟8.2s，QLoRA方案对抗测试集准确率93.7%、比embedding高2.6pp。Gemini live pilot抽取成功率70%，可正常输出零售商曝光排名。

### 核心结论
ASoS指标的核心是衡量大模型对零售商的认知曝光，而非传统的商品库匹配结果，直接对齐卖家可实际影响的优化表面
