---
title: 'Reading the Unreadable: Text-Aware Image Super-Resolution Needs Reasoning'
title_zh: 《阅读不可读内容：文本感知图像超分辨率需要引入推理能力》
authors:
- Jaeseong Lee
- Jinwoo Kim
- Jinho Jeong
- Seon Joo Kim
affiliations:
- CIPLAB, Yonsei University
arxiv_id: '2611.15449'
url: https://arxiv.org/abs/2611.15449
pdf_url: https://arxiv.org/pdf/2611.15449
published: '2026-11-10'
collected: '2026-11-23'
category: Multimodal
direction: 多模态大模型 · 文本感知图像超分优化
tags:
- MLLM
- Image Super-Resolution
- Text Restoration
- Multimodal Reasoning
- Training-free Plug-in
one_liner: 提出ReasonText基准与GTTCA指标，用训练无关RTC插件借助MLLM推理提升文本超分效果
practical_value: '- 电商商品主图/详情页低清文字修复场景可复用RTC架构：外接MLLM做低分辨率文本推理，喂入文本条件超分模型，无需重训即可提升文字清晰度

  - 广告/UGC内容审核场景可借鉴MLLM推理补全模糊文本的思路，配合OCR工具提升低质图片的文本提取准确率

  - 涉及图像文本质量评估的业务，可直接复用GTTCA指标，排除文本检测误差干扰，更精准衡量文本恢复效果'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有文本感知图像超分（TAISR）仅将任务视为视觉还原问题，严重退化的文本仅靠局部像素无法识别，现有方法存在系统性性能短板。
### 方法关键点
1. 发布ReasonText人工标注基准，区分需依赖上下文/先验推理恢复的文本与局部可恢复文本
2. 提出GTTCA识别导向评估指标，排除文本检测误差干扰，精准衡量文本恢复质量
3. 提出训练无关插件RTC：用MLLM推理低分辨率图像中的退化文本，生成文本描述后输入文本条件超分模型
### 关键结果
12款SOTA超分模型在需推理的文本场景下性能出现一致性大幅下降；RTC可稳定提升全部6款测试的文本条件超分模型效果，尤其在推理类文本上提升显著，通用超分模型加RTC效果甚至超过专用TAISR模型加RTC。
