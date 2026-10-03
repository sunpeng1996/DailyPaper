---
title: 'SILSA: Sliding-Window Slice Latents for Topology-Preserving High-Resolution
  3D Generation'
title_zh: SILSA：基于滑动窗口切片隐变量的保拓扑高分辨率3D生成
authors:
- Tianjiao Yu
- Xinzhuo Li
- Yifan Shen
- Ying Shen
- Kiet A. Nguyen
- Adheesh Sunil Juvekar
- Ismini Lourentzou
affiliations:
- University of Illinois Urbana-Champaign
- PLAN Lab
arxiv_id: '2610.02201'
url: https://arxiv.org/abs/2610.02201
pdf_url: https://arxiv.org/pdf/2610.02201
published: '2026-09-30'
collected: '2026-10-03'
category: Other
direction: 高分辨率3D生成 · 保拓扑隐表示
tags:
- 3D Generation
- Sliding Window
- Latent Representation
- Topology Preservation
- VAE
one_liner: 提出基于滑动窗口切片隐变量的保拓扑3D生成框架，降本同时显著提升结构保真度
practical_value: '- 滑动窗口聚合局部信息压缩token量的思路可迁移到长序列用户行为建模，降低大模型推理与训练成本

  - 多流特征通过共享空间锚点网格对齐的架构可借鉴到多模态推荐的跨模态特征融合场景

  - 邻接单元拓扑一致性监督方法可复用在推荐/搜索链路的前后序结果一致性约束'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有高分辨率3D生成依赖体素隐变量与多阶段流水线，存在连续表面碎片化、生成成本高、薄/高连接形状拓扑一致性差的痛点。
### 方法关键点
1. 采用三轴固定重叠滑动窗口切片隐变量表征形状，每个token聚合局部深度窗口信息，支持单阶段整流流生成，避免高成本体素token
2. 设计Slice VAE编码定向表面样本为多轴切片隐变量，搭配稀疏体素解码器重建；引入Volumetric Anchor Lattice在共享3D工作区协调多方向切片流
3. 新增切片级拓扑监督，匹配持久图并对齐相邻切片的Betti转换，保障结构正确性
### 关键结果
较SOTA基线PSNR提升8.7%、覆盖率提升5.96个百分点、Betti误差降低9.2%；token量较最紧凑基线少70%、较稀疏/分层分词器少98%，训练内存降低40.4%，推理时间缩短58.5%
