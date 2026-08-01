---
title: Codebook Capacity Governs Perceptual Quality Across Resolutions in Hierarchical
  Discrete Video Compression
title_zh: 分层离散视频压缩中码本容量对跨分辨率感知质量的调控作用
authors:
- Manikanta Kotthapalli
- Banafsheh Rekabdar
affiliations:
- Portland State University
arxiv_id: '2607.23366'
url: https://arxiv.org/abs/2607.23366
pdf_url: https://arxiv.org/pdf/2607.23366
published: '2026-07-25'
collected: '2026-08-01'
category: Other
direction: 离散视频编码 · 码本容量优化
tags:
- Video Compression
- VQ-VAE
- Codebook
- Perceptual Quality
- Discrete Tokenizer
one_liner: 验证分层离散视频编码中码本容量对感知质量的影响是分辨率的10倍，简化多分辨率部署
practical_value: '- 做生成式视频/多模态Tokenizer设计时，优先调优码本容量而非盲目提升输入分辨率，可在更低计算成本下提升内容感知质量

  - 多分辨率短视频/广告内容分发场景，可复用同码本的分层离散编码器，无需按分辨率单独重训，大幅降低部署适配成本

  - 低带宽电商短视频推流场景，采用该码本优化策略可比传统H.264/H.265编码降低21%~52%的感知损失，同时保持更低码率'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
基于连续隐表示的学习型视频编码跨分辨率部署时需单独重训或率失真重校准，适配成本高，分层离散编码的跨分辨率鲁棒性尚未被验证。
### 方法关键点
基于MS-VQ-VAE架构在UCF101数据集做控制变量实验，覆盖4类码本规模（128/256/512/1024）、3类分辨率（64×64/128×128/256×256）共12组参数，拟合感知质量与码本、分辨率的对数线性关系。
### 关键结果数字
1. 感知质量（LPIPS）仅与码本容量强相关，码本每对数单位提升的影响力是分辨率的10倍，模型拟合R²=0.82；
2. 底层熵效率随分辨率提升从84~87%升至92~94%，大分辨率下码本利用率更高；
3. 所有参数组均优于同/更低码率的H.264，128×128分辨率LPIPS降低25~52%，256×256分辨率优于H.265达21~37%。
