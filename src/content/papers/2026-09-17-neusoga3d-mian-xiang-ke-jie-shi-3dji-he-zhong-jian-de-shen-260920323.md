---
title: 'NeuSOGA3D: A Neuro-Symbolic Framework for Explainable 3D Geometric Reconstruction'
title_zh: NeuSOGA3D：面向可解释3D几何重建的神经符号混合框架
authors:
- Qingde Li
- Qingqi Hong
- Zihan Li
- Jie Tian
arxiv_id: '2609.20323'
url: https://arxiv.org/abs/2609.20323
pdf_url: https://arxiv.org/pdf/2609.20323
published: '2026-09-17'
collected: '2026-09-18'
category: Other
direction: 3D几何重建 · 神经符号混合建模
tags:
- Neuro-Symbolic
- 3D Reconstruction
- Point Cloud
- Geometric Modeling
- Explainable AI
one_liner: 提出融合神经感知先验与符号几何推理的3D点云重建框架，输出CAD兼容的可解释几何表征
practical_value: '主要是学术贡献，电商/推荐/Agent领域通用业务可借鉴点有限，若涉及3D数字商品建模场景可参考：

  - 可复用「神经感知先验+显式符号推理」的混合架构思路，平衡生成效果与输出可解释性

  - 符号化输出可直接对接CAD等工业流程，能大幅降低3D内容落地的后处理成本'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有神经隐式3D点云重建方法精度较高，但几何信息被编码在隐层表征中，可解释性差，无法直接适配工程设计工作流复用。
### 方法关键点
1. 采用混合架构融合NeuSOGA的感知先验与显式符号几何推理能力：先将点云投影到主正交平面，生成符号隐式样条表征，通过保形构造实体几何操作融合得到粗粒度视觉外壳；
2. 采用部分保形样条做横截面分解与体素重建，补充缺失的几何细节；
3. 全流程将输入逐步转换为控制多边形、隐式样条场、横截面、体素放样等显式符号实体，天然具备可解释性。
### 关键结果
在ModelNet40基准全40类数据上验证，可从各类点云输入中恢复结构语义明确、CAD兼容的几何表征。
