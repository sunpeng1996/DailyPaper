---
title: 'WeMM-Ecom: Advancing Multimodal Content Understanding for WeChat E-Commerce'
title_zh: WeMM-Ecom：面向微信电商的多模态大模型系列
authors:
- Binhui Xie
- Jinmin Li
- Haomiao Tang
- Guangting Wang
- Song Jin
- Jianwei Zhu
- Fengyun Rao
- Jing Lyu
affiliations:
- Tencent Inc. WeChat Vision
arxiv_id: '2611.30662'
url: https://arxiv.org/abs/2611.30662
pdf_url: https://arxiv.org/pdf/2611.30662
published: '2026-11-22'
collected: '2026-11-24'
category: GenRec
direction: 生成式电商 · 多模态内容理解
tags:
- MLLM
- E-commerce
- MoE
- Multimodal Understanding
- Open Source
one_liner: 开源0.8B至35B MoE规模的电商多模态模型系列，兼顾领域与通用能力，已落地微信亿级请求场景
practical_value: '- 训练流程可复用：两阶段继续预训练逐步提升领域数据占比（45.8%→61.1%），结合OPD蒸馏、参数合并、GRPO强化学习，兼顾领域能力和通用能力不掉点，适合业务领域MLLM定制

  - 评测体系可直接复用：覆盖商品属性抽取、合规审核、跨模态检索、OCR、空间定位8大场景的28个评测基准，可直接用于电商MLLM效果验收

  - 部署选型参考：0.8B/2B小模型电商效果超越同尺寸通用MLLM，35B MoE（激活3B）效果超越5~22倍更大参数的开源旗舰模型，适合不同 latency
  要求的业务场景选型

  - 双模式设计可借鉴：单 checkpoint 支持思考（高准确率）和非思考（低延迟）两种模式，可根据业务场景（如审核用思考模式、实时搜索用非思考模式）动态切换'
score: 10
source: huggingface-daily
depth: full_pdf
---

### 动机
通用多模态大模型（MLLM）在电商场景存在两大核心痛点：一是无法满足SKU粒度细粒度感知、规则约束下的合规判断等强业务属性要求；二是领域微调容易导致通用能力退化，小模型难以在 latency 约束下兼顾效果与性能。
### 方法关键点
- 模型系列：覆盖0.8B、2B、4B、9B四个稠密模型，以及35B MoE（激活参数3B），基于Qwen3.5初始化
- 训练流程：两阶段继续预训练，阶段1电商数据占比45.8%，训练370.3B tokens；阶段2电商数据占比提升至61.1%，训练76.7B tokens；后训练结合on-policy蒸馏（OPD）、与Qwen3.5后训练 checkpoint 等权合并、GRPO强化学习，单 checkpoint 支持思考/非思考双模式
- 数据设计：电商数据覆盖SKU粒度属性抽取、合规审核、跨模态检索、内容生成5大类，同时保留通用多模态/文本数据避免通用能力退化
### 关键结果
- 电商评测集（28个基准，20.7万样本）：35B MoE模型得分74.35，超越5~22倍参数的Qwen3.8-Flash-Next、HY4等开源旗舰；9B模型得分72.45，超越3倍参数的Qwen3.8-27B；2B小模型得分64.24，领先同尺寸所有开源轻量MLLM
- 通用评测集（64个基准）：全尺寸模型均超越同尺寸Qwen3.5，2B轻量模型在6大通用领域得分位列同尺寸第一
### 核心结论
领域专业化不必然以牺牲通用能力为代价，小尺寸域定制模型效果可远超大参数通用模型
