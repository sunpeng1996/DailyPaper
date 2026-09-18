---
title: 'Treadstone: A Social-Media-Inspired Platform for Multi-Agent Collaborative
  Data Analysis'
title_zh: Treadstone：基于社交媒体范式的多智能体协同数据分析平台
authors:
- Hyunwook Lee
- Sungbeom Cho
- William Benjamin
- Changhee Lee
- Hyotaek Jeon
- Daeun Jeong
- Sungbok Shin
- Sungahn Ko
- Niklas Elmqvist
affiliations:
- Soongsil University
- Pohang University of Science and Technology (POSTECH)
- Sogang University
- Aarhus University
arxiv_id: '2609.19774'
url: https://arxiv.org/abs/2609.19774
pdf_url: https://arxiv.org/pdf/2609.19774
published: '2026-09-17'
collected: '2026-09-18'
category: MultiAgent
direction: 多智能体 · 人-Agent协同工作流设计
tags:
- Multi-Agent Collaboration
- Human-AI Collaboration
- Social Media Metaphor
- Data Analysis Platform
- Agent Coordination
one_liner: 提出类社交媒体共享协作Feed范式，实现人-Agent多角色协同数据分析并保留人类控制权
practical_value: '- 可复用类社交Feed的多Agent协作架构：用共享时间线+结构化标签+线程隔离解决多Agent输出混乱、上下文丢失问题，适合电商场景下运营分析、用户洞察等多Agent协同任务

  - 可直接借鉴讨论式Agent调度机制：不需要预先路由，所有Agent并行计算任务匹配度，阈值触发响应，减少人工prompt工程负担，适配推荐策略分析、广告效果归因等多角色Agent场景

  - 轻量级人类干预设计可复用：用点赞、标签引用、建议横幅等低摩擦操作替代复杂prompt输入，降低业务人员使用多Agent系统的门槛，适合运营、产品等非技术用户操作

  - 多Agent输出的语义标注+溯源方案可迁移：自动给Agent输出打Hypothesis/Evidence/Insight等标签，构建关联关系图谱，解决多Agent分析结果不可追溯、难整合的问题，适合电商大促复盘、用户行为路径分析等需要留痕的场景'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
现有多Agent协同数据分析工具依赖非结构化聊天或单线程对话，无法追踪假设演化、关联证据与结论，当Agent数量增加时，协作成本剧增，人类容易失去分析控制权，同时认知负担大幅提升，亟需高效的人-Agent协同范式。

### 方法关键点
- 提出Agent社交数据分析范式，仿社交媒体设计共享协作Feed，所有人类/Agent用户可异步发布帖子、回复、关联历史内容，支持证明/反驳已有结论
- 设计5个分工明确的专业化Agent：统计分析师、可视化专家、情报Agent、摘要Agent、主动探索Data Scout，覆盖定量计算、可视化、背景调研、总结、主动发现全流程
- 采用讨论式Agent调度：无需预先路由，所有Agent并行评估任务匹配度，高于阈值则响应，支持Agent间@互助、用户手动@指定Agent，避免路由错误
- 内置多视图辅助分析：Feed视图作为主交互入口，Activity视图按标签过滤结果，Branch视图可视化分析路径关联关系，Summary视图自动聚合全局结论，Data视图统一管理数据资产

### 关键实验
用户研究招募24名有LLM使用经验的参与者，采用组内对照，基线为单线程ChatGPT（同GPT-5.2底座），用恐怖袭击数据库、IMDB电影Top1000两个数据集做开放式探索分析。核心结果：75%参与者认为Treadstone更支持数据探索，66.7%愿意未来用它做复杂任务；在多样化探索维度得分比ChatGPT高34.8%，创造力得分高24%，人-AI协作体验得分高13.6%，可用性得分68.65仍高于行业平均水平。

### 最值得记住的一句话
多Agent协作的核心不是让机器替代人类，而是通过透明、低摩擦的协作架构让人类从操作执行者升级为全局监督者，释放认知资源做高价值判断。
