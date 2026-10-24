---
title: 'MoG-VLM: Efficient Video Anomaly Detection through Motion-Guided Vision-Language
  Models'
title_zh: MoG-VLM：基于运动引导视觉语言模型的高效视频异常检测
authors:
- Khaled Waleed Dawoud
- Muhammad Zaigham Zaheer
- Khan Muhammad
- Muhammad Haris Khan
affiliations:
- Mohamed bin Zayed University of Artificial Intelligence
- Sungkyunkwan University
arxiv_id: '2610.31478'
url: https://arxiv.org/abs/2610.31478
pdf_url: https://arxiv.org/pdf/2610.31478
published: '2026-10-22'
collected: '2026-10-24'
category: Other
direction: 多模态视频分析 · VLM推理效率优化
tags:
- VLM
- Video Anomaly Detection
- Inference Optimization
- Zero-shot
- Motion Guided
one_liner: 提出运动引导的VLM调度框架，零样本视频异常检测达SOTA同时实现推理加速
practical_value: '- 可复用「轻量信号触发大模型推理」的调度思路：电商/广告场景可先用规则/小模型预判query/物料价值，仅高价值请求调用LLM/VLM，大幅降本

  - 分层触发+动态上下文窗口+早停的架构可直接迁移到短视频内容审核、电商实时风控场景，高风险样本才启动深度多模态推理

  - 轻量时序信号+大模型语义融合的零样本架构，可降低内容类新业务冷启动成本，无需大量标注即可快速上线'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
VLM在视频异常检测任务上性能表现突出，但逐帧密集推理延迟过高，现有均匀采样方案忽略内容动态，要么在静态片段浪费算力，要么漏检局部异常，无法满足实时部署要求。
### 方法关键点
1. 引入Temporal Gradient Magnitude（TGM）轻量运动信号做内容感知采样，将算力集中在高信息密度片段，避免冗余处理
2. 采用分层双流设计，仅异常概率较高的锚点帧才触发上下文窗口扩展的多帧VLM推理，支持早停
3. 融合模块对齐瞬时语义线索与时序动作动态，保证检测精度
### 关键结果
零样本免训练设置下，在XD-Violence、UCF-Crime、MSAD、ShanghaiTech四个基准AUC-ROC分别达91.91%、84.30%、87.88%、78.96%，在三个基准上取得SOTA；XD-Violence数据集上较此前最优方案提升0.57% AUC，同时实现1.31倍推理提速
