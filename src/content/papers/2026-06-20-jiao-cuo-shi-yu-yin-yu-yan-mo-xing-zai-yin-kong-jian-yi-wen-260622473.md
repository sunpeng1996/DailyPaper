---
title: Interleaved Speech Language Models Latently Work In Text
title_zh: 交错式语音语言模型在隐空间以文本模态运作
authors:
- Talia Sternberg
- Gallil Maimon
- Yossi Adi
affiliations:
- The Hebrew University of Jerusalem
arxiv_id: '2606.22473'
url: https://arxiv.org/abs/2606.22473
pdf_url: https://arxiv.org/pdf/2606.22473
published: '2026-06-20'
collected: '2026-06-30'
category: Eval
direction: 多模态语音模型内部机制分析
tags:
- SpeechLM
- Logit Lens
- Model Analysis
- Interleaved Modality
- Implicit Transcription
one_liner: 借助logit lens分析揭示交错语音文本LM隐空间隐式文本转录的内在机制
practical_value: '- 多模态混训场景（如多模态推荐、语音Agent）可复用logit lens分析内部模态交互规律

  - 文本预训练初始化的多模态模型会自发将非文本模态隐式转文本推理，可减少显式转写训练成本

  - 非文本+文本交错训练能激发隐转文本行为，进而提升原模态任务性能，可指导多模态训练数据构造'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
当前交错语音文本训练的语音语言模型（SLM）已被验证可提升纯语音任务性能，但两类模态在隐空间的交互机制不明确，阻碍了SLM的进一步优化。
### 方法
通过logit lens工具，对不同模型结构、不同参数量的交错式SLM展开内部机制分析，探究隐转写行为的成因，以及该行为和模型语音知识能力的关联。
### 结果
发现交错式SLM即使未经过语音识别训练，也会在中间层自发进入隐式转写阶段：将输入语音转换为对应文本token，在文本空间完成下一个token预测后再转回语音域；77%的测试样本中，正确转写文本位列模型输出的top候选；证实从预训练文本LM初始化、加入交错训练数据是诱发该隐行为的核心原因，该行为与模型的语音知识能力正相关。
