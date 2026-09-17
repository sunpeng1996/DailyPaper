---
title: Understanding AI Provider Recommendations in Local Service Markets
title_zh: 本地服务市场AI服务商推荐的可信度审计研究
authors:
- Hazem Ibrahim
- Yasir Zaki
affiliations:
- New York University Abu Dhabi
arxiv_id: '2609.18341'
url: https://arxiv.org/abs/2609.18341
pdf_url: https://arxiv.org/pdf/2609.18341
published: '2026-09-16'
collected: '2026-09-17'
category: Eval
direction: LLM服务推荐 · 可信度评估
tags:
- LLM
- recommendation audit
- trustworthiness
- RAG
- local service recommendation
one_liner: 跨4类本地服务域实测验证，LLM服务商推荐可信度核心取决于检索配置而非模型本身
practical_value: '- 做本地生活、服务类Agent推荐业务时必须强制挂载检索模块，无检索的LLM原生推荐真实率不足15%，完全不可用

  - 检索模块可大幅降低低质/违规实体的推荐概率，本实验中接入检索后带违规记录的理财顾问推荐率从高于基线3.6倍降至低于基线

  - 服务类推荐的排序权重天然向曝光量（评论数）倾斜，需手动补入质量分（如评分）校准，避免劣币驱逐良币'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
用户依赖AI助手获取本地服务推荐，但现有LLM推荐的真实度、合规性缺乏量化验证，模型能力与检索模块对推荐质量的影响权重不明确。
### 方法关键点
覆盖美国Top100都市区4类有官方注册库的服务域（医生、理财顾问、餐厅等），对比三组实验：开源大模型、无检索闭源模型、带检索闭源模型，所有推荐结果与官方注册数据交叉校验。
### 关键结果
无检索时开源模型推荐医生匹配率仅4%，闭源模型仅11%，匹配多为名字巧合；带检索后匹配率提升至64%~71%。无检索时推荐理财顾问违规率是基线3.6倍，带检索后低于基线。餐厅推荐有3~5倍评论数溢价，但评分溢价仅0.1星以内。检索可消除城市规模偏差，不同量级城市匹配率基本一致。
