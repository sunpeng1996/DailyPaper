---
title: 'KAISEN: Reproducible Subgroup Fairness Auditing for Clinical Risk Models'
title_zh: 《KAISEN：面向临床风险模型的可复现子群公平性审计框架》
authors:
- Sparsh Roy
- Samuel Girmachew
- Nishita Chavan
affiliations:
- Massachusetts Institute of Technology
- Hopewell Valley Central High School
- East Brunswick High School
arxiv_id: '2607.28608'
url: https://arxiv.org/abs/2607.28608
pdf_url: https://arxiv.org/pdf/2607.28608
published: '2026-07-30'
collected: '2026-08-02'
category: Other
direction: 算法公平性 · 模型审计
tags:
- algorithmic fairness
- model auditing
- subgroup disparity
- equalized odds
- drift monitoring
one_liner: 五阶段子群公平性审计框架KAISEN，经合成基准压力测试输出4项可落地审计结论
practical_value: '- 可借鉴5阶段审计框架（分层→度量→诊断→缓解→漂移监控），适配电商推荐的人群公平性（如不同消费层级、地域用户的误差差异）审计流程

  - 子群差异度量时需结合每组最小可检测效应标准化EOD，避免直接对比原始差异带来的误判，可用于推荐算法的人群公平性归因

  - 漂移监控的阈值不要在单一队列上调优后直接迁移，跨人群部署时需要重新校准阈值，降低误报漏报

  - 公平性缓解方案优先选分组阈值优化，Platt scaling这类校准方法对公平性提升无稳定收益，避免踩坑'
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
临床风险模型整体表现优异，但不同患者子群误差差异大，现有审计管道未经过充分压力测试，各模块可信性与适用条件不明确。
### 方法关键点
5阶段KAISEN审计管道覆盖子群分层、差异度量、机制诊断、事后缓解、漂移监控，在包含16类疾病任务、15个社会决定因子维度、3个预设交叉维度的合成基准上开展失效模式测试。
### 关键结果
1. 原始EOD与显著性计数的秩相关为0.56，经每组最小可检测效应标准化后提升至0.78；
2. 分组阈值优化在48次测试中全量降低EOD（平均下降0.285），分组Platt scaling仅19次优化EOD，平均效果接近0；
3. 机制诊断在受控场景下准确率100%，但代理变量错配时无检出能力且无失败提示；
4. CUSUM漂移检测的误报漏报主要由队列抽样差异导致，单一队列调优的阈值无法跨 cohort 迁移。
