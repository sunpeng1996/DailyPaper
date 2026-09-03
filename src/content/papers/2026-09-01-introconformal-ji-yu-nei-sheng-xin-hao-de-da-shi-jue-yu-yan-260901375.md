---
title: 'IntroConformal: Conformal Factuality Guarantees for Large Vision-Language
  Models via Introspective Signals'
title_zh: IntroConformal：基于内省信号的大视觉语言模型共形事实性保障
authors:
- Md. Atabuzzaman
- Christian Alexander
- Chris Thomas
affiliations:
- Virginia Tech Department of Computer Science
arxiv_id: '2609.01375'
url: https://arxiv.org/abs/2609.01375
pdf_url: https://arxiv.org/pdf/2609.01375
published: '2026-09-01'
collected: '2026-09-03'
category: LLM
direction: 多模态大模型 事实性风险控制
tags:
- LVLM
- Conformal Prediction
- Factuality Check
- Introspective Signal
- Risk Control
one_liner: 提出无训练共形风险控制框架，用模型内省信号为LVLM提供可证事实性输出保障
practical_value: '- 电商多模态商品理解、直播话术校验场景可复用层间语义稳定性、自验证概率两种内省信号，替代外部事实校验模块，降低系统外部依赖

  - 高风险合规场景（如医药保健品推荐、广告合规校验）可直接引入该无训练共形框架，获得可量化的事实错误率上限保证

  - 多模态导购Agent落地时可将该方法作为输出校验层，无需额外微调即可在可控错误率下最小化有效输出的弃用率'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
LVLM在多模态任务上表现优异，但生成内容事实错误问题突出，现有事实性保障方案要么依赖外部校验器引入额外依赖，要么依赖生成置信度无法识别高置信度错误输出，缺乏可证的统计风险边界。
### 方法关键点
1. 提出无训练的IntroConformal共形风险控制框架，基于模型自身内省信号提供有限样本、分布无关的事实性保证；
2. 设计两种合规性打分规则：一是基于隐层表征的层间语义稳定性，二是捕捉模型对输出事实性自判断的验证概率。
### 关键结果
跨多种LVLM架构测试，IntroConformal完全满足预设的共形风险保证，相比外部校验器基线，输出弃用率大幅降低，声明级事实判别能力达到同等或更优水平。
