---
title: 'Towards Physically Grounded Articulated 3D Assets: A Multi-Agent Pipeline
  and Benchmark'
title_zh: 面向物理可落地铰接式3D资产的多智能体生成流水线与基准
authors:
- Xudong Cai
- Ruijie Zhu
- Haoliang Shang
- Ruining Li
- Marc Pollefeys
- Shangzhe Wu
- Andrea Vedaldi
- Chuanxia Zheng
affiliations:
- Nanyang Technological University
- ETH Zurich
- University of Oxford
- Microsoft
- University of Cambridge
arxiv_id: '2610.13947'
url: https://arxiv.org/abs/2610.13947
pdf_url: https://arxiv.org/pdf/2610.13947
published: '2026-10-09'
collected: '2026-10-13'
category: MultiAgent
direction: 多智体协作 · 3D资产生成
tags:
- Multi-Agent
- 3D Generation
- Physical Simulation
- Benchmark
- Articulated Assets
one_liner: 提出融合物理仿真反馈的多智能体铰接式3D资产生成系统Artisan及多维度统一评测基准
practical_value: '- 多Agent协作+外部工具（物理仿真器）反馈的闭环架构可迁移至电商3D商品生成场景，自动校验生成内容的物理合理性，大幅降低人工审核成本

  - 「空间保真-物理合理-下游性能-整体质量」的分层评测体系可复用至数字人、3D商品等生成式内容的效果评估流程，解决生成效果难量化的问题

  - 多Agent分工处理生成全链路的设计思路可用于优化生成式推荐的内容生成环节，提升生成文案/素材的落地可用性'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有3D资产生成技术仅聚焦几何与外观还原，忽略运动逻辑、物理属性等功能特征，生成结果无法满足AR/VR、电商3D展示等场景的实际使用需求。
### 方法关键点
1. 提出Artisan多Agent生成管线，在现有Articraft方案基础上引入物理仿真反馈闭环，支持生成具备无碰撞运动、重力下稳定、质量材质属性准确的铰接式3D资产；
2. 构建覆盖4维度的统一评测基准，包含100个参考资产、50个稳定性prompt、50个带标注质量的ABO对象及配套评测协议。
### 关键结果
在10+代表性生成模型的对比评测中，Artisan空间保真度表现具备竞争力，同时取得参评方法中最低碰撞率、最高稳定性率。
