---
title: 'SARA: An Auditor-in-the-Loop LLM Recommender for Sustainability Reports'
title_zh: 面向可持续发展报告审计的人在回路大语言模型推荐系统SARA
authors:
- Lars Hillebrand
- Thiago B. F. de Oliveira
- Tim Dilmaghani
- Mohamed Khaled
- Writwick Das
- Rafet Sifa
affiliations:
- Fraunhofer IAIS
- Lamarr Institute for Machine Learning and Artificial Intelligence
- PwC GmbH WPG
- University of Bonn
arxiv_id: '2611.30839'
url: https://arxiv.org/abs/2611.30839
pdf_url: https://arxiv.org/pdf/2611.30839
published: '2026-11-23'
collected: '2026-11-24'
category: RecSys
direction: 合规审计场景 · 人在回路LLM内容推荐
tags:
- Human-in-the-loop
- LLM4Rec
- Content-based Recommendation
- ESG
- Regulatory Compliance
one_liner: 提出嵌入Word的审计人在回路ESG报告推荐系统，通过主题过滤大幅降低LLM匹配成本
practical_value: '- 针对固定查询集（如电商合规校验、商品属性匹配）场景，可先做粗粒度主题过滤再调用LLM精排，能大幅降低token成本同时提升匹配精度，规避长上下文丢信息问题

  - 人在回路推荐系统可直接嵌入用户现有工作流（如电商运营ERP、商家后台），减少工具切换成本，用户反馈可直接沉淀为标注数据迭代模型

  - 高风险推荐场景（如合规校验、广告审核）可采用保守过滤策略，不确定候选全部保留避免漏召回，错召成本远低于漏召的场景优先保障召回'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
欧盟CSRD新规要求企业可持续发展报告需匹配约1700项监管要求，传统人工审计需反复核对多版本长文档，效率极低；直接将全文档喂入LLM做单要求匹配，token成本高、推理速度慢，长上下文匹配还易出现信息遗漏，亟需兼顾效率、成本、精度的辅助审计方案。

### 方法关键点
- 系统作为插件嵌入Microsoft Word，直接读取文档结构，全审计流程无需切换工具，替代传统表格手动作业
- 采用两级匹配架构：先对所有文档段落做主题/子主题分类，匹配每个监管要求时仅召回同子主题的段落作为候选，候选集不足时回退到全文档，避免漏召
- 人在回路设计：LLM输出的匹配结果和合规判定仅作为建议，审计师可一键确认/驳回/新增匹配，所有操作留痕形成审计 trail，匹配记录可跨文档版本迁移，仅需复核修改段落
- 单次LLM调用同时完成段落匹配和合规三级判定（已满足/部分满足/未满足），输出分维度判定依据和原文引用，可解释性强

### 关键实验
在2份专家标注的CSRD报告（共874项标注要求）上对比3种策略，均基于gpt-5.4：1）Azure混合向量+关键词检索；2）全文档喂入LLM匹配；3）SARA的主题过滤方案。结果显示SARA比全文档方案成本降低6倍，推理速度提升42%，F1提升3.1个点，精度提升4.4个点，召回略高于全文档方案，同时比Azure混合检索成本低2.7倍。

*最值得记住的一句话：针对固定分类体系下的多查询匹配场景，前置粗粒度主题过滤不仅能大幅降低LLM推理成本，还能减少长上下文匹配噪声，同时提升精度。*
