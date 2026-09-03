---
title: On the Design Fundamentals of Pixel Text Representation Learning
title_zh: 像素文本表示学习的核心设计原则研究
authors:
- Chaohao Yuan
- Ruifeng Yuan
- Zhuoxu Huang
- Yu Rong
- Hong Cheng
- Hou Pong Chan
- Chenghao Xiao
affiliations:
- The Chinese University of Hong Kong
- DAMO Academy, Alibaba Group
- Fudan University
- University of Macau
- Shanghai University of Finance and Economics
arxiv_id: '2609.01147'
url: https://arxiv.org/abs/2609.01147
pdf_url: https://arxiv.org/pdf/2609.01147
published: '2026-08-31'
collected: '2026-09-03'
category: Multimodal
direction: 多模态表示学习 · 像素文本编码
tags:
- Visual Text Encoding
- Multimodal Representation
- Cross-lingual Learning
- RAG
- MLLM
one_liner: 通过系统消融确定像素文本表示学习四大核心组件，训练出跨语言SOTA的像素文本编码器
practical_value: '- 可变分辨率+多字体训练方案可直接复用在电商主图/详情页文本识别、商品海报语义检索场景，提升跨版式泛化性

  - 80% visual token压缩仍保持鲁棒性的特性，可用于多模态RAG长文档（如商品说明书、活动规则页）上下文压缩，降低KV cache开销

  - 两阶段多语言课程学习方法可迁移至多语言跨境电商的商品图片语义理解、跨语种多模态召回任务'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有像素文本编码器存在固定分辨率预训练泛化差、视觉捷径学习、visual grounding弱、多语言理解能力不足的问题，无法满足富文本视觉输入（文档、海报、图表）的读取、检索、压缩需求。
### 方法关键点
通过系统消融实验确定4个核心设计组件：可变图像分辨率+多渲染字号提升高分辨率文档泛化性；引入自然图文对增强grounding避免纯文本坍缩；布局感知渲染规避像素级捷径；两阶段多语言课程学习实现跨语言对齐。基于上述组件训练280M样本规模的Pixel Linguist II原生分辨率视觉编码器，采用动态渲染、统一对比grounding、多语言课程训练策略。
### 关键结果
在英文、跨语言、多语言Visual STS、ViDoRe数据集上达到SOTA，80% visual token压缩下仍保持鲁棒性，可有效提升下游MLLM效果。
