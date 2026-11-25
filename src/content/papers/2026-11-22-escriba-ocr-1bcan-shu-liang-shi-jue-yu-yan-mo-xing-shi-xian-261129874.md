---
title: 'Escriba-OCR: A 1B Vision-Language Model for Error-Preserving Transcription
  of Handwritten Portuguese Essays'
title_zh: Escriba-OCR：1B参数量视觉语言模型 实现保留原始错误的葡萄牙语手写转录
authors:
- Tardelli Ronan Coelho Stekel
affiliations:
- Federal Institute of São Paulo (IFSP), Brazil
arxiv_id: '2611.29874'
url: https://arxiv.org/abs/2611.29874
pdf_url: https://arxiv.org/pdf/2611.29874
published: '2026-11-22'
collected: '2026-11-25'
category: Multimodal
direction: 多模态OCR · 手写内容保真转录
tags:
- VLM
- OCR
- Handwriting Recognition
- Multimodal
- Model Fine-tuning
one_liner: 微调1B参数量OCR专用VLM，实现保留手写错误、编辑标记的低CER葡萄牙语作文转录
practical_value: '- 垂直场景小模型微调思路：针对电商手写面单、用户手写评价、线下小票识别等场景，仅用少量标注数据微调1-3B级专用VLM，即可大幅超过通用大模型识别精度，同时降低部署门槛

  - 评估体系设计：可借鉴在通用指标（如CER）之外新增场景专属指标（如错字保留率、特殊格式召回）的思路，避免通用指标与业务实际需求脱节

  - 轻量化部署：1B级VLM经4bit量化后可在普通CPU运行，精度损失可控，适合C端、线下端离线识别场景落地'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有VLM做手写转录时会自动修正错字、改写原始内容，无法满足需要保留手写错误、划改内容、换行结构的场景需求，通用大模型部署成本高，不适用于中小机构私有化部署。
### 方法关键点
构建BRESSAY评测基准，在传统CER指标外新增错误保留率、编辑标记精度/召回、行结构一致性等专属指标；仅用单GPU花费85分钟微调1B参数量OCR专用VLM LightOnOCR-3-1B适配葡萄牙语手写作文场景。
### 关键结果
Escriba-OCR-1B CER达2.06%，较最优基线Qwen3-VL 235B低3.5个百分点；可恢复77%划除内容、67%插入内容，97%页面行结构完全匹配；4bit量化后可在普通CPU运行，单页处理约1分钟，CER仅比GPU版本高0.1以内。
