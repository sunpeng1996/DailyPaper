---
title: 'SCULPT: Subtractive Composition for 3D Part Generation'
title_zh: SCULPT：基于减法合成的3D部件生成框架
authors:
- Sikuang Li
- Chen Yang
- Jiemin Fang
- Jiazhong Cen
- Yuhe Wei
- Jichen Pang
- Wei Shen
- Qi Tian
affiliations:
- Shanghai Jiao Tong University
- Huawei
arxiv_id: '2608.13541'
url: https://arxiv.org/abs/2608.13541
pdf_url: https://arxiv.org/pdf/2608.13541
published: '2026-08-13'
collected: '2026-08-15'
category: Other
direction: 3D内容生成 · 部件感知生成
tags:
- 3D Generation
- Part-aware Generation
- Denoising
- Latent Space
- Digital Asset
one_liner: 提出减法合成的3D部件生成方案，解决现有方法边界不连续、结构割裂问题
practical_value: '- 电商3D商品素材生产可借鉴减法拆分思路，自动拆分商品可编辑部件，降低建模后二次编辑成本

  - 多输出联合预测的耦合denoising思路可迁移至多模态内容生成任务，避免拆分后结果不匹配问题

  - 自适应终止的迭代生成逻辑可复用至分层内容生成场景，无需预设拆分数量，适配不同对象复杂度'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
Part-aware 3D生成是数字资产生产的核心需求，现有两类方案均存在缺陷：分割类方法生成完整几何后再拆分，部件边界确定滞后；加法合成类方法先生成独立部件再拼接，易出现边界缝隙、穿插、材质不连续问题。

### 方法关键点
提出SCULPT减法合成框架，基于结构化3D隐空间的完整对象，迭代调用联合拆分预测器，同步生成拆分出的部件与剩余对象；采用耦合denoising，同时对齐输入图像与当前3D状态，拆分与剩余内容共享稀疏3D支撑域，允许边界重叠而非强制体素disjoint划分；迭代过程自适应终止，无需预设部件数量。

### 关键结果
在PartObjaverse数据集上取得SOTA几何生成效果，部件拼接后完整对象重建精度领先；支持数据集图像、文生图输出、真实照片输入的细粒度带纹理部件拆分，效果超现有基准。
