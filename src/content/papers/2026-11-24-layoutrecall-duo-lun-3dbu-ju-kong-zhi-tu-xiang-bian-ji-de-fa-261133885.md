---
title: 'LayoutRecall: Preserving Appearance in Multi-Round 3D Layout-Controlled Image
  Editing'
title_zh: LayoutRecall：多轮3D布局控制图像编辑的外观保留方法
authors:
- Yankuan Chi
- Xin Lin
- Baihan Yang
- Yuheng Liu
- Jason Li
- Truong Nguyen
affiliations:
- University of California San Diego
- University of California Irvine
- Nanyang Technological University
arxiv_id: '2611.33885'
url: https://arxiv.org/abs/2611.33885
pdf_url: https://arxiv.org/pdf/2611.33885
published: '2026-11-24'
collected: '2026-11-28'
category: Multimodal
direction: 多模态生成 · 3D布局可控图像编辑
tags:
- Image Editing
- 3D Layout Control
- Memory Mechanism
- Diffusion Model
- Benchmark
one_liner: 提出基于3D框局部外观存储的多轮图像编辑框架LayoutRecall及配套基准LayoutLoop
practical_value: '- 电商3D商品展示、虚拟场景搭建场景可复用Box-Surface Latent Memory机制，保证多轮编辑下商品外观一致性

  - 多轮交互式营销素材编辑场景，可借鉴Geometry-Aligned Memory Conditioning对齐3D几何约束与外观特征

  - 自研多轮可控图像生成能力时，可直接使用LayoutLoop基准做效果验证，减少自建测试集成本'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
多轮3D布局控制图像编辑过程中，物体被遮挡或移出视野后再出现时，易出现外观不一致问题，现有方法无法从历史编辑记录中恢复原有物体外观，无法满足连续场景编辑需求。
### 方法关键点
1. 设计Box-Surface Latent Memory模块，将图像隐码存储在3D框的各个面上，目标视角下沿光线检索对应外观隐码
2. 提出Geometry-Aligned Memory Conditioning机制，将检索到的token结合目标视角位置、框局部嵌入、物体级注意力输入FLUX.2编辑器
3. 新增对应损失，引导去噪过程中编辑器关注匹配的历史观测；同时发布多轮3D布局编辑基准LayoutLoop，包含校准布局与物体重访设计
### 关键结果
在LayoutLoop基准及真实场景数据上，均验证了方法可稳定保留重新出现物体的历史外观，编辑一致性、布局准确率均显著优于现有基线方法
