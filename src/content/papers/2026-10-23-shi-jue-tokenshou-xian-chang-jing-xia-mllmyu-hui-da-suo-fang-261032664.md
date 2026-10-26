---
title: 'The Answer Knows Where to Look: Zooming before MLLMs Answer under Visual-Token
  Budgets'
title_zh: 视觉token受限场景下MLLM预回答缩放机制LookZoom
authors:
- Zhensheng Hu
- Guanglong Xu
- Guanqiang Hu
affiliations:
- Southern Medical University
- Xinjiang Medical University
- Zhaoqing University
- Guangdong Kamfu Technology Co., Ltd.
arxiv_id: '2610.32664'
url: https://arxiv.org/abs/2610.32664
pdf_url: https://arxiv.org/pdf/2610.32664
published: '2026-10-23'
collected: '2026-10-26'
category: Multimodal
direction: 多模态大模型 · 视觉推理效率优化
tags:
- MLLM
- Visual Token Budget
- Attention Distillation
- LoRA
- Zoom Mechanism
one_liner: 通过专用<look>token蒸馏正确回答的注意力，预回答阶段实现MLLM高效视觉缩放，性能优于现有方案
practical_value: '- 电商多模态搜索/商品OCR场景可复用<look>专用token设计：隔离指向和阅读任务，避免监督注意力指向时损失文本理解精度，解决低分辨率商品图小字识别问题

  - 多模态Agent的视觉信息定位可借鉴hindsight distillation思路：不需要标注框，用模型自身正确回答的注意力蒸馏指向能力，降低标注成本

  - 多模态推理的资源受限优化可参考自适应视图选择策略：根据单样本信息gap动态选缩放方式，在低token预算下精度提升明显，适合端侧多模态应用

  - 小样本LoRA微调技巧可复用：仅在专用token位置激活LoRA，不影响原有模型能力，微调成本低，适配业务场景快'
score: 8
source: arxiv-cs.CV
depth: full_pdf
---

### 动机
MLLM部署时受限于视觉token预算，高分辨率图像被下采样后，文档、图表、商品图上的小字信息无法识别；现有缩放方案要么依赖顶层扩散的预回答注意力定位精度差，要么需要先生成中间回答/依赖标注框，推理延迟高且落地成本高，无法兼顾性能和效率。

### 方法关键点
- 设计专用<look>特殊token，仅在预填充阶段处理，回答阶段直接移除，搭配仅作用于该token位置的LoRA权重，彻底隔离区域指向和内容阅读任务，避免监督指向时损失文本理解精度
- 采用hindsight distillation策略：无需任何标注框，用模型自身正确回答的注意力作为监督信号，蒸馏<look>token的注意力到固定中间层，实现预回答阶段的精准证据区域定位
- 预设8种可选视图（无缩放、不同比例裁剪、自适应窗口、中心扭曲等），通过反事实监督训练动作头，根据单样本信息gap（原生分辨率/预算分辨率比值）动态选择最优视图，最大化低token预算下的有效信息密度

### 关键结果
在Qwen3-VL 2B/4B/8B三个模型尺寸、DocVQA/ChartQA等5个文本密集型多模态基准上测试：98视觉token预算下，比最优基线高4.8~9.1个点，比注意力引导的缩放方法高11.1~17.0个点；推理速度比注意力引导/基于接地的缩放方法快40%~70%；196token预算下比最优基线高4.0~5.5个点。

> 最值得记住的一句话：MLLM的正确回答本身就隐式包含证据区域的位置信息，通过专用token蒸馏该隐式知识，可在无前置生成开销的前提下实现高效精准的视觉缩放。
