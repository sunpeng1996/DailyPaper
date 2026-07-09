---
title: 'CAIRN: Cross-Room 3D Scene Understanding with Topology-Aware Large Multimodal
  Models'
title_zh: CAIRN：面向跨房间3D场景理解的拓扑感知多模态大模型
authors:
- He Liang
- Chenyang Ma
- Yiming Zhang
- Sangyun Shin
- Andrew Markham
- Niki Trigoni
- Yuhang He
affiliations:
- University of Oxford
- Microsoft
- Simon Fraser University
arxiv_id: '2607.06534'
url: https://arxiv.org/abs/2607.06534
pdf_url: https://arxiv.org/pdf/2607.06534
published: '2026-07-07'
collected: '2026-07-09'
category: Multimodal
direction: 多模态大模型 · 3D场景拓扑感知推理
tags:
- Multimodal LLM
- 3D Scene Understanding
- Topology Awareness
- GNN
- Hierarchical Attention
one_liner: 提出拓扑感知多模态大模型CAIRN，实现多房间3D场景的跨空间推理
practical_value: '- 家居场景电商导购Agent可借鉴分层拓扑注意力机制，建模不同展区/空间的物品关联，提升跨空间物品查询准确率

  - 大场景多区域推荐/导购场景可复用多粒度聚合思路：先通过GNN做局部区域物品关系编码，再引入上层抽象token做全局拓扑路由

  - 递进式评测思路可复用：搭建从单区域感知到跨区域推理的分层评测集，更全面验证大场景Agent的能力边界'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有3D-LLM仅适配简化单房间场景推理，无法支撑真实家庭多房间互联、物品品类丰富的环境下的跨空间查询需求，限制了家庭助理Agent的落地能力。
### 方法关键点
1. 用GNN为物体token注入房间局部关系上下文，增强物体级关联感知；
2. 引入可学习房间token实现房间层级语义抽象，建模全局空间拓扑；
3. 加入带几何偏置的分层注意力掩码，按场景拓扑路由信息，使Transformer注意力匹配场景层级结构；
4. 开源基于HM3D的多房间3D理解基准CAIRN-MR，覆盖grounding、captioning及4类QA任务，递进评测从房内感知到跨房推理的能力。
### 关键结果
在所有CAIRN-MR任务上大幅领先原有3D-LLM，同时在5个单房间基准上保持竞争力。
