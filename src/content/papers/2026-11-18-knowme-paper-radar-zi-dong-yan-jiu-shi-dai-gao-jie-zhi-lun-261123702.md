---
title: 'KnowMe Paper Radar: Lightweight Discovery of Promising Papers in the Age of
  Autoresearch'
title_zh: KnowMe Paper Radar：自动研究时代高价值论文轻量发现工具
authors:
- Zhuo Chen
- Jian Wang
- Jinjie Gu
- Lijun Wu
affiliations:
- Ant Group
arxiv_id: '2611.23702'
url: https://arxiv.org/abs/2611.23702
pdf_url: https://arxiv.org/pdf/2611.23702
published: '2026-11-18'
collected: '2026-11-21'
category: Agent
direction: Agent 文献检索工具优化
tags:
- Paper Retrieval
- Agent Tool
- Cache Reuse
- Personalized Ranking
- Lightweight System
one_liner: 融合多维度证据的轻量高价值论文发现工具，适配人类用户与研究Agent双端
practical_value: '- 多维度排序特征设计可直接复用：个性化内容/商品推荐场景中，可融合相关性、新鲜度、供给方历史表现、领域机构权重多维特征做排序，降低单一相关性偏差

  - 轻量服务架构思路可迁移：高QPS的推荐/搜索业务中，可前置离线计算全量特征，在线阶段直接复用缓存结果，无需调用LLM即可降本提效

  - 双端适配设计可参考：内部工具开发时，可同时提供面向人类的可视化界面与面向Agent的结构化CLI接口，满足多角色使用需求'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
当前学术论文数量爆发、同主题内容过载，研究者难以快速筛选出能提供研究洞见、方法指导的高价值文献，现有工具要么依赖LLM推理成本高，要么个性化不足。
### 方法关键点
1. 多维度特征融合排序：整合主题相关性、时效性、作者研究历史、协作路径、领域机构背景多维度特征生成个性化阅读优先级，公开各得分组件及支撑来源提升可解释性。
2. 轻量运行架构：采用自动采集、版本合并、图缓存复用机制，日常使用无需调用LLM推理，同时提供浏览器界面与结构化CLI，适配人类研究者与研究Agent。
### 关键结果数字
- 基于17.46万条采集记录实验显示，重复上下文准备速度提升3倍以上
- 专家标注检索任务中，缓存摘要将NDCG@10从0.412提升至0.598
- 积累的记录可同时支撑语义检索、研究历史建模、文献驱动规划等下游任务
