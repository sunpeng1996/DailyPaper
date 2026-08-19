---
title: Leveraging Association Context Retrieval in Knowledge Edit- ing to Build White-Box
  Attacks on LLMs
title_zh: 利用知识编辑中的关联上下文检索构建LLM白盒攻击
authors:
- Roman Maksimov
- Vladimir Aletov
- Vladimir Solodkin
- Dmitry Bylinkin
- Daniil Medyakov
- Aleksandr Beznosikov
affiliations:
- Basic Research of Artificial Intelligence Laboratory
- Innopolis University
arxiv_id: '2608.17836'
url: https://arxiv.org/abs/2608.17836
pdf_url: https://arxiv.org/pdf/2608.17836
published: '2026-08-18'
collected: '2026-08-19'
category: LLM
direction: LLM安全 · 白盒攻击与知识编辑
tags:
- LLM Safety
- White-box Attack
- Knowledge Editing
- Context Retrieval
- Jailbreak Attack
one_liner: 受知识编辑定位编辑范式启发，引入模型关联知识检索，实现全主题类别LLM白盒攻击，效果优于基准且不损通用性能
practical_value: '- 电商/广告LLM Agent上线前，可参考该攻击逻辑反向排查知识编辑模块脆弱点，避免恶意篡改导致安全对齐约束失效

  - 业务侧需要定向修改LLM特定领域输出时，可复用「关联上下文检索+知识编辑」思路，解决单条prompt修改生效范围窄的问题

  - 做LLM对齐效果鲁棒性评估时，可引入该白盒攻击方法作为测试用例，提升业务场景下对齐方案的可靠性'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
当前LLM广泛用于电商客服、推荐决策等业务场景，对齐后的安全鲁棒性直接影响业务合规性，但现有对齐方案普遍存在脆弱性，已有的白盒越狱攻击大多仅能突破预定义数据集内的prompt约束，生效范围极窄，无法覆盖全主题类别，亟需更高效的攻击方法用于验证对齐方案的可靠性。
### 方法关键点
1. 受知识编辑领域「定位-编辑」范式启发，利用知识编辑后模型对编辑目标预测概率显著升高的特性设计攻击逻辑，大幅提升攻击成功率；
2. 引入从模型内部检索的关联知识改造编辑框架，将约束解除范围从预定义数据集扩展到整个主题类别，无需依赖预设prompt即可实现同主题全场景越狱。
### 关键结果
在多种主流LLM架构上实验，攻击效果显著优于现有同类基线方法，同时模型通用性能下降幅度可忽略，不会对正常业务推理能力造成显著损伤。
