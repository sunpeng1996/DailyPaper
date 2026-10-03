---
title: 'O-Funnel: Lossless Structural Capture and Requirement-Driven Extraction from
  Drifting, Heterogeneous Documents'
title_zh: O-Funnel：面向漂移异构文档的无损结构捕获与需求驱动提取
authors:
- Osama Mustafa
affiliations:
- Intellusion
arxiv_id: '2609.39209'
url: https://arxiv.org/abs/2609.39209
pdf_url: https://arxiv.org/pdf/2609.39209
published: '2026-09-30'
collected: '2026-10-03'
category: Other
direction: 异构半结构化文档schema漂移适配抽取
tags:
- Information Extraction
- Semi-structured Data
- Schema Drift
- Schema Matching
- Data Integration
one_liner: 提出无训练依赖的异构文档解析框架O-Funnel，解决schema漂移下正则解析失效问题
practical_value: '- 电商异构商品数据（商家上传的Excel/CSV/JSON、爬虫获取的详情页）字段抽取场景，可直接复用O-Funnel的多证据（键名/路径/值形态/同义词等）融合匹配逻辑，替代手写正则，解决商家字段命名/格式漂移问题

  - 推荐系统多源用户行为日志归一化场景，可复用其「转统一类型树+可逆校验」架构，保证抽取结果100%可溯源，避免脏数据流入召回/排序模块

  - 小样本异构数据抽取场景可直接pip安装调用，无需预训练即可上线，效果优于传统正则匹配器，降低中小业务数据处理 pipeline 搭建成本'
score: 6
source: arxiv-cs.IR
depth: abstract
---

### 动机
半结构化异构文档的固定字段抽取长期依赖手写正则，遇到schema漂移（键名变更、值格式修改、干扰值前置）就会失效，根源是正则同时耦合了值描述与定位两个任务。

### 方法关键点
1. 解耦定位与匹配：先将XML/JSON/CSV/HTML/键值文本统一转换为5种构造器组成的类型树，引入oracle校验确保转换完全可逆、无损捕获源结构；
2. 多证据融合定位：融合键名、路径、值形态、同义词、拼写、邻域、值分布7类独立证据匹配目标字段，输出最优结果，缺失字段可给出明确原因；
3. 自学习优化：无需求匹配的残差数据会反向关联需求，自动学习新的键别名。

### 关键结果
34989条真实PubMed数据集上F1达1.00，与手写正则持平；5个字段schema重命名后，正则F1跌到0.20，O-Funnel仍保持1.00；正则失效的构造测试集上，F1从0.43提升到1.00，自优化后从0.80提升到0.94，无需训练即可媲美传统匹配器。
