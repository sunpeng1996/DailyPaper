---
title: 'PaMuk-Bench: A Parallel Multilingual Multitask Benchmark for Vision-Language
  Tasks'
title_zh: PaMuk-Bench：面向视觉语言任务的并行多语言多任务基准
authors:
- Silviu-Florin Gheorghe
- Radu-Stefan Popa
- Adriana Valentina Costache
- Adrian-Gabriel Chifu
- Alessia Amelio
- Paul Irofti
- Anders Skaarup Johansen
- Lallouani Bouchakour
- Mohamed Lichouri
- Khaled Lounnas
affiliations:
- Univ. of Bucharest
- Aix-Marseille Univ.
- Univ. of Chieti-Pescara
- Aalborg Univ.
- Poineer Centre AI
arxiv_id: '2611.27521'
url: https://arxiv.org/abs/2611.27521
pdf_url: https://arxiv.org/pdf/2611.27521
published: '2026-11-20'
collected: '2026-11-23'
category: Multimodal
direction: 多模态VLM · 多语言多任务评测基准
tags:
- VLM
- Multilingual
- Benchmark
- Vision-Language
- Low-resource
- Multimodal
one_liner: 构建覆盖7种语言5类VLM任务的并行多语言基准，解决低资源语言VLM评测数据缺失问题
practical_value: '- 跨境电商多模态搜索/推荐场景的低资源语言适配，可复用该基准的半自动化多语言prompt标注流程，通过多MT工具投票+少量人工校准降低小语种标注成本

  - 出海业务的多模态模型选型与优化，可直接基于该基准验证VLM在目标小语种上的文生图、图文检索性能差距，指导fine-tuning数据配比与训练策略

  - 电商商品图生成、营销内容生产场景，可借鉴基准中生成/检索难度预测的标注思路，构建prompt难度预估模型，提升内容生产效率'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
当前VLM在英语等高资源语言上表现优异，但在低资源语言上性能下滑明显，缺乏统一的跨语言跨任务并行评测基准支撑性能优化。
### 方法关键点
1. 基于MS COCO、DrawBench等开源数据集筛选10K+高质量英文prompt，通过多机器翻译工具投票+少量人工校准的半自动化流程，翻译成阿拉伯语、丹麦语、法语等6种语言，形成并行多语言prompt集
2. 覆盖文生图、图像描述、图文检索、生成难度预测、检索难度预测5类核心VLM任务，配套相关性、难度标注
3. 支持零样本、微调两种设置下的多架构VLM跨语言对比评测
### 关键结果
实证显示零样本、通用多语言预训练VLM的跨语言性能普遍显著低于微调版本，该基准可有效量化并缩小不同VLM架构的语言性能gap
