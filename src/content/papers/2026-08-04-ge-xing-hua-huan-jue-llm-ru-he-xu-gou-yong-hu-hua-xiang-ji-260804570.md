---
title: 'The Personalization Mirage: How LLMs Fabricate User Profiles, and Why Self-Monitoring
  Misleads'
title_zh: 个性化幻觉：LLM 如何虚构用户画像及自我监控失效的原因
authors:
- Yushi Sun
- Yanjie Zhang
- Rui Sheng
affiliations:
- LIGHTSPEED, Shenzhen
- The Hong Kong University of Science and Technology
arxiv_id: '2608.04570'
url: https://arxiv.org/abs/2608.04570
pdf_url: https://arxiv.org/pdf/2608.04570
published: '2026-08-04'
collected: '2026-08-06'
category: LLM
direction: LLM 个性化 · 幻觉评估
tags:
- Personalization
- Over-Inference
- Hallucination
- Benchmark
- Self-Monitoring
one_liner: 构建首个个性化LLM过度推断基准MirageBench，发现跨模型自评估与真实表现负相关
practical_value: '- 构建个性化LLM/Agent系统时，禁止使用模型自报告的置信度作为跨模型选型的安全指标，优先采用外部中立Judge校验个性化输出的忠实度

  - 用户记忆存储必须增加来源标签，明确区分「用户明确陈述」「有证据支持的推断」「无证据生成内容」三类，禁止将无依据推断作为事实用于后续推荐、交互逻辑

  - 不同个性化任务的过度推断率差异极大：礼品推荐、行程规划类可落地任务OI率仅27%~39%，创意描述类任务OI率高达48%~58%，业务场景中优先选择低OI率的任务引入LLM个性化能力

  - 多轮交互场景需定期清理无依据的记忆推断，尤其能力较强的大模型几乎不会主动修正错误推断，会导致记忆污染随交互轮次线性累积'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前带持久记忆的个性化LLM已广泛应用于对话、推荐等场景，但行业默认模型可可靠区分已知用户事实与猜测内容的假设从未被验证。过度推断（生成超出用户披露证据支持的用户属性）的风险完全未知，且其不同于通用事实幻觉和群体偏见，属于个体层面的无依据虚构，会直接破坏个性化服务的可信度。
### 方法关键点
- 构建MirageBench基准：包含150个平衡刻板印象、反刻板印象、中立的用户画像，每个仅暴露3条事实，搭配6个覆盖从低到高想象梯度的个性化任务
- 设计四分类忠实度体系：将输出分为Grounded（事实复述）、Reasonable（合理推断）、Stereotype（刻板印象推导）、Fabricated（完全虚构），后两类统一定义为过度推断（OI）
- 评估流程采用独立外部Judge（Claude-Opus-4-7）标注所有输出，经人类标注验证四分类Cohen's κ=0.863，二分类κ=0.900，标注可靠性极高
### 关键结果
覆盖7个模型家族的12款主流大模型，共标注143616条个性化声明：
1. 过度推断普遍且严重：所有模型OI率35%~49%，跨模型均值41.6%，仅24%~31%的输出有事实依据
2. 自我监控反转效应：跨模型层面自报告OI率与外部Judge测得的OI率呈显著负相关（ρ=-0.60，p=0.044），自认为错误最少的模型实际表现最差
3. 任务差异显著：礼品推荐类落地型任务OI率仅27%，公寓描述类创意任务OI率高达57.8%；多轮交互中9/12模型的错误推断每轮线性新增5~15条，几乎不主动修正
### 核心结论
模型自评估仅可在单模型内部用于排序输出可信度，跨模型选型必须依赖外部验证，无来源标签的记忆推断必然导致渐进式记忆污染。
