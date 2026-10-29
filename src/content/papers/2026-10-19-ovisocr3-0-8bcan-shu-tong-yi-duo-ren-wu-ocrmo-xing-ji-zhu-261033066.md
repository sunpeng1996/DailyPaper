---
title: OvisOCR3 Technical Report
title_zh: OvisOCR3：0.8B参数统一多任务OCR模型技术报告
authors:
- Yu Xia
- Yinglun Li
- Yuhui Chen
- Jinlong Huang
- Yuyang Wanyan
- Shengze Shi
- Yifei Song
- Yue Duan
- Shubo Lin
- Jianshan Zhao
affiliations:
- ATH-MaaS, Alibaba Group
arxiv_id: '2610.33066'
url: https://arxiv.org/abs/2610.33066
pdf_url: https://arxiv.org/pdf/2610.33066
published: '2026-10-19'
collected: '2026-10-29'
category: Multimodal
direction: 多模态OCR · 小模型多任务统一训练
tags:
- OCR
- Multimodal
- Knowledge Distillation
- Reinforcement Learning
- Document Understanding
- Small Model
one_liner: 0.8B参数小模型通过多阶段训练实现5类OCR相关任务性能全面达SOTA
practical_value: '- 电商场景可直接复用0.8B OvisOCR3处理商品详情页、资质证照、用户评论截图的信息提取、表格还原，部署成本远低于大模型，精度满足业务需求

  - 多任务小模型训练的「领域平衡中期训练+多教师on-policy蒸馏+分领域奖励RL」范式可直接迁移到推荐多目标排序小模型、Agent专用工具小模型的训练流程

  - 跨页表格还原、图表caption生成能力可用于电商商品规格表自动结构化、商品卖点自动生成，替代人工处理长文档类素材的流程'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有OCR相关任务多依赖单领域专用大模型，部署成本高，小参数模型难以同时覆盖文档解析、通用OCR、KIE、图表caption、跨页表格还原等多类下游需求，不同任务数据量、输出长度差异大导致统一训练难度高。

### 方法关键点
1. 基于真实+合成数据做持续预训练，引入领域平衡中期训练解决不同任务数据量、响应长度差异的监督不均衡问题；
2. 采用5个4B参数领域专用教师模型做多教师on-policy蒸馏，迁移领域知识到共享小模型；
3. 最后加入分领域reward的混合任务RL优化模型输出效果。

### 关键结果
0.8B参数模型在OmniDocBench v1.6得分96.74，OCRBench v2中英分榜分别获65.9、61.3分位列第一，在所有KIE基准、跨页表格任务上均优于基线，图表caption得分接近Qwen3.8-Max。
