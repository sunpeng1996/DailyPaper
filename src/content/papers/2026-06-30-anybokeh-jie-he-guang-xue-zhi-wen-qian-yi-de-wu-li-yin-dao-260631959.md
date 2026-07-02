---
title: 'AnyBokeh: Physics-Guided Any-to-Any Bokeh Editing with Optical Fingerprint
  Transfer'
title_zh: AnyBokeh：结合光学指纹迁移的物理引导任意散景编辑框架
authors:
- Xinyu Hou
- Xiaoming Li
- Zongsheng Yue
- Chen Change Loy
affiliations:
- Nanyang Technological University
- S-Lab, College of Computing & Data Science
arxiv_id: '2606.31959'
url: https://arxiv.org/abs/2606.31959
pdf_url: https://arxiv.org/pdf/2606.31959
published: '2026-06-30'
collected: '2026-07-02'
category: Other
direction: 计算摄影 · 物理引导散景编辑
tags:
- ComputationalPhotography
- BokehEditing
- PhysicsGuidedModeling
- OpticalFingerprint
- GenerativeImageEditing
one_liner: 提出物理引导的任意散景编辑框架，无需全焦重建即可实现跨焦距光圈的可控散景编辑
practical_value: 主要是学术贡献，业务可借鉴点有限
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
单张图像拍摄后散景编辑难度高，现有方法普遍要求输入为全焦图或先重建全焦图再渲染散景，会丢失原始图像的有效模糊线索，还会将重建伪影传播到最终结果，且需要测试时散景等级校准。
### 方法关键点
1. 不将原始模糊视为待消除的退化，先估计带符号的弥散圆（CoC）图与视差图，建模带符号CoC与视差差的线性关系，提取源图像专属光学指纹，实现光学特征向目标焦距、光圈参数迁移；
2. 基于源、目标CoC图作为条件的生成编辑器，完成空间自适应的去模糊、模糊保留、虚化渲染；
3. 构建带精确深度、对焦距离、全量EXIF元数据的高保真合成数据集，支撑物理监督训练。
### 关键结果
在真实世界基准测试中，任意散景编辑、全焦转散景、散景去模糊任务上均实现高保真可控编辑，无需全焦重建与测试时散景校准，效果优于现有方法。
