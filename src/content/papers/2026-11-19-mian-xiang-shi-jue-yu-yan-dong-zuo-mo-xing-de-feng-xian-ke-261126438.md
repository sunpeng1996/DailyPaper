---
title: Risk-Controlled Test-Time Adaptation for Vision-Language-Action Models
title_zh: 面向视觉-语言-动作模型的风险可控测试时适配框架
authors:
- Zixuan Liu
- Hashem Haghbayan
- Zizhan Zheng
- Siavash Khajavi
affiliations:
- Tulane University
- University of Turku
- Aalto University
arxiv_id: '2611.26438'
url: https://arxiv.org/abs/2611.26438
pdf_url: https://arxiv.org/pdf/2611.26438
published: '2026-11-19'
collected: '2026-11-21'
category: Agent
direction: Agent 测试时适配 · 风险控制
tags:
- VLA
- Test-Time Adaptation
- Uncertainty Estimation
- Risk Control
- Retrieval Augmented
one_liner: 提出R2-VLA风险可控检索增强VLA框架，以最少专家干预实现满足指定成功率的可靠测试时适配
practical_value: '- 可复用「不确定性预测+阈值校准」逻辑，给生成式推荐/Agent决策加风险控制，满足业务指定的bad case率要求，比如商品推荐的错发风险、智能客服的答非所问风险

  - 测试时适配阶段将人工修正的case动态存入RAG检索库的思路，可直接迁移到搜推的在线冷启动场景，不用更新模型参数即可快速适配新流量/新item

  - 检索相关性与结果有效性解耦的判断逻辑，可优化现有RAG搜推系统，避免仅用检索相似度高就直接用召回内容生成结果导致的bad case'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有检索增强VLA模型无需更新参数即可通过专家演示实现测试时适配，但即使召回的演示与当前任务高度相关，模型仍可能无法有效利用召回信息导致任务失败，且无法保障指定成功率要求，专家干预成本高。
### 方法关键点
1. 训练不确定性预测器，基于召回演示评估VLA预测动作的不确定性，指导自主执行或请求专家协助；
2. 设计任务级风险控制流程，动态校准不确定性阈值，满足用户指定的任务失败风险约束；
3. 持续将专家修正的案例存入检索记忆库，在不突破风险约束的前提下迭代提升后续适配效果。
### 关键结果
在3种VLA骨干、4个LIBERO基准测试集上验证，平均任务成功率提升9.2~11.2个百分点，同时所需专家请求量远低于基线方法。
