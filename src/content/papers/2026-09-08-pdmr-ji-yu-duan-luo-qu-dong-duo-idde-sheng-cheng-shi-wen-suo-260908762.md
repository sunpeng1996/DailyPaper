---
title: 'PDMR: Passage-Driven Multi-ID Document Retrieval'
title_zh: PDMR：基于段落驱动多ID的生成式文档检索方法
authors:
- Smail Oussaidene
- Mohand Boughanem
affiliations:
- Institut de Recherche en Informatique de Toulouse (IRIT)
arxiv_id: '2609.08762'
url: https://arxiv.org/abs/2609.08762
pdf_url: https://arxiv.org/pdf/2609.08762
published: '2026-09-08'
collected: '2026-09-09'
category: GenRec
direction: 生成式检索 · 多Semantic ID设计
tags:
- Generative Retrieval
- Semantic ID
- Multi-Target Learning
- Passage Retrieval
- DocID Design
one_liner: 为文档拆分多个语义段落分配独立ID，提升生成式检索的多意图匹配能力
practical_value: '- 电商商品/广告落地页这类多面内容的生成式推荐场景，可借鉴多段落ID思路，给同个商品分配多个语义子ID（对应不同卖点、品类标签），提升多意图用户查询的匹配准确率

  - 生成式检索的ID设计可复用TC-ID（文档标题在前+段落标题在后）的结构，既保留全局归属信息又提供局部语义信号，降低自回归解码的前缀错误率

  - 多ID训练可复用加权多目标损失：主匹配ID分配0.6权重，其余同文档ID均分剩余权重，兼顾核心匹配精度和多语义覆盖

  - 针对内容异质性强的数据集（如电商详情页、商家主页），训练时优先使用最佳匹配段落对齐策略，避免弱相关段落引入的噪声；同构内容（如百科类参数页）可采用全段落对齐提升覆盖'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有生成式检索框架默认每个文档对应单一全局ID，强制将多语义、长文本内容压缩为单个序列，导致局部语义丢失，不同查询意图仅能竞争同一生成路径，召回鲁棒性差，尤其不适用于多面性强的文档场景。
### 方法关键点
- 段落拆分与多ID分配：用LLM两步法拆分文档为独立语义段落，去重后给每个段落分配独立ID，同文档对应多个语义入口，召回时映射回父文档
- ID结构设计：最优为Doc→Pass格式的TC-ID，即「文档标题/段落标题」，自回归解码时先锁定全局文档归属，再匹配局部段落语义，降低前缀错误率
- 训练对齐策略：合成段落专属query+原始训练query对齐，异构文档采用最佳匹配段落对齐，同构文档采用全段落对齐
- 加权多目标损失：主匹配ID分配0.6权重，其余同文档ID均分剩余权重，兼顾核心匹配精度和多路径覆盖
### 关键结果
在NQ320K基准上，R@1达67.6，较DSI-QG提升4.5pp、较多视图ID方法MINDER提升4.9pp；在MS MARCO Document基准上，R@1达37.71、MRR@10达48.66，均为同配置下最优水平。
### 核心结论
生成式检索无需局限于单全局ID设计，基于内容内部语义拆分的多ID体系，可在可控的训练成本下大幅提升多意图匹配的精度和泛化性
