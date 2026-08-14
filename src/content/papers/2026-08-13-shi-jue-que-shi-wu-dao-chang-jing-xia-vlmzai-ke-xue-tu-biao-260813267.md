---
title: How Do VLMs Behave When Blind or Misled? Behavioral Evaluation of VLMs on Scientific
  Figures
title_zh: 视觉缺失/误导场景下VLM在科学图表中的行为表现评估
authors:
- Paul Osemudiame Oamen
- Owusu-Banahene Osei
- Ananya Mukherjee
- Christian Greisinger
- Steffen Eger
- Pius Onobhayedo
- Wei Zhao
affiliations:
- University of Aberdeen, UK
- International Institute of Information Technology Hyderabad, India
- University of Technology Nuremberg, Germany
- University of Southern California, USA
arxiv_id: '2608.13267'
url: https://arxiv.org/abs/2608.13267
pdf_url: https://arxiv.org/pdf/2608.13267
published: '2026-08-13'
collected: '2026-08-14'
category: Eval
direction: 多模态模型·不确定场景行为可靠性评估
tags:
- VLM
- Evaluation Benchmark
- Multimodal Reliability
- Scientific Figure Understanding
- Hallucination
one_liner: 提出SciFigBench评估基准与A-R-I框架，量化不确定环境下VLM在科学图表理解场景的行为可靠性
practical_value: '- 可复用A-R-I评估框架，检测多模态推荐/广告Agent在商品图模糊、水印遮挡、信息不全场景下的幻觉率，优化生成输出的可靠性

  - 可借鉴选择性模糊、误导性探针的构造方法，构建业务场景的压力测试集，提前排查多模态生成式推荐系统的bad case

  - 选型多模态大模型时，不能只看感知推理准确率，需额外评估不确定场景下的拒答/抗误导能力，降低线上hallucination风险'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有VLM基准仅侧重感知与推理准确率，忽略视觉证据缺失、误导等不确定场景下的行为可靠性评估，无法支撑高风险场景的模型落地选型。
### 方法关键点
1. 构建SciFigBench评估基准，包含250张科学图表高质量人工标注（累计标注耗时600+小时），通过图像变换、选择性模糊、误导性探针等方式扩展出3.4万+压力测试用例；
2. 提出A-R-I评估框架，分别衡量模型对证据不足的承认度、对误导信息的抗性、对部分信息的谨慎推理能力。
### 关键结果
GPT-5.2描述质量MQM达91.6、推理准确率78.4%，但96%的信息缺失场景会产生幻觉；Gemini 3.1 Pro MQM达90.2、推理准确率81%，71%的信息缺失场景会主动承认不确定，抗误导得分达0.91，验证高感知推理能力不等同于高行为可靠性。
