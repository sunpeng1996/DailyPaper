---
title: 'CHASE: How Content Ecosystems Are Reshaped When Ranking Is the Only Target'
title_zh: CHASE：反复优化LLM排名信号下的内容生态演化研究
authors:
- Qianwen Gao
- Zichang Su
- Yiwen Hou
- Arlen Kumar
- Leanid Palkhouski
affiliations:
- University of California, Berkeley
- Zhejiang University
arxiv_id: '2608.30466'
url: https://arxiv.org/abs/2608.30466
pdf_url: https://arxiv.org/pdf/2608.30466
published: '2026-08-31'
collected: '2026-09-01'
category: RecSys
direction: 推荐排序 · 长期生态效应仿真
tags:
- GEO
- LLM Ranker
- Content Ecosystem
- Goodhart Effect
- Simulation Framework
one_liner: 提出CHASE仿真框架，量化多轮Generative Engine Optimization下的排名-质量对齐度下降现象
practical_value: '- 做内容/商品生态治理的团队，可复用CHASE的「排序-特征识别-改写-评估」四阶仿真框架，提前预判固定排序策略长期运行下的内容同质化、质量偏离风险，避免线上问题爆发后再被动调整

  - 做LLM排序的团队，需定期审计排序模型的top特征重要性，避免单一结构/语义特征权重过高被创作者定向刷榜，导致排名与真实质量的对齐度快速下跌

  - 做电商商详/内容创作优化的业务方，可参考论文提取的25个排名关联特征（结构/证据/语义三类），在不造假的前提下针对性优化内容，提升LLM推荐/搜索场景下的曝光量

  - 做排序策略A/B测试时，不能仅观测短期NDCG、点击率等指标，需补充长期生态指标（内容同质化度、质量-排名对齐度）的长期观测，避免短期收益换长期生态恶化'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前Generative Engine Optimization（GEO）研究多聚焦单轮个体内容优化效果，忽略了多轮全群体优化下的反馈循环：当大量创作者反复针对固定LLM排名信号调整内容时，会出现类似Goodhart效应的偏差，但具体对内容生态的影响缺乏量化的系统性研究。

### 方法关键点
- 搭建CHASE四阶仿真框架，循环执行RANK（LLM对文档洗牌5次取平均排名，消除输入顺序效应）、DISCRIMINATE（用L2正则逻辑回归从25个预定义特征中筛选top5排名关联特征，生成优胜者特征画像）、REWRITE（随机抽取29%的非优胜文档，基于特征画像定向改写，要求保留原始事实、长度浮动不超50%）、EVALUATE四个步骤，全程固定排名模型，仅模拟创作者侧的内容迭代
- 预定义25个可离线计算的特征，分为三类：结构特征（8个，如词数、可读性）、证据特征（8个，如引用密度、统计数据密度）、语义特征（9个，如查询相似度、词汇多样性），无需LLM调用即可提取

### 关键结果
- 实验基于C-SEO Bench数据集，覆盖零售、游戏、图书、网页、新闻、辩论6个领域，采用跨模型家族配置：Gemini 3.1 Flash做ranker，GPT-5.4-mini做rewriter，Claude Haiku做独立质量裁判，累计运行20轮迭代，设5个随机种子
- 核心结论：排名与独立质量评分的斯皮尔曼相关系数在所有领域均下降，平均降幅0.068，网页领域降幅最大达0.107；排名与生成回答引用的AUC达0.853±0.093，验证了排名可作为内容曝光的有效代理；随机目标对照组证明对齐度下降是排名信号优化导致，而非单纯改写的副作用

> 最值得记住的结论：固定LLM排序策略长期运行下，即使排序模型本身没有任何变化，创作者的群体优化行为也会导致排名对内容质量的指示性持续下降，排序系统设计必须考虑长期生态激励。
