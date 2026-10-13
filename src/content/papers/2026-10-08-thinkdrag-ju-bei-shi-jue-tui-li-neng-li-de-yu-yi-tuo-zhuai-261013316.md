---
title: 'ThinkDrag: Semantic Drag-Based Image Editing with Visual Reasoning'
title_zh: ThinkDrag：具备视觉推理能力的语义拖拽图像编辑方法
authors:
- Armando Fortes
- Tianyi Wei
- Chindanai Trakantannarong
- Shangchen Zhou
- Xingang Pan
affiliations:
- S-Lab, Nanyang Technological University, Singapore
arxiv_id: '2610.13316'
url: https://arxiv.org/abs/2610.13316
pdf_url: https://arxiv.org/pdf/2610.13316
published: '2026-10-08'
collected: '2026-10-13'
category: Multimodal
direction: 多模态生成 · 可控图像编辑
tags:
- Multimodal Generation
- Image Editing
- Visual Reasoning
- Controllable Generation
- Generative AI
one_liner: 提出融合视觉推理的多模态拖拽图像编辑框架ThinkDrag，可输出编辑推理轨迹，生成质量达SOTA
practical_value: '- 电商商品图快速改场景/调姿态场景可复用语义拖拽逻辑，替代纯文本引导编辑解决空间控制精度不足问题

  - 模糊用户意图的交互生成场景可借鉴「先输出推理轨迹再生成」的范式，提升生成结果可解释性和用户满意度

  - 多模态交互任务可复用Drag Endpoint Markers设计，给稀疏交互信号增加显式空间对应约束，提升生成准确率'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有拖拽式图像编辑方法仅将用户拖拽指令解析为几何位移，无法结合图像内容语义推断合理变换，在需要语义理解的复杂编辑场景效果受限。
### 方法关键点
1. 提出统一多模态框架ThinkDrag，将点约束关联到对象/场景级语义变换，支持在生成前输出显式推理轨迹解释编辑意图，解决模糊拖拽的歧义问题；
2. 基于跨图像注意力分析设计Drag Endpoint Markers，提供显式空间对应信号，锚定拖拽操作在图像空间的位置；
3. 构造带推理轨迹标注的语义拖拽变换监督数据集，推出面向复杂拖拽编辑场景的基准DragBench++。
### 关键结果
实验达到SOTA性能，生成质量与语义合理性显著提升，同时保持有竞争力的点跟随精度。
