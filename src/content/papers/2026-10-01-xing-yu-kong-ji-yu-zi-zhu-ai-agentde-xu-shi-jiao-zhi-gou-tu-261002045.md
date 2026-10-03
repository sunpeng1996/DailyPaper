---
title: 'Form and Void: Entangled Composition through an Autonomous AI Agent'
title_zh: 形与空：基于自主AI Agent的虚实交织构图生成
authors:
- Shiwen Wang
- Jian Yang
- Xu Wang
- Xincan Wang
- Weiming Dong
affiliations:
- School of AI, University of Chinese Academy of Sciences
- Renmin University of China
- Shanghai Theatre Academy
- MAIS, Institute of Automation, Chinese Academy of Sciences
arxiv_id: '2610.02045'
url: https://arxiv.org/abs/2610.02045
pdf_url: https://arxiv.org/pdf/2610.02045
published: '2026-10-01'
collected: '2026-10-03'
category: Agent
direction: 多模态Agent · 视觉正负空间构图生成
tags:
- Multimodal Agent
- MLLM
- Visual Composition
- Text-to-Image
- Autonomous Agent
one_liner: 提出分阶段生成正负空间语义对齐视觉构图的多模态Agent FaV-A，性能优于零样本MLLM基线
practical_value: '- 复杂生成任务的多步Agent拆解workflow可复用：先生成基础元素、再分析结构推导关联语义、最后输出生成指令，适合电商复杂营销素材生成场景

  - 正负空间语义对齐的设计思路可迁移到电商海报/信息流广告设计，提升素材创意层次感与信息传递效率

  - 无需微调现有MLLM/T2I模型，仅通过Agent编排即可提升复杂生成任务效果，降低业务侧大模型落地成本'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
正负空间是视觉构图的核心原则，需协同控制共享边界的两个语义概念生成，现有T2I模型、MLLM通过单轮prompt很难生成视觉连贯、语义对齐的正负空间构图作品。
### 方法关键点
提出多模态Agent FaV-A，采用三阶渐进式工作流：1. 基于输入主题生成基础正空间对象；2. 分析对象形状与空间结构，推导匹配的负空间语义概念；3. 输出结构化构图指令调用生成模型，得到最终虚实交织的作品。
### 关键结果
实验显示FaV-A生成的正负空间构图在视觉一致性、语义对齐度上均优于零样本MLLM直接生成基线，消融实验验证了三阶工作流各模块的必要性
