---
title: 'MetaRefine: Score Refinement with Multi-Level Features for Image Assessment'
title_zh: MetaRefine：基于多层特征的图像评估分数优化方法
authors:
- Chuanzhi Xu
- Chengkun Yue
- Haolan Guo
- Xuanhua Yin
- Boyu Wei
- Zihan Deng
- Qiang Qu
- Weidong Cai
affiliations:
- The University of Sydney
- Indiana University
- The University of Hong Kong
arxiv_id: '2610.40487'
url: https://arxiv.org/abs/2610.40487
pdf_url: https://arxiv.org/pdf/2610.40487
published: '2026-10-29'
collected: '2026-10-31'
category: Other
direction: 图像评估 · 轻量分数修正架构
tags:
- Image Assessment
- Score Refinement
- Multi-level Features
- Metadata-aware
- Lightweight Module
one_liner: 提出元数据感知的轻量残差修正模块，无需改动原评分管线即可提升图像评估模型性能
practical_value: '- 电商商品主图/广告素材质量评估场景，可复用该轻量修正思路，不改动现有成熟评估管线的前提下提升打分准确率

  - 所有需要分数后优化的排序/打分场景，都可以参考这种用元数据+原模型中间层特征+原始分数做残差预测的范式，参数量开销极低

  - 多模态推荐的物料质量过滤模块可直接引入该架构，补足图像缩放/裁剪丢失的原始几何、构图特征损失'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有图像评估方法为适配固定输入尺寸，会对原图做缩放、裁剪、填充等操作，丢失原始几何尺寸、构图等核心质量相关特征；同时现有评估模型编码的多层视觉特征未被充分利用，缺少不改动原有评分管线的分数优化方案。

### 方法关键点
提出MetaRefine元数据感知的轻量分数修正架构，冻结原有图像评估模型，仅新增极小的残差预测头，输入三类信息：原图几何元数据、原模型输出的多层视觉特征、原模型输出的初始评分，直接预测分数修正值得到最终优化评分。

### 关键结果
在21个数据集的100种配置下，88%配置PLCC提升、85%配置SRCC提升，平均相对涨幅分别为7.55%、7.10%；90%配置MAE下降、89%配置RMSE下降，平均相对降幅分别为23.27%、21.93%，中位数参数量 overhead仅1.11%
