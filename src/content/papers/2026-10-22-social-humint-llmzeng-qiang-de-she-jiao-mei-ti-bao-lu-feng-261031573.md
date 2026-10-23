---
title: 'Social-HUMINT: An LLM-Augmented Unified Framework for Measuring Social Media
  Exposure'
title_zh: Social-HUMINT：LLM增强的社交媒体暴露风险统一测量框架
authors:
- Pellegrino Casoria
- Simon Pietro Romano
affiliations:
- University of Naples Federico II
arxiv_id: '2610.31573'
url: https://arxiv.org/abs/2610.31573
pdf_url: https://arxiv.org/pdf/2610.31573
published: '2026-10-22'
collected: '2026-10-23'
category: Agent
direction: Agent 多智体用户风险画像
tags:
- Multi-Agent
- User Profiling
- LLM
- Social Engineering
- CTI
one_liner: 统一SOCMINT与Cyber-HUMINT能力体系，通过LLM多Agent管道量化社交媒体用户社工暴露风险
practical_value: '- 复用「dumb scraper + smart LLM」架构：爬取层仅做最小化内容获取，语义解析全交由LLM处理，可大幅降低反爬适配、DOM结构变动带来的维护成本，适合电商公开信息爬取、用户评论分析场景

  - 多Agent分层调用LLM的成本优化方案：按任务复杂度匹配不同规格模型（简单提取用轻量模型、复杂推理用大模型），实测可在保证效果的前提下将API开销控制在可忽略水平

  - 可溯源的双层用户画像范式：明确区分可验证的提取事实和带置信度、推理链路的推断属性，满足推荐系统用户兴趣建模、潜客挖掘的可解释性要求'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
后API时代主流社交媒体平台收紧公开数据接口，但LLM可从非结构化公开内容中批量提取结构化信息、推断用户未披露的隐性属性，用户真实暴露风险远高于其主动发布的内容量级。现有CTI框架仅覆盖攻击技术环节，未打通从被动公开信息收集到主动社工诱导的完整链路，无法量化用户暴露程度，而近年依托社交画像的钓鱼攻击量同比增长84%，亟需可落地的风险测量体系。
### 方法关键点
- 构建统一Social-HUMINT能力框架：整合SOCMINT（被动社交媒体情报）和Cyber-HUMINT（主动社工情报）两个独立领域，输出覆盖CTI全生命周期5个阶段的38项能力 taxonomy，经13名安全专家验证内容有效性
- 落地LLM多Agent pipeline：采用「极简爬取+LLM语义解析」架构，爬取层仅做页面内容拉取，全量语义解析、跨源融合交由分工Agent处理，适配平台反爬规则迭代；按任务复杂度分层调用不同规格LLM，平衡效果与成本
- 双层可溯源用户画像模型：明确区分可验证的提取事实（身份、经历等公开字段）和带置信度、推理链路的推断属性（行为特征、兴趣偏好等），支持审计与人在回路校验
### 关键结果
实体提取F1=97.3%，推断属性用户自评得分4.73/5，均大幅优于规则、NER基线；个性化接触选项排序匹配度显著高于随机水平，可有效支撑定制化社工攻击；单用户全链路处理平均耗时约8.5分钟，API成本可忽略。
### 核心结论
一个人的真实暴露风险不是他公开发布的内容，而是可以从这些内容中推断出的信息。
