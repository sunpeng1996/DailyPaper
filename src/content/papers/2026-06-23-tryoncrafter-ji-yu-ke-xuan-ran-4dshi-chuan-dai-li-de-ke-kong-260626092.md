---
title: 'TryOnCrafter: Unleashing Camera Trajectories for Realistic Video Virtual Try-on
  via a Renderable 4D Try-on Proxy'
title_zh: TryOnCrafter：基于可渲染4D试穿代理的可控视角视频虚拟试穿
authors:
- Hao Sun
- Hao Yan
- Mengting Chen
- Quanjian Song
- Yu Li
- Juan Cao
- Jinsong Lan
- Xiaoyong Zhu
- Bo Zheng
- Sheng Tang
affiliations:
- 中国科学院计算技术研究所
- 中国科学院大学
- 厦门大学
- 阿里巴巴集团
arxiv_id: '2606.26092'
url: https://arxiv.org/abs/2606.26092
pdf_url: https://arxiv.org/pdf/2606.26092
published: '2026-06-23'
collected: '2026-06-27'
category: Multimodal
direction: 多模态生成 · 电商视频虚拟试穿
tags:
- Virtual Try-on
- 4D Gaussian Splatting
- Diffusion Transformer
- 3DGS
- SMPL-X
- Video Generation
one_liner: 首个DiT驱动的相机可控视频虚拟试穿框架，以4D代理为锚点实现任意视角试穿生成
practical_value: '- 电商服装类商品详情页/直播间可复用「4D试穿代理+Video DiT」架构，替代传统像素级虚拟试穿方案，支持用户自由切换视角查看试穿效果，提升转化

  - 可借鉴2D试穿先验蒸馏到3DGS穿衣化身的方法，大幅降低3D试穿内容制作成本，无需大量3D标注数据即可生成高保真试穿效果

  - 360°环绕查看、子弹时间特效等能力可直接复用到互动营销模块，提升用户停留时长与商品种草效率'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有视频虚拟试穿（VVT）方案完全依赖源视频的相机轨迹，无法支持用户自主切换视角的交互需求，难以满足电商场景下用户多维度查看服装试穿效果的诉求。
### 方法关键点
1. 首次定义相机可控视频虚拟试穿（CaM-VVT）任务，要求任意相机运动下同时保证视角无关纹理生成、非刚性人体动态与背景的结构同步
2. 提出首个DiT驱动的TryOnCrafter框架，引入可渲染4D试穿代理，将高保真2D试穿先验蒸馏到3DGS穿衣化身，通过SMPL-X序列驱动动画并对齐背景点云，实现人与环境解耦
3. 以4D代理为几何锚点训练Proxy-Anchored Video DiT，保证生成视频严格符合预设相机轨迹、形变符合物理规律
### 关键结果
支持任意未在源视频中出现的相机轨迹下的高保真试穿视频生成，可直接落地人体重定位、子弹时间特效、360°环绕查看等多类下游互动应用
