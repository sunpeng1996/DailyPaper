---
title: Shieldstral
title_zh: Shieldstral：适配多策略的3B参数多模态内容安全分类器
authors:
- Antonia Calvi
- Avinash Sooriyarachchi
- Giada Pistilli
- Guillaume Lample
- Maarten Buyl
- Maximilian Augustin
- Maximilian Müller
- Pierre Stock
- Tom Bewley
- Wassim Bouaziz
arxiv_id: '2607.25857'
url: https://arxiv.org/abs/2607.25857
pdf_url: https://arxiv.org/pdf/2607.25857
published: '2026-07-27'
collected: '2026-07-29'
category: LLM
direction: 大模型Guardrail 多模态内容安全审核
tags:
- Content-Moderation
- Multimodal-Classifier
- LLM-Guardrail
- Small-LLM
- Policy-Adaptive
one_liner: 将内容安全审核转化为二元QA任务，3B小模型实现媲美7倍体量大模型的多模态安全分类SOTA
practical_value: '- 可将电商全链路内容审核（商品详情、评论、生成式推荐文案、Agent客服回复合规校验）统一为二元QA任务，避免多场景单独训练分类器的冗余成本

  - 小底座+大规模定制化数据集的方案可复用在低延迟要求的审核场景，用3B级小模型替代大模型，推理成本降低80%以上，同时保障准确率

  - 策略自适应设计可直接适配不同业务线的差异化合规要求（如母婴/酒类品类的特殊审核规则），无需重新训练，仅修改规则描述query即可上线'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有大模型guardrail多采用固定分类类目，一方面无法兼容不同安全数据集的异构类目体系，训练数据整合难度高；另一方面无法适配不同业务场景的差异化安全策略要求，且大参数审核模型推理成本过高，难以落地高吞吐场景。
### 方法关键点
1. 将内容审核重构为二元QA任务，输入为安全规则描述query+待审核内容（文本/图像），输出连续安全得分，统一所有异构审核任务的建模范式；
2. 基于Ministral-3B底座，构建54.1M规模的多源审核训练样本+细粒度策略适配评估集，完成适配训练。
### 关键结果
3B参数模型在文本安全基准上媲美甚至超过7倍体量（约20B）的大模型，同时在多模态安全分类任务上达到SOTA。
