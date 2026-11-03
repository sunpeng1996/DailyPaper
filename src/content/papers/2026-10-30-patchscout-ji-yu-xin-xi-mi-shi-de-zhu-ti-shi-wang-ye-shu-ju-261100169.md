---
title: 'PatchScout: Thematic Web Data Collection via Information Foraging'
title_zh: PatchScout：基于信息觅食的主题式网页数据采集多Agent框架
authors:
- Michael West
- Eduard Dragut
affiliations:
- Temple University
arxiv_id: '2611.00169'
url: https://arxiv.org/abs/2611.00169
pdf_url: https://arxiv.org/pdf/2611.00169
published: '2026-10-30'
collected: '2026-11-03'
category: MultiAgent
direction: 多智体协作 · 主题式网页数据采集
tags:
- Web Agent
- Multi-Agent System
- Information Foraging
- Data Crawling
- Long-Horizon Reasoning
one_liner: 提出多Agent主题网页采集框架，通过信息觅食策略平衡局部开采与区域切换提升采集效率与覆盖
practical_value: '- 电商商品/商家信息、竞品舆情、用户评论等跨站采集场景，可直接复用三角色Agent分工：Scout生成搜索query扩充召回范围、Forager做站内链接优先级排序、Critic判断内容相关性，比传统固定规则爬虫的覆盖范围提升明显

  - 长周期探索类Agent（如市场调研Agent、新品发现Agent）可直接复用patch切换策略，用已开采区域的生产率EMA作为基线，低于基线就切换新query区域，避免在无效页面浪费调用预算

  - 需平衡采集深度和广度的场景可参考策略选型：追求高相关内容产出率选Realized-EMA策略，追求高跨域覆盖选Scent-EMA策略，目标极稀疏的场景用固定阈值切换效果最优'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有主题式网页数据采集需求（如跨站点收集特定领域实体、合规舆情、行业文档）无法被现有方案满足：传统聚焦爬虫依赖种子链接的连通性，对结构分散的异构站点覆盖差；现有搜索增强推理Agent为短任务导向，收集到足够回答就终止，无法支撑长周期全量采集，难以同时兼顾采集深度（单站点内相关内容提取率）和广度（跨不同来源的覆盖量）。
### 方法关键点
- 将采集任务建模为预算约束下的长周期信息觅食问题，核心决策逻辑是判断何时停止当前语义区块（由搜索query返回结果+可遍历邻接页面构成的patch）的开采、切换到新区域
- 采用三角色多Agent架构：Scout根据历史采集效果生成差异化新query发现新patch；Forager基于信息 scent 对patch内链接排序做局部开采；Critic判断页面相关性，计算当前patch的生产率
- 提供5种可适配的patch切换策略：结合当前patch的已实现生产率/未来预期信息 scent 两个触发信号，搭配固定阈值/历史均值/EMA三个动态基线，适配不同稀疏度的采集场景
### 关键结果
在4个真实web主题数据集（美国四年制大学、财富500强招聘页、美国认证法学院、自闭症支持项目）上，对比传统聚焦爬虫ACHE、DeepResearcher等搜索增强Agent，1万页预算下：最优变体比传统爬虫覆盖最高提升11.3倍，在分散无统一目录的场景比商用深度搜索Agent覆盖最高提升2.3倍，自闭症支持项目场景新发现102个未被权威列表收录的实体。
### 核心结论
主题式数据采集不是单纯的相关性排序问题，而是预算约束下的探索决策问题，显式建模区块切换才能同时兼顾采集的深度和广度。
