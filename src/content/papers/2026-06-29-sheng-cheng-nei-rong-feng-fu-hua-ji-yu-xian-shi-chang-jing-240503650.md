---
title: Generated Contents Enrichment
title_zh: 生成内容丰富化：基于显式场景表示的条件图像生成方法
authors:
- Mahdi Naseri
- Jiayan Qiu
- Zhou Wang
affiliations:
- University of Waterloo, Canada
arxiv_id: '2405.03650'
url: https://arxiv.org/abs/2405.03650
pdf_url: https://arxiv.org/pdf/2405.03650
published: '2026-06-29'
collected: '2026-07-07'
category: Multimodal
direction: 多模态生成 · 场景图语义补全
tags:
- Scene Graph
- Graph Convolutional Network
- Adversarial Training
- Conditional Image Generation
- Content Enrichment
one_liner: 提出基于场景图与GCN的对抗式GCE框架，显式补全对象及关联后生成语义更丰富的合理图像
practical_value: '- 电商营销素材生成：输入稀疏的商品+场景描述（如「户外冲锋衣+山顶」），可自动补全关联对象（登山包、登山杖等）生成符合真实场景的商品图，降低美工设计成本

  - 多模态推荐素材优化：为推荐系统中的商品生成适配用户偏好的场景化配图，提升商品点击转化率

  - 智能设计Agent组件：可作为Agent的语义补全模块，支持用户输入短描述生成可校验的结构化设计中间结果'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有条件图像生成系统从稀疏场景描述生成内容时，补全的语义信息完全隐式包含在生成器中，无中间可解释可校验的结构，易出现生成内容结构不一致、语义不符合常识的问题，且无法针对补全的语义做定向调整。
### 方法关键点
1. 定义Generated Contents Enrichment（GCE）任务，将显式场景表示作为中间层，实现语义补全过程可解释、可干预
2. 提出联合训练的对抗式框架：先将输入稀疏描述转换为场景图，用Graph Convolutional Networks预测新增对象及对象间关联，补全场景图后输入下游图像生成管线生成最终内容
3. 端到端优化同时兼顾场景图补全的语义准确性、结构一致性与生成图像的视觉合理性
### 关键结果
在Visual Genome数据集上验证，场景图补全的各项代理指标均优于基线模型，生成图像质量评分显著高于传统隐式补全方案，用户调研中超过75%的参与者认为其输出的语义丰富度、结构合理性更符合预期
