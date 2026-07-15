---
title: 'MonkeyOCRv2: A Visual-Text Foundation Model for Document AI'
title_zh: MonkeyOCRv2：面向文档AI的视觉文本基础模型
authors:
- Yuliang Liu
- Zhang Li
- Ziyang Zhang
- Shuo Zhang
- Qiang Liu
- Jiajun Song
- Zidun Guo
- Xinhan Wang
- Handong Zheng
- Yang Liu
affiliations:
- Huazhong University of Science and Technology
- Kingsoft Office
arxiv_id: '2607.11562'
url: https://arxiv.org/abs/2607.11562
pdf_url: https://arxiv.org/pdf/2607.11562
published: '2026-07-13'
collected: '2026-07-15'
category: Multimodal
direction: 多模态文档理解 · OCR预训练
tags:
- Document AI
- OCR
- Multimodal Pre-training
- Vision Encoder
- MLLM
one_liner: 基于1.13亿多语言文档语料与联合预训练策略，打造轻量高效的文档AI视觉文本基础模型
practical_value: '- 电商场景中商品详情页、买家秀晒单文字、电子发票等文档类内容的OCR识别，可直接复用MonkeyOCRv2作为视觉编码器，降本提效

  - 搭建文档类多模态Agent时，采用冻结的MonkeyOCRv2搭配小参数语言模型即可超过大模型效果，大幅降低部署成本

  - 垂直领域多模态预训练可参考「跨模态对齐+像素级重建」双任务策略，兼顾语义对齐和细粒度特征保留'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
通用自然图像预训练的视觉编码器缺乏文档场景适配，无法满足密集文本、细粒度字符笔画的字符级感知需求。
### 方法关键点
1. 构建1.13亿张覆盖17种语言的大规模文档图像预训练语料库MonkeyDoc v2；
2. 采用「图像到文本生成+像素级文档重建」联合预训练策略，前者对齐视觉表征与文本内容，后者保留字符笔画、布局细节。
### 关键结果数字
- 5类文档分析任务替换原编码器均获稳定提升，CRNN识别准确率从58.7%提升至67.3%；
- 冻结编码器搭配轻量语言模型得到0.7B文档解析模型，在MDPBench上超此前最优3B模型2.8个百分点，视觉编码器体积小11倍；
- OmniDocBench上性能超过Qwen3-VL-235B、GPT-5.2等大模型，8个文档理解基准上优于CLIP、DINO、SAM等通用视觉编码器。
