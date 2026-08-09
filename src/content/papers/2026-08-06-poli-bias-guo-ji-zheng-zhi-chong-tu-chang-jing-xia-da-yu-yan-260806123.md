---
title: 'Poli-Bias: Understanding and Measuring Large Language Model Biases in International
  Political Conflicts'
title_zh: Poli-Bias：国际政治冲突场景下大语言模型偏见的理解与度量
authors:
- Massi-Nissa Abboud
- Aladin Djuhera
- Elena Cabrio
- Holger Boche
affiliations:
- Université Côte d’Azur
- Technical University Munich
arxiv_id: '2608.06123'
url: https://arxiv.org/abs/2608.06123
pdf_url: https://arxiv.org/pdf/2608.06123
published: '2026-08-06'
collected: '2026-08-09'
category: Eval
direction: LLM公平性审计 · 政治立场偏见评估
tags:
- LLM Bias
- Fairness Evaluation
- Counterfactual Assessment
- Audit Framework
- Political LLM
one_liner: 提出反事实框架Poli-Bias，多维度细粒度度量LLM在国际政治冲突场景的立场偏见
practical_value: '- 反事实配对对照+多维度拆解的评估思路，可迁移到电商场景检测推荐/客服LLM对不同品牌、地域用户的公平性偏见，避免双标输出

  - 身份变量系统置换的prompt构造方法，可用于定向审计Agent在涉及用户身份、商品品类敏感场景的输出一致性，排查合规风险

  - 不依赖单一指标、拆解偏见表现维度的评估框架，可复用在生成式推荐的输出质量评测，更精准定位问题点'
score: 4
source: arxiv-cs.CL
depth: abstract
---

### 动机
LLM已广泛用于政治、法律类信息的检索、摘要与研判，现有偏见度量方法难以捕捉框架表述、论证逻辑、法律推理层面的细微差异，且单一指标无法定位偏见的具体发生环节。
### 方法关键点
Poli-Bias反事实度量框架构造国家身份系统置换的配对prompt，覆盖不同地缘关系、违法类型、推理任务，将响应差异拆解为5个可解释维度，精准定位不公平对待的具体表现。
### 关键结果
在13个不同架构、不同体量的主流LLM上验证，发现国家身份、用户所属阵营会系统性影响LLM对同等行为的描述、评价与国际法层面的辩护倾向，可实现LLM政治公平性与迎合性的细粒度审计。
