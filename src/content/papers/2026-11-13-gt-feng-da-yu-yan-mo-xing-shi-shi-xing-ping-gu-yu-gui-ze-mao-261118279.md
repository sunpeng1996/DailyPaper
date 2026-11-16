---
title: 'GT-FENG: General Theory of Factual Evaluation and Normative Grounding in Language
  Models *Author(s)'
title_zh: GT-FENG：大语言模型事实性评估与规则锚定通用理论
authors:
- Jiayu Feng
affiliations:
- Harvard T.H. Chan School of Public Health
arxiv_id: '2611.18279'
url: https://arxiv.org/abs/2611.18279
pdf_url: https://arxiv.org/pdf/2611.18279
published: '2026-11-13'
collected: '2026-11-16'
category: Eval
direction: 大语言模型事实性评估 · 规则领域错误归因
tags:
- Factuality Evaluation
- LLM Evaluation
- Rule-based Grounding
- Error Attribution
- Context-aware Evaluation
one_liner: 首个统一上下文/时序正确性校验与规则级错误归因的规则类领域LLM事实评估框架
practical_value: '- 电商/Agent回答规则类问题（如售后政策、活动规则、地域准入要求）时，可复用GT-FENG的上下文关联校验逻辑，降低跨场景/跨时效的规则回答错误

  - 大模型应用的bad case归因可借鉴其错误匹配规则库的思路，将错误答案映射到已知规则条目，快速定位幻觉来源是其他场景规则还是过时规则

  - 可直接调用开源gtfeng包对规则类Query的大模型回答做自动校验，降低人工标注评估成本'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有LLM事实性评估仅校验答案与参考的匹配度，无法对错误答案做规则级归因；法律、政策、平台规则等场景下答案正确性高度依赖上下文（管辖范围、时间、规则定义），同一值在不同上下文下对错完全不同。
### 方法关键点
GT-FENG是首个统一规则类场景下正确性校验与错误归因的通用框架：1）基于适用规则校验答案的上下文/时序正确性；2）匹配错误答案对应的已收录规则条目，定位错误来源；3）明确单靠答案无法反推模型实际调用的规则依据。
### 关键结果
在Medicaid收入上限问答场景测试，引入提问对应州的官方规则记录后，仅匹配其他州规则的错误答案占比下降68-78%，超半数剩余稳定错误答案匹配至少2条已收录的异场景/过时规则。框架已开源为Python包gtfeng。
