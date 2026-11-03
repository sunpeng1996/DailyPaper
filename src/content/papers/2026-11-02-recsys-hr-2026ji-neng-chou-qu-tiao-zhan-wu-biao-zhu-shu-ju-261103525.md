---
title: 'Grading the Unannotated: Insights from the WorkRB Skill Extraction Challenge
  at RecSys-HR 2026'
title_zh: RecSys-HR 2026技能抽取挑战：无标注数据分级标注方法与洞察
authors:
- Warre Veys
- Luis Gasco
- Jens-Joris Decorte
affiliations:
- TechWolf
- Avature
- Ghent University – imec
arxiv_id: '2611.03525'
url: https://arxiv.org/abs/2611.03525
pdf_url: https://arxiv.org/pdf/2611.03525
published: '2026-11-02'
collected: '2026-11-03'
category: RecSys
direction: 招聘场景技能推荐 · 分级标注评估
tags:
- Skill Recommendation
- Graded Relevance
- LLM-as-Judge
- RecSys Benchmark
- Retrieve-and-Rerank
one_liner: 提出四元二元级联LLM标注框架，发布5个分级相关性基准并拆解挑战赛优胜方案共性
practical_value: '- 标注方法可直接迁移：电商/搜索推荐场景的相关性标注可拆分为多个独立简单二元判断的级联，用小LLM当标注员，比直接打0-4分的一致性高20%以上，大幅降低人工标注成本

  - 评估体系优化：传统二元MAP/MRR仅看正样本排名，会隐藏排序窗口内的无关垃圾内容，业务评估需加窗口内grade0内容占比指标，避免高估模型效果、训练出依赖词汇捷径的劣化模型

  - 排序优化ROI参考：多阶段召回排序的效果提升主要来自清除排序窗口中的无关内容，而非挖掘更多正样本，优化中长尾排序的投入产出比远高于挖新正样本

  - 标注Trick：给LLM标注员的输入需包含实体完整描述而非仅短标签，可避免标签歧义（如电商同名不同款商品）带来的标注错误'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
传统技能推荐/抽取的二元评估仅将少量人工标注正样本视为正确，其他全算错误，在13939条的ESCO技能词表下，会奖励靠词汇捷径排对正样本、但排序顶部存在大量无关内容的模型，完全无法暴露语义理解缺陷；过往三元标注粒度太粗，标注一致性差，无法满足benchmark需求。

### 方法关键点
- 将0-4级相关性标注拆解为4个顺序二元判断（同领域？活动被提及？粒度合适？等价于金标？），每个问题单独优化prompt，用小LLM级联标注，比同模型直接打分的标注准确率更高
- 重新标注4个现有技能抽取数据集+1个新构建的 lexical distant 技能归一化数据集，共产出4.3M条分级标注，结果经盲测人工/前沿大模型验证，二次加权kappa达0.69-0.73
- 挑战赛以nDCG@100为核心指标，设计专门的作弊检测机制，排除利用原始二元标注作弊的提交

### 关键结果数字
- 共154份有效提交，优胜方案均采用多路召回+重排架构，top12团队的分级指标排名与二元MAP排名的Kendall τ仅为0.06，完全无相关性
- 分级指标下最优方案比基线高0.217 nDCG@100，二元指标下差距仅为前者的1/3，二元评估严重压缩模型真实效果差距
- 所有可统计的提交方案参数量至少是109M基线的42倍，中位数达167倍，参数量超过10B后与效果的相关性消失

> 最值得记住的话：任何仅用少量正样本做二元评估的推荐任务，都可能隐藏着模型大量输出无关内容的缺陷，真实效果差距远大于二元指标显示的数值
