---
title: 'ABACUS: Adapting Unified Foundation Model for Bridging Image Count Understanding
  and Generation'
title_zh: ABACUS：适配统一基础模型打通图像计数理解与生成
authors:
- Anindya Mondal
- Sauradip Nag
- Anjan Dutta
affiliations:
- University of Surrey
- Simon Fraser University
arxiv_id: '2606.23835'
url: https://arxiv.org/abs/2606.23835
pdf_url: https://arxiv.org/pdf/2606.23835
published: '2026-06-21'
collected: '2026-06-27'
category: Multimodal
direction: 多模态 · 计数理解与生成统一建模
tags:
- Vision-Language Model
- Foundation Model
- Counting
- Image Generation
- GRPO
one_liner: 基于3B统一基础模型提出三项适配策略，无需基准定制训练打通图像计数理解与生成，七大基准达SOTA
practical_value: '- 密度感知自适应缩放+objectness图的空间定位方案，可迁移到电商货架商品计数、用户晒单图物品识别、多模态Agent计数问答等场景，提升密集场景准确率，无需任务级定制训练

  - 基于GRPO的边界感知计数策略，可复用在商品图裁切后的SKU数量校验、局部区域计数场景，解决裁剪边界导致的计数偏差

  - 循环一致GRPO的自批判对齐思路，无需额外标注即可对齐多模态理解与生成能力，可用于电商指定数量商品图生成的自监督优化，降低标注成本'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有图像计数（物体计数、人群计数、指代表达计数）与计数条件图像生成任务长期割裂，依赖任务专属架构、损失函数与训练流程；统一视觉语言模型存在「理解-生成不同步」问题（如能正确数出4个苹果却无法生成正好4个），且密集场景计数易给出粗粒度估计、生成结果数量不可控。

### 方法关键点
基于3B参数统一视觉语言基础模型适配，无需任何benchmark-specific训练，核心创新三点：
1.  带objectness maps的density-aware adaptive zooming，实现精准空间定位；
2.  基于GRPO的boundary-aware计数策略，消除裁剪边界导致的计数误差；
3.  cycle-consistent GRPO策略：用理解分支自批判生成结果，无需外部标注即可打通理解与生成的能力鸿沟。

### 关键结果
在7个计数与生成基准上达到SOTA，性能超越任务专属specialist模型和更大参数的通用模型。
