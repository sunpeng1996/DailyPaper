---
title: 'Media Intelligence Platform: Multimodal Detection of Synthetic and Manipulated
  Content'
title_zh: 媒体智能平台：面向合成与篡改内容的多模态检测系统
authors:
- David Fischinger
- Marcel Hasenbalg
- Silvia Poletti
- Davide Antonutti
- Mina Schütz
- Lam Pham
- Justin Ilyes
- Péter Rjabcsenkó
- Simon Freitter
- Martin Boyer
affiliations:
- Austrian Institute of Technology
arxiv_id: '2610.27974'
url: https://arxiv.org/abs/2610.27974
pdf_url: https://arxiv.org/pdf/2610.27974
published: '2026-10-20'
collected: '2026-10-24'
category: Multimodal
direction: 多模态内容造假检测 · 统一平台架构
tags:
- Multimodal Forensics
- Deepfake Detection
- Synthetic Media
- Modular Architecture
- Content Audit
one_liner: 提出集成6类伪造检测模块的统一多模态媒体取证平台，支持灵活扩展且配套公开演示
practical_value: '- 内容风控架构参考：电商/内容平台的多模态违规内容检测（AI生成虚假商品图、伪造宣传视频、P改资质证明等）可复用「统一调度框架+专项检测模块」的松耦合架构，新增检测能力无需重构整体系统，迭代效率更高。

  - 多模态检测落地思路：针对不同模态/不同类型的造假任务分别优化小模型，比训通用大模型检测的成本更低、准确率更高、推理速度更快，更适合高并发的业务风控场景。

  - 产品验证思路：新检测能力上线前可先搭建公开演示页面，收集真实业务样本反哺模型迭代，同时方便业务方快速验证效果降低对接成本。'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
生成式AI技术快速迭代导致多模态伪造/篡改内容（合成人脸、伪造音视频、AI生成图片、局部修图、虚假文本）爆发式增长，现有检测方案大多针对单一篡改类型设计，无法适配真实场景异构媒体来源的统一检测需求。
### 方法关键点
推出统一Web端媒体智能平台MIP，采用模块化松耦合架构，内置6类专项检测模块：假视频检测、人脸融合检测、AI生成图像检测、音频深度伪造检测、图片局部篡改检测、文本分析，支持灵活接入新模型适配新兴伪造技术，配套易用交互界面支撑取证调查。
### 关键结果
在多类代表性基准数据集上，所有模态检测任务均达到可靠识别性能，配套发布公开演示器支持可复现验证与社区评估，可直接落地于真实环境的多模态造假全链路检测。
