---
title: 'Counterfactual Neighborhood Risk Fields: Evidence-Grounded Selective Safety
  for Vision-Language Models'
title_zh: 反事实邻域风险场：基于证据的视觉语言模型选择性安全方法
authors:
- Tianshi Wang
- Jingsong Wang
- Fengling Li
- Jingjing Li
- Xin Li
- Lei Zhu
affiliations:
- 同济大学
- 穆罕默德·本·扎耶德人工智能大学
- 电子科技大学
- 上海人工智能实验室
arxiv_id: '2610.20679'
url: https://arxiv.org/abs/2610.20679
pdf_url: https://arxiv.org/pdf/2610.20679
published: '2026-10-14'
collected: '2026-10-17'
category: Multimodal
direction: 多模态大模型安全防御
tags:
- VLM
- safety defense
- counterfactual learning
- selective intervention
- multimodal jailbreak
one_liner: 提出基于反事实邻域风险场的VLM选择性安全框架，兼顾高防御率与良性任务可用性
practical_value: '- 电商多模态Agent（图文客服、商品生成Agent）可借鉴反事实对构造方法做安全防护，大幅降低正常请求误拒率

  - 推荐系统多模态内容审核模块可复用风险方向与邻域支持度分离的思路，减少合规误判，提升审核效率

  - Agent服务安全网关可参考选择性干预架构，仅拦截高风险请求，不影响正常用户使用体验

  - 多模态越狱攻击防御可直接复用CNRF的基座适配接口，快速兼容不同架构的VLM底座'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有VLM基于表征的安全防御仅简单区分有害/良性输入，未明确风险评分的可解释性与可信边界，易将不熟悉的正常样本误判为有害，带来过高误拒率，严重损失良性任务可用性。
### 方法关键点
1. 构造上下文匹配的良性-有害反事实对，将二者的表征差异作为与能力相关的风险方向；
2. 单独估计邻域支持度与风险值，避免将陌生样本与有害样本混淆，支持选择性干预而非全量拒答；
3. 设计适配不同VLM架构的接口，仅对高风险请求做响应审核，输出低危害替代结果。
### 关键结果
在3类VLM、5种多模态越狱攻击测试集上，宏防御成功率达86.06%~89.30%，同时保留较高的良性任务效用；低误报场景下，查询匹配参考与上下文-方向对应机制可显著提升风险排序效果。
