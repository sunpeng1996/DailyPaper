---
title: 'SpaceFlow: Locally Controllable 3D Generation'
title_zh: SpaceFlow：支持局部可控的3D生成方法
authors:
- Neil De La Fuente
- Joan Lafuente
- Mukhammadali Sayfiddinov
- Felicia Scharitzer
- Marc Pollefeys
- Ata Celen
- Sayan Deb Sarkar
- Elisabetta Fedele
affiliations:
- ETH Zürich
- Stanford University
- Microsoft
arxiv_id: '2610.12399'
url: https://arxiv.org/abs/2610.12399
pdf_url: https://arxiv.org/pdf/2610.12399
published: '2026-10-07'
collected: '2026-10-10'
category: Other
direction: 可控3D生成 · 训练免微调管线
tags:
- 3D Generation
- Controllable Generation
- Training-Free
- Flow-based Generation
- Text-to-3D
one_liner: 提出无需训练的3D生成管线，支持局部几何、外观的自定义粒度控制
practical_value: '- 若业务涉及3D商品素材生成，可复用局部粒度控制方案，支持按商品部位指定几何约束、材质/颜色提示，降低素材定制成本

  - 训练免微调的约束注入思路可迁移至多条件可控生成场景，减少特定生成需求的微调数据量与训练成本

  - 跨部件信息泄漏抑制方法可复用至分区多提示生成任务，避免不同区域的生成条件互相干扰'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有3D生成方法缺乏显式局部控制能力，几何遵循度仅支持全局统一设置，也无法针对局部区域单独指定外观属性，无法满足精细化定制生成需求。

### 方法关键点
1. 构建训练-free的SpaceFlow管线，支持基于文本描述+几何基元输入的局部可控3D生成，每个几何基元对应物体部件，可单独分配控制等级，区分「严格遵循输入形状」/「自由生成」两类区域；
2. 结构生成阶段在生成流过程中注入空间约束保证控制规则生效；外观合成阶段先将生成结构做分割匹配到对应基元，每个部件仅对应当前分配的文本/图像提示，抑制跨部件信息泄漏。

### 关键结果
高控制区域几何保留度达标，低控制区域生成形状合理性达标；固定几何下的外观生成达到SOTA的提示忠实度与颜色/材质准确率；用户调研显示其几何保真度与生成自由度的平衡效果整体质量具备竞争力。
