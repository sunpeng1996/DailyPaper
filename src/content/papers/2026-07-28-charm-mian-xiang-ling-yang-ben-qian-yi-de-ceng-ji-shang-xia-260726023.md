---
title: 'CHARM: A Multimodal Graph Foundation Model with Hierarchical Context Modeling
  for Zero-Shot Transfer'
title_zh: CHARM：面向零样本迁移的层级上下文建模多模态图基础模型
authors:
- Ankang Yang
- Jitao Zhao
- Di Jin
- Yuxiao Huang
- Dongxiao He
affiliations:
- 天津大学智能与计算学部计算机科学与技术学院
- 乔治华盛顿大学哥伦比亚文理学院数据科学项目
arxiv_id: '2607.26023'
url: https://arxiv.org/abs/2607.26023
pdf_url: https://arxiv.org/pdf/2607.26023
published: '2026-07-28'
collected: '2026-07-29'
category: LLM
direction: 多模态图基础模型 · 零样本跨域迁移
tags:
- Multimodal Graph
- Foundation Model
- Zero-Shot Transfer
- Hierarchical Context
- Graph Tokenization
- LLM
one_liner: 提出层级上下文建模的多模态图基础模型CHARM，显著提升零样本跨域多模态图任务性能
practical_value: '- 可复用层级上下文建模思路，将电商场景下用户/商品/交互构成的多模态图（含文本、图像、行为特征）中的孤立节点映射到通用高层概念，大幅降低冷启动场景的标注成本

  - 模态感知图上下文编码器的设计可迁移至多模态召回/排序场景，融合商品多模态属性与用户交互结构特征，输出统一特征供LLM做推荐推理使用

  - 图结构转token的转换方法可直接复用在LLM4Rec的预处理流程中，解决图结构信息难以输入LLM的通用问题'
score: 7
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有图基础模型（GFM）要么需下游任务适配，要么仅支持单模态/单域图任务，多模态图零样本跨域迁移方向存在研究空白；且多模态图节点表示易与领域专属结构、模态特有特征耦合，无法泛化到未见过的目标域，全量标注各新域的成本极高难以落地。
### 方法关键点
1. 采用层级图上下文替代孤立原始节点，同时捕获多模态语义与跨模态关联，将领域专属节点模式映射到通用高层概念，无需目标域微调或适配；
2. 设计模态感知图上下文编码器，融合多模态信息与图结构特征，将输出转换为可输入LLM的图token。
### 关键结果
在零样本多模态图任务上取得一致性的性能提升
