---
title: Grounding LLM Reasoning under Incomplete Graph Evidence
title_zh: 不完整图证据下大语言模型推理的 grounding 理论框架
authors:
- Jiaqi Li
- Fanghui Song
affiliations:
- Tianjin Normal University
- Harbin Institute of Technology
arxiv_id: '2606.30247'
url: https://arxiv.org/abs/2606.30247
pdf_url: https://arxiv.org/pdf/2606.30247
published: '2026-06-29'
collected: '2026-06-30'
category: Reasoning
direction: 知识图谱增强LLM推理
tags:
- LLM Reasoning
- Knowledge Graph
- Grounding
- GraphRAG
- Posterior Regularization
one_liner: 证明不完整知识图谱下硬 grounding 的信息论局限，提出KL正则化软 grounding 框架
practical_value: '- 构建GraphRAG/Graph Agent类多跳推理系统时，不要用硬规则过滤所有无图支持的推理轨迹，给未被观测但不矛盾的路径分配有限slack惩罚，可保留真但未检索到的正确路径，提升召回

  - KG关系建模需要保留类型和方向敏感度，不要用普通同构图拉普拉斯平滑，使用类型化有向残差能量，可避免关系反转类幻觉（如错误混淆“商品属于品牌”和“品牌属于商品”）

  - 需根据KG覆盖度选择约束强度：闭域结构化商品库/规则库可使用硬约束，开放域搜索/导购Agent场景优先选择软 grounding + 对未支持结果标注/弃权，提升输出可信度

  - 多路径推理时使用带温度的熵聚合方式保留备选路径概率，不要直接选单最优路径，降低路径检索缺失带来的错误率'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**：现有知识图谱增强LLM推理（覆盖GraphRAG、KGQA、图Agent等场景）依赖的都是检索得到的局部不完整子图，而非全局完整KG。现有方法要么将未出现在观测图中的推理路径直接过滤，要么仅把图作为上下文不做显式约束，没有区分「未观测到支持」和「本身错误」两种情况，容易错误删除正确但未被检索的路径，或保留错误路径，在开放场景下这个问题尤为突出，亟需理论层面澄清。

**方法关键点**：
1. 证明信息论不可能定理：不完整图下，任何仅基于观测的硬规则都无法同时保留所有真但未观测的轨迹、拒绝所有假的未支持轨迹，该局限是信息性的而非算法性的，更强搜索或更好嵌入都无法解决；
2. 提出软grounding框架：将LLM对推理轨迹的原生分布作为先验，由观测不完整图诱导实体锚点、类型化关系残差、路径能量，通过KL正则化后验变形重加权轨迹，给未支持但不矛盾的路径分配有限惩罚（有限slack），硬约束是无限惩罚的边界特例；
3. 推导得到后验稳定性边界：证据的有界扰动只会带来后验分布的有界变化，给出带温度的熵聚合多备选路径方法，避免单路径选择的脆性。

**关键结果**：本文为理论框架研究，未开展新的实证实验，所有核心结论均为理论推导得到。

**最值得记住的一句话**：开放世界不完整KG下，「没有观测到支持」不等于「命题为假」，有限slack的软grounding是更合理的默认选择。
