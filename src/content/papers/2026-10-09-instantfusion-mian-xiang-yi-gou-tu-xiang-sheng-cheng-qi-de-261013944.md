---
title: 'InstantFusion: A Shared Latent Interface for Heterogeneous Image Generators'
title_zh: InstantFusion：面向异构图像生成器的共享隐层接口
authors:
- Xuanlang Dai
- Jiazi Bu
- Yujie Zhou
- Yuhong Liu
- Beichen Zhang
- Penghui Yang
- Ziyu Liu
- Yuhang Zang
affiliations:
- 复旦大学
- 上海人工智能实验室
- 上海交通大学
- 香港中文大学
arxiv_id: '2610.13944'
url: https://arxiv.org/abs/2610.13944
pdf_url: https://arxiv.org/pdf/2610.13944
published: '2026-10-09'
collected: '2026-10-13'
category: Multimodal
direction: 多模态生成 · 异构模型隐层对齐
tags:
- Diffusion Model
- Latent Alignment
- Image Generation
- Model Fusion
- Latent AutoEncoder
one_liner: 提出轻量共享隐层接口实现异构图像生成器去噪轨迹无缝切换 无需两两配对训练映射
practical_value: '- 异构生成模型对齐可复用LAE架构，无需两两训练映射对，大幅降低电商多风格商品图生成的多模型组合工程成本

  - 共享隐空间的双约束目标（同噪声层级状态对齐、去噪速度同步）可直接迁移到推荐系统跨域用户/物品特征对齐任务

  - 冻结基座仅训练轻量适配模块的思路可复用在LLM4Rec多模型融合场景，显著降低大模型调优算力开销'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
当前扩散/流模型已成为图像生成事实范式，不同架构生成器的隐层表示跨模型对齐、去噪动力学一致性研究不足，但观测发现独立训练的生成器存在隐空间结构相似、中间态传递可保留粗粒度内容的兼容性。
### 方法关键点
引入模型专属Latent AutoEncoders（LAEs），将不同异构生成器的中间态投影到统一共享隐空间，再解码到目标生成器的隐空间；共享空间采用双约束优化：同图像同噪声层级的中间态对齐、对应局部去噪速度同步。
### 关键结果
训练完成后可在多个冻结生成器间无缝切换去噪流程，无需为每对模型单独训练映射，在生成加速、多偏好组合、跨架构蒸馏、跨模型组合任务上均达到竞争性性能
