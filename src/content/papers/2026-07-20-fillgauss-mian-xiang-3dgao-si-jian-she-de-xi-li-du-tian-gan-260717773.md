---
title: 'FillGauss: Fine-Grained Filling-Aware Impact Sound Generation for 3D Gaussian
  Splatting'
title_zh: FillGauss：面向3D高斯溅射的细粒度填充感知撞击声生成
authors:
- Chen Yang
- Ganye Wen
- Bin Huang
- Jiayi Lyu
- Zehai Niu
- Linlin Shen
- Jinbao Wang
arxiv_id: '2607.17773'
url: https://arxiv.org/abs/2607.17773
pdf_url: https://arxiv.org/pdf/2607.17773
published: '2026-07-20'
collected: '2026-07-26'
category: Multimodal
direction: 多模态跨模态生成 · 3D音频合成
tags:
- 3D Gaussian Splatting
- Latent Diffusion Model
- Cross-Modal Synthesis
- Impact Sound Generation
- Multimodal Learning
one_liner: 提出填充感知3D高斯撞击声生成框架及配套多模态数据集，达物理约束跨模态音频生成SOTA
practical_value: '- 电商3D商品互动展示场景可借鉴多条件融合逻辑，为商品叠加符合物理规则的敲击/互动音效，提升用户浏览沉浸感

  - 多模态生成任务可复用「3D特征+空间坐标+文本物理条件」的多控制信号融合latent diffusion架构设计

  - 做物理规则约束的生成任务时，可参考其数据集验证思路，先验证采集数据符合物理规律再开展建模'
score: 4
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有3D感知音频生成方法仅建模空心刚体的表面几何特征，完全忽略会显著调制声学共振、阻尼效果的内部填充状态，无法生成符合真实物理规律的撞击声，难以满足VR、互动场景的多感官真实感需求。
### 方法关键点
1. 定义细粒度填充感知撞击声生成新任务，构建FillImpact多模态数据集：包含88类真实物体、超5000条严格采集的声学记录，覆盖不同填充物类型、连续填充程度、不同撞击物材质，且经声学验证符合共振、阻尼等物理规律。
2. 提出FillGauss生成框架：在latent diffusion架构中融合3DGS几何特征、精确3D撞击坐标、细粒度文本物理条件，支持位置感知、撞击物感知、填充状态感知的音频生成。
### 关键结果
生成的高保真撞击声完全符合底层物理原理，在物理约束跨模态音频生成任务上达到新SOTA。
