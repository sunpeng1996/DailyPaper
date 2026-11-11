---
title: 'MotionGraphicsBench: Evaluating Motion Graphics Generation with Programmatic
  Verification'
title_zh: MotionGraphicsBench：基于程序化验证的动效生成评估基准
authors:
- Jiaju Ma
- Ashvini Kumar Jindal
- Chuhua Wang
- Sumithra Bhakthavatsalam
affiliations:
- Stanford University
- Figma
arxiv_id: '2611.10592'
url: https://arxiv.org/abs/2611.10592
pdf_url: https://arxiv.org/pdf/2611.10592
published: '2026-11-06'
collected: '2026-11-11'
category: Eval
direction: 动效生成评估 · 程序化多智能体验证
tags:
- LLM
- Evaluation
- MultiAgent
- Programmatic Verification
- Motion Generation
one_liner: 提出配套程序化验证的动效生成评估基准，解决多维度动效需求的一致性评估难题
practical_value: '- 做电商广告动效、短视频动效等生成类内容的效果评估时，可复用程序化验证思路，替代VLM打分/人工比对，大幅提升评估准确率和效率

  - 构建带验证逻辑的测试集时，可参考多Agent+人工标注结合的pipeline，降低规则编写成本同时保证验证的灵活性

  - 对动效、文案等需要多轮生成重试的生成类业务，可参考pass@k的评估逻辑，平衡生成成本与效果达标率，确定最优重试次数'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
LLM可基于静态图像和自然语言生成动效，但现有评估方案难以同时校验空间、外观、时序多维度需求的符合度，VLM打分或参考动效比对的准确率低、灵活性差。
### 方法关键点
1. 构建含100个真实Lottie动效场景的专家标注基准，任务为给静态SVG添加指定动效，隔离动效生成与图形生成任务；
2. 每个case配套确定性、可读的验证程序，支持多种合法实现的校验，直接输出各需求项的通过/失败结果，无需参考动效或VLM打分；
3. 验证程序通过多Agent pipeline结合人工标注动效、合成测试用例构建。
### 关键结果
验证程序与人工判断的一致性达93.3%，优于GPT-6 Astra VLM基线的83.3%；32个LLM共47种配置的pass@1为6.0%~67.7%；15个模型开启最高推理能力时每实例重试32次的pass@32为38.0%~95.0%。
