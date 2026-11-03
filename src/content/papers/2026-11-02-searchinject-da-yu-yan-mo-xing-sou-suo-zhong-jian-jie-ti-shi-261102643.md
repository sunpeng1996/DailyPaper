---
title: 'SearchInject: Retrieval Exposure Control for Indirect Prompt Injection in
  Language-Model Search'
title_zh: SearchInject：大语言模型搜索中间接提示注入的检索曝光控制机制
authors:
- Kainan Zhou
- Gangzhen Qian
- Janet Sung
- Zhi Jing
- Rong Bao
- Qianru Lao
affiliations:
- Google LLC
- Harvard University
arxiv_id: '2611.02643'
url: https://arxiv.org/abs/2611.02643
pdf_url: https://arxiv.org/pdf/2611.02643
published: '2026-11-02'
collected: '2026-11-03'
category: RAG
direction: RAG 检索阶段间接提示注入防御
tags:
- Indirect Prompt Injection
- Retrieval Augmented Generation
- Search Security
- Risk Scoring
- Prompt Defense
one_liner: 通过多特征联合打分在检索环节拦截注入页面，83%+恶意曝光降低，正常NDCG损失<0.002
practical_value: '- 搭建电商RAG导购/搜索问答系统时，可在召回后、送入LLM上下文前加风险过滤层：融合检索相关性、内容滥用特征、指令概率三个维度打分，按可接受的正常内容误杀率（如0.5%）设置阈值，能大幅降低恶意注入内容曝光，对正常NDCG影响极小

  - 风险打分可补充2个交叉特征：相关性*滥用特征、相关性*指令概率，让高相关页面的风险判断更严格，平衡防御效果和用户体验

  - 恶意页面隔离后不要留空位，用后续排名的正常内容补位到固定上下文长度，避免用户感知到检索结果数量变化'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
搜索增强LLM依赖第三方检索内容生成回答，攻击者可在网页嵌入恶意prompt，只要页面被检索进入LLM上下文就能触发间接提示注入攻击；现有防御多聚焦于上下文注入后的检测，未在检索准入环节拦截，且容易大幅损伤正常检索效果，需要低代价的前置拦截方案。

### 方法关键点
- 干预位置：召回top100候选后、组装LLM上下文前打分，高于阈值的页面直接隔离，剩余页面保留原排名补位到top10送入上下文
- 风险特征：融合5维特征：归一化检索相关性r、搜索滥用特征a（标题覆盖、词密度、重复度、源重叠、标记指标）、指令概率i（n-gram特征识别指令类文本）、a与r交叉项、i与r交叉项，用类别平衡逻辑回归输出风险得分
- 阈值校准：在校验集上约束正常内容误隔离率≤0.5%，选择最优阈值固定后直接用于测试集，无需二次调优

### 关键实验
基于SciFact科学文献数据集，300个held-out测试查询，覆盖标题堆砌、门页、近重复、隐藏元数据4种常见恶意页面构造类型，对比BM25、混合检索、LSA三种召回器：恶意页面top10曝光率相对降低83.2%~83.7%，BM25下从0.9408降至0.1583，混合检索下从0.9158降至0.1508；正常检索NDCG@10最大下降仅0.0018，测试集正常内容误隔离率0.59%~0.65%，接近预设的0.5%约束。

最值得记住的结论：在检索环节做前置风险过滤，能以可忽略的正常检索损失为代价，大幅降低间接提示注入攻击的曝光概率，是RAG安全架构中性价比极高的一环。
