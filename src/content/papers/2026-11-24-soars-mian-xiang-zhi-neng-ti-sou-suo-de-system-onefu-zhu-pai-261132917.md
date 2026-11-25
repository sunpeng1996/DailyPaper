---
title: 'SOARS: System One Assisted Reranking for Agentic Search'
title_zh: SOARS：面向智能体搜索的System One辅助重排序框架
authors:
- Amin Bigdeli
- Liye Fu
- Fattane Zarrinkalam
- Joel Stremmel
- Elizabeth Lingg
affiliations:
- University of Waterloo
- Thomson Reuters Labs
- University of Guelph
arxiv_id: '2611.32917'
url: https://arxiv.org/abs/2611.32917
pdf_url: https://arxiv.org/pdf/2611.32917
published: '2026-11-24'
collected: '2026-11-25'
category: Agent
direction: 智能体搜索 · 轻量重排序优化
tags:
- Agentic Search
- Reranking
- System One Model
- Efficiency Optimization
- Information Retrieval
one_liner: 免训练轻量重排序框架，同时提升深度搜索智能体的回答效果与运行效率
practical_value: '- 电商导购Agent、多轮搜索推荐场景可复用「全局原始Query+当前子Query」的联合重排序Query构造方法，兼顾用户长期需求与当前意图，提升召回相关性

  - 长文档/商品详情页的重排序可采用「子Query匹配最早非停用词对应截取段落+标题」的压缩表示，既降低重排序算力开销，又避免头部截断遗漏有效信息

  - 低延时要求的在线重排序场景可优先考虑System One类轻量校准模型，其效果接近大模型重排器，但速度快1-2个数量级，额外开销可被减少的后续检索/推理调用抵消

  - 智能体迭代推理链路中加入轻量中盘重排序，可显著降低大模型调用次数与整体链路延迟，在电商多轮导购、复杂问题咨询场景下ROI极高'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
深度搜索Agent依赖多轮检索推理完成复杂信息需求任务，现有重排器需在每步检索后调用，会引入极高的延迟和成本；且现有方法仅基于Agent生成的子Query排序，遗漏原始问题的全局约束，还常因仅取文档头部内容丢失有效证据，导致重排效果差、Agent冗余检索次数居高不下。

### 方法关键点
- 免训练框架，直接集成System One轻量校准模型作为每轮检索后的重排器，单次前向即可输出校准的相关性分布
- 重排Query采用「原始问题+当前子Query」拼接，同时匹配全局需求和局部检索意图
- 长文档截断不用头部内容，而是以子Query的首个非停用词在文档中出现的位置为起点截取固定长度段落，拼接标题作为文档表示，降低输入长度同时保留有效证据
- 基于相关性分布的期望得分排序，比直接取最高概率的相关性等级排序更平滑

### 关键实验
在BrowseComp-Plus（830个复杂问题+10万文档）和WebShaper两个智能体搜索基准上，对比monoT5、RankGPT、Qwen3-Reranker-4B等主流重排器，覆盖6种不同大小的LLM backbone：
- 重排阶段效果接近最强的RankGPT，延迟仅254ms，是RankGPT的1/34
- 加入SOARS后，GPT-5.4 Mini准确率从73.9%提升到84.7%，搜索调用次数从23次降到14次，端到端延迟从113s降到84s
- 5/6的LLM backbone总成本下降，Opus 4.7总成本从247美元降到119美元，降幅超50%

### 核心结论
在智能体迭代检索链路中加入轻量高效的中盘重排序，提升证据利用率带来的检索、推理次数减少，远高于重排本身的额外开销，是兼顾效果与效率的高性价比优化方向
