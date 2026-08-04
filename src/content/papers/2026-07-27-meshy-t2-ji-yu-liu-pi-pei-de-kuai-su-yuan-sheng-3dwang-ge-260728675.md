---
title: 'Meshy T2: Fast Native Mesh Generation with Flow Matching'
title_zh: Meshy T2：基于流匹配的快速原生3D网格生成框架
authors:
- Jiale Xu
- Rendong Liang
- Yuhao Long
- Siyuan Shen
- Zangyueyang Xian
- Zeyi Xu
- Yuanming Hu
affiliations:
- Meshy AI
arxiv_id: '2607.28675'
url: https://arxiv.org/abs/2607.28675
pdf_url: https://arxiv.org/pdf/2607.28675
published: '2026-07-27'
collected: '2026-08-04'
category: Other
direction: 3D内容生成 · 流匹配模型应用
tags:
- Flow Matching
- 3D Mesh Generation
- VAE
- Cascade Generation
- Generative AI
one_liner: 基于两级流匹配级联架构实现比自回归基线快10倍以上的高质量原生3D网格生成
practical_value: '- 流匹配替代自回归实现结构化内容并行生成的思路可复用，电商商品多模态/结构化属性生成场景下可大幅提升推理速度

  - 粗到细的级联生成架构可借鉴到多模态推荐物料生成场景，先定全局骨架再填充细节，平衡生成质量与效率

  - 可控预算的生成约束设计可迁移到广告/商品素材生成场景，支持按业务需求灵活控制输出的复杂度/规模'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
当前主流3D网格生成方案依赖自回归序列化解码，推理速度慢、误差累积问题突出，无法满足影视、游戏、交互式3D场景的资产创作效率要求。
### 方法关键点
1. 核心采用顶点集网格VAE，单步并行解码顶点、边连接、面缠绕顺序，无需顶点量化或焊接即可保留高精度几何信息与艺术家创作的拓扑结构；
2. 采用两级流匹配级联生成架构：先由图像条件体素流生成粗粒度占位骨架，再由网格流基于输入图像、骨架、指定顶点预算生成逐顶点隐向量填充骨架；
3. 天然支持多部件资产生成、面数灵活可控。
### 关键结果
几何保真度达到SOTA水平，端到端图像转3D网格中位耗时仅6秒，推理速度比自回归基线快1个数量级以上。
