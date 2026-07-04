---
title: 'ESC: Emotional Self-Correction for Reliable Vision-Language Models'
title_zh: ESC：面向高可靠多模态大模型的情绪自校正方法
authors:
- Tien-Huy Nguyen
- Minh-Nhat Nguyen
- Nguyen Nhat Huy
- Hung Viet Nguyen
- Huy Nguyen Minh Nhat
- Thanh-Huy Nguyen
- Cuong Tuan Nguyen
- Hoang M. Le
- Dat Nguyen
- Phat Kim Huynh
affiliations:
- GenAI4E Lab
- Carnegie Mellon University
- Harvard University
- Northwestern University
- Vietnam National University, Ho Chi Minh City
arxiv_id: '2607.02089'
url: https://arxiv.org/abs/2607.02089
pdf_url: https://arxiv.org/pdf/2607.02089
published: '2026-07-01'
collected: '2026-07-04'
category: Multimodal
direction: 多模态大模型无训练自校正优化
tags:
- VLM
- Self-Correction
- Training-Free
- Emotional Cue
- Multimodal Reasoning
one_liner: 提出无训练情绪触发自校正框架ESC，大幅提升多模态大模型推理可靠性
practical_value: '- 电商多模态客服、商品内容审核场景可直接复用情绪触发prompt trick，无需额外训练即可降低VLM幻觉，提升响应准确率

  - 多模态推荐系统的商品理解、种草内容质检模块可引入「轻量校验+情绪反馈」流程，在不重训模型的前提下降低bad case率

  - 面向用户的导购Agent交互场景可叠加情绪反馈机制，触发模型反思推理，减少错误回答引发的用户投诉'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有VLM在多模态任务中表现优异，但推理可靠性不足，易出现幻觉、安全违规问题；现有自校正方案依赖后训练或定制化人工反馈，计算成本高，业务落地门槛高。

### 方法关键点
提出完全训练-free的ESC框架：1. 外置轻量校验器识别模型初始响应的潜在错误；2. 向模型注入情绪类反馈触发内置反思能力，输出修正后响应，全程无需调整模型参数，接入成本极低。

### 关键结果
在12个覆盖安全、幻觉检测、视觉感知、多模态推理的基准上验证：相比基线模型，LLaVA的安全攻击成功率最高下降51.6%，POPE幻觉检测准确率提升4.3pp；Qwen2-VL的多模态推理任务平均准确率提升7.2pp，且完全不损失模型原有通用能力。
