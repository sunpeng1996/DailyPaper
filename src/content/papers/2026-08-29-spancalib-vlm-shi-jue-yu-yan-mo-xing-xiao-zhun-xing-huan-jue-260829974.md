---
title: 'SpanCalib-VLM: Calibrated Hallucination Span Detection in Vision-Language
  Models'
title_zh: SpanCalib-VLM：视觉语言模型校准型幻觉跨度检测方法
authors:
- Amanuel Gizachew Abebe
- Yasmin Moslem
affiliations:
- Shaggar Institute of Technology
- Trinity College Dublin
arxiv_id: '2608.29974'
url: https://arxiv.org/abs/2608.29974
pdf_url: https://arxiv.org/pdf/2608.29974
published: '2026-08-29'
collected: '2026-09-02'
category: Multimodal
direction: 多模态大模型 · 幻觉检测与校准
tags:
- LVLM
- Hallucination Detection
- Sequence Tagging
- Generative VLM
- Confidence Calibration
one_liner: 结合生成式VLM与判别式标注器，通过联合校准融合提升LVLM幻觉检测的定位精度与置信度校准度
practical_value: '- 电商多模态生成场景（商品图文生成、AI直播口播文案）的幻觉检测可复用这套双系统融合架构：生成式模型召回可疑片段，判别式标注器做校准打分，兼顾召回率和置信度可靠性

  - 涉及高置信度校准要求的序列标注任务（用户评论风险片段识别、商品属性抽取），可参考Union-Calibrated Fusion策略做多模型结果融合，降低过置信问题

  - 对 latency 敏感的在线多模态内容校验场景，可优先用判别式多模态序列标注器做基线，再用小参数生成式VLM做召回补全，平衡速度和效果'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
LVLM幻觉检测需要同时满足精准的跨度定位和高校准度的置信度打分：现有生成式VLM方案跨度召回高但存在过置信、推理延迟高问题；判别式序列标注器速度快、校准效果好但召回保守，两类方案各有短板。
### 方法关键点
提出双系统混合框架SpanCalib-VLM：1）判别侧为融合SigLIP视觉编码器与XLM-RoBERTa-Large的多模态序列标注器，通过交叉注意力对齐图文特征；2）生成侧为微调的Qwen3.5-4B-SHROOM-SFT生成式VLM；3）通过Union-Calibrated Fusion策略，用标注器输出的校准概率对生成模型得到的候选幻觉跨度重新打分。
### 关键结果
在SHROOM-Visions英文测试集上：Pearson校准相关系数0.41，整体IoU 0.39，无幻觉响应IoU 0.91，整体检测准确率70.7%
