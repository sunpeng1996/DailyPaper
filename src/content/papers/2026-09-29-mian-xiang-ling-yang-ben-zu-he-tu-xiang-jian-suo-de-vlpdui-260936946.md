---
title: Optimizing VLP-aligned Multimodal Intent Representation with Correct Visual
  Instantiation for Zero-Shot Composed Image Retrieval
title_zh: 面向零样本组合图像检索的VLP对齐多模态意图表示优化方法
authors:
- Xuri Ge
- Chunhao Wang
- Junchen Fu
- Haokun Wen
- Zhiwei Xu
- Ying Zhou
- Zhumin Chen
- Pengjie Ren
- Zhaochun Ren
- Xin Xin
affiliations:
- 山东大学
- 格拉斯哥大学
- 哈尔滨工业大学（深圳）
- 莱顿大学
arxiv_id: '2609.36946'
url: https://arxiv.org/abs/2609.36946
pdf_url: https://arxiv.org/pdf/2609.36946
published: '2026-09-29'
collected: '2026-09-30'
category: Multimodal
direction: 多模态检索 · 零样本组合图像检索
tags:
- Zero-shot CIR
- Multimodal Retrieval
- VLP
- MLLM
- Visual Instance Disentanglement
one_liner: 提出融合MLLM推理与无训练视觉实例解耦的零样本CIR框架，刷新三类基准SOTA
practical_value: '- 电商多模态搜图场景可复用VMIR模块的prompt设计思路：给MLLM喂VLP原生风格的few-shot样例，生成更贴合VLP检索空间的query描述，直接提升召回精度

  - 可复用TVID无训练视觉实例解耦方法：基于预训练VLP的图文对齐能力，从参考图中提取和目标相关的视觉实例特征，过滤无关背景噪声，不需要额外标注训练

  - 多模态融合可参考HIAF的轻量设计：仅训练MLP投影层和融合权重，冻结VLP和MLLM主干，训练成本极低（单卡2080Ti 3小时即可完成），业务落地门槛低'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
零样本组合图像检索（ZS-CIR）支持用户输入参考图+修改文本检索目标图，是电商以图搜图、交互式搜索的核心技术。现有主流方案存在两类缺陷：基于视觉伪词的方法会引入参考图无关噪声，且拼接后的query不符合VLP原生文本空间分布；基于MLLM推理的方法生成的描述弱视觉锚定，易丢失参考图细粒度实例特征，两类方案都无法充分利用预训练VLP的检索能力。

### 方法关键点
- VMIR模块：给MLLM注入VLP原生风格的few-shot CoT prompt，引导生成精简、符合VLP检索偏好的目标描述，同时显式输出需要从参考图保留的视觉实例列表
- TVID模块：无需额外训练，利用VLP预训练的图文对齐能力，从参考图中解耦出和指定实例对应的细粒度视觉特征，过滤背景等无关噪声
- HIAF模块：仅预训练轻量MLP投影层和自适应融合器，将文本描述与实例级视觉特征融合为统一的混合模态表示，完全适配VLP检索空间

### 关键结果
在CIRR（通用场景）、CIRCO（开放域）、FashionIQ（电商服饰场景）三个公开基准测试，基于ViT-G/14 backbone时，相比SOTA基线：CIRR平均Recall@k提升2.21个点，CIRCO平均mAP提升6.92个点，FashionIQ平均Recall@10提升1.55个点，所有提升均统计显著。

### 核心结论
多模态检索的query表示需要同时满足「对齐预训练VLP原生分布」和「锚定意图相关细粒度视觉实例」两个条件，才能达到最优召回效果
