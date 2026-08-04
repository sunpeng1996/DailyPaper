---
title: 'CoDe-SSM: Context-Detail Decoupled State Space Model for Efficient UHD Image
  Restoration'
title_zh: 面向高效超高清图像恢复的上下文-细节解耦状态空间模型CoDe-SSM
authors:
- Jiaxu Su
- Zhijian Wu
- Jun Li
- Bo Zhang
- Yefeng Zheng
affiliations:
- School of Computer and Electronic Information, Nanjing Normal University
- Medical Artificial Intelligence Laboratory, Westlake University
arxiv_id: '2607.29595'
url: https://arxiv.org/abs/2607.29595
pdf_url: https://arxiv.org/pdf/2607.29595
published: '2026-07-31'
collected: '2026-08-04'
category: Other
direction: 超高清图像恢复 · SSM架构优化
tags:
- SSM
- UHD Image Restoration
- Feature Decoupling
- Mixture of Experts
- Efficient Inference
one_liner: 提出上下文-细节双通路解耦SSM架构，平衡超高清图像恢复的效果与计算效率
practical_value: '- 可复用上下文-细节解耦设计思路，优化电商商品UHD主图超分、去噪、去雾等画质修复pipeline，平衡推理效率与细节保留效果

  - 全局聚类降维+SSM建模的方案可迁移至高分辨率内容特征的全局关联计算场景，降低高分辨率特征处理时延

  - 稀疏卷积MoE处理高频残差的trick可复用至需要保留边缘/纹理细节的图像生成/修复任务，减少细结构损耗'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
UHD图像恢复需平衡全局退化特征聚合效率与局部纹理/边缘等细节保留，现有降采样、窗口分割等降本方案易丢失共享聚合无法覆盖的细粒度信息，无法同时兼顾效果与算力成本。
### 方法关键点
1. 双通路解耦架构：分开处理聚合上下文与聚类残差
2. 上下文通路（GCSM模块）：将特征聚合为K个输入依赖的聚类中心，对固定长度序列做选择性SSM推理，实现跨区域上下文共享且算力成本与空间分辨率解耦
3. 细节恢复通路（LHFM模块）：用输入衍生的高频掩码+稀疏卷积MoE处理聚类残差，保留局部细结构
### 关键结果
在5个UHD基准数据集、5种退化类型上验证，解耦策略在保持理想效率的同时，恢复质量获得显著提升
