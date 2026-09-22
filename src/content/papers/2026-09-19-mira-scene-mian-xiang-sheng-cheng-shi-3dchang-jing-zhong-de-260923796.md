---
title: 'Mira-Scene: Pixel-Aligned Layouts for Generative 3D Scene'
title_zh: Mira-Scene：面向生成式3D场景重建的像素对齐布局框架
authors:
- Yang-Tian Sun
- Tianjia Liu
- Zehuan Huang
- Yi-Hua Huang
- Xiaoyang Lyu
- Ziyi Yang
- Zi-Xin Zou
- Yuan-Chen Guo
- Yan-Pei Cao
- Xiaojuan Qi
affiliations:
- The University of Hong Kong
- VAST
arxiv_id: '2609.23796'
url: https://arxiv.org/abs/2609.23796
pdf_url: https://arxiv.org/pdf/2609.23796
published: '2026-09-19'
collected: '2026-09-22'
category: Other
direction: 生成式3D场景 · 像素对齐布局重建
tags:
- 3D_Generation
- Diffusion_Transformer
- Layout_Reconstruction
- Pixel_Alignment
- Multimodal_Generation
one_liner: 提出像素对齐规范坐标映射，实现无需场景级标注的高精度3D场景重建
practical_value: '- 多模态Diffusion Transformer的模态专属专家流+共享注意力/位置编码设计，可迁移至多模态生成任务保证跨模态输出一致性

  - 用有界空间稠密对应替代稀疏回归的思路，可借鉴至推荐系统稀疏行为的稠密表征建模，降低标注依赖

  - 仅需对象级数据、无需全局场景标注的训练范式，可复用至电商3D商品场景搭建等缺全局标注的业务'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
当前单图像3D生成已能产出高保真资产，但全局场景布局对齐仍存在瓶颈：整体式方法牺牲对象级细节，组合式方法用稀疏无界姿态变量表征布局，学习难度高、缺场景级标注时泛化性差。

### 方法关键点
1. 提出组合式3D场景重建框架Mira-Scene，用稠密有界对应恢复替代稀疏姿态回归；
2. 核心引入像素对齐的Canonical Coordinate Map（CCM），将可见对象像素映射到对象有界规范空间的表面坐标，搭配单目几何估计得到的Point Cloud Map（PCM），通过几何对齐恢复对象变换，仅需对象级3D数据即可训练，无需场景级布局标注；
3. 新增多模态扩散Transformer，联合生成对象几何与CCM，采用模态专属专家流+共享注意力/位置编码保证几何与布局一致性。

### 关键结果
在室内、室外、合成、真实场景实验中，布局精度大幅优于基线，较SAM3D的3D-IoU相对提升39.8%，2D-IoU相对提升16.5%，仅使用有限开源训练数据。
