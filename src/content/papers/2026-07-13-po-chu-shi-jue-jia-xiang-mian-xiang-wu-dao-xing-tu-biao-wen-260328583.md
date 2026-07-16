---
title: 'Navigating the Mirage: A Dual-Path Agentic Framework for Robust Misleading
  Chart Question Answering'
title_zh: 破除视觉假象：面向误导性图表问答的双路径Agent框架
authors:
- Yanjie Zhang
- Yafei Li
- Rui Sheng
- Zixin Chen
- Yanna Lin
- Huamin Qu
- Lei Chen
- Yushi Sun
affiliations:
- HKUST
- HKUST(GZ)
arxiv_id: '2603.28583'
url: https://arxiv.org/abs/2603.28583
pdf_url: https://arxiv.org/pdf/2603.28583
published: '2026-07-13'
collected: '2026-07-16'
category: Agent
direction: Agent 多模态误导性图表问答优化
tags:
- VLM
- Agentic Framework
- Chart QA
- SFT
- GRPO
one_liner: 双路径Agent框架ChartCynics大幅提升VLM误导性图表识别准确率，较Qwen3-VL-8B提升29%
practical_value: '- 双路径解耦感知+验证的架构可复用在电商多模态内容审核场景，精准识别虚假营销类误导性图表（如轴缩放/倒置的夸张销量柱状图）

  - 两阶段训练范式（Oracle-Informed SFT + 欺骗感知GRPO）可迁移至需对抗鲁棒性的Agent任务，优化虚假广告、商品宣传图的识别效果

  - ROI针对性裁剪+OCR数值校验的技巧可直接落地于电商运营数据报表自动校验工具，避免异常图表误导业务决策'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有VLM对包含视觉欺骗结构、失真数据的误导性图表识别鲁棒性差，无法满足可信图表解析的落地需求
### 方法关键点
ChartCynics双路径Agent框架解耦感知与验证流程：
1. 诊断视觉路径通过战略ROI裁剪捕捉坐标轴倒置等结构异常；
2. OCR驱动数据路径完成数值grounding；
引入Agentic Summarizer通过两阶段协议优化：先通过Oracle-Informed SFT蒸馏推理逻辑，再通过Deception-Aware GRPO完成对抗对齐，解决跨模态冲突，惩罚视觉陷阱，强制逻辑一致性
### 关键结果
两个基准数据集上准确率分别达74.43%、64.55%，较Qwen3-VL-8B backbone绝对提升~29%，性能超越SOTA专有模型，验证了专用Agent工作流可赋予小尺寸开源模型更强鲁棒性
