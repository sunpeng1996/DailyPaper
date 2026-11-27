---
title: Can image generation help visual reasoning? An empirical study
title_zh: 图像生成是否助力视觉推理？一项实证研究
authors:
- Xueyang Yu
- Yifan Jing
- Taiming Lu
- Linrong Cai
- Zhipeng Cai
- Yunyang Xiong
- Gabriel Sarch
- Zhuang Liu
affiliations:
- Princeton University
- Meta
arxiv_id: '2611.34935'
url: https://arxiv.org/abs/2611.34935
pdf_url: https://arxiv.org/pdf/2611.34935
published: '2026-11-25'
collected: '2026-11-27'
category: Reasoning
direction: 多模态视觉推理·生成图像辅助效果验证
tags:
- Multimodal Reasoning
- Visual Question Answering
- Image Generation
- Vision-Language Model
- Empirical Study
one_liner: 系统性验证多数场景下引入生成辅助图像会降低多模态模型视觉推理准确率
practical_value: '- 多模态导购Agent、商品图文问答场景不要盲目加生成辅助图像步骤，优先验证生成图像保真度再落地，避免推理准确率下降

  - 图表类、数学类多模态推理需求（如电商销量图表问答）生成辅助图像增益极低，优先优化原生VLM能力而非引入生成分支

  - 若尝试生成辅助图像方案，可对实体关系推理类特定场景做多轮编辑调优，少量场景可能获得正向收益'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有多模态研究常类比人类「脑内构图辅助推理」逻辑，尝试引入生成辅助图像提升视觉推理效果，但缺乏系统性实证验证该思路的实际有效性。

### 方法关键点
测试范式为VLM先输出所需辅助图像的描述，调用图像生成器产出对应图，再结合原图+生成图共同回答视觉问题；覆盖13组VLM与生成器配对、10项主流视觉推理任务，同时测试多轮图像编辑的效果。

### 关键结果数字
平均准确率下降3.7个百分点，10项任务中有9项出现精度下跌；BAGEL、Janus-Pro-7B两款统一多模态模型在8项任务上精度下降；VSTAR任务引入生成图后精度下跌10.47个百分点；仅ERQA任务经过10轮图像编辑后精度提升3个百分点，ChartQAPro、MathVista等任务始终低于无生成图基线。
