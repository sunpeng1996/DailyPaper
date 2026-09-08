---
title: 'To See a World in a Living Context: Unified Indoor-Outdoor Urban World Generation'
title_zh: 基于生活上下文的统一室内外3D城市世界生成框架
authors:
- Xiaobin Huang
- Zilong Huang
- Yang Luo
- Hongchao Fan
- Yiping Chen
- Ting Han
affiliations:
- Sun Yat-sen University
- Norwegian University of Science and Technology
arxiv_id: '2608.05879'
url: https://arxiv.org/abs/2608.05879
pdf_url: https://arxiv.org/pdf/2608.05879
published: '2026-08-28'
collected: '2026-09-08'
category: Other
direction: 3D城市生成 · 跨尺度上下文统一建模
tags:
- 3D Generation
- Text-to-3D
- Cross-Scale Context
- Urban Scene Synthesis
- Indoor-Outdoor Alignment
one_liner: 首个统一室内外的3D城市生成框架，基于动态跨尺度上下文保证全局连贯性与建筑内外对应
practical_value: '- 跨尺度上下文动态更新的设计思路可迁移到多粒度内容生成场景，如商圈-店铺-商品层级的文案/3D素材生成

  - 自回归生成时引入相邻已生成内容作为约束的技巧，可用于序列生成类推荐任务，保证推荐结果全局一致性

  - 层级化生成先验传递的架构，可优化生成式推荐中粗粒度召回-细粒度排序的语义一致性'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有文本驱动3D生成方案独立合成室内、室外场景，缺少建筑内外、相邻街区的语义与空间对应关系，无法输出连贯统一的城市级3D场景。
### 方法关键点
提出HoloWorld统一生成框架，基于动态更新的跨尺度世界上下文，从用户文本指令出发层级化完成全链路生成：自回归生成室外街区时引入已生成相邻块作为约束，保证跨街区空间、视觉风格一致性；室外生成结果锚定3D建筑实例与轮廓，约束室内布局生成并继承外观特征，建立明确的建筑内外对应关系。
### 关键结果
相比现有SOTA方案，平均AQS得分提升7.68%，平均RDR得分达到最优，同时保持了高准确度的建筑内外对应与跨街区连贯性。
