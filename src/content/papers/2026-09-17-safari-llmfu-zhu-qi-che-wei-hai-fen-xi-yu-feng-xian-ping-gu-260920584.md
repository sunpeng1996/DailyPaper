---
title: 'SAFARI: An Industrial Benchmark for LLM-Assisted Hazard Analysis and Risk
  Assessment'
title_zh: SAFARI：LLM辅助汽车危害分析与风险评估工业基准
authors:
- Chenxi Wu
- Zimu Wang
- Haiyang Zhang
- Wei Wang
- Zhijie Xu
affiliations:
- Xi’an Jiaotong-Liverpool University
arxiv_id: '2609.20584'
url: https://arxiv.org/abs/2609.20584
pdf_url: https://arxiv.org/pdf/2609.20584
published: '2026-09-17'
collected: '2026-09-20'
category: Eval
direction: LLM安全合规场景评估基准
tags:
- LLM
- Benchmark
- Risk Assessment
- LLM-as-judge
- Safety Evaluation
one_liner: 推出首个符合ISO 26262的汽车HARA工业基准，含3000条案例与高相关性评估协议
practical_value: '- 做合规类生成（如广告文案合规校验、商品宣传话术生成）的评估时，可复用reference-anchored LLM-as-judge范式，降低人工标注成本、提升评估一致性

  - 大模型分类任务（如广告标签分类、商品类目预判）的prompt优化中，不要默认CoT一定提效，需针对性做AB测试避免效果劣化

  - 落地强规则约束的Agent任务（如合规审核Agent、商品风险识别Agent）时，不要高估LLM规则对齐能力，需针对上下文遗漏、属性误判两类高频错误设置人工核验节点'
score: 4
source: arxiv-cs.CL
depth: abstract
---

### 动机
LLM在强监管功能安全工作流中的可靠性缺乏系统性验证，汽车领域ISO 26262标准下的HARA任务尚无工业级评测基准。
### 方法关键点
1. 发布SAFARI基准，包含3000条去标识工业HARA案例，覆盖开放危害分析、标准对齐风险评估两个耦合任务
2. 提出首个锚定参考的LLM-as-judge评估协议，和专家判断相关性高，可用于开放生成任务的自动评测
3. 对9款前沿LLM做基准测试，完成错误归因分析
### 关键结果
最佳大模型的ASIL风险分类macro-F1仅为0.261；CoT提示对分类任务收益有限甚至会劣化效果；主要错误来自危害生成环节的场景关键上下文遗漏、风险评估环节的可控性误判。
