---
title: Which Language Should a Skeleton Speak? Language Choices in Multilingual Reasoning
title_zh: 多语言推理场景下结构化推理骨架的语言选择策略研究
authors:
- HyeonSeok Lim
- SeungWoo Song
- Inho Won
- Hoyun Song
- Jihyo Kim
- KyungTae Lim
affiliations:
- ETRI
- KAIST
- Dankook University
arxiv_id: '2610.09607'
url: https://arxiv.org/abs/2610.09607
pdf_url: https://arxiv.org/pdf/2610.09607
published: '2026-10-06'
collected: '2026-10-12'
category: Reasoning
direction: 多语言推理 · Prompt策略优化
tags:
- Multilingual Reasoning
- Prompt Engineering
- Skeleton Prompt
- LLM Reasoning
- Mathematical Reasoning
one_liner: 提出LASEF框架分析多语言数学推理的骨架语言规律，验证英文骨架并非全局最优
practical_value: '- 部署多语言场景Agent、商品文案生成、跨境电商搜索Query理解服务时，不要默认选择英文prompt骨架，需针对目标语种、模型规模做小范围AB实验验证最优骨架语言

  - 小参数LLM落地低资源语种业务（如东南亚、拉美跨境电商客服、推荐理由生成）时，可优先尝试英文推理骨架，大概率获得平均正向收益

  - 多语言大模型业务效果评估需排除测试集、评测规则的特异性干扰，避免基于单一benchmark的结论直接上线'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有骨架引导的结构化推理prompt方法普遍默认英语中心场景，多语言场景下骨架语言选择无明确指导规则，缺乏系统性分析框架。
### 方法关键点
提出LASEF框架覆盖不同数学推理benchmark、模型参数规模、语种维度，结合greedy decoding、多轮rollout评测、翻译消融、跨benchmark验证，系统分析骨架语言的效应模式。
### 关键结果
平均来看英文骨架存在小幅正向倾向，在小模型、低资源语种场景下收益最显著；统计校正后仅少数语种的英文骨架收益显著，英文并非全局最优选择；总结出3类骨架语言效应：方向一致型、评测/benchmark依赖型、非对称负向型，效应无法仅用生成质量完全解释。
