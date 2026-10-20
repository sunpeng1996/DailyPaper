---
title: MOSS-Image Technical Report
title_zh: MOSS-Image 开源文生图系统技术报告
authors:
- MOSI. AI
affiliations:
- MOSI Intelligence
- SII
- Fudan University
- Shanghai Jiao Tong University
arxiv_id: '2610.23374'
url: https://arxiv.org/abs/2610.23374
pdf_url: https://arxiv.org/pdf/2610.23374
published: '2026-10-15'
collected: '2026-10-20'
category: Multimodal
direction: 多模态文生图 · Agent提示增强
tags:
- Text-to-Image
- Diffusion Transformer
- Agentic Prompt Enhancement
- Multimodal
- Evaluation Benchmark
one_liner: 推出开源5B参数量DiT文生图系统与Agent式提示增强模块，填补开源模型密集文本、复杂布局生成短板
practical_value: '- 电商营销海报、商品详情图、活动Banner生成场景可复用Agentic PE模块，将运营的模糊需求自动转成带布局、文本细节的标准化提示，降低提词门槛

  - 需生成含密集文字的营销素材（如优惠券、价签、活动规则图）的业务可直接复用MOSS-Image预训练权重，96.3%的文本覆盖率可满足大部分商用需求

  - 文生图类业务的效果评估可直接复用LLTB、RLA两个开源评测基准，分别覆盖文本准确性、布局合理性两个核心业务指标，减少自研评测成本'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有开源文生图模型在密集文本渲染、复杂布局控制能力上远落后于闭源系统，无法满足营销海报、信息图、知识卡片等实用场景的生成需求。
### 方法关键点
1. 从头预训练5B参数量单流DiT，支持中英双语长文本渲染与精准布局控制
2. 设计意图感知Agentic PE模块，可将模糊用户需求自动转换为含内容、布局细节的标准化生成提示
3. 构建两个专用评测基准：LLTB用于评估长文本渲染能力，RLA用于评估富布局端到端生成效果
### 关键结果
在LLTB上平均文本覆盖率达96.3%，位列开源模型SOTA；RLA端到端系统评测排名第二，固定增强提示下生成器backbone位列所有参评模型第一
