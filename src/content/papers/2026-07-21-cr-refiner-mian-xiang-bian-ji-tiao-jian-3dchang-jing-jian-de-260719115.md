---
title: 'CR-Refiner: An Object-Centric Optimal Transport Reranker for Edit-Conditioned
  3D Scene Retrieval'
title_zh: CR-Refiner：面向编辑条件3D场景检索的物体中心最优传输重排器
authors:
- Hao Wu
- Jinjing Zhu
- Nanyu Wu
- Qianyi Cai
- Heyi Lin
- Hao Wang
- Hui Xiong
affiliations:
- Hong Kong University of Science and Technology
- Hong Kong University of Science and Technology (Guangzhou)
arxiv_id: '2607.19115'
url: https://arxiv.org/abs/2607.19115
pdf_url: https://arxiv.org/pdf/2607.19115
published: '2026-07-21'
collected: '2026-07-23'
category: Other
direction: 3D场景检索 · 免训练重排优化
tags:
- Reranker
- Optimal Transport
- LLM
- 3D Retrieval
- Training-Free
one_liner: 提出免训练编辑条件3D场景检索重排器CR-Refiner，配套发布专用评测基准3D-CER
practical_value: '- 可复用「基础召回TopK + 冻结LLM结构化解析 + 轻量多维度匹配 + 小范围LLM校验」的免训练重排架构，降低电商多条件检索、个性化推荐重排模块的训推成本

  - 非平衡最优传输的非对称匹配方法可迁移到用户带修改条件的搜索场景，例如「把这款布艺沙发换成同尺寸皮质款」类需求的召回排序，天然过滤无关特征维度

  - 不同编辑维度注入对应结构化先验的技巧可直接复用，例如给空间类查询加位置锚点、给属性类查询加属性权重，无需额外训练即可提升细粒度匹配准确率'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有编辑条件3D场景检索方案存在明显短板：2D组合检索无3D物体集合处理能力，3D基础编码器无法完成场景级特征组合，3D场景grounding仅支持单静态场景内定位、无跨库排序能力，且行业缺乏对应评测基准。

### 方法关键点
免训练重排架构可适配任意基础召回器的TopK结果：1. 用冻结LLM将自然语言编辑指令解析为结构化查询实体；2. 基于类别、风格、材质、几何4个维度构建成本矩阵，通过非平衡最优传输计算匹配分，天然过滤无关物体适配非对称匹配逻辑；3. 加入轴条件结构先验增强几何/空间类编辑的匹配效果，最后用LLM对Top3结果做置信度校验。同时发布3D-CER评测基准，包含4963个编辑条件查询、23381个室内场景，覆盖5类编辑维度。

### 关键结果
在3种架构差异显著的基础召回器上，所有编辑维度的难例子集R@1、mAP@10均获得稳定提升。
