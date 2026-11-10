---
title: 'Click3R: Interactive Stereo 3D Reconstruction with Sparse Correspondence Clicks'
title_zh: Click3R：基于稀疏对应点点击的交互式立体3D重建
authors:
- Hao Gu
- Jin Yao
- Zezhou Cheng
affiliations:
- University of Virginia
arxiv_id: '2611.12875'
url: https://arxiv.org/abs/2611.12875
pdf_url: https://arxiv.org/pdf/2611.12875
published: '2026-11-08'
collected: '2026-11-10'
category: Other
direction: 交互式3D重建 · 人机交互校正
tags:
- 3D Reconstruction
- Human-in-the-loop
- Adapter
- Interactive Correction
- Sparse Supervision
one_liner: 提出基于稀疏点击约束的交互式3D重建框架，仅需单点点击即可有效降低重建误差
practical_value: '- 轻量Adapter注入外部约束的思路可迁移到RecSys/GenRec的bad case快速修正场景，无需重训全模型即可快速校准输出

  - 稀疏人工反馈优化模型输出的框架可复用在生成式推荐的人工干预链路，少量标注即可快速修正批量bad case

  - 专门构造暴露模型失效模式的评测基准的思路，可用于搜推广算法的bad case专项评测集建设'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有前馈3D重建模型仅输出单次不可修改的预测结果，无错误校正机制，在重复纹理、对称结构、大视角变化、无纹理区域等复杂场景易出现失效问题，现有方案无法低成本修正输出偏差。
### 方法关键点
1. 设计Click3R交互式校正框架，通过轻量级点对应Adapter，将用户输入的跨视图稀疏点对应几何约束直接注入3D重建网络，无需重训全量模型即可校正输出偏差；
2. 构建专门暴露前馈重建方法失效模式的高难度评测基准，适配交互式重建效果评测需求。
### 关键结果
仅需1次对应点点击即可降低重建误差，在标准3D重建基准和自建高难度基准上均实现稳定性能提升。
