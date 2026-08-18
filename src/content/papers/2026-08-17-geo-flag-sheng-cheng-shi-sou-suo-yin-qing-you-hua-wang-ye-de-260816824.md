---
title: 'GEO-Flag: Detecting and Measuring GEO-Optimized Web Content'
title_zh: GEO-Flag：生成式搜索引擎优化网页的检测与规模测量
authors:
- Junjie Chu
- Ye Leng
- Mingjie Li
- Yun Shen
- Xinyue Shen
- Yang Zhang
affiliations:
- CISPA Helmholtz Center for Information Security
- HPE
- University of Waterloo
arxiv_id: '2608.16824'
url: https://arxiv.org/abs/2608.16824
pdf_url: https://arxiv.org/pdf/2608.16824
published: '2026-08-17'
collected: '2026-08-18'
category: Other
direction: 生成式搜索 · GEO检测与生态审计
tags:
- GEO Detection
- Generative Search
- Intervention Paired Training
- Agent System
- Web Content Audit
one_liner: 提出干预配对训练IPT与GEO门控Agent系统，实测真实搜索结果GEO优化网页占比8.9%
practical_value: '- 干预配对训练（IPT）可直接迁移到「区分特定优化 vs 通用AI改写」的分类任务，比如电商场景区分刻意SEO的商品详情、种草笔记与普通AI润色内容，解决基线依赖通用AI生成特征的捷径问题

  - GEO-gated Agent的分层架构可复用：先通过轻量分类过滤高优样本，再调用重成本工具/大模型做细粒度审计，例如电商合规审核场景可先筛疑似违规内容再做证据核验，大幅降低推理成本

  - 实测2026年修改的网页GEO占比达16.36%，说明生成式搜索优化已形成产业趋势，搜索/内容生态团队需提前布局GEO检测机制，避免低质优化内容抢占合规流量'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
生成式搜索普及催生了GEO（生成式引擎优化）产业，即修改网页内容提升被生成式搜索引用的概率，这类优化可能将低质/虚假信息包装为权威内容，而现有检测方法普遍依赖AI生成特征而非GEO专属信号，跨优化策略、跨作者来源的稳定性差，且缺乏对GEO网页引用可信度的审计能力。
### 方法关键点
- 构建GEOFlagBench基准：覆盖健康、金融、科技、旅行4个领域共400条查询、8类GEO优化策略，合计3200个网页样本，明确区分人类撰写、AI润色、AI生成、GEO优化四类样本，避免模型训练走特征捷径
- 提出干预配对训练（IPT）：用「原网页+GEO优化后网页」正pair约束优化后GEO分数升高，用「原网页+AI润色后网页」零pair约束分数不变，引导模型学习GEO专属特征而非通用AI生成信号
- 搭建GEO-gated Agent审计系统：先用IPT训练的检测器筛出GEO网页，再调用工具解析引用URL、核验访问状态、分级来源权威性，最终输出引用可验证性标签
### 关键结果
- 现有最优基线aggregate F1为0.88，但最差组准确率低至0.375，存在严重的作者来源捷径依赖；IPT将ModernBERT的F1从0.862提升至0.944，最差组准确率从0.725提升至0.883，跨作者来源的FPR差从0.263降至0.108
- 真实场景实测10095条谷歌搜索、Gemini检索的网页中，GEO整体占比8.9%，2026年修改的网页中GEO占比达16.36%，检测出的GEO网页中69.34%的引用属于低可验证性

> 最值得记住的一句话：生成式搜索的生态攻防已进入工业化阶段，仅靠aggregate指标评估的检测模型极易被绕过，必须用配对约束训练+分层审计的架构保障鲁棒性
