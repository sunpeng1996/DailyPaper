---
title: 'Ink3D: Sculpting 3D Assets with Extremely Complex Textures via Video Generative
  Models'
title_zh: Ink3D：基于视频生成模型生成带极复杂纹理的3D资产
authors:
- Yue Han
- Chong Li
- Zhening Liu
- Cong Huang
- Fang Deng
- Yong Liu
- Fangyun Wei
- Yan Lu
affiliations:
- ZGCA & ZGCI
- Microsoft Research
- Zhejiang University
- HKUST
arxiv_id: '2607.01222'
url: https://arxiv.org/abs/2607.01222
pdf_url: https://arxiv.org/pdf/2607.01222
published: '2026-07-01'
collected: '2026-07-02'
category: Other
direction: 3D资产生成 · 复杂纹理合成
tags:
- 3D Generation
- Texture Synthesis
- Video Generative Model
- Multi-view Fusion
- Diffusion Model
one_liner: 提出几何纹理解耦的Ink3D框架，借助预训练视频生成模型实现高保真复杂3D纹理合成
practical_value: '- 可复用「几何生成-纹理生成解耦」架构，低成本生成电商3D商品素材，无需大量3D纹理标注数据

  - OrbitPainter多视角视频生成+TextureOptimizer纹理对齐的管线，可直接迁移到3D商品纹理修复、定制化纹理生成场景

  - 利用大模型预训练视觉先验补全下游小样本任务的思路，可借鉴到推荐系统稀缺样本的内容生成场景，比如小众商品素材生成'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有3D生成模型几何生成质量较高，但因带丰富表面信息的3D训练数据稀缺，很难还原参考图中的复杂纹理；而2D/视频生成模型训练数据规模大几个数量级，擅长建模复杂视觉模式，二者存在明显能力gap。

### 方法关键点
1. 解耦几何与纹理生成流程，先用成熟的开源3D生成模型得到无纹理白模几何；
2. 提出OrbitPainter条件视频生成模型，生成环绕物体的轨道扫描视频，覆盖全视角外观特征；
3. 提出TextureOptimizer神经烘焙模块，融合密集多视角观测结果，消除视频生成带来的几何不一致问题，输出连贯纹理。

### 关键结果
相比现有SOTA 3D生成方法，纹理还原的保真度、丰富度均显著提升，可复现衣物精细纹样、高分辨率装饰细节等复杂表面效果。
