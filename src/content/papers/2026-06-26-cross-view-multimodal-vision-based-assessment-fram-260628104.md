---
title: Cross-view Multimodal Vision-Based Assessment Framework for Traditional Chinese
  Medicine Rehabilitation Training
title_zh: Cross-view Multimodal Vision-Based Assessment Fram
authors:
- Francis Xiatian Zhang
- Hao Yao
- Shengxuan Chen
- Hong Zhu
- Hongxiao Jia
- Sisi Zheng
- Hubert P. H. Shum
arxiv_id: '2606.28104'
url: https://arxiv.org/abs/2606.28104
pdf_url: https://arxiv.org/pdf/2606.28104
published: '2026-06-26'
collected: '2026-06-29'
category: RAG
direction: RAG
tags:
- RAG
- LLM
one_liner: Vision-based assessment can provide convenient and cost-effective evaluation
  in Traditional Chi...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 摘要

Vision-based assessment can provide convenient and cost-effective evaluation in Traditional Chinese Medicine (TCM) rehabilitation training, where action quality assessment (AQA) from computer vision offers a promising solution. Existing automatic AQA frameworks for physical therapy typically rely on skeletal data captured from a single viewpoint, which is inefficient for TCM techniques such as acupuncture or Tuina that involve dense hand self-occlusion and complex hand-object interactions. To address these challenges, we propose CME-AQA, a cross-view, multimodal vision-based assessment framework that integrates visual-pose fusion to enhance understanding of environmental context and leverages both first-person and third-person videos during training to improve inference robustness. We collected two dual-view datasets, TCM-AQA61-A (Acupuncture) and TCM-AQA61-T (Tuina), each containing synchronized first-person and third-person recordings of 61 subjects with expert annotations. Experimental results show that our approach achieves superior or comparable mean performance against competitive baselines, achieving over 10% relative improvement in weighted F1 over the best competing method on key rating tasks such as Needle Depth and Quick Needle Insertion, while also reducing mean absolute error in quantitative measures such as insertion time and manipulation frequency. Testing on a CPR dataset further demonstrates comparable performance on several posture-based criteria, suggesting applicability to related structured simulated clinical skill assessments where participant motion is central to evaluation. Overall, CME-AQA enhances assessment accuracy for structured TCM rehabilitation training and facilitates more convenient and effective training-oriented skill evaluation.

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。
