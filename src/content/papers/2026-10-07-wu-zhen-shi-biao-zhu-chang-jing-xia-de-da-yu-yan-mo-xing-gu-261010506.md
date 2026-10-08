---
title: 'Validity Without Ground Truth: What Stated-Preference Economics Offers the
  Evaluation of Language Models'
title_zh: 无真实标注场景下的大语言模型评估：陈述偏好经济学方案
authors:
- Daniel Robert Kling Alexander
- Catherine Louise Kling
affiliations:
- University of Michigan School of Information
arxiv_id: '2610.10506'
url: https://arxiv.org/abs/2610.10506
pdf_url: https://arxiv.org/pdf/2610.10506
published: '2026-10-07'
collected: '2026-10-08'
category: Eval
direction: LLM无标注评估 · 经济学框架迁移
tags:
- LLM Evaluation
- Stated Preference
- Validity Testing
- Ground-Truth-Free
- Economic Framework
one_liner: 将陈述偏好经济学的有效性框架迁移到无标注LLM评估场景，完成6款大模型效果验证
practical_value: '- 无ground truth的LLM回答评估（如Agent给用户的购买决策建议、生成式推荐的合理性判断）可直接复用内容/结构/效标有效性三层评估框架，替代零散的人工主观打分

  - 涉及用户偏好类的LLM输出校验（如个性化消费方案、多属性商品权衡推荐）可引入经济学理论约束（如需求随价格下降、支付意愿与收入正相关等）做自动化合理性校验

  - 用LLM模拟用户做A/B测试、偏好调研时，可加入激励相容性、结果相关性校验，提升模拟用户回答的可信度，降低调研成本'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
大量LLM落地场景（如用户消费决策建议、多维度价值权衡类问题）无可用ground truth，传统匹配人类回答的评估方式可信度低，缺乏统一的无标注评估体系。
### 方法关键点
引入陈述偏好经济学领域成熟的有效性评估框架，包含内容有效性、结构有效性、效标有效性、可靠性、激励相容性、结果相关性6个核心维度，可针对具体业务场景匹配领域理论设计可量化的校验规则。
### 关键结果数字
在水质价值评估场景对6款LLM测试：2款旧模型在家庭年收入7.5万美元档位的基础需求向下校验即失败，2款最新模型可通过所有理论有效性测试，但在收敛有效性上存在显著差异；框架仅验证回答逻辑一致性，不保证绝对正确性。
