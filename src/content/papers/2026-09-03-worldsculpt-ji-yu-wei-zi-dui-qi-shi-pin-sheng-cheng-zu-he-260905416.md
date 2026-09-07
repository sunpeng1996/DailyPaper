---
title: 'WorldSculpt: Generating Compositional Worlds from Grounded Videos'
title_zh: WorldSculpt：基于位姿对齐视频生成组合式3D世界表示
authors:
- Muyao Niu
- Jixuan He
- Ruihan Yu
- Lian Fu
- Yonghao Yu
- Zheng-Hui Huang
- Yifan Zhan
- Fengbo Lan
- Yongtao Ge
- Yinqiang Zheng
affiliations:
- Alaya Lab
- The University of Tokyo
arxiv_id: '2609.05416'
url: https://arxiv.org/abs/2609.05416
pdf_url: https://arxiv.org/pdf/2609.05416
published: '2026-09-03'
collected: '2026-09-07'
category: Multimodal
direction: 多模态3D场景组合式生成
tags:
- 3D_Generation
- Multi_View_Reconstruction
- Generative_Prior
- 3D_Benchmark
- Scene_Reconstruction
one_liner: 适配单物体3D生成先验实现高遮挡复杂场景的组合式3D重建，配套发布高密度场景基准
practical_value: '- 可复用「单物体生成先验适配多视角观测」的思路，优化电商3D商品建模效率，无需全场景标注即可生成完整商品3D网格，降低3D内容制作成本

  - 针对多物体遮挡严重的场景重建需求，可借鉴该组合式生成范式，降低AR购物、虚拟卖场的3D场景构建成本，提升场景还原度

  - UE-MeshyScene的逐物体标注思路可复用，用于构建电商3D商品/场景评测数据集，统一3D内容生成效果的评估标准'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有几何类3D重建方法在密集遮挡场景下易出现几何残缺，带生成先验的组合式重建方法仅支持简单场景，无法满足AR/VR、虚拟场景等下游对多物体组合式3D表示的需求。
### 方法关键点
1. 适配强单物体3D生成先验Pixal3D，扩展多视角条件通路，基于多个位姿对齐的观测生成物体3D网格；
2. 仅在规范空间的单物体数据上微调，无需场景级训练即可泛化到高遮挡复杂大场景；
3. 开源UE-MeshyScene基准，包含数百物体的高密度写实场景、逐物体标注和真值网格。
### 关键结果
在单物体、可控多物体、UE-MeshyScene三类测试集上均优于现有方法，场景复杂度、遮挡程度越高性能增益越大，还支持将3DGS生成的世界转换为组合式网格场景
