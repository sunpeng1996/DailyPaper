---
title: 'DraMaze: A Multi-Agent Pipeline with Future-Aware Memory for Diverse Microdrama
  Script Generation'
title_zh: DraMaze：融合未来感知记忆的多Agent微短剧脚本生成流水线
authors:
- Siyang He
- Qiqi Wang
- Fan Liu
- Yuncheng Huang
- Pengfei Xu
- Xi Chen
- Ziwei He
- Xipeng Qiu
affiliations:
- Fudan University
- Shanghai Innovation Institute
- Tencent
arxiv_id: '2610.32002'
url: https://arxiv.org/abs/2610.32002
pdf_url: https://arxiv.org/pdf/2610.32002
published: '2026-10-21'
collected: '2026-10-26'
category: MultiAgent
direction: 多智体长文本生成 · 记忆机制优化
tags:
- MultiAgent
- Long-Form Generation
- Future-Aware Memory
- Script Generation
- Evolutionary Search
one_liner: 通过未来感知记忆与进化树搜索，生成高逻辑一致性高多样性的长序列微短剧脚本
practical_value: '- 未来感知记忆的倒推索引设计可直接迁移到电商用户生命周期运营Agent场景，从最终转化目标倒推关联历史行为检索，替代传统语义匹配RAG，减少无效召回、提升运营策略连贯性

  - 进化树搜索+归一化trope库去重的机制，可用于电商商品详情页文案、信息流广告脚本、系列种草内容的批量生成，降低内容同质化、提升用户点击与转化效率

  - 多Agent分层规划+动态状态追踪的架构，可复用在直播话术生成、系列短剧广告制作等长序列内容生成场景，保障前后内容逻辑、人物/品牌设定一致'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
微短剧行业爆发导致高质量脚本需求激增，现有LLM长序列生成存在两个核心痛点：一是随着生成推进，叙事机制熵持续下降，剧情套路重复严重削弱用户吸引力；二是传统语义检索的记忆管理会强化套路复用，同时遗漏后续剧情必需的历史铺垫信息，导致长剧情逻辑断裂。

### 方法关键点
- 构建归一化trope记忆库存储去表面信息的因果模式，通过进化树搜索扩展剧情分支，搭配0.25概率的突变机制，结合novelty评分筛选分支，避免套路重复
- 构造Backward Narrative Dependency Tree (BNDT)，从最终剧情目标倒推拆解子目标，将历史记忆绑定到对应目标节点，实现基于未来需求的记忆检索，替代传统语义匹配
- 搭配动态世界状态记忆，实时追踪人物、关系、资产状态，保障全序列叙事一致性
- 开源双语微短剧生成评测基准MiDramaBench，覆盖20/40/60集三个长度，配套因果模式重复度、叙事多样性等量化指标

### 关键结果
基于Qwen3.6-27B、DeepSeek-V4-Pro、GLM5.3-Flash三个骨干LLM验证，对比DOME、StoryWriter两个SOTA基线，60集（最高6万字）脚本场景下，因果模式重复率降低32.1%，逻辑评分达82.5，领先最优基线8.5分，跨模型均保持一致提升。

**最值得记住的一句话**：长序列生成中，语义相似度不等于叙事价值，基于未来目标的因果依赖检索比表面语义匹配更能同时保障内容一致性与多样性。
