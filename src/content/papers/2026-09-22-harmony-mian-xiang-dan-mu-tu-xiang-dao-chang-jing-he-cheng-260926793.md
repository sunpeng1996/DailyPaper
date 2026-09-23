---
title: 'HARMONY: Hierarchical Agentic Reasoning for MONocular Image-to-Scene Synthesis'
title_zh: HARMONY：面向单目图像到场景合成的分层智能体推理
authors:
- Shufan Sun
- Chen Wang
- Enxin Song
- Jiatao Gu
- Lingjie Liu
affiliations:
- University of Pennsylvania
arxiv_id: '2609.26793'
url: https://arxiv.org/abs/2609.26793
pdf_url: https://arxiv.org/pdf/2609.26793
published: '2026-09-22'
collected: '2026-09-23'
category: MultiAgent
direction: 多模态多智能体 · 3D场景生成
tags:
- Agentic Reasoning
- VLM
- 3D Reconstruction
- Chain-of-Thought
- Multimodal
one_liner: 提出分层CoT框架HARMONY，融合Agent推理与视觉几何模型实现高精度单目图像3D场景合成
practical_value: '- 分层推理+反思反馈闭环的架构可迁移至多模态Agent任务，比如电商虚拟家居搭配、AR试穿场景的物品布局生成，有效避免误差累积

  - 先语义推理后几何校验的两阶段范式，可复用在商品素材的3D重建pipeline中，大幅提升生成3D内容与实拍图的对齐精度

  - 按依赖优先级（固定大件→附属小件）的生成顺序，可借鉴到家居、3C类目的场景化推荐搭配生成任务中，优化搭配合理性'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有单目3D场景重建存在两类技术短板：Agent推理方案空间语义理解能力强但与输入图像对齐精度低，视觉几何基础模型可生成稠密点云但重建质量受限，同时保证对象间关系准确、重建保真度高的单目3D场景恢复难度大。

### 方法关键点
分层CoT框架HARMONY流程如下：1）先基于参考图像校准相机建立语义空间坐标系，通过VLM Agent推理得到3D房间布局与初始放置顺序；2）按壁挂组件→独立家具→附属装饰的分层优先级放置对象，搭配深度优先遍历与反思反馈环避免误差累积；3）每次对象放置后用点云估计做几何层面精调，保证渲染图与输入对齐。

### 关键结果
在合成与真实图像数据集上效果优于所有参测重建基线，对比GPT-6 Astra生成的对象布局更贴合真实场景、场景细节保留度更高。
