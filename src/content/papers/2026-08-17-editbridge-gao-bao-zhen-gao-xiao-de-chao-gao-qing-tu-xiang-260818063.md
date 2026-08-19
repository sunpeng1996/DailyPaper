---
title: 'EDITBRIDGE: Towards Faithful and Efficient Ultra-High-Resolution Image Editing'
title_zh: EditBridge：高保真高效的超高清图像编辑框架
authors:
- Jiayi Song
- Shijie Huang
- Fangtai Wu
- Yubo Huang
- Zhenxiong Tan
- Songhua Liu
- Jiaming Liu
- Ruihua Huang
affiliations:
- Shanghai Jiao Tong University
- Qwen Business Unit of Alibaba
- National University of Singapore
arxiv_id: '2608.18063'
url: https://arxiv.org/abs/2608.18063
pdf_url: https://arxiv.org/pdf/2608.18063
published: '2026-08-17'
collected: '2026-08-19'
category: Multimodal
direction: 多模态超高清图像内容编辑优化
tags:
- Diffusion
- Image Editing
- Sparse Attention
- High Resolution
- Generative Content
one_liner: 提出带先验引导块稀疏注意力的扩散桥框架，实现4K分辨率高保真高效图像编辑
practical_value: '- 电商商品主图/详情页高清修图可复用两阶段编辑+原高清图源约束的框架，避免低清编辑放大后的失真问题，降本提效

  - 先验引导块稀疏注意力的设计思路可迁移至高分辨率多模态内容生成场景，大幅降低显存占用与推理时延

  - 扩散桥的数据到数据翻译范式可替代传统独立超分流程，适合广告素材批量高清化的业务需求，减少伪影'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：现有扩散图像编辑模型受注意力复杂度限制仅支持1K以下分辨率，行业通用的「低清编辑+独立超分」两阶段方案存在信息发散（生成细节与原高清源冲突）、纹理退化（过平滑/过锐化伪影）两大问题，无法满足超高清编辑需求。

**方法关键点**：1. 提出扩散桥EditBridge框架，将高清化任务定义为低清编辑结果到高清版本的结构化数据到数据翻译，显式引入原高清图源作为条件保留真实细节；2. 设计先验引导块稀疏注意力机制，利用第一阶段编辑的语义对应关系，将跨图像交互限制在空间对齐区域，大幅降低计算开销。

**关键结果**：支持最高4K分辨率高保真编辑，感知质量显著优于基线；2K分辨率下推理速度提升3.6~8.4倍，4K编辑仅需61秒
