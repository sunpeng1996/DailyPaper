---
title: 'GroundedGEO: Auditing the Evidence Gap in Generative Search Rankings'
title_zh: GroundedGEO：审计生成式搜索排序中的证据缺口
authors:
- Yihan Xia
- Huiling Fan
- Kangrong Zhong
- Taotao Wang
affiliations:
- Shenzhen University
arxiv_id: '2609.25189'
url: https://arxiv.org/abs/2609.25189
pdf_url: https://arxiv.org/pdf/2609.25189
published: '2026-09-21'
collected: '2026-09-23'
category: RecSys
direction: 生成式搜索排序 · 可信度审计
tags:
- Generative Search
- Ranking Robustness
- Fact Grounding
- GEO
- Reranking
one_liner: 提出声明-证据匹配的后重排审计框架，量化生成式搜索无证据内容的排名增益风险
practical_value: '- 电商生成式搜索场景可复用claim级证据校验的后重排架构，无需修改基础排序模型，仅对query相关的无证据声明做惩罚，可实现对合规内容的零误伤

  - 做GEO（生成式引擎优化）攻防评估时，可复用packet twin对照实验范式，固定候选文本仅修改证据包，精准剥离文本表面特征和证据对排序的影响

  - 落地证据校验模块时优先保障标签精度（而非整体准确率），精度≥0.9即可实现零误杀合规内容，再优化召回率提升无证据内容的打压效果

  - 暂无高可靠自动声明-证据匹配能力的团队不建议直接上线自动防御，当前主流开源LLM judge的五分类证据匹配准确率不足70%，易出现规则漏洞'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
生成式搜索系统直接为用户排序推荐产品，商家可通过生成大量query相关的虚假描述刷高排名，而纯文本排序模型和防御手段无法区分内容是真实合规还是虚假捏造，存在可识别性缺口；且虚假描述生产成本远低于真实证据举证，行业缺乏可量化的审计框架验证这类风险。

### 方法关键点
- 构建电商证据配对基准，覆盖50个ESCI电商query、1950个排序案例，证据包来自商品登记记录、买家评价、官方认证registry三类不同可信度的数据源
- 提出GroundedGEO后重排框架：先从候选文本提取原子级query相关声明，和证据包匹配打标，再对无证据声明量化罚分后调整排序，保留完整的声明-证据审计链路
- 设计packet twin对照实验：固定候选文本不变，仅给无证据声明补充对应证据，单独验证证据对排序的影响，排除文本长度、措辞等干扰

### 关键结果
- Qwen2.5-7B对无证据的丰富描述存在显著排名增益，NRG达+0.065~+0.092，甚至超过真实合规的丰富描述，该效应在GLM-5.3-Flash上完全不存在
- 基于oracle标签的GroundedGEO重排在λ=40时，无证据内容的top-3曝光率从0.65降至0.43，证据洗白类内容从0.61降至0.39，对合规内容零误杀
- 所有测试的自动LLM judge均未达到预设可靠性阈值（macro-F1≥0.75，Cohen's κ≥0.6），最优的Qwen3.8-27B仅能实现79%~100%的oracle打压效果

**最值得记住的一句话**：生成式搜索的可信度防御不能只看文本表面特征，必须打通独立证据校验链路，且证据覆盖率和标签精度的优先级远高于整体匹配准确率
