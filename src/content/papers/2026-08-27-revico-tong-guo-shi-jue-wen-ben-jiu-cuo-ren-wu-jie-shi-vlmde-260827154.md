---
title: 'ReViCo: Unveiling the Limitations of VLMs in Visual Text Understanding via
  Error Correction'
title_zh: ReViCo：通过视觉文本纠错任务揭示VLM的图文理解局限性
authors:
- Bojun Zhang
- Junhong Liang
- Feifei Zhai
- Fengxian Ji
- Yu Zhou
affiliations:
- 中国科学院自动化研究所多模态人工智能系统全国重点实验室
- 中国科学院大学人工智能学院
- 中科凡语科技有限公司凡语AI实验室
- 穆罕默德·本·扎耶德人工智能大学
arxiv_id: '2608.27154'
url: https://arxiv.org/abs/2608.27154
pdf_url: https://arxiv.org/pdf/2608.27154
published: '2026-08-27'
collected: '2026-08-28'
category: Multimodal
direction: 多模态大模型 · 视觉文本理解评测
tags:
- VLM
- Multimodal Benchmark
- Visual Text Understanding
- OCR
- Error Correction
one_liner: 提出ReViCo视觉文本纠错基准，评测发现现有VLM的视觉文本理解能力与人类存在显著差距
practical_value: '- 电商主图/商品海报文案纠错、违规信息识别场景，可引入视觉文本纠错范式替代OCR+文本纠错两阶段方案，降低badcase率

  - 多模态推荐/搜索场景需解析图片内嵌文本时，先测试现有VLM的视觉文本理解准确率，避免直接上线引发的语义错误

  - VLM业务选型时可复用ReViCo基准的测试用例做定向评测，筛选对图文上下文理解能力匹配业务需求的模型'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有VLMs在通用视觉任务表现优异，但对图片内嵌文本的深度理解能力缺乏有效评估，难以支撑需要解析图文上下文的电商、广告等实际场景。

### 方法关键点
1. 构建ReViCo基准，基于真实场景图片的视觉文本纠错任务评测VLMs，要求模型同时识别文本错误、结合视觉上下文修正内容；
2. 采用prompt调优、定向训练两种范式测试主流VLM的能力上限。

### 关键结果数字
最优VLM的视觉文本纠错表现仍与人类存在显著差距，核心瓶颈是80%以上的模型无法精准感知视觉文本细节，导致超60%的纠错错误，为后续更鲁棒的文本感知VLM研发提供了基准支撑。
