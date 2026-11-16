---
title: 'JVT: Just Video Transformer makes pixel-space video diffusion simple'
title_zh: JVT：基于纯Transformer的简化像素空间视频扩散模型
authors:
- Jianjun Zhou
- Hua Geng
- Haoyu Guo
affiliations:
- Zhejiang University
- Shanghai Innovation Institute
- Shanghai AI Laboratory
arxiv_id: '2611.18549'
url: https://arxiv.org/abs/2611.18549
pdf_url: https://arxiv.org/pdf/2611.18549
published: '2026-11-12'
collected: '2026-11-16'
category: Multimodal
direction: 多模态生成 · 视频扩散架构优化
tags:
- Video Diffusion
- DiT
- Pixel-space Generation
- Transformer
- Multimodal Generation
one_liner: 提出无额外冗余组件的DiT风格JVT架构，像素空间视频生成效果媲美隐空间扩散基线，支持多模态联合生成
practical_value: '- 电商商品展示、营销短视频生成场景可复用JVT的简化DiT架构，无需预训练自编码器即可直接生成像素级视频，降低部署链路复杂度

  - 虚拟逛店、3D商品交互展示场景可借鉴其像素对齐多模态联合生成能力，同时输出RGB视频与深度图，无需额外重构模型即可生成3D点云，降低交互内容生产成本

  - 内容推荐场景下的AIGC内容生产链路可参考其架构精简思路，砍掉U-Net跳跃连接、级联阶段等冗余组件，平衡生成质量与推理效率，降低批量生成内容的算力成本'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
高维原始视频直接扩散建模难度高，现有像素空间生成方法依赖复杂专用架构，组件冗余导致部署与迭代成本较高。
### 方法关键点
1. 采用大patch DiT风格Transformer搭建JVT，无需预训练自编码器、辅助细化器、级联阶段、U-Net跳跃连接等额外组件；
2. 系统性调优视频patch embedding、register token、自适应层归一化的设计策略，平衡生成质量与计算效率；
3. 像素空间原生设计天然支持像素对齐的多模态联合生成。
### 关键结果
1. 类条件、无条件视频生成场景下，质量与隐空间扩散基线相当；
2. 相机条件下RGB-视差联合生成相比仅RGB基线相机跟随效果更优，推理阶段无需额外重构模型即可输出显式场景几何信息
