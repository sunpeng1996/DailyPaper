---
title: Program-Verified Self-Evolution for Vision-Language Models
title_zh: 面向视觉语言模型的程序验证式自进化方法
authors:
- Ahmed Heakl
- Sungik Choi
- Moontae Lee
- Salman Khan
arxiv_id: '2609.33855'
url: https://arxiv.org/abs/2609.33855
pdf_url: https://arxiv.org/pdf/2609.33855
published: '2026-09-26'
collected: '2026-09-29'
category: Training
direction: 多模态大模型 · 自进化训练优化
tags:
- Vision-Language Model
- Self-Evolution
- Program Verification
- QA Generation
- Multimodal Training
one_liner: 基于结构化图像解析与程序自动QA生成，提升视觉语言模型自进化的标注质量与下游性能
practical_value: '- 商品图文理解任务的自标注环节可复用「结构化解析→程序生成标注→单事实校验」流程，替代投票/模型打标，降低约20%的标注错误率

  - 多模态电商Agent的属性识别、场景问答模块可引入固定程序做事实校验，减少大模型幻觉，提升多模态召回排序准确性

  - 小参数多模态推荐模型迭代可参考三轮自进化训练范式，在低标注成本下持续提升性能，适配端侧多模态推荐场景'
score: 8
source: huggingface-daily
depth: abstract
---

### 动机
现有视觉语言模型自进化方法依赖多数投票或模型裁判为无标注图像生成的QA打标，人工评估发现24%的投票标注、18%的模型裁判标注存在错误，严重限制自进化效果。
### 方法关键点
提出VQS自进化方案：先将图像解析为场景图、图表、示意图等结构化记录，再通过固定程序基于结构化记录自动生成问题并计算标准答案，VLM仅作为视觉校验器逐事实校验程序读取的单条短声明，校验结果同时用于无监督优化解析器。
### 关键结果
人工评估显示VQS生成的答案准确率达94%，远超多数投票的76%；在10个基准测试集上，VQS可将2B/4B/8B全规模Qwen3-VL性能最高提升3.18个点，优于所有现有自进化基线；2B规模模型经过三轮自进化训练后增益可达3.84个点，效果随训练轮次持续提升。
