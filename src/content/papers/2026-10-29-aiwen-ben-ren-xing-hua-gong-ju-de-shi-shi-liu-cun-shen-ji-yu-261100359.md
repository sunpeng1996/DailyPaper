---
title: Humanized but Still True? Auditing Facts and Detection in AI-Text Humanizers
title_zh: AI文本人性化工具的事实留存审计与检测方法研究
authors:
- Ziyuan Wang
- Genliang Zhu
- Xiaobo Chen
affiliations:
- Independent Researcher
- Georgia Institute of Technology
- University of Massachusetts Amherst
arxiv_id: '2611.00359'
url: https://arxiv.org/abs/2611.00359
pdf_url: https://arxiv.org/pdf/2611.00359
published: '2026-10-29'
collected: '2026-11-15'
category: LLM
direction: LLM生成文本处理 · 事实审计与检测
tags:
- AI-Humanizer
- Fact-Checking
- LLM-Text-Detection
- Zero-Shot
- Text-Audit
one_liner: 审计主流AI文本人性化工具的事实篡改率，提出零-shot检测方案远超现有基线
practical_value: '- 电商/广告生成文案（商品详情、营销话术）使用humanizer工具时，可复用论文开源的规则事实检查器，校验数字、产品参数、引用内容的留存率，避免不实宣传风险

  - 业务侧需识别经过humanizer改写的AI生成内容（如虚假评论、UGC营销内容），可采用Jev零-shot检测方案，AUROC比现有主流检测器高0.18-0.22，无需额外训练即可上线

  - 自研业务端humanizer工具时，无需盲目追求检测逃逸率，其与事实留存率无显著相关性，可优先优化核心事实保留逻辑'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
AI文本humanizer的公开榜单仅评估检测逃逸率与语义相似度，未覆盖可验证事实的留存情况，改写易产生事实偏差，且现有AI文本检测器对humanized内容识别准确率低。
### 方法关键点
自研规则式事实检查器，校验改写前后数字、日期、人名、机构名、引用片段的留存度，经AI标注验证precision达0.84-1.00、recall达0.93-0.95；提出Jev通用决策模型，通过单条零-shot提问区分人类原生文本与humanized改写文本。
### 关键结果
11款商用humanizer在35%~65%含事实的文档中会篡改/删除至少1项事实单元，仅统计数字与人名时仍有10款工具在20%以上文档中篡改事实；事实留存率与检测逃逸率无显著相关性（Spearman rho=-0.46）；Jev检测AUROC达0.864，较Binoculars等基线高0.18~0.22，现有困惑度检测器对2026款模型生成的AI文本检测精度低于随机水平（AUROC 0.37~0.39）
