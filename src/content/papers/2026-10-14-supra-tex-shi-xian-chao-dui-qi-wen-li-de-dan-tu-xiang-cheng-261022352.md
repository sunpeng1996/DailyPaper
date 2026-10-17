---
title: 'SUPRA-TEX: 3D Generation with Super-Aligned Texture'
title_zh: SUPRA-TEX：实现超对齐纹理的单图像3D生成方法
authors:
- Chen Yang
- Jiemin Fang
- Fanpeng Meng
- Zihao Huang
- Jichen Pang
- Guanjun Wu
- Zhikuan Bao
- Qi Tian
affiliations:
- Huawei Inc.
- Shanghai Jiao Tong University
- Huazhong University of Science and Technology
arxiv_id: '2610.22352'
url: https://arxiv.org/abs/2610.22352
pdf_url: https://arxiv.org/pdf/2610.22352
published: '2026-10-14'
collected: '2026-10-17'
category: Other
direction: 3D生成 · 超对齐纹理生成
tags:
- 3D_Generation
- Texture_Generation
- MLLM
- Flow_Transformer
- VAE
- PBR_Map
one_liner: 提出解耦式超对齐3D纹理生成框架SUPRA-TEX，单图3D材质生成效果超主流商业系统
practical_value: '- 电商商品3D建模场景可复用解耦式处理思路：先提取参考图PBR材质再做投影对齐，大幅降低3D商品建模的人工成本

  - 多模态生成中锚定固定可见区域做补全的思路可迁移至AIGC商品图生成/修复场景，避免品牌Logo、参数文字等关键细节丢失

  - MLLM做图像材质解析、流Transformer做隐空间补全的架构组合可复用至多模态内容生成任务，提升生成内容与输入的匹配度'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
单图像3D生成现有方案存在多视图预测融合伪影、隐式特征约束难以保留细粒度视觉细节的问题，无法满足电商商品数字化、具身AI对参考图外观高保真还原的需求。
### 方法关键点
1. 采用三模块解耦架构：分别负责可见材质估计、表面对齐、观测引导的3D补全，降低有限3D训练数据下的模型学习压力
2. 先基于MLLM图像编辑模型预测参考视图的光照分离PBR材质图，投影到可见表面后经预训练材质VAE编码为与生成目标同空间的观测隐向量
3. 用交错流Transformer将观测隐向量作为固定只读锚点，交替更新未观测区域与全表面生成完整材质隐向量
### 关键结果
仅用公开数据集训练，在几何条件纹理生成、端到端资产生成任务上达到SOTA，野生图像效果匹配甚至超越头部商业系统
