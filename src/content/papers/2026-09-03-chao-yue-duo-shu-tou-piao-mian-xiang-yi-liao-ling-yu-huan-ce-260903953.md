---
title: 'Beyond Majority Vote: Multi-Perspective Adjudication for Medical Hallucination
  Detection'
title_zh: 超越多数投票：面向医疗领域幻觉检测的多视角裁决方法
authors:
- Joe Cecil
- Marjorie Freedman
affiliations:
- Information Sciences Institute, University of Southern California
arxiv_id: '2609.03953'
url: https://arxiv.org/abs/2609.03953
pdf_url: https://arxiv.org/pdf/2609.03953
published: '2026-09-03'
collected: '2026-09-05'
category: Eval
direction: LLM 医疗幻觉检测 多视角标注评估
tags:
- Hallucination Detection
- LLM-as-a-Judge
- Annotation Pipeline
- Fact Checking
- Medical LLM
one_liner: 提出融合人工初标、LLM-as-a-Judge候选挖掘、双维度裁决的医疗幻觉标注方案，解决单轮标注漏检问题
practical_value: '- 生成式推荐/电商Agent回复的事实性校验场景，可复用「人工初筛+LLM-as-a-Judge候选召回+领域专家/业务真实数据交叉核验」的多轮标注
  pipeline，大幅降低标注漏检率

  - 构建RAG生成结果幻觉检测benchmark时，避免仅依赖单轮标注或纯LLM打分，多源候选挖掘+多维度裁决可显著提升benchmark完整性，避免低估业务场景下的幻觉率

  - 业务上线LLM-as-a-Judge作为自动校验环节时，必须保留人工兜底核验路径，纯LLM校验会漏过大量人工可识别的事实错误'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
当前LLM事实错误检测多采用单轮单标注员标注方案，长文本场景下细微错误易被漏检，导致幻觉检测benchmark低估真实错误率，无法准确衡量大模型安全能力。

### 方法关键点
设计多视角标注流程，融合两类错误候选来源：标注员首轮标注结果、LLM-as-a-Judge补充挖掘的漏检候选；最终通过「医疗专家裁决+证据链交叉核验」双维度判定错误是否成立。

### 关键结果
首轮标注员漏检了大量后续经裁决验证的事实错误；LLM-as-a-Judge可提升错误候选召回率，但单独使用仍会漏过标注员可识别的错误；现有公开幻觉benchmark普遍存在标注缺失问题，单轮标注方案虽易扩量，但会显著低估真实幻觉率；多轮裁决可提升标注覆盖度，但最终结果仍受裁决人员专业度、证据来源的影响。
