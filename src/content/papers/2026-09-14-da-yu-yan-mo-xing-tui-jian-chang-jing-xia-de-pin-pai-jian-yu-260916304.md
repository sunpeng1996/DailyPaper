---
title: Evaluating Brand Retrieval and Ranking in Large Language Model Recommendations
title_zh: 大语言模型推荐场景下的品牌检索与排序评估方法
authors:
- Edward Malthouse
- Kun-Yu Lee
- Jing Yang
- Sanchary Pal
- Xueyan Feng
affiliations:
- Northwestern University
- Boston University
arxiv_id: '2609.16304'
url: https://arxiv.org/abs/2609.16304
pdf_url: https://arxiv.org/pdf/2609.16304
published: '2026-09-14'
collected: '2026-09-16'
category: Eval
direction: 生成式推荐 · 品牌推荐评估
tags:
- LLM4Rec
- Brand Recommendation
- Evaluation Framework
- Popularity Bias
- Generative Recommendation
one_liner: 提出开放式LLM品牌推荐5步评估框架与BRP@k、MRR@k量化指标
practical_value: '- 搭建LLM推荐效果评估体系时，放弃单次生成结果的指标计算逻辑，采用多次重复采样方案统计BRP@k、MRR@k，覆盖生成结果的随机性，避免漏评品牌漏召问题

  - 品牌运营方优化LLM推荐露出时，优先提升用户搜索热度、社交平台讨论量这类公开关联信号，其对推荐优先级的影响远高于传统广告投放、媒体报道

  - 优化LLM品牌推荐召回能力时可采用分层测试逻辑：先测纯类目prompt的基础露出，再测用户需求场景prompt的匹配度，最后用品牌定位探针测试条件召回阈值'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
LLM已成为用户获取产品购买建议的核心入口，但与传统推荐系统从固定候选集排序不同，LLM品牌推荐无明确候选集，同个prompt多次返回的品牌列表、排序波动极大，现有评估方法无法衡量品牌漏召情况，也不能适配生成结果的随机性，品牌方缺乏有效方法监控自身在LLM推荐中的露出表现。

### 方法关键点
1.  先独立于LLM输出定义品类竞争品牌集，避免仅统计模型返回结果导致的漏评问题
2.  定义两个核心评估指标：BRP@k（多次采样中品牌进入前k推荐的概率，衡量露出覆盖率）、MRR@k（结合出现概率与排名倒数的均值，衡量推荐优先级）
3.  标准化5步评估流程：定义竞争集→纯类目prompt测基础露出→探索露出关联的市场信号→需求场景prompt测匹配度→品牌定位探针测条件召回能力

### 关键结果
实验覆盖6款主流商用LLM（GPT-5.5、Gemini 3.1 Pro、Claude Opus 4.7等）、5个消费品类，每个prompt重复40次采样：
- 纯类目prompt下超30%知名品牌完全未被推荐，传统品牌知名度与LLM推荐优先级相关性极低，仅邮轮品类存在弱相关
- 推荐优先级与市场信号的相关度：Google搜索热度（相关系数0.63）> 社交平台讨论量 > 新闻提及、广告投放、维基浏览量
- 类目prompt下露出为0的品牌，在符合其定位的需求场景prompt下BRP@5最高可提升至35.4%，输入明确品牌定位探针时BRP@5可提升至80%以上

**最值得记住的话**：LLM品牌推荐是随机检索排序过程，不能用单次生成列表评估，品牌露出不仅取决于知名度，更取决于公开场景关联信号的强度
