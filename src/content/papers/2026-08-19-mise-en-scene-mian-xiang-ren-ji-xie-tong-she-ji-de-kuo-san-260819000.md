---
title: 'Mise-en-Scène: Implicit Layout Emergence in Diffusion Transformers for Human-AI
  Design Co-Creation'
title_zh: Mise-en-Scène：面向人机协同设计的扩散Transformer隐式布局生成框架
authors:
- Zipeng Xu
- Ryan Murdock
- Umberto Michieli
affiliations:
- Canva Research
arxiv_id: '2608.19000'
url: https://arxiv.org/abs/2608.19000
pdf_url: https://arxiv.org/pdf/2608.19000
published: '2026-08-19'
collected: '2026-08-20'
category: Multimodal
direction: 多模态生成 · 隐式布局编排
tags:
- Diffusion Transformer
- LoRA
- Layout Generation
- Graphic Design
- Human-AI Co-creation
one_liner: 用轻量LoRA微调扩散Transformer实现隐式布局生成，两阶段框架兼顾设计美感与素材保真
practical_value: '- 电商海报/商品主图自动生成场景可复用两阶段框架：第一阶段用轻量LoRA微调预训练扩散模型生成布局草稿，第二阶段匹配替换高清商品、Logo等素材，兼顾美观度与素材保真度

  - 无需单独训练显式布局预测模型，仅对预训练扩散Transformer做小样本LoRA微调即可实现多元素自动编排，大幅降低定制化设计生成的训练成本

  - 确定性匹配-替换后处理步骤可迁移到所有需保留特定素材的AIGC场景，解决生成图素材失真、无法分层二次编辑的业务痛点'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有图形设计生成方法先通过LLM预测显式 bounding box 布局再粘贴素材，空间规划与视觉生成流程割裂，易出现布局僵化、素材缩放失衡问题，且输出为扁平化图片无法支持二次编辑。

### 方法关键点
两阶段Mise-en-Scène框架：
1. 第一阶段：仅用经knockout筛选的小参数量LoRA微调预训练图像编辑扩散Transformer，联合生成画布渲染效果与元素隐式布局，无需额外多元素生成专用条件模块
2. 第二阶段：通过确定性匹配-放置步骤将原始高清素材移动到草稿对应位置，保证素材100%保真，输出可编辑的分层设计

### 关键结果
在大规模PrismLayersPlus基准上，生成设计的感知质量大幅优于LLM布局规划器、专用布局Transformer等所有对比方案，是最接近真值的方法，匹配放置阶段完全填补了素材保真度缺口。
