---
title: 'GaussianRenderFormer: Transformer-based Rendering of 3D Gaussian Splats'
title_zh: GaussianRenderFormer：基于Transformer的3D高斯泼溅渲染框架
authors:
- Shahaf Valencia Levy
- Sagie Benaim
affiliations:
- The Hebrew University of Jerusalem
arxiv_id: '2611.05593'
url: https://arxiv.org/abs/2611.05593
pdf_url: https://arxiv.org/pdf/2611.05593
published: '2026-11-03'
collected: '2026-11-06'
category: Other
direction: 3D神经渲染 · 无光栅器Transformer实现
tags:
- 3D Gaussian Splatting
- Transformer
- Neural Rendering
- 3D Content Generation
- View Encoding
one_liner: 提出无光栅器的Transformer架构，实现端到端3D高斯泼溅神经渲染
practical_value: '- 若业务涉及3D商品展示、AR试穿、虚拟场景搭建，可复用其3D高斯转Token的Transformer编码设计，降低对传统光栅化渲染组件的依赖

  - 3D内容生成类业务可参考其视图无关编码器+视图相关解码器的架构，实现跨视角3D内容的统一建模与渲染

  - 纯推荐排序、Agent决策类业务无直接可迁移点，价值主要集中在3D内容生产链路'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有3D Gaussian Splatting（3DGS）渲染依赖手工开发的光栅器组件，无法端到端融入神经网络管线，亟需完全基于学习的无光栅器渲染方案。
### 方法关键点
1. 每个3D高斯被映射为独立Token，输入视图无关编码器完成全局特征编码；
2. 视图相关解码器以相机光线小片为输入，通过注意力机制查询编码器Token直接输出像素值，全程无光栅器参与；
3. 可额外注入高斯投影足迹信息降低解码器推理负担，进一步提升渲染效果。
### 关键结果
基于26820个裁剪为20000个高斯的Objaverse对象训练后，在300个未见对象上渲染PSNR达38.08dB，注入投影足迹后可提升1.4dB，当前与原始光栅化渲染的44.02dB仍有差距，瓶颈主要集中在视图解码器。
