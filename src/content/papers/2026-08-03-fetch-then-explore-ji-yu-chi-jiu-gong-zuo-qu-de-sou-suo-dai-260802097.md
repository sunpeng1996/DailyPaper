---
title: 'Fetch-then-Explore: Decoupling Selection from Extraction over a Persistent
  Workspace for Search Agents'
title_zh: Fetch-then-Explore：基于持久工作区的搜索代理选爬与抽取解耦方法
authors:
- Qi Liu
- Yiqun Chen
- Zidan Chen
- Yan Gao
- Yi Wu
- Yao Hu
- Jiaxin Mao
- Fengbin Zhu
- Tat-Seng Chua
affiliations:
- Renmin University of China
- Xiaohongshu Inc.
- National University of Singapore
arxiv_id: '2608.02097'
url: https://arxiv.org/abs/2608.02097
pdf_url: https://arxiv.org/pdf/2608.02097
published: '2026-08-03'
collected: '2026-08-04'
category: Agent
direction: 搜索Agent · 文档访问工具链优化
tags:
- Search Agent
- Persistent Workspace
- Document Access
- ReAct
- Tool Design
one_liner: 为搜索Agent设计持久工作区解耦页面选择与证据抽取，降低重复开销提升长路径任务性能
practical_value: '- 电商导购/搜索Agent的商品详情页/测评页访问可复用该范式：将原访问即写入上下文的模式改为先缓存到本地工作区，按需抽取信息，避免重复爬取和上下文浪费

  - 多跳电商查询（如跨多页验证商品资质、对比参数）场景下，持久化已爬页面支持跨页查询，可减少30%以上的重复搜索请求，降低接口成本同时提升信息召回率

  - 工具链设计可复用fetch/grep/read分层逻辑：选择操作仅返回轻量元数据不占上下文，抽取按需调用，可大幅降低长对话的KV cache开销

  - 长路径Agent的非结构化文档记忆无需全存在上下文，外置到文件系统仅回填关键信息，可平衡记忆容量和推理效率'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有搜索Agent的两类文档访问模式均存在缺陷：visit-and-read模式在爬取时就将页面片段/摘要固定写入上下文，尚未明确信息需求就完成抽取，易丢失关键内容；有状态浏览模式一次仅保留单页面，切换后立即释放，回溯需重新爬取，长路径多跳任务下开销高、信息召回率低。

### 方法关键点
- 完全解耦页面选择与证据抽取：fetch工具仅将网页全量明文存储到单问题专属文件系统工作区，仅返回路径、大小等轻量元数据，不占用上下文窗口
- 配套grep/read/list_fetched三类抽取工具：支持跨所有缓存页的正则匹配、指定行范围读取、缓存列表查询，抽取可延迟到Agent明确信息需求后执行，支持重复查询
- 工作区内容全程不被驱逐，所有已爬页面全程可访问，支持任意次数回溯

### 关键实验
在BrowseComp（多跳深度搜索）、WideSearch（宽范围表格填充）两个公开基准上，对比snippet-only、两类visit-and-read、有状态浏览基线，覆盖3个不同能力级别的backbone：
- 全backbone下BrowseComp准确率均为最高，较次优基线高2~4.5pp，最高达70.5%
- WideSearch Row-F1追平或超过最优基线，最高达51.4%
- 页面回访率是基线的3~12倍，单问题搜索请求量较visit-and-read低10%以上

### 核心结论
Agent的工作记忆不必全部放在上下文窗口，非结构化外部资源可外置到持久存储，仅回填必要抽取结果到上下文，可同时降低开销、提升性能。
